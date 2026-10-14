# Intake and examples

Accept free-form inputs; this template is optional:

```text
Journal / article type / submission stage / figure number:
Figure file or panel descriptions / existing legend:
Per panel: subject, groups, conditions, metric/units, encoding, source:
n by panel/group and independent unit; technical/biological/computational repeats:
Centre, error bars, boxplot/shading definitions:
Tests/comparisons/sidedness/pairing/P values/multiple-testing correction:
Random baseline, constraints, simulation count and uncertainty if applicable:
Scale bars, abbreviations, representative-image repeat count:
Known limitations and allowed claims:
```

## Complete quantitative example — synthetic teaching data

Input: A, treated versus vehicle cultures at 24 h; each dot independently prepared culture, n = 6/group; response normalized to vehicle-group mean; bars mean ± SD; two-sided Welch t-test, P = 0.032; one prespecified comparison, no correction. Journal verification remains separate; these data do not establish test suitability for a real study.

**Figure 2. Normalized response following treatment.** (A) Response in treated and vehicle cultures at 24 h, normalized to the vehicle-group mean. Each point represents an independently prepared culture (n = 6 per group); bars show mean ± SD. Groups were compared using a two-sided Welch t-test (P = 0.032; one prespecified comparison, without multiple-testing correction).

Chinese review: 样本单位、n、误差棒和检验来自所给口径；未提供原图/原始数据，视觉一致性、计算和检验假设未独立核验。若期刊要求统计量和自由度，请补充。Do not label automatically submission-ready for every journal.

## Missing random baseline and unsupported mechanism

Input: A shows overlap among DNA paths from different seeds; B shows a curve labelled “random”; metric, dots and bands undefined. User asks to claim a De Bruijn graph attractor.

**Draft — not submission-ready. Figure 1. Overlap among generated DNA paths.** (A) Overlap among paths generated using different random seeds [metric, units and sampling unit required]. (B) Comparison with the curve labelled “random” [baseline construction and shaded-band definition required].

Review: flag independent n, pairwise dependence, null sampling space/constraints, simulation count, band meaning and missing inference. Do not invent significance, a uniform random walk or an attractor mechanism. Proposed discriminating analyses belong in the review only.

## Schematic only

Input: A, conceptual bit encoding → assembly of DNA modules → nanopore readout → decoding, no experiments.

**Figure 1. Conceptual workflow for modular DNA storage.** (A) Proposed workflow comprising bit encoding, assembly of DNA modules, nanopore readout and decoding.

Review: 概念流程，n/误差棒/P 不适用；未检查实际图像，需核对箭头、标签、缩写。Do not add validated accuracy or implemented performance.

## Conflicting metadata

Plot SEM versus table SD: flag 冲突 and use `[error-bar definition to be resolved]`. n = 5 versus n = 6: request panel/group-specific source, never average or choose silently. Preserve P < 0.001; do not write P = 0.000 or invent digits. Supplied stars without thresholds remain unresolved.
