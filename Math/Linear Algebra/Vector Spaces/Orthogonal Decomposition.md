---
tags:
  - atom
  - math
  - linear
---
For [[Subspaces|subspace]] $U$ of an [[Inner Products|inner product space]] $V$, and the [[Orthogonal Complements|orthogonal complement]] $U^\bot$ of $U$ under $V$,
$$V = U \oplus U^\bot$$
\[[[Direct Sums]]\]

> [!note]
> For $\vecbf{x} \in V$, the $\vecbf{u} \in U$ and $\vecbf{u}^\bot \in U^\bot$ such that $\vecbf{x} = \vecbf{u} + \vecbf{u}^\bot$ are given by
> $$\begin{align}
> 	\text{proj}_{U}(\vecbf{x}) &= \vecbf{u} \\
> 	\text{perp}_{U}(\vecbf{x}) &= \vecbf{u}^\bot \color{gray}=\text{proj}_{U^\bot}(\vecbf{x})\\
> \end{align}$$

> [!proof]-
> As shown in the [[Orthogonal Complements|orthogonal complements lemma]],
> $$\text{dim}\,U + \text{dim}\,U^\bot = V.$$
> Thus, $V$ can be written as a [[Linear Combinations|linear combination]] of the combined [[Basis|basis vectors]] of $U$ and $U^\bot$.
> $$\vecbf{x}  = \underbrace{c_{1}\vecbf{u}_{1} + \dots + c_{m}\vecbf{u}_{m}}_{U} + \underbrace{c_{m+1}\vecbf{u}_{m+1} + \dots + c_{n}\vecbf{u}_{n}}_{U^\bot}$$
> This is a [[Basis|basis]], as $U$ and $U^\bot$ are [[Linear Independence|linearly independent]] (by definition), so each of their [[Basis|basis vectors]] are [[Linear Independence|linearly independent]].
