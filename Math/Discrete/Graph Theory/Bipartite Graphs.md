---
tags:
  - atom
  - math
  - discrete
---
![500|center](bipartite-graph.excalidraw.md)
A *bipartite graph* is a [[Simple Graphs|simple graph]] whose [[Vertices|vertex set]] can be [[Partitions|partitioned]] into two [[Empty Set|non-empty sets]] such that all [[Edges|edges]] connect a [[Vertices|vertex]] in one part to a [[Vertices|vertex]] in the other part.

> [!definition]- [[Complete Graphs|Complete]] *bipartite graphs*.
> A *bipartite graph* is said to be a **[[Complete Graphs|complete]] bipartite [[Graphs|graph]]** if every [[Vertices|vertex]] is [[Connectivitiy|connected]] to every [[Vertices|vertex]] in the other part. If the [[Cardinality|cardinality]] of the parts are $m$ and $n$, the [[Graphs|graph]] is denoted $K_{m,n}$. Note that a [[Complete Graphs|complete graph]] can not be *bipartite*.

> [!proof]- For all [[Graphs|graphs]] $G$ such that $\left| E(G) \right| > 0$,$$\chi(G) = 2 \iff G\text{ is bipartite}$$
> ($\impliedby$)
> Suppose $G$ is [[Bipartite Graphs|bipartite]]. Then its vertex set can be [[Partitions|partitioned]] into two [[Sets|sets]]/parts $V_1$ and $V_2$, so that all [[Edges|edges]] have endpoints in $V_1$ and $V_2$.
> 
> Colour the [[Vertices|vertices]] in $V_1$ blue and colour the vertices in $V_2$ red. As $G$ is [[Bipartite Graphs|bipartite]], this is a 2-colouring of $G$. 
> 
> Moreover, $G$ is not 1-colourable, as it has at least one edge. Hence, $\chi(G) = 2$.
> 
> ($\implies$)
> For the [[Converse, Inverse, and Contrapositive|converse]], assume $G$ is a [[Graphs|graph]] with at least one [[Edges|edge]] and $\chi(G)=2$.
> 
> Consider a 2-colouring of $G$ using blue and red.
> 
> Let $V_1$ be the [[Sets|set]] of blue [[Vertices|vertices]] and $V_2$ be the [[Sets|set]] of red [[Vertices|vertices]].
> 
> Since we have a 2-colour, no edge of $G$ joins a vertex in $V_1$ to another vertex in $V_1$ and no edge joins a vertex in $V_2$ to another vertex in $V_2$. Furthermore, since it has at least one edge, all edges to $G$ must join vertices in $V_1$ to vertices in $V_2$.
> 
> By definition, $G$ is [[Bipartite Graphs|bipartite]].