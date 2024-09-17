---
tags:
  - atom
  - math
  - discrete
---
$$\chi(G) = 2 \iff \text{$G$ is bipartite}$$

> [!proof]- 
> ($\leftarrow$) Assume $G$ is [[Bipartite Graphs|bipartite]]. Then its vertex set can be **partitioned** into two sets $V_1$ and $V_2$ so that all edges have endpoints at $V_1$ and $V_2$. > Colour the vertices in $V_1$ blue and colour the vertices in $V_2$ red. As $G$ is [[Bipartite Graphs|bipartite]], this is a 2-colouring of $G$. Moreover, $G$ is not 1-colourable  as it has at least one edge. Hence $\chi(G) = 2$.
> ($\rightarrow$)
> For the converse, assume $G$ is a graph with at least one edge and $\chi(G)=2$. Consider a 2-colouring of $G$ using blue and red. Let $V_1$ be the set of blue vertices and $V_2$ be the set of red vertices. Since we have a 2-colour, no edge of $G$ joins a vertex in $V_1$ to another vertex in $V_1$ and no edge joins a vertex in $V_2$ to another vertex in $V_2$. Furthermore, since it has at least one edge, all edges to $G$ must join vertices in $V_1$ to vertices in $V_2$. By definition, $G$ is [[Bipartite Graphs|bipartite]].

\[[[Chromatic Numbers]], [[Bipartite Graphs]]\]