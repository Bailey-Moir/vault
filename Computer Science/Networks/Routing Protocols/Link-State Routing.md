---
tags:
  - atom
  - comp
---
In *link-state routing*, each [[Routers|router]] has the complete [[Networks|network picture]], meaning it knows the topology and the link costs.

To do this, each router checks the distance/cost metric to its neighbours, and [[Broadcasting|broadcasts]]/[[Routing Protocols#Routing Strategies|floods]] this to all other [[Routers|routers]]. Then every [[Routers|router]] can construct an [[Adjacency Matrices|adjacency matrix]]/[[Adjacency Lists|adjacency list]].

The best outgoing interface is then chosen using [[Dijkstra's Algorithm|Dijkstra's algorithm]] 

> [!complexity]
> - **Message complexity** $O(nm)$,
> - **Speed of Convergence** $O(n^2)$.

> [!note] This [[Routing Protocols#Routing Strategies|flooding]] occurs on
> - **Topology Change** - Link or node failure or recovery (turning on or off).
> - **Configuration Change** - Link cost change.
> - **Peridoically Change** - Every ~30 minutes, to correct for possible corruption of data or missed updates.