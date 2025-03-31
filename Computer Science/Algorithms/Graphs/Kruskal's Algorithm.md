---
tags:
  - atom
  - comp
---
For a given [[Connectivitiy|connected]] [[Graphs|graph]], *Kruskal's algorithm* finds a [[Spanning Trees|minimum spanning tree]] by placing all [[Edges|edges]] in a [[Priority Queues|minimum priority queue]] based on [[Weighted Graphs|weight]], adding them to the [[Trees|tree]] if they don't create a [[Walks|cycle]].
$$\mathcal{O}(\left| E \right| \log \left|  E \right|  )$$
> [!note] This is a [[Greedy Algorithms|greedy algorithm]].