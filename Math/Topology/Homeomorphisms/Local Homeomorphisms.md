---
tags:
  - atom
  - math
---
A [[Functions|function]] $f$ between [[Topology|topological spaces]] $X$ and $Y$ is a *local homeomorphism* iff every point $p \in X$ has a [[Neighbourhoods|neighbourhood]] on which $f$ is a [[Homeomorphisms|homeomorphism]], and $f(U) \in \mathcal{T}_{Y}$; iff
$$\forall p \in X, \exists U \in \mathcal{N}_{p} : f(U) \in \mathcal{T}_{Y} \land  f\bigr|_{U} \text{ is a homeomorphism}$$
> [!theorem-1]- A [[Bijective Functions|bijective]] *local homeomorphism* is a [[Homeomorphisms|homeomorphism]].
> Let $f:X \to Y$ be a [[Bijective Functions|bijective]] *local homeomorphism*.
> 
> Let $U \in \mathcal{T}_{X}$, and let $y \in f(U)$ where $y = f(x)$ for some $x \in U$.
> 
> Since $f$ is a *local homeomorphism*, $x$ has a [[Neighbourhoods|neighbourhood]] $V$ such that $f(V) \in \mathcal{T}_{Y}$ and $f\bigr|_{V}$ is a [[Homeomorphisms|homeomorphism]].
> 
> $U \cap V \in \mathcal{T}_{X}$, so since $f\bigr|_{V}$ is a [[Homeomorphisms|homeomorphism]] (and $U \cap V \subseteq V$), $f(U \cap V) \in \mathcal{T}_{Y}$. 
> 
> Since $y \in f(U \cap V) \subseteq f(U)$, every point $y \in f(U)$ has [[Neighbourhoods|neighbourhood]] ($U \cap V$) contained in $f(U)$.
> Thus, by the [[Interiors|characterisation of interiors]], $f(U) = \text{int}\,f(U)$, meaning $f(U) \in \mathcal{T}_{Y}$[^1].
> 
> Thus, $\forall U \in \mathcal{T}_{X}, f(U) \in \mathcal{T}_{Y}$, so $f$ is a [[Bijective Functions|bijective]] [[Open & Closed Maps|open map]], so $f$ is [[Homeomorphisms|homeomorphic]][^2].


[^1]: [[Interiors]], Theorem 1

[^2]: [[Open & Closed Maps]], Theorem 1
