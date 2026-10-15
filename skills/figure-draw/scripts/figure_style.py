"""Matplotlib figure styling/export, without data processing or inference.

Journal defaults follow the dated official source ledger. Preflight is partial.
"""
from contextlib import contextmanager
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import matplotlib as mpl
from matplotlib import font_manager
import matplotlib.pyplot as plt
from matplotlib.text import Text
from matplotlib.transforms import ScaledTranslation


@dataclass(frozen=True)
class Profile:
    journal: str
    width_mm: float
    body_pt: float
    panel_pt: float
    panel_case: str
    min_text_pt: float
    policy_status: str


def build_profile(journal, width_mm=None):
    journal = journal.strip().lower()
    if journal not in {"nature", "science"}:
        raise ValueError("Use exact flagship nature or science; no family substitution.")
    if journal == "science" and width_mm is None:
        raise ValueError("Select Science width explicitly, usually 57, 121 or 184 mm; see current guide.")
    width = 89.0 if width_mm is None else float(width_mm)
    if not 0 < width < float("inf"):
        raise ValueError("width_mm must be positive and finite")
    if journal == "nature":
        return Profile(journal, width, 7, 8, "lower", 5,
                       "Nature snapshot 2026-10-15; recheck current type/stage rules.")
    return Profile(journal, width, 7, 10, "upper", 5,
                   "Science official HTML/PDF snapshot 2026-10-15; HTML widths and stricter 0.5 pt lines used; recheck current rules.")


def resolve_font(font_family=None, font_file=None):
    if font_file is not None:
        path = Path(font_file).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(path)
        font_manager.fontManager.addfont(str(path))
        return font_manager.FontProperties(fname=str(path)).get_name()
    candidates = [font_family] if font_family else ["Arial", "Helvetica"]
    for family in candidates:
        try:
            font_manager.findfont(font_manager.FontProperties(family=family), fallback_to_default=False)
            return family
        except ValueError:
            pass
    raise ValueError("Selected font unavailable. Supply a font file or explicitly recorded substitute.")


@contextmanager
def paper_style(profile, font_family=None, font_file=None):
    family = resolve_font(font_family, font_file)
    rc = {"font.family": family, "font.size": profile.body_pt,
          "axes.labelsize": profile.body_pt, "axes.titlesize": profile.body_pt,
          "xtick.labelsize": profile.body_pt, "ytick.labelsize": profile.body_pt,
          "legend.fontsize": profile.body_pt, "figure.titlesize": profile.body_pt,
          "axes.linewidth": 0.6, "lines.linewidth": 0.9,
          "lines.markersize": 6.0 if profile.journal == "science" else 3.5,
          "axes.spines.top": False, "axes.spines.right": False, "axes.grid": False,
          "xtick.minor.visible": False, "ytick.minor.visible": False,
          "xtick.major.width": 0.6, "ytick.major.width": 0.6,
          "xtick.major.size": 2.5, "ytick.major.size": 2.5,
          "text.color": "black", "axes.labelcolor": "black",
          "xtick.color": "black", "ytick.color": "black",
          "figure.facecolor": "white", "axes.facecolor": "white",
          "savefig.facecolor": "white", "savefig.bbox": None,
          "pdf.fonttype": 42, "ps.fonttype": 42, "svg.fonttype": "none"}
    with mpl.rc_context(rc):
        yield family


def make_figure(profile, height_mm, nrows=1, ncols=1, **kwargs):
    height = float(height_mm)
    if not 0 < height < float("inf"):
        raise ValueError("height_mm must be positive and finite")
    if profile.journal == "nature" and height > 170:
        raise ValueError("Nature snapshot height maximum 170 mm; verify editor instructions.")
    if "figsize" in kwargs:
        raise ValueError("Use profile width/height_mm instead of conflicting figsize.")
    kwargs.setdefault("layout", "constrained")
    return plt.subplots(nrows, ncols, figsize=(profile.width_mm / 25.4, height / 25.4), **kwargs)


def label_panels(fig, axes, profile, labels=None, x_offset_mm=2, y_offset_mm=1.3):
    """Call after plotting; inspect placement, never shrink labels automatically."""
    if hasattr(axes, "flat"):
        axes = list(axes.flat)
    elif hasattr(axes, "get_position"):
        axes = [axes]
    else:
        axes = list(axes)
    if labels is None:
        if len(axes) > 26:
            raise ValueError("Supply explicit labels for more than 26 panels")
        base = ord("a" if profile.panel_case == "lower" else "A")
        labels = [chr(base + i) for i in range(len(axes))]
    if len(labels) != len(axes):
        raise ValueError("One label per supplied panel required")
    fig.canvas.draw()
    texts = []
    for ax, label in zip(axes, labels):
        transform = ax.transAxes + ScaledTranslation(-x_offset_mm / 25.4,
                                                    y_offset_mm / 25.4, fig.dpi_scale_trans)
        text = ax.text(0, 1, label, transform=transform, clip_on=False,
                        fontsize=profile.panel_pt, fontweight="bold", fontstyle="normal",
                        color="black", ha="left", va="bottom")
        text.set_gid("panel_label")
        texts.append(text)
    fig.canvas.draw()
    return texts


def preflight(fig, profile):
    """Partial geometry/text checks; no overlap, statistics or font-embedding test."""
    fig.canvas.draw()
    renderer, page = fig.canvas.get_renderer(), fig.bbox
    issues, families = [], set()
    inactive_ticks = set()
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            lo, hi = sorted(axis.get_view_interval())
            for tick in axis.get_major_ticks() + axis.get_minor_ticks():
                if not lo <= tick.get_loc() <= hi:
                    inactive_ticks.update((id(tick.label1), id(tick.label2)))
    for text in fig.findobj(match=Text):
        if id(text) in inactive_ticks or not text.get_visible() or not text.get_text().strip():
            continue
        # Explicitly clipped text needs separate visual inspection.
        if text.axes is not None and text.get_clip_on():
            continue
        families.update(text.get_fontfamily())
        size = text.get_fontsize()
        if size < profile.min_text_pt:
            issues.append({"check": "text_size", "text": text.get_text(), "size_pt": size})
        if profile.journal == "nature" and size > 7 and text.get_gid() != "panel_label":
            issues.append({"check": "nature_body_max", "text": text.get_text(), "size_pt": size})
        box = text.get_window_extent(renderer)
        if box.x0 < page.x0 - 1 or box.y0 < page.y0 - 1 or box.x1 > page.x1 + 1 or box.y1 > page.y1 + 1:
            issues.append({"check": "page_containment", "text": text.get_text()})
    width, height = fig.get_size_inches() * 25.4
    if abs(width - profile.width_mm) > 0.01:
        issues.append({"check": "width_mismatch", "actual_mm": float(width)})
    if profile.journal == "nature" and height > 170.01:
        issues.append({"check": "height", "actual_mm": float(height)})
    if profile.journal == "science":
        for ax in fig.axes:
            for line in ax.get_lines():
                if not line.get_visible() or not len(line.get_xdata()):
                    continue
                if line.get_linestyle() not in {"None", "none", "", " "} and line.get_linewidth() < 0.5:
                    issues.append({"check": "science_line_width", "width_pt": line.get_linewidth()})
                data_markers = {"o", "s", "^", "v", "<", ">", "D", "d", "p", "h", "H", "*", "8", "+", "x", "P", "X"}
                if line.get_marker() in data_markers and line.get_markersize() < 6:
                    issues.append({"check": "science_marker_size", "size_pt": line.get_markersize()})
    return {"width_mm": float(width), "height_mm": float(height),
            "requested_font_families": sorted(families), "issues": issues,
            "limitations": "Inspect scatter/collection marker size, overlaps, clipped text, glyphs, embedding, data, accessibility and current policy separately."}


def export_figure(fig, stem, profile, preview_dpi=300):
    if not 0 < preview_dpi < float("inf"):
        raise ValueError("preview_dpi must be positive and finite")
    stem = Path(stem)
    stem.parent.mkdir(parents=True, exist_ok=True)
    audit = preflight(fig, profile)
    if audit["issues"]:
        raise ValueError("Resolve preflight issues before export: " + json.dumps(audit["issues"]))
    paths = {}
    with mpl.rc_context({"savefig.bbox": None, "pdf.fonttype": 42, "svg.fonttype": "none"}):
        for ext in ("pdf", "svg", "png"):
            path = stem.parent / (stem.name + "." + ext)
            fig.savefig(path, format=ext, dpi=preview_dpi, bbox_inches=None)
            paths[ext] = str(path)
    path = stem.parent / (stem.name + ".json")
    path.write_text(json.dumps({"profile": asdict(profile), "preflight": audit,
                              "preview_dpi": preview_dpi, "matplotlib": mpl.__version__}, indent=2), encoding="utf-8")
    paths["metadata"] = str(path)
    return paths
