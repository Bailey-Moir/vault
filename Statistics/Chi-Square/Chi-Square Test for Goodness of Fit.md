---
tags:
  - atom
  - stats
---
Use a $\chi^2$ [[Goodness-of-fit|goodness-of-fit]] test to assess [[Statistical Hypotheses|hypotheses]] about the distribution of categories for a single [[Variable Types|categorical variable]].
1.  State [[Statistical Hypotheses|null hypothesised]] [[Proportion|proportions]] for each category, $p_i$. The [[Statistical Hypotheses|alternative hypothesis]] is that at least one of the [[Proportion|proportions]] is different than specified in the null.
2. Calculate the expected counts for each cell as $np_i$ .
3. Calculate the $\chi^2$ statistic[^1].
4. Compute the [[p-value|p-value]] as the area in the tail above the $\chi^2$ statistic[^1], for a $\chi^2$-distribution[^2] with $df = (\text{\# of categories} – 1)$
5. Interpret the [[p-value|p-value]] in context.

[^1]: [[Chi-Square Statistic]]
[^2]: [[Chi-Square Distribution]]