---
tags:
  - atom
  - comp
---
In *distance-vector routing*, each [[Routers|router]] knows the best distances for any destination for each of its neighbours.

This is done in three steps that it repeats:
1. Wait for change in local link cost or message from neighbour,
2. Recompute estimates/distances using [[Bellman-Ford Algorithm|Bellman-Ford]], and
3. If the estimates/distances change, notify neighbours.

Each node holds the cost of the limits to it's neighbours, $c(x,y)$, and the *distance-[[Vectors|vectors]]* of itself and it's neighbours $D_x, D_y, \dots$, which give the best estimate of the distances from the respective node and any other node.

> [!note] Just like [[Link-State Routing|link-state routing]], $D_x$ is sent to $x$'s neighbours on a
> - **Topology Change** - Link or node failure or recovery (turning on or off).
> - **Configuration Change** - Link cost change.
> - **Peridoically Change** - Every ~30 minutes, to correct for possible corruption of data or missed updates.

> [!edge-case] 
> To avoid the count-to-infinity problem, **poisoned reverse** is used, where if a node $x$ gets to $z$ through $y$, when $x$ sends $D_x$ to $y$, it will set $D_x(z) = \infty$.
> [[Stations|Station]] $x$ can figure this out by consulting it's [[Forwarding Tables|forwarding table]] to $z$ (as $y$ must be a neighbour of $x$).
> It should be noted that **poisoned reverse** does not solve the general count-to-infinity problem.

> [!complexity]
> - **Message complexity** $O(nm)$,
> - **Speed of Convergence** varies.

> [!note] unlike [[Link-State Routing|LS]], errors propagate through the whole network.