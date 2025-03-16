---
tags:
  - atom
  - math
  - comp
  - discrete
---
A *components* of a [[Graphs|graph]] $G = (V,E)$ is a [[Subgraphs|subgraph]] $G' = (V',E')$ where
- $G'$ is a non-empty [[Subgraphs|subgraph]].
- Every pair of vertices in $G'$ is connected by a [[Walks|path]] in $G$.
- For all $v' \in V'$ and $u \in V\setminus V'$, there is no [[Walks|path]] between $v'$ and $u$ in $G$.
- $E'$ contains all [[Edges|edges]] in $E$ that involve [[Vertices|vertices]] in $V'$.

In other words, a *component* of a [[Graphs|graph]] is a maximal [[Connectivitiy|connected]] [[Subgraphs|subgraph]].
