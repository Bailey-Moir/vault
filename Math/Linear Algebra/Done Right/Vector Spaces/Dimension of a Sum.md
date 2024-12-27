---
tags:
  - atom
  - math
---
If $U$ and $W$ are [[Subspaces|subspaces]] of a [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]], then, similar to the [[Cardinality|cardinality]] law,
$$\begin{array}{rll}
	& \text{dim}(U+W) = \text{dim}\,U + \text{dim}\,W - \text{dim}(U \cap W) & \\
	\implies& \text{dim}(U \oplus W) = \text{dim}\,U + \text{dim}\,W &\phantom{\implies} \\
\end{array}$$

> [!proof]-
> Let $\vecbf{v}_{1}, \dots, \vecbf{v}_{n}$ be a [[Basis|basis]] of $U \cap W$, meaning $\text{dim}(U \cap W) = n$.
> 
> This implies that $\vecbf{v}_{1}, \dots, \vecbf{v}_{n}$ is [[Linear Independence|linearly independent]] in $U$ and $W$. Thus, it can be extended to
> - a [[Basis|basis]] $\vecbf{v}_{1}, \dots, \vecbf{v}_{n}, \vecbf{u}_{1}, \dots, \vecbf{u}_{j}$ of $U$, and
> - a [[Basis|basis]] $\vecbf{v}_{1}, \dots, \vecbf{v}_{n}, \vecbf{w}_{1}, \dots, \vecbf{w}_{k}$ of $W$.
> 
> Thus $\text{dim}\,U = m+j$ and $\text{dim}\,W = m + k$. If
> $$\begin{align*}
> 	\vecbf{v}_{1}, \dots, \vecbf{v}_{n}, , \vecbf{u}_{1}, \dots, \vecbf{u}_{j}, \vecbf{w}_{1}, \dots, \vecbf{w}_{k} && (1)
> \end{align*}$$
> is a [[Basis|basis]] of $U+W$, the proof will be complete as
> $$\begin{align*}
> 	\text{dim}(U+W) &= \text{dim}\,U + \text{dim}\,W - \text{dim}(U \cap W) \\
> 	&= (m+j) + (m+k) - (m) \\
> 	&= m+j+k \\
> \end{align*}$$
> 
> $$\begin{align*}
> 	U + W &= \text{span}(\vecbf{v}_{1}, \dots, \vecbf{v}_{n}, \vecbf{u}_{1}, \dots, \vecbf{u}_{j}) + \text{span}(\vecbf{v}_{1}, \dots, \vecbf{v}_{n}, \vecbf{w}_{1}, \dots, \vecbf{w}_{k}) \\
> 	&= \text{span}(\vecbf{v}_{1}, \dots, \vecbf{v}_{n}, \vecbf{u}_{1}, \dots, \vecbf{u}_{j}, \vecbf{w}_{1}, \dots, \vecbf{w}_{k}) \\
> \end{align*}$$
> Thus, $(1)$ is a [[Span|spanning list]] of $U+W$. To prove the [[Linear Independence|linear independence]] of $(1)$, consider
> $$\begin{align*}
> 	a_{1}\vecbf{v}_{1} + \dots + a_{n}\vecbf{v}_{n} + b_{1}\vecbf{u}_{1} + \dots + b_{j}\vecbf{u}_{j} + c_{1}\vecbf{w}_{1} + \dots + c_{k}\vecbf{w}_{k} = 0, && (2)
> \end{align*}$$
> where the $a$'s, $b$'s, and $c$'s are scalars. This can be rewritten as
> $$ c_{1}\vecbf{w}_{1} + \dots + c_{k}\vecbf{w}_{k} = -a_{1}\vecbf{v}_{1} - \dots - a_{n}\vecbf{v}_{n} - b_{1}\vecbf{u}_{1} - \dots - b_{j}\vecbf{u}_{j}. $$
> It is clear that $\text{RHS} \in U$ and $\text{LHS} \in W$, thus both sides must be in $U\cap W$. Since $\vecbf{v}_{1},\dots,\vecbf{v}_{n}$ is a [[Basis|basis]] of $U \cap W$, there must exist scalars $d_{1},\dots,d_{m}$ such that
> $$ c_{1}\vecbf{w}_{1} + \dots + c_{k}\vecbf{w}_{k} = d_{1}\vecbf{v}_{1} + \dots + d_{n}\vecbf{v}_{n},$$
> but since $\vecbf{v}_{1}, \dots, \vecbf{v}_{n}, \vecbf{w}_{1}, \dots, \vecbf{w}_{k}$ is [[Linear Independence|linearly independent]], the $c$'s and $d$'s must be $0$, meaning equation $(2)$ becomes
> $$\begin{align*}
> 	a_{1}\vecbf{v}_{1} + \dots + a_{n}\vecbf{v}_{n} + b_{1}\vecbf{u}_{1} + \dots + b_{j}\vecbf{u}_{j} = 0.
> \end{align*}$$
> but since $\vecbf{v}_{1}, \dots, \vecbf{v}_{n}, \vecbf{u}_{1}, \dots, \vecbf{u}_{j}$ is also [[Linear Independence|linearly independent]], the $a$'s and $b$'s must also be $0$, completing the proof.

\[[[Sums of Subspaces]], [[Direct Sums]]\]