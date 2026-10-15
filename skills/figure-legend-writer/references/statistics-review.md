# Evidence and statistical review

This is an editorial audit, not a guarantee of statistical validity. Apply relevant checks and distinguish missing reporting from demonstrated design problems.

| Item | Check |
|---|---|
| n and units | Exact n by panel/group/time and what it counts: subjects, cultures, batches, sequences, reads, runs or seeds. Distinguish independent units from technical repeats and plotted points. |
| Dependence | Pairing, repeated measures, nested fields/cells, shared data, overlapping windows and pairwise sequence comparisons; number of pairs is not automatically independent n. Flag uncertainty without assuming a design flaw. |
| Metrics/aggregation | Numerator, denominator, units, normalization/reference and weighting. Full-sequence coverage and equal-weight window coverage differ; preserve the user's estimand. |
| Centre/uncertainty | Mean/median, SD/SEM, confidence/credible/prediction intervals and level; calculation method and units. Define box bounds, centre, whiskers, outliers and shaded bands; never supply defaults. |
| Tests | Exact comparisons, name, sidedness, pairing, assumptions, statistic/degrees of freedom where applicable, post hoc procedure. A suggested test is not performed work. |
| P/multiplicity | Preserve exact values/inequalities and precision; distinguish raw/adjusted P, correction and family of hypotheses. Explain displayed stars/brackets/ns from actual metadata, never customary thresholds. |
| Effect/absence | Separate effect size, uncertainty and significance. Nonsignificance does not establish equivalence, no effect or a validated null model. |
| Random baseline | Null hypothesis, sampling space, constraints preserved (length, GC, graph degree, marginals), statistic, simulations/permutations, replacement, seed/reproducibility and tail/uncertainty calculation. Do not invent uniform random walks or Monte Carlo P values. |
| Computational repetitions | Distinguish optimization seeds, resampled datasets and independent experiments. A baseline may be descriptive; inferential conclusions require supported analysis. |
| Representative images | Identity, supplied selection rule, channels/stains, scale-bar units/length and repetition count. One image does not establish repeatability. |
| Mechanism | Correlation, overlap, clustering, shared graph nodes and schematic arrows do not prove attractors, feedback or causality. Require discriminating evidence/causal design; label conceptual models as proposed if supplied as such. |

Ask for the narrowest missing evidence, e.g. “请确认阴影是独立培养间的 SD 还是均值的置信区间，并提供计算单位”. Unknown is not 不适用; use 不适用 with a reason, such as a nonquantitative conceptual schematic.
