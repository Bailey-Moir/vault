---
tags:
  - atom
  - math
---
A general method for solving [[Linear Differential Equations|linear]] [[Order|1st order]] DEs, i.e. DEs that can be put into the following **standard form**:
$$ y' + p(x) \cdot y = q(x) $$
$$ \begin{align*}
	\mu \left( y' + p(x) \cdot y \right) &= \mu \cdot q(x) && \text{s.t. }\mu = e^{\int p(x) \, dx} \\
	\dfrac{d}{dx} \left( \mu \cdot y \right) &= \\
	y &= \dfrac{1}{\mu} \int \mu \cdot q(x) \, dx \\
\end{align*} $$
This working can often be skipped and replaced with [[Bernoulli Equations|Bernoulli's equation]] where $n=0$.
$$ y' + p(x)y = q(x) \implies y = \dfrac{1}{\mu} \int \mu \cdot q(x) \, dx \,\text{  s.t. }\, \mu = e^{\int p(x) \, dx} $$