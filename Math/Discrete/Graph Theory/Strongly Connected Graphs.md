---
tags:
  - atom
  - math
  - discrete
---
A [[Directed Graphs|directed graph]] is *strongly connected* iff there is a [[Walks|path]] between every [[Ordered Sets|ordered pair]] of [[Vertices|vertices]].

> [!algorithm]
> This can be tested for by starting a [[Vertices|vertex]] $h$, and
> 1. Run a [[Graph Traversal|graph traversal]] ([[Breadth First Search|BFS]] or [[Depth First Search|DFS]]) on $G$ from $h$.
> 2. If any vertex remains [[Graph Traversal|undiscovered]], return $\text{F{\scriptsize ALSE}}$.
> 3. Construct the [[Transpose of Graphs|transpose]] of $G$, $G^T$.
> 4. Run a [[Graph Traversal|graph traversal]] ([[Breadth First Search|BFS]] or [[Depth First Search|DFS]]) on $G^T$ from $h$.
> 5. If any vertex remains [[Graph Traversal|undiscovered]], return $\text{F{\scriptsize ALSE}}$, otherwise return $\text{T{\scriptsize RUE}}$