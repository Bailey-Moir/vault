---
tags:
  - atom
  - math
---
Let $f$ be a [[Functions|function]] and $a \in\text{dom}\,f$. Then $f$ is [[Differentiation|differentiable]] at $a$ iff there exists a [[Functions|function]] $\phi \in \mathcal{C}(\{ a \})$ such that
$$\begin{array}{c}
	\dfrac{f(x)-f(a)}{x-a} = \phi(x) \\
	f(x) = f(a) + (x-a)\phi(x)
\end{array}$$
[[Defined Near|near]] (and at) $a$. More over, if such a $\phi$ exists, then $f'(a) = \phi(a)$.

> [!proof]- **5.2**
> $\left( \impliedby \right)$
> If $f(x) = f(a) + (x-a)\phi(x)$ as above, then we rearrange to get
> $$\begin{align}
> 	\dfrac{f(x)-f(a)}{x-a} &= \phi(x) \\
> 	\lim_{ x \to a } \dfrac{f(x)-f(a)}{x-a} &= \lim_{ x \to a } \phi(x) \\
> 	f'(a) &= \phi(a), \\
> \end{align}$$
> by the [[Continuity|continuity]] of $\phi$.
> 
> $\left( \implies \right)$
> Suppose $f$ is [[Differentiation|differentiable]] at $a$. Define
> $$\phi(x) = \begin{cases}
> 	\dfrac{f(x)-f(a)}{x-a} & x \ne a \\
> 	f'(a) & x = a
> \end{cases}$$
> 
> Thus, by the [[Limits of Real Functions|epsilon-delta definition of a limit]] with [[Differentiation|differentiation]], $\phi$ must be [[Defined Near|defined near]] (and at) $a$.
> 
> $\phi$ is [[Continuity|continuous]] at $a$ since
> $$\lim_{ x \to a } \phi(x) = \lim_{ x \to a } \dfrac{f(x)-f(a)}{x-a} = f'(a) = \phi(a),$$
> by definition.