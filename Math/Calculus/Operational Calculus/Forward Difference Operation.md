---
tags:
  - atom
  - math
---
The *forward difference* $\Delta$ of an arbitrary [[Functions|function]] is given by
$$\Delta f(x) = f(x+1) - f(x),$$
a [[Linear Maps|linear map]] operation.

> [!proof]- of [[Linear Maps|Linearity]]
> **[[Additive Property|Additive Property]]**
> $$\begin{align*}
> 	\Delta f(x) + \Delta g(x) &= f(x+1) - f(x) + g(x+1) - g(x) \\
> 	&= \left[ f(x+1) + g(x+1) \right] - \left[ f(x) + g(x) \right] \\
> 	&= \Delta\left[ f(x) + g(x) \right] \\
> \end{align*}$$
> **Homogeneity**
> $$\begin{align*}
> 	\Delta af(x) &= af(x+1) - af(x) \\
> 	&= a\left[ f(x+1) - f(x) \right] \\
> 	&= a\Delta f(x) \\
> \end{align*}$$