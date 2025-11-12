---
tags:
  - atom
  - math
---
![[lipschitz-continuity.gif|350]]
A [[Functions|function]] $f$ is *Lipschitz continuous* on $I$ iff
$$\begin{align}
	\exists M > 0 : \forall x,y \in I, \left| f(x) - f(y) \right| &\le M\left| x - y \right| \\
	\left| \dfrac{f(x) - f(y)}{x - y} \right| &\le M, \\
\end{align}$$
> [!note] Note the similarity to the [[Functions|function]] $\phi$ from \[[[Limiting Function of Differentiation]]\].

> [!theorem]- For $f$ on $I$, *Lipschitz continuity* implies [[Uniform Continuity|uniform continuity]].
> Let $\varepsilon > 0$ be given, and $\delta = \dfrac{\varepsilon}{M}$. Then if $\left| x-y \right| < \delta$,
> $$\begin{align}
> 	\left| x-y \right| &< \dfrac{\varepsilon}{M} \\
> 	M\left| x-y \right| &< \varepsilon.
> \end{align}$$
> Thus, by the *Lipschitz continuity* of $f$ on $I$,
> $$\begin{align}
> 	\left| f(x)-f(y) \right| \le M\left| x-y \right| &< \varepsilon \\
> 	\left| f(x)-f(y) \right| &< \varepsilon && \square
> \end{align}$$