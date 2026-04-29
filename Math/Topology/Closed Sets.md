---
tags:
  - atom
  - math
---
A [[Subsets|subset]] $S \subseteq X$ of a [[Topology|topological space]] $\left( X,\mathcal{T} \right)$ is a *closed set* iff its [[Complement|complement]] is [[Open Sets|open]] ($S^c \in \mathcal{T}$).

The axioms of a [[Topology|topology]]/[[Open Sets|open set]] can be restated in terms of *closed sets* as so:
1. $\emptyset$ and $X$ are *closed*,
2. *closed sets* are closed under finite [[Unions & Intersections|unions]], and
3. they are closed under arbitrary [[Unions & Intersections|intersections]].

> [!proof]-
> $X^c = \emptyset \in \mathcal{T}$, and $\emptyset^c = X \in \mathcal{T}$.
> 
> Let $A_{i}$ be a *closed set* for $i \in I$ for some [[Indexing Set|indexing set]] $I$. Then
> $$\begin{align}
> 	A &= \bigcap_{i \in I} A_{i} \\
> 	A^c &= \left( \bigcap_{i \in I} A_{i} \right)^c \\
> 	&= \bigcup_{i \in I} A_{i}^c. \\
> \end{align}$$
> Thus, $A$ is *closed*, as $A^c_{i} \in \mathcal{T}$ for all $i \in I$, and [[Open Sets|open sets]] are closed under arbitrary union.
> 
> Let $A_{1},\dots,A_{n}$ be *closed sets*.  Then
> $$\begin{align}
> 	A &= \bigcup_{i \in 0}^n A_{i} \\
> 	A^c &= \left( \bigcup_{i \in 0}^n A_{i} \right)^c \\
> 	&= \bigcap_{i \in 0}^n A_{i}^c. \\
> \end{align}$$
> Thus, $A$ is *closed*, as $A^c_{i} \in \mathcal{T}$ for all $i$, and [[Open Sets|open sets]] are closed under finite intersection.