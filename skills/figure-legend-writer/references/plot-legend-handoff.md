# Statistical figure and legend consistency

Use the plotting metadata rather than guessing from appearance. The English legend must agree with the rendered figure and analysis source.

| Figure component | Information needed in the legend or review |
|---|---|
| Axes | Quantity, units, normalization reference, transformation/log base; distinguish counts, fractions, percent and density. |
| Dots/lines | What a dot counts, paired connections, experimental versus computational units; a connecting line does not prove temporal order or causality. |
| Summary/error bars | Central estimate, SD/SEM/interval level, independent unit and exact n by group/panel. Do not call an unknown band a confidence interval. |
| Box/violin | Quartiles, centre, whisker rule, outlier convention, density meaning/processing; never assume software defaults were used. |
| Heatmap | Colour quantity/units, scale, reference/centre, row/column order and clustering if actually performed; define masked/missing values. |
| Histograms/ECDF | Count versus probability/density, relevant binning, weighting and denominator. |
| Statistical labels | Actual comparison, test/sidedness/pairing, P precision, adjustment and star meanings. A displayed “ns” does not establish equivalence. |
| Insets/facets | Panel identity, changes in scale, group identity and nonshared definitions. |

Suggested handoff fields: `panel; source; unit; groups; n; metric; transform; encodings; centre; uncertainty; test; P; multiplicity; exclusions; missingness; visual QA status`.

Panel naming follows the actual artwork. Nature uses lower-case panel labels in its official figure specifications; Science also explicitly requires uppercase panel labels in its official initial guide; recheck the applicable live guide before changing labels. Full legends belong in manuscript text, not baked into the exported statistical artwork. Do not claim a journal-specific visual rule is satisfied unless it was verified on the actual export.
