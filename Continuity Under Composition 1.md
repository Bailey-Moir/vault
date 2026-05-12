---
tags:
  - atom
  - math
---
$$\forall f \in \mathcal{C}_{X}^Y, \forall g \in \mathcal{C}_{Y}^Z, (g \circ f) \in \mathcal{C}_{X}^Z$$
> [!proof]-
> Let $f$, $g$, and $W \in \mathcal{T}_{Z}$ be given.
> 
> By the [[Continuity|continuity]] of $g$, since $W \in \mathcal{T}_{Z}$, there exists $V \in \mathcal{T}_{Y}$ such that $V = g^{-1}(W)$.
> 
> By the [[Continuity|continuity]] of $f$, since $V \in \mathcal{T}_{Y}$, there exists $U \in \mathcal{T}_{X}$ such that $U = f^{-1}(V)$.
> 
> Thus, for all $W \in \mathcal{T}_{Z}$, $(g\circ f)^{-1}(W) = U \in \mathcal{T}_{X}$. $\square$

> [!theorem]- The same holds for partial [[Metric Continuity|metric continuity]] (e.g. at $x_{0}$).
> Let $\left( x_{n} \right) \subseteq X$ [[Metric Convergence|converge]] to $x_{0} \in X$.
> By the [[Metric Continuity#^sequences|sequence definition of metric continuity]], $\left( f(x_{n}) \right) \subseteq Y$ [[Metric Convergence|converges]] to $f(x_{0})$.
> Applying this again, $\left( g(f(x_{n})) \right) \subseteq Z$ [[Metric Convergence|converges]] to $g(f(x_{0}))$.
> 
> Thus, for every $\left( x_{n} \right) \subseteq X$ that [[Metric Convergence|converges]] to $x_{0} \in X$, $\left( (g \circ f)(x_{n}) \right) \subseteq Z$ [[Metric Convergence|converges]] to $(g \circ f)(x_{0}) \in Z$. Applying this same theorem again for the last time, $(g \circ f)$ is [[Metric Continuity|continuous]]  at $x_{0}$.

^metric