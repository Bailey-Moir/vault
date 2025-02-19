---
tags:
  - atom
  - math
---
If $V_{1},\dots,V_{n}$ are [[Finite-Dimensional Vector Spaces|finite-dimensional vector spaces]], then, contrarily to the [[Cardinality|cardinality]] law for [[Cartesian Product|Cartesian products]],
$$ \text{dim}(V_{1}\times \dots \times V_{n}) = \text{dim}\,V_{1} + \dots + \text{dim}\,V_{n} $$

> [!proof]-
> Choose a [[Basis|basis]] for each $V_{k}$. For each [[Basis|basis vector]] $\vecbf{v}$ of each $V_{k}$, consider
> $$\begin{array}{cccccc}
> 	(\vecbf{0}, &\cdots, &\vecbf{v}, &\cdots, &\vecbf{0}) &\hspace{-0.8em}\in V_{1}\times \dots \times V_{n} \\
> 	\tiny 0\text{-th} && \tiny k\text{-th} && \tiny n\text{-th} &\\
> \end{array}$$
> These vectors are [[Linear Independence|linearly independent]] and [[Span|span]] $V_{1}\times \dots \times V_{n}$. Thus, this is a [[Basis|basis]] of length $\text{dim}\,V_{1} + \dots + \text{dim}\,V_{n}$.

\[[[Products of Vector Spaces]]\]