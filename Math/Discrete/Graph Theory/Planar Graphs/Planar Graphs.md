---
tags:
  - atom
  - math
  - discrete
---
A [[Graphs|graph]] is *planar* if it can be drawn in the **plane** without any [[Edges|edges]] crossing. Such a drawing is called a *planar drawing*.

> [!definition] A *planar drawing* [[Partitions|partitions]] the plane into **faces**. The **face** not enclosed is called the **exterior face**.

> [!lemma] Let $G$ be a *planar graph*, and let $e \in E(G)$.
> - If $e$ lies on a [[Walks|cycle]] of $G$, then $e$ lies on the boundary of exactly $2$ faces of $G$.
> - If $e$ is a [[Bridges|bridge]] (not on a [[Walks|cycle]]) of $G$, then $e$ lies on the boundary of exactly $1$ face of $G$.