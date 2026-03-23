---
tags:
  - atom
  - math
  - comp
  - discrete
---
A *components* of a [[Graphs|graph]] $G = (V,E)$ is a [[Subgraphs|subgraph]] $G' = (V',E')$ where
- $G'$ is a non-empty [[Subgraphs|subgraph]].
- Every pair of vertices $G'$ is connected by a [[Walks|path]] in $G$.
- $\forall u', v' \in V', d_{G}(u',v') \ne \infty$
- $\forall u \in V', v' \in V \setminus V', d_{G}(u,v') = \infty$
- $\forall (u,v) \in E, \left( u \in V' \lor v \in V' \to (u,v) \in E'  \right)$

In other words, a *component* of a [[Graphs|graph]] is a maximal [[Connectivitiy|connected]] [[Subgraphs|subgraph]].
