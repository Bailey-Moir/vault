---
tags:
  - atom
  - math
---
$$\forall f \in \mathcal{C}_{X}^Y, \forall g \in \mathcal{C}_{Y}^Z, (g \circ f) \in \mathcal{C}_{X}^Z$$
> [!proof]-
> Let $f$, $g$, and $W \in \mathcal{T}_{Z}$ be given.
> 
> By the [[Continuous Maps|continuity]] of $g$, since $W \in \mathcal{T}_{Z}$, there exists $V \in \mathcal{T}_{Y}$ such that $V = g^{-1}(W)$.
> 
> By the [[Continuous Maps|continuity]] of $f$, since $V \in \mathcal{T}_{Y}$, there exists $U \in \mathcal{T}_{X}$ such that $U = f^{-1}(V)$.
> 
> Thus, for all $W \in \mathcal{T}_{Z}$, $(g\circ f)^{-1}(W) = V \in \mathcal{T}_{X}$. $\square$
