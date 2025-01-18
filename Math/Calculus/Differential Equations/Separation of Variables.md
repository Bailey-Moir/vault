---
tags:
  - atom
  - math
---
A method of solving [[Order|1st order]] DEs where the derivative is the product of a function of the dependent variable ($y$) and a function of the independent variable ($x$). This uses the [[Integration by Substitution#Reverse Chain Rule|reverse chain rule]]. 
$$
\begin{align*}
	\dfrac{dy}{dx} &= f(x) \cdot g(y) && \ni g(y) \ne 0\\
	\dfrac{1}{g(y)} \dfrac{dy}{dx} &= f(x) \\
	\int \dfrac{1}{g(y)} \, dy &= \int f(x) \, dx
\end{align*}
$$