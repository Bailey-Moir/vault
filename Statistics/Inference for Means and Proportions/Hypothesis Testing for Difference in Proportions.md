---
tags:
  - atom
  - stats
---
In order to test $H_0: p_1 - p_2 = 0$, based on sample size $n_1$ and $n_2$, we use the [[Test Statistic|standard test statistic]]:
$$ z = \dfrac{\text{statistic} - \text{null value}}{SE} = \dfrac{\hat p_1 - \hat p_2}{\sqrt{\hat p(1-\hat p) \left(\dfrac{1}{n_1} + \dfrac{1}{n_2}\right)}} $$
where $\hat p$ is the [[Pooled Proportion|pooled proportion]]. See [[CLT for Difference in Proportions|central limit theorem for difference in proportions]] for original equations and conditions.

> [!proof]- Justification of SE
> The [[Standard Error|standard error]] must assume the null hypothesis is true, and thus that $p_1 = p_2$. [[Pooled Proportion|Pooling proportions]] assumes the two proportions are representative of the same population, which is perfect for this null hypothesis test, justifying its usage.