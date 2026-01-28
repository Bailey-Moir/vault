---
tags:
  - atom
  - math
---
A [[Topology|topological space]] is called *first countable* iff every point has a countable [[Neighbourhood Bases|neighbourhood basis]].

> [!theorem-1]- [[Second Countable Spaces|Second countability]] $\to$ *first countability*.
> Suppose a [[Topology|topological space]] $\left( X,\mathcal{T} \right)$ is [[Second Countable Spaces|second countable]].
> Let $p \in X$. 
> 
> Let $\mathcal{B}$ be a [[Countability|countable]] [[Topological Bases|basis]] of $X$ given by [[Second Countable Spaces|second countability]]. Let 
> $$\mathcal{B}_{p} = \mathcal{N}_{p} \cap \mathcal{B}.$$
> Since $\mathcal{B}$ is [[Countability|countable]] and $\mathcal{B}_{p} \subseteq \mathcal{B}$, $\mathcal{B}_{p}$ is [[Countability|countable]]. All that remains to be shown is that $\mathcal{B}_{p}$ is a [[Neighbourhood Bases|neighbourhood basis]].
> 
> Let $A \in \mathcal{N}_{p}$. Since $A \in \mathcal{T}$, by the definition of a [[Topological Bases|basis]], $A = \bigcup \mathcal{C}$ for some $\mathcal{C} \in \mathcal{B}$.
> Since $p \in A$, there must be some $B \in \mathcal{C}$ such that $p \in B \subseteq A$.
> Thus, $B \in \mathcal{N}_{p} \cap \mathcal{B} = \mathcal{B}_{p}$, and by its definition $B \subseteq A$.