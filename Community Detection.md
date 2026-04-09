---
tags:
  - atom
  - comp
---
Consider an [[Directed Graphs|undirected graph]] $G$, the *Girvan-Newman* [[Algorithms|algorithm]] constructs a hierachy of densely linked clusters, i.e. of **communities**, by iteratively removing the [[Edges|edges]] with highest **betweenness**.

> [!definition] The **betweeness** of a given [[Edges|edge]] is the number of [[Shortest Paths|shortest paths]] that include that [[Edges|edge]].
^betweenness