---
tags:
  - atom
  - comp
---
The *point inclusion test* is the problem of determining if a [[Points|point]] is inside of a polygon.

A [[Points|point]] $P$ lies inside a simple polygon iff a **horizontal** [[Rays|ray]] from the [[Points|point]] intersects the edges an
odd number of times.
![500|center](point-inclusion-test-basic.excalidraw.md)
> [!edge cases]-
> - The ray passes through a vertex, **staying** outside/inside the polygon.
> - The ray passes through a vertex, **moving** outside/inside the polygon.
> - The ray and an edge overlap.
> ![1000|center](point-inclusion-test-edge-eg.excalidraw.md)
> These edge cases can be accounted for by only counting the lowest vertex of edge edge.

> [!preprocessing] A boundary box can be created, and if the [[Points|point]] isn't in the box, this algorithm can be skipped.