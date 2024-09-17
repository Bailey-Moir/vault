---
tags:
  - atom
  - stats
---
To test
$$\begin{align*}
	H_0 : \rho &= 0 \\
	H_a : \rho &\ne 0 \\
\end{align*}$$
(or a one-tailed alternative) we use the [[Test Statistic|standard test statistic]]
$$ t = \dfrac{r - 0}{\sqrt{\dfrac{1-r^2}{n-2}}} = \dfrac{r\sqrt{n-2}}{\sqrt{1-r^2}} $$
where $r$ is the [[Population v. Sample|sample]] [[Correlation|correlation]] for a sample of size $n$. To find the [[p-value|p-value]] we use a [[t-distributions|t-distribution]] with $n-2$ degrees of freedom.