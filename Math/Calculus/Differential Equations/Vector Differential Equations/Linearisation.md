---
tags:
  - atom
  - math
---
Let $\vecbf{x}' = \vecbf{F}(\vecbf{x})$, and $\vecbf{x}_{*}$ be a [[Fixed Points|fixed point]]. Let $\vecbf{x} = \vecbf{x}_{*} + \vecbf{\delta}$ be a point near $\vecbf{x}_{*}$. Then
$$\vecbf{\delta}' = \mathbf{J}_{\vecbf{F}}(\vecbf{x}_{*})\delta.$$
> [!proof]- with 1D
> Let $x_{*}$ be a fixed point of $x' = g(x)$, and let $x = x_{*} + \delta$ for some small $\delta$. By [[Taylor Series|Taylor's theorem]] about $x_{*}$,
> $$\begin{align}
> 	g(x) &= g(x_{*}) + g'(x_{*})(x-x_{*}) + R_{1}(x) \\
> 	&= 0 + g'(x_{*})((x_{*} + \delta)-x_{*}) + R_{1}(x_{*}+\delta) \\
> 	&= g'(x_{*})\delta + R_{1}(x_{*}+\delta) \\
> \end{align}$$
> By [[Taylor's Remainder Theorem|Taylor's remainder theorem]], there exists $c$ between $x_{*}$ and $x_{*}+\delta$ such that
> $$\begin{align}
> 	R_{1}(x_{*}+\delta) &= \dfrac{g''(c)}{2}((x_{*}+\delta)-x_{*})^{2} \\
> 	&= \dfrac{g''(c)}{2}\delta^{2}. \\
> \end{align}$$
> Thus,
> $$\begin{align}
> 	\delta' &= (x_{*} + \delta)' && x_{*} \text{ is constant}\\
> 	&= x' \\
> 	&= g(x) \\
> 	&= g'(x_{*})\delta + \dfrac{g''(c)}{2}\delta^2 \\
> 	&= g'(x_{*})\delta + \mathcal{O}(\delta^2). \\
> \end{align}$$
> So as an approximation near $x_{*}$,
> $$\delta' = g'(x_{*})\delta$$

> [!theorem] Linearisation Theorem
> Let $\lambda_{1},\lambda_{2},\dots,\lambda_{n}$ be the [[Eigenvectors & Eigenvalues|eigenvalues]] of $\mathbf{J}_{\vecbf{F}(\vecbf{x}_{*})}$. Then if
> - $\forall k, \Re(\lambda_{k}) < 0$, then $\vecbf{x}_{*}$ is a [[Stable and Unstable Nodes|stable node (or spiral)]].
> - $\forall k, \Re(\lambda_{k}) > 0$, then $\vecbf{x}_{*}$ is a [[Stable and Unstable Nodes|unstable node (or spiral)]].
> - $\exists j,k : \Re(\lambda_{j}) < 0 < \Re(\lambda_{k})$, then $\vecbf{x}_{*}$ is a [[Hyperbolic Systems|saddle]].

> [!caution] This applies iff $\Re(\lambda_{k}) \ne 0$ for all $\lambda_{k}$.

\[[[Jacobian Matrices]]\]