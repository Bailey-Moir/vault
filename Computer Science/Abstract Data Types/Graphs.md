---
tags:
  - atom
  - comp
---
[[Math/Discrete/Graph Theory/Graphs|Graphs]] are normally either represented with an **adjacency [[Matrices|matrix]]**, an **adjacency list**, or an **adjacency dictionary**.
- **Adjacency Matrix**
  In an *adjacency [[Matrices|matrix]]*, each entry $a_{ij}$ gives the [[Weighted Graphs|weighting]] of the edge([[Multigraphs|s]]) from [[Vertices|vertices]] $i$ to $j$. n Note an [[Directed Graphs|undirected graph]] has a [[Symmetric Matrices|symmetric]] *adjacency matrix*.
> [!complexity]-
> **Space Complexity:** The space complexity for an *adjacency matrix* is always $\mathcal{O}(\left| V \right|^2)$ (best and worst case).
- **Adjacency List**
  In an *adjacency list*, the $i$-th item contains a list of all of [[Vertices|vertices]] that [[Vertices|vertex]] $i$ is adjacent/incident to.
  > [!complexity]-
> **Space Complexity:** The space complexity for an *adjacency list* is always $\mathcal{O}(\left| V \right| + \left| E \right|)$ (best and worst case).
- **Adjacency Dictionary**
  An *adjacency dictionary* is the same as an **adjacency list** except instead of being a list of lists, it is a dictionary of lists.
