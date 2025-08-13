---
tags:
  - atom
  - math
  - linear
---
For a [[Subspaces|subspace]] $U$ of a [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]] $V$,
$$\text{dim}\,U^0 = \text{dim}\,V - \text{dim}\,U$$

> [!proof]-
> Let $i \in \mathcal{L}(U,V)$ be the inclusion [[Linear Maps|map]] defined by $i(\vecbf{u})=\vecbf{u}$ for each $\vecbf{u} \in U$.
> 
> Thus, $i'$[^1] is a [[Linear Maps|linear map]] from $V'$ to $U'$. By [[Rank-Nullity Theorem|rank-nullity theorem]],
> $$\begin{align}
> 	\text{dim}\,V' &= \text{rank}\,i' + \text{nullity}\,i' \\
> 	&= \text{rank}\,i' + \text{dim}\,U^0 && \text{null}\,i' = U^0 \\
> 	\text{dim}\,V&= \text{rank}\,i' + \text{dim}\,U^0 && \text{dim}\,V' = \text{dim}\,V \\
> \end{align}$$
> If $\varphi \in U'$, then $\varphi$ can be [[Linear Independence and Span with Dimension|extended]] to a [[Linear Functionals|linear functional]] $\psi \in V'$. The definition of $i'$ gives $i'(\psi) = \varphi$. Thus, $\varphi \in\text{range}\,i'$ ($\forall \varphi \in U'$), meaning $\text{range}\,i'=U'$, meaning
> $$\text{rank}\,i' = \text{dim}\,\text{range}\,i' = \text{dim}\,U' = \text{dim}\, U.$$
> Thus,
> $$\begin{align}
> 	\text{dim}\,V &= \text{dim}\,U + \text{dim}\,U^0 \\
> 	\text{dim}\,U^0 &= \text{dim}\,V - \text{dim}\,U \\
> \end{align}$$

> [!corollary]- For a [[Subspaces|subspace]] of a [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]] $V$, <ul style="margin-top:0.5em"><li> $U^0 = \{ 0 \} \iff U = V$, and <li> $U^0 = V' \iff U = \{ \vecbf{0} \}$.</ul>
> The first item is given by
> $$\begin{align}
> 	U^0 = \{ 0 \} &\iff \text{dim}\,U^0 = 0 \\
> 	&\iff \text{dim}\,V = \text{dim}\,U && \text{Ant.}\\
> 	&\iff V = U, && (1) \\
> \end{align}$$
> 
> and the second item is given by
> $$\begin{align}
> 	U^0 = V' &\iff \text{dim}\, U^0 = \text{dim}\,V' && (1) \\
> 	&\iff \text{dim}\, V - \text{dim}\,U = \text{dim}\,V && (2), \text{Ant.} \\
> 	&\iff \text{dim}\,U = 0 \\
> 	&\iff U = \{ \vecbf{0} \} \\
> \end{align}$$
> \[$(1)$ [[Dimension Equality Theorem]], $(2)$ [[Dual Space]], Theorem 1\]


\[[[Annihilators]]\]

[^1]: [[Dual Map]]
