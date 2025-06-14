---
tags:
  - atom
  - math
  - discrete
---
A *[[Vertices|vertex]] covering* $C$ of $G$ is a [[Sets|set]] of [[Vertices|vertices]] such that every [[Edges|edge]] of $G$ is incident with at least one [[Vertices|vertex]] in $C$;
$$\forall (u,v) \in E(G), u \in C \lor v \in C$$
> [!definition]- Minimum and Minimal Coverings
>  A *covering* $C$ of $G$ is a **minimum covering** iff there is no *covering* that has less [[Vertices|vertices]] than $C$.
>  
>  A *covering* $C$ of $G$ is a **minimal covering** iff no [[Vertices|vertices]] can be removed while maintaining $C$ being *covering*.

> [!theorem]
> For any *covering* $C$ and [[Matchings|matching]] $M$ of $G$,
> $$\left| M \right| \le \left| C \right|$$