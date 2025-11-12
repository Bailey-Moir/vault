---
tags:
  - atom
  - math
---
For a [[Functions|function]] $f$, we say a point $a \in\text{dom}\,f$ is a
- **local maximum** iff for all $x$ [[Defined Near|near]] (and at) $a$, $f(x) \le f(a)$, and a
- **local minimum** iff for all $x$ [[Defined Near|near]] (and at) $a$, $f(x) \ge f(a)$.

> [!theorem]- If a [[Functions|function]] $f$ is [[Differentiation|differentiable]] at a *local extrema* $a$, then $f'(a) = 0$
> Suppose $a$ is a **local maximum**, meaning for all $x$ on some [[Intervals|open interval]] $I_{1}$ containing $a$, $f(x) \le f(a)$. 
> Since $f$ is [[Differentiation|differentiable]] at $a$, by [[Limiting Function of Differentiation|theorem 5.2]], there exists $\phi \in \mathcal{C}(\{ a \})$ such that on some [[Intervals|open interval]] $I_{2}$ containing $a$,
> $$f(x) = f(a) + (x-a)\phi(x).$$
> Let $I = I_{1}\cap I_{2}$. Then for all $x \in I$, $f(x) = f(a) + (x-a)\phi(x)$ and $f(x) \le f(a)$, giving
> $$\begin{align}
> 	f(a) + (x-a)\phi(x) = f(x) &\le f(a) \\
> 	f(a) + (x-a)\phi(x)&\le f(a) \\
> 	(x-a)\phi(x)&\le 0 \\
> \end{align}$$
> For $x>a$, dividing this [[Inequalities|inequality]] by $x-a> 0$ gives $\phi(x)\le 0$.
> For $x<a$, dividing this [[Inequalities|inequality]] by $x-a < 0$ gives $\phi(x)\ge 0$.
> Thus, $\lim_{ x \to a^{+} } \phi(x) \le 0$ and $\lim_{ x \to a^{-} } \phi(x) \ge 0$, so by [[Two-Sided Limit Theorem|two-sided limit theorem]],
> $$f'(a) = \phi(a) = \lim_{ x \to a } \phi(x) = 0.$$

> [!note] All *local extrema* are [[Critical Points|critical points]].

[^1]: [[Continuity of Differentiable Functions]]
