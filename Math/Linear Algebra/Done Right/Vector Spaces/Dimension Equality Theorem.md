---
tags:
  - atom
  - math
---
If $U$ is a [[Subspaces|subspace]] of a [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]] $V$,
$$ \text{dim}(U)=\text{dim}(V) \implies U=V $$

> [!proof]-
> Let $B = \vecbf{u}_{1}, \dots, \vecbf{u}_{n}$ be a [[Basis|basis]] of $U$. 
> 
> Thus, since $U$ is a [[Subspaces|subspace]] of $V$ and $\text{dim}(U)=\text{dim}(V)$, $B$ is a [[Linear Independence|linearly independent]] [[Lists|list]] in $V$ of length $\text{dim}(V)$.
> 
> Thus, $B$ must be a [[Basis|basis]] of $V$[^1].
> 
> This means $V=\text{span}(B) = U$[^2], thus $U = V$.

[^1]: [[Linear Independence and Span with Dimension]]
[^2]: [[Span]]