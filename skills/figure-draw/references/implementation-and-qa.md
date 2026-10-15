# Implementation and final-size QA

Use Python/Matplotlib or R/ggplot2 as appropriate. The bundled Python helper needs Python ≥3.9 and Matplotlib; NumPy/Pillow are only needed for particular user plotting code or QA. It does not install dependencies or access a network. Use workspace dependencies if available, otherwise the task's environment. Do not change global software settings merely to run a plot.

## Helper usage

```python
# Add this skill's scripts directory to your import path.
import matplotlib.pyplot as plt
from figure_style import build_profile, paper_style, make_figure, label_panels, export_figure

profile = build_profile("nature", width_mm=183)
# Science: select the intended column width explicitly (typically 57, 121 or 184 mm).
# profile = build_profile("science", width_mm=user_selected_width_mm)
with paper_style(profile, font_family="Arial"):
    fig, axes = make_figure(profile, height_mm=70, nrows=1, ncols=2)
    # Plot supplied data here. Do not insert fictitious observations or statistics.
    # Use English quantity (unit) labels and actual error definitions.
    label_panels(fig, axes, profile)
    paths = export_figure(fig, "figure1", profile)
    plt.close(fig)
```

Supply a permitted local font file via `font_file` if needed. The helper raises if a requested font is unavailable, preventing silent family fallback. Current official/editor choices override preset values with dataclass replacement; record provenance. `paper_style` uses a scoped rc context. It retains SVG text and requests PDF Type 42 embedding. Math text/glyph fallbacks still require inspection.

## Export invariants

- Canvas size in inches = mm / 25.4. Font and line widths are points. Raster pixels ≈ mm / 25.4 × DPI. DPI alone does not establish final-size resolution, and vectors are resolution independent.
- Save the fixed-size canvas. Avoid `bbox_inches="tight"` when it changes the requested publication dimensions; reserve adequate layout margin and fix clipping instead. The helper exports PDF, SVG, PNG and JSON with dimensions/profile/audit; it does not guarantee the final PDF has editable layers in every editor.
- Text should remain text, not paths/outlines; embed fonts in PDF where supported. For selective rasterization of dense marks, preserve axes/text/vector annotations and report those artists and effective DPI. No upsampling to conceal deficient source resolution.
- SVG is an editable source; its fonts may remain external references. Inspect it in a second renderer/editor. Confirm actual PDF fonts with an available PDF inspector, text extraction or editor; Type 42 settings alone do not prove all exported glyphs are editable.
- Keep a source-data reference/table, code, dependency versions, transforms, exclusions, units/n and panel metadata. Jitter seed is a display setting; it does not create independent replicates. Synthetic testing outputs must be unmistakably separate from study results.

## Required checks

1. Data: plotted values/group counts/pairing/summary computations match source; no unintended exclusions or zero-filled missingness; quantitative encodings and test metadata faithful.
2. Geometry: actual PDF/SVG page width/height, final text size, panel order and whitespace; no labels outside the page, collisions, truncated annotations or cramped ticks. Zoom aids diagnosis but does not replace the final-size review.
3. Accessibility: marker/line identity without colour, text/background contrast, grayscale and colour-vision checks when available; scientific colourbar and missingness meaning.
4. Production: embedded actual fonts, no outlined/rasterized text, sufficient resolution of embedded rasters; final files open successfully. Verify submission-stage formats separately.
5. Caption handoff: exact metrics, units, centre/error definition, independent n, tests/P/corrections, random-baseline construction and source provenance. Never use polished formatting as evidence of validity.

The helper's audit checks visible text size/page containment, basic geometry and Science Line2D marker/line minima; collection/scatter marks require separate inspection. It cannot detect every overlap, all font substitutions, false statistics, invalid inference, accessibility or current journal compliance. Report unperformed checks as unverified; do not say “all checks passed” when only preflight ran. Use Chinese status entries: 已核实 / 缺失 / 冲突 / 未验证 / 不适用, with consequence and next required evidence.
