---
tags:
  - atom
  - math
---
If $f : X\to Y$ is [[Continuous Maps|continuous]] and $U \in \mathcal{T}_{X}$, then $f \bigr|_{U} : U \to Y$ is [[Continuous Maps|continuous]];
$$\forall f \in \mathcal{C}_{X}^Y, \forall U \in \mathcal{T}_{X}, f \bigr|_{U} \in \mathcal{C}_{U}^Y$$
> [!proof]-
> Let $V \in \mathcal{T}_{Y}$. By the [[Continuous Maps|continuity]] of $f$, $f^{-1}(V) \in \mathcal{T}_{X}$.
> 
> Further, since $f\bigr|_{U}$ is a restriction of $f$,
> $$f^{-1}\bigr|_{U}(V) = f^{-1}(V) \cap U.$$
> By [[Topology|the axioms]], since this is a finite [[Unions & Intersections|intersection]] of elements in $\mathcal{T}_{X}$, $f^{-1}\bigr|_{U}(V) \in \mathcal{T}_{X}$. $\square$