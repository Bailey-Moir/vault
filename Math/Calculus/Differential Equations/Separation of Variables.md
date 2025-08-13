---
tags:
  - atom
  - math
---
A method of solving [[Order|1st order]] [[Ordinary Differential Equations|ODEs]] where the derivative is the product of a [[Functions|function]] of the [[Explanatory and Response Variables|dependent variable]] ($y$) and a function of the [[Explanatory and Response Variables|independent variable]] ($x$). This uses the [[Integration by Substitution#Reverse Chain Rule|reverse chain rule]]. 
$$
\begin{align*}
	\dfrac{dy}{dx} &= f(x) \cdot g(y) && \ni g(y) \ne 0\\
	\dfrac{1}{g(y)} \dfrac{dy}{dx} &= f(x) \\
	\int \dfrac{1}{g(y)} \, dy &= \int f(x) \, dx
\end{align*}
$$

> [!theorem] If $\displaystyle\lim_{ y \to r }g(y) = \pm \infty$, then $y = r$ is a solution.