---
tags:
  - atom
  - stats
---
The [[Proportion|proportion]] of samples giving a [[Statistics and Parameters|statistic]] as or more extreme than the observed statistic, **given the [[Statistical Hypotheses|null hypothesis]] is true**.

If the [[Percentile|percentile]] of the observed statistic on the randomisation distribution is $P$, and the observed statistic is $\hat \theta$, then:
$$p = \left\{\begin{array}{lr}
	P & \hat\theta < k \text{ (left tail)} \\ 
	1-P & \hat\theta > k \text{ (right tail)}\\ 
\end{array}\right.$$
The smaller the *$p$-value*, the stronger the statistical evidence against the [[Statistical Hypotheses|null hypothesis]] and in support of the [[Statistical Hypotheses|alternative hypothesis]]. If the $p$-value is below the [[Significance Level|significance level]], we say the sample results **statistically significant**. 

**One-sided** - The p-value is the proportion in the tail in the direction specific to $H_a$ further than $\hat \theta$.
**Two-sided** - The p-value is the proportion in the tail in the direction of $\hat\theta$ further than $\hat \theta$ **multiplied by two**.