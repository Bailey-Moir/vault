---
tags:
  - atom
  - math
---
Define a [[Functions|function]] $f(x) = x^n$ for some $n \in \N$. Then $f$ is [[Differentiation|differentiable]] for all $a \in \R$ and $f'(a) = na^{n-1}$.

> [!proof]-
> $$\begin{align}
> 	f'(a) &= \lim_{ x \to a } \dfrac{f(x)-f(a)}{x-a} \\
> 	&= \lim_{ x \to a } \dfrac{x^n-a^n}{x-a} \\
> 	&= \lim_{ x \to a } \dfrac{\left( x-a \right)\sum_{k=0}^{n-1}x^{n-1-k}a^k}{x-a} \\
> 	&= \lim_{ x \to a } \sum_{k=0}^{n-1}x^{n-1-k}a^k \\
> 	&= \sum_{k=0}^{n-1}a^{n-1} \\
> 	&= na^{n-1} \\
> \end{align}$$