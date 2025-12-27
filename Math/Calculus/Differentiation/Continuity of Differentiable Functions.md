---
tags:
  - atom
  - math
---
Let $f$ be a [[Functions|function]] and $a \in\text{dom}\,f$. Then if $f$ is [[Differentiation|differentiable]] at $a$, then $f$ is [[Math/Calculus/Limits/Continuity/Continuity|continuous]] at $a$.

> [!proof]- **5.3**
> Since $f(a)$ is a constant, and $x-a$ is a polynomial, and $\phi(x)$ is [[Math/Calculus/Limits/Continuity/Continuity|continuous]] at $a$, they are all [[Limits of Real Functions|convergent]] at $a$ and (by the [[Limit Laws|limit laws]]),
> $$\begin{align}
> 	f(x) &= f(a) + (x-a)\phi(x) \\
> 	\lim_{ x \to a } f(x) &= \lim_{ x \to a } f(a) + \lim_{ x \to a } (x-a) \times \lim_{ x \to a } \phi(x) \\
> 	\lim_{ x \to a } f(x) &= f(a) + 0 \times \phi(a) \\
> 	\lim_{ x \to a } f(x) &= f(a). \\
> \end{align}$$
> Thus, $f(x)$ is [[Math/Calculus/Limits/Continuity/Continuity|continuous]] as $a$.