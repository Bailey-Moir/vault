---
tags:
  - atom
  - math
  - comp
  - discrete
---
A *components* of a [[Graphs|graph]] $G = (V,E)$ is a [[Subgraphs|subgraph]] $G' = (V',E')$ where
- $G'$ is a non-empty [[Subgraphs|subgraph]].
- $G' \ne \emptyset$
- Every pair of vertices $G'$ is connected by a [[Walks|path]] in $G$.
- $\forall v' \in V, u \in V \setminus V', d_{G}(v',u) = \infty$
- $\forall (u,v) \in E, \left( u \in V' \lor v \in V' \to (u,v) \in E'  \right)$

In other words, a *component* of a [[Graphs|graph]] is a maximal [[Connectivitiy|connected]] [[Subgraphs|subgraph]].
