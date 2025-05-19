---
tags:
  - atom
  - comp
---
![1000|center](topological-order.excalidraw.md)
A *topological ordering* of a [[Directed Graphs|directed graph]] is an ordering of its [[Vertices|vertices]], such that, if there is an [[Edges|edge]] $\left( u,v \right)$ in the [[Graphs|graph]], then [[Vertices|vertex]] $u$ is placed in some position before vertex $v$.  [[Directed Graphs|Directed]] [[Walks|acyclic]] [[Graphs|graphs]] (DAG) have at least one *topological ordering*.

> [!algorithm]
> 1. Initialise the [[Graph Traversal|state]] and [[Parent Arrays|parent arrays]].
> 2. Initialise an empty [[Stacks|stack]].
> 3. Iterate over all [[Vertices|vertices]] of the [[Graphs|graph]].
> 	- If the vertex is [[Graph Traversal|undiscovered]], start a modified version of $\text{DFS-L{\scriptsize OOP}}$[^1] on the [[Vertices|vertex]], where as soon as a [[Vertices|vertex]] is [[Graph Traversal|processed]], it is pushed to the [[Stacks|stack]].
> 1. Return the content of the [[Stacks|stack]] from top to bottom as a *topological ordering*.

[^1]: [[Depth First Search]]
