---
tags:
  - atom
  - math
  - linear
---
The *forward difference* $\Delta \in \mathcal{L}(?)$[^1] of an arbitrary [[Functions|function]] $f$ is given by
$$\Delta f(x) = f(x+1) - f(x),$$

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

[^1]: [[Linear Maps]]
