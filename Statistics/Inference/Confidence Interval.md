---
tags:
  - atom
  - stats
---
A *confidence interval* is an [[Interval Estimate|interval estimate]] that captures the given [[Statistics and Parameters|population parameter]] for a specified [[Proportion|proportion]] of samples (the **confidence level**).

> **Confidence Level**
> The proportion of all samples whose intervals contain the parameter; the success rate. e.g. 95% or 99%.

If the sampling distribution is normal, then the [[Margin of Error|margin of error]] of this interval can be calculated using the [[Standard Error|standard error]] (the [[Standard Deviation|standard deviation]] of a [[Statistics and Parameters|statistic]]'s the sampling distribution). For example, if the **confidence level** is 95%, then 95% of the sample statistic's interval must contain the [[Point Estimate|point estimate]]/[[Statistics and Parameters|population parameter]], meaning the [[Margin of Error|margin of error]] must be two [[Standard Error|standard errors]].
\[[[The 95% Rule (of Thumb)|The 95% Rule (of Thumb)]]\]

This is an estimate, as our math works with the proportion of sample intervals that include the [[Point Estimate|point estimate]]  rather than the [[Statistics and Parameters|population parameter]], and the sample is an estimate of the population, so the sample distribution may vary.

Instead of using [[Standard Error|standard errors]], you can use percentiles instead. For example, for a confidence level of $\gamma$%, the interval will be:
$$ (\gamma n \text{-th entry}, (1-\gamma)n\text{-th entry}) $$
These intervals work for skewed (asymmetric) distributions, meaning that they can no longer be defined by the equation $\text{Statistic} \pm {MoE}$.

"We are 95% confident/sure that average amount of carbon per square kilometer in the tropical forest is between 9600 and 13600 tons."
"We are $\gamma$% confident/sure that the $\text{\{parameter\}}$ is between $\text{\{lower bound\}}$ and $\text{\{upper bound\}}$ tons."
**not probability**