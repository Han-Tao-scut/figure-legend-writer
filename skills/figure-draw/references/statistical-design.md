# Plot selection and truthful statistical representation

The table gives local methodological recommendations. Verify inference from supplied analysis/design, not from chart type.

| Question/data | Prefer | Essential safeguards |
|---|---|---|
| Small independent continuous samples | Dot/strip/beeswarm plus supplied summary/interval | Show actual observations; jitter only categorical position with recorded seed. Do not fabricate raw values from summaries. |
| Paired/repeated measures | Paired dots/lines or changes, optionally summaries | Match actual subject IDs; connect the same unit. Missing pairs remain missing. Do not connect unrelated groups. |
| Distribution | ECDF/histogram; box or violin when enough data support it | State denominator/binning; common bins for comparisons; disclose KDE bandwidth/support. Define box/whisker/outlier rules. Avoid density smoothing that implies unsupported structure in tiny samples. |
| Counts/proportions | Bars or point/interval | Bars normally start at zero; provide numerator/denominator. If uncertainty is absent, do not invent it. Percent is not fraction; categorical counts are not density. |
| Time/dose response | Points/lines at measured positions plus supplied interval | Do not imply interpolation/extrapolation as measurements; distinguish model fit, uncertainty and prediction. Preserve time spacing and missingness. |
| Two continuous variables | Scatter; hexbin/density for truly dense samples | Report transformations/counts; disclose aggregation/rasterization. A fitted trend or correlation does not establish causality. |
| Many effects/comparisons | Effect/forest plot | Use supplied estimates/intervals; meaningful null line, common scale; significance stars are secondary. |
| Matrix/heatmap | Heatmap with labelled colourbar | Sequential for ordered magnitude; diverging only with meaningful centre; cyclic for periodic quantity. Preserve shared normalization, distinguish missing from zero, record clustering/order. |
| Algorithms/benchmarks | Dot/box/line plot with run/dataset units defined | Distinguish seeds, datasets, folds, test samples and simulations; preserve test/training boundaries and paired benchmark structure. |

Show information available in the source; make no single chart mandatory for every study. A bar of means may be the only supported option for summary-only input, but say raw distributions cannot be assessed. Do not automatically add SD, SEM or bootstrap CI; preserve the requested estimand and definition.

For axes: share scales among comparable panels; if limits differ, make that visible. Bar-length comparisons need a meaningful baseline. A scatter/line axis may focus on the data range if clearly marked and not misleading. Do not use broken axes or a second independent y axis as a cosmetic shortcut. Log axes must handle zero/negative observations explicitly and preserve units/base. Show a reference line only when its meaning is supplied.

Quantitative safeguards: independent n by group/panel; paired/nested/dependent observations; metrics/normalization/weights; missingness/exclusions; centre/interval; test/sidedness/comparison; raw versus adjusted P and correction family; real null-model constraints and simulations. Pair counts, reads or windows do not automatically equal independent n. Overlap alone does not prove a graph attractor or mechanism. Never manufacture a baseline to make a figure statistically convincing.
