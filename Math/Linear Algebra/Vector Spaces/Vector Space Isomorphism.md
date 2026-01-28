---
tags:
  - atom
  - math
  - linear
---
Two [[Vector Spaces|vector spaces]] are *isomorphic* iff there exists an *isomorphism* (an [[Linear Map Invertibility|invertible]]/[[Bijective Functions|bijective]] [[Linear Maps|linear map]]) between them.

> [!proof]- Two [[Finite-Dimensional Vector Spaces|finite-dimensional vector spaces]] $V, W$ over $\F$ are *isomorphic* iff $\text{dim}\,V =\text{dim}\,W$.
> ($\implies$)
> If $V$ and $W$ are *isomorphic*, there must exist a [[Bijective Functions|bijective map]] between them, meaning $\text{dim}\,V =\text{dim}\,W$ by \[[[Function Types with Dimension]]\] or \[[[Rank-Nullity Theorem]]\].
> 
> ($\impliedby$)
> Suppose $\vecbf{v}_{1},\dots,\vecbf{v}_{n}$ and $\vecbf{w}_{1},\dots,\vecbf{w}_{n}$ are bases of $V$ and $W$ respectively.
> Let $T \in \mathcal{L}(V,W)$ be defined by
> $$T\left( a_{1}\vecbf{v}_{1}+\dots+a_{n}\vecbf{v}_{n} \right) = a_{1}\vecbf{w}_{1} + \dots + a_{n}\vecbf{w}_{n}.$$
> By the [[Linear Map Lemma|linear map lemma]], $T$ is well-defined.
>  $T$ is surjective as $\vecbf{w}_{1},\dots,\vecbf{w}_{n}$ [[Span|spans]] $W$, and it is also [[Injective Functions|injective]] as $\vecbf{w}_{1},\dots,\vecbf{w}_{n}$ is [[Linear Independence|linearly independent]], meaning $\text{null}\,T = \{ \vecbf{0} \}$.
> Thus, $T$ is [[Bijective Functions|bijective]],  and thus an *isomorphism*, meaning the spaces are *isomorphic*.

\[[[Isomorphisms]]\]