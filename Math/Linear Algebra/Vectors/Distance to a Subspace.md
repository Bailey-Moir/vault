---
tags:
  - atom
  - math
  - linear
---
For a [[Math/Linear Algebra/Vectors/Vectors|vector]] $\vecbf{x} \in \R^n$ and [[Subspaces|subspace]] $U$ of $\R^n$, the *distance from $\mathit{\vecbf{x}}$ to $\mathit{U}$* is
$$d(\vecbf{x},U) = \| \vecbf{x} - \text{proj}_{U}(\vecbf{x}) \| = \| \text{perp}_{U}(\vecbf{x}) \| $$
where $d(\vecbf{x},U) := \underset{\vecbf{u} \in U}{\text{min}}\, d(\vecbf{x},\vecbf{u})$.

> [!theorem]- $\forall \vecbf{u} \in U, d(\vecbf{x}, \vecbf{u}) \geq d(\vecbf{x}, \text{proj}_{U}(\vecbf{x}))$
> Let $\vecbf{u} \in U$. Consider the triangle in $\R^n$ with vertices $$\begin{array}{ccc} A = \text{proj}_{U}(\vecbf{x}), & B = \vecbf{u}, & C = \vecbf{x}.
> \end{array}$$
> The sides of this triangle correspond to
> ![400|center](distance-to-subspace.excalidraw)
> $$\begin{align}
> 	AB &= \vecbf{u} - \text{proj}_{U}(\vecbf{x}) \\
> 	AC &= \vecbf{x} - \text{proj}_{U}(\vecbf{x}) = \text{perp}_{U}(\vecbf{x}) \\
> 	BC &= \vecbf{x} - \vecbf{u} \\
> \end{align}$$
Since $AB \in U$ (by closure), and $AC$ is [[Orthogonal Projection|orthogonal]] to $U$, this is a right angle triangle; $AB \perp AC$.
> 
> By the Pythagorean theorem,
> $$\begin{align}
> 	\| AC \|^2 + \| AB \|^2 &= \| BC \|^2 \\
> 	\| \text{perp}_{U}(\vecbf{x}) \|^2 + \| \vecbf{u} - \text{proj}_{U}(\vecbf{x}) \|^2 &= \| \vecbf{x} - \vecbf{u} \|^2 \\
> 	d(\vecbf{x},U)^2 + \| \vecbf{u} - \text{proj}_{U}(\vecbf{x}) \|^2 &= d(\vecbf{x},\vecbf{u})^2 \\
> 	d(\vecbf{x},U)^2 &\le d(\vecbf{x},\vecbf{u})^2 \\
> 	d(\vecbf{x},U) &\le d(\vecbf{x},\vecbf{u}) \\
> \end{align}$$

> [!note] $\text{proj}_{U}(\vecbf{x})$ is the closest point $U$ to $\vecbf{x}$.

\[[[Vector Length]], [[Vector Projection]]\]