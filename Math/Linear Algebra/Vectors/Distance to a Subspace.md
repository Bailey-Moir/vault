---
tags:
  - atom
  - math
  - linear
---
For [[Subspaces|subspace]] $U$ of an [[Inner Products|inner product space]] $V$, the *[[Vector Length|distance]] from $\mathit{\vecbf{x}} \in V$ to $\mathit{U}$* is
$$d(\vecbf{x},U) = \| \vecbf{x} - \text{proj}_{U}\,\vecbf{x} \| = \| \text{perp}_{U}\,\vecbf{x} \| $$
where $d(\vecbf{x},U) := \underset{\vecbf{u} \in U}{\text{min}}\, d(\vecbf{x},\vecbf{u})$.

> [!theorem]- $\forall \vecbf{u} \in U, d(\vecbf{x}, \text{proj}_{U}\,\vecbf{x}) \le d(\vecbf{x}, \vecbf{u})$
> Let $\vecbf{u} \in U$. Consider the triangle in $V$ with vertices $$\begin{array}{ccc} A = \text{proj}_{U}\,\vecbf{x}, & B = \vecbf{u}, & C = \vecbf{x}.
> \end{array}$$
> The sides of this triangle correspond to
> ![400|center](distance-to-subspace.excalidraw)
> $$\begin{align}
> 	AB &= \vecbf{u} - \text{proj}_{U}\,\vecbf{x} \\
> 	AC &= \vecbf{x} - \text{proj}_{U}\,\vecbf{x} = \text{perp}_{U}\,\vecbf{x} \\
> 	BC &= \vecbf{x} - \vecbf{u} \\
> \end{align}$$
Since $AB \in U$ (by closure), and $AC$ is [[Orthogonal Projection|orthogonal]] to $U$, this is a right angle triangle; $AB \perp AC$.
> 
> By the [[Pythagoreas' Theorem|Pythagorean theorem]],
> $$\begin{align}
> 	\| AC \|^2 + \| AB \|^2 &= \| BC \|^2 \\
> 	\| \text{perp}_{U}\,\vecbf{x} \|^2 + \| \vecbf{u} - \text{proj}_{U}\,\vecbf{x} \|^2 &= \| \vecbf{x} - \vecbf{u} \|^2 \\
> 	d(\vecbf{x},\text{proj}_{U}\,\vecbf{x})^2 + \| \vecbf{u} - \text{proj}_{U}(\vecbf{x}) \|^2 &= d(\vecbf{x},\vecbf{u})^2 \\
> 	d(\vecbf{x},\text{proj}_{U}\,\vecbf{x})^2 &\le d(\vecbf{x},\vecbf{u})^2 \\
> 	d(\vecbf{x},\text{proj}_{U}\,\vecbf{x}) &\le d(\vecbf{x},\vecbf{u}) \\
> \end{align}$$

> [!note] In other words, $\text{proj}_{U}(\vecbf{x})$ is the closest point in $U$ to $\vecbf{x}$. This is often used in approximation.

\[[[Vector Length]], [[Vector Projection]]\]