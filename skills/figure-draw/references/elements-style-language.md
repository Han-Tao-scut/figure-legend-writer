# Elements, style, composition and language

These are implementation defaults unless a journal rule is explicitly cited in journal-specifications.md. Aim for clarity at final size, not a generic “Nature-like” look.

## Composition

Choose one scientific question per figure and a coherent role per panel; arrange supporting comparisons in reading order. For a single result, one panel may suffice. Align plot boxes, related baselines and panel-letter origins; keep consistent physical spacing. Give dense plots more space rather than shrinking fonts. Use enough margin for labels, ticks, legends and brackets; wasted blank area and cramped data are both defects. Do not impose a fixed panel count or decorative layout.

Separate four text functions: panel letters identify parts; axes name quantities/units; an internal key maps encodings; a manuscript figure legend explains evidence and statistics. Put the overall figure title/full legend in manuscript prose. Optional short panel headings should identify the comparison, not proclaim an unsupported mechanism.

## Element inventory

| Element | Drawing decision |
|---|---|
| Axes/ticks | Keep visible axes/ticks and readable quantitative scale; local default bottom/left spines for ordinary Cartesian plots. Full frames may help matrix plots; retain scientific requirements. Disable grids by default; any necessary deviation from Nature guidance must be explained. |
| Data marks | Distinct markers/line styles reinforce colours. Keep markers and line thickness visible at final size; local Nature starting points 3–4 pt markers, 0.6 pt axes and 0.8–1.0 pt lines; Science requires symbols ≥6 pt and lines ≥0.5 pt. For Matplotlib scatter, nominal s starts at 36 pt² for 6 pt marks, but actual shape/readability needs visual verification. Avoid 3D perspective for 2D data. |
| Uncertainty | Use unobtrusive caps/bands and matching meaning across panels. Keep individual observations visible. Define interval, level and units; absence of uncertainty is a metadata gap, not permission to compute arbitrary CI. |
| Legends | Compact key outside dense data or direct labels with space; retain marker/line samples. Fixed group order and colour mapping across panels. Do not rely on prose colour names alone. |
| Colourbars | Label quantity/units and scale, limits, centre and ticks; same mapping for comparable panels. Mark missing values distinctly. |
| Statistical brackets | Only supported comparisons; keep clear of data/ticks; exact supplied P or defined thresholds. Do not turn all pairs into overlapping brackets. |
| Insets | Use only for an explicit scale/question; show different limits and indicate source region if meaningful. |

## Typography and English labels

Apply sizes in points at final export dimensions. Scaling an image after export changes effective fonts/lines; regenerate at the intended size. Use one verified sans-serif family; prefer Arial/Helvetica for the Nature profile. Check availability and embedding; an unavailable font requires a recorded substitute/provisional status. Manuscript Times New Roman instructions are not figure-font instructions.

Use concise English, sentence case, standard scientific names and SI units: `Time (s)`, `Read length (nt)`, `Coverage (%)`, `Normalized response`. Define the reference for “normalized”; define `a.u.` rather than using it as a missing unit. Distinguish probabilities (0–1), percentages (0–100), counts and densities. Keep leading zero (`0.05`), meaningful precision, correct minus signs, multiplication signs and superscripts. Use `n`/`P` consistently with the journal; mathematical variables may be italic but unit symbols stay upright. Verify Greek glyphs and scientific-name italics after export. Avoid chatty labels, claims such as “excellent” or “significant” without evidence, unexplained software column names and entire sentences squeezed onto axes.

## Colour

Local categorical starting palette: blue `#0072B2`, orange `#E69F00`, green `#009E73`, vermillion `#D55E00`, purple `#CC79A7`, black `#000000`. Keep the palette stable and add shapes/styles; do not imply these hex codes are mandated or universally accessible on all backgrounds. Yellow or pale colours need contrast checks on white. Use a tested continuous palette such as cividis/viridis for magnitude; choose an appropriate tested diverging palette for a real centre. Do not stretch colours or clip outliers silently. Review grayscale and, where tools permit, colour-vision simulation; grayscale alone does not validate all colour-vision deficiencies.

Default white background, dark text, flat fills, minimal borders, no shadows, bevels, textures, logos or ornamental illustrations. Data evidence should carry the emphasis; highlights need a scientific role and must not hide unfavourable observations.

Science-specific note: its HTML discourages grayscale as a primary encoding and permits hatching for emphasis; the linked PDF emphasizes redundant shapes/contrasting colours. Grayscale preview is a diagnostic, not a mandate to publish in gray. Nature discourages patterns, so do not apply Science hatching to Nature. Refer to the source ledger for differences.
