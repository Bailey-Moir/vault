---
tags:
  - atom
  - math
  - linear
---
If $U$ is a [[Subspaces|subspace]] of a [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]] $V$,
$$ \text{dim}(U)=\text{dim}(V) \iff U=V $$

> [!proof]-
> ($\implies$)
> Let $B = \vecbf{u}_{1}, \dots, \vecbf{u}_{n}$ be a [[Vector Bases|basis]] of $U$. 
> 
> Thus, since $U$ is a [[Subspaces|subspace]] of $V$ and $\text{dim}(U)=\text{dim}(V)$, $B$ is a [[Linear Independence|linearly independent]] [[Lists|list]] in $V$ of length $\text{dim}(V)$.
> 
> Thus, $B$ must be a [[Vector Bases|basis]] of $V$[^1].
> 
> This means $V=\text{span}(B) = U$[^2], thus $U = V$.
> 
> ($\impliedby$)
> Since $U = V$, they obviously must have the same [[Dimension|dimension]].

[^1]: [[Linear Independence and Span with Dimension]]
[^2]: [[Span]]