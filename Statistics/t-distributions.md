---
tags:
  - atom
  - stats
---
Replacing $\sigma$ with $s$ changes the distribution of the [[Test Statistic|test statistic]] from a [[Normal Distributions|normal distribution]] to a *$t$-distribution*.
- *$t$-distributions* have slightly thicker tails than [[Normal Distributions|normal distributions]] to reflect the added uncertainty.
- They are characterized by their **degrees of freedom ($\mathbf{df}$)**, which can be calculated based on the sample size ($s$). The $\bf{df}$ represent the number of values that are free to vary. In the case of the *$t$-distribution*, the degrees of freedom are $n-1$ as one degree of freedom is reserved for estimating the mean, and $n-1$ degrees remain for estimating the variability.
$$\begin{array}{ccc}
t\text{-distribution} \to \text{normal distirbution} & \text{ as } & df \to \infty
\end{array}$$

*$t$-distributions* require that either the sample size is sufficiently large ($n \ge 30$) or that the **data comes from an approximately normal population**.

\[[[Standard Deviation]]\]