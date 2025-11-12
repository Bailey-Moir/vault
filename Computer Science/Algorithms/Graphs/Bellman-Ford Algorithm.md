---
tags:
  - atom
  - comp
---
The *Bellman–Ford* [[Algorithms|algorithm]] finds the [[Shortest Paths|shortest paths]] from a starting [[Vertices|node]] to all [[Vertices|nodes]] of a [[Graphs|graph]] with no negative [[Walks|cycle]].

Initially, the distance to the starting [[Vectors|node]] is $0$ and the distance to all other [[Vectors|nodes]] in $\infty$. The [[Algorithms|algorithm]] reduces the distances by finding [[Edges|edges]] that shorten the [[Walks|paths]] until it is not possible to shorten any further.

```py
def bellman(n, v0, edges):
    distance = [float('inf')]*n
    distance[v0] = 0

    for _ in range(n-1):
        for u, v, w in edges:
            distance[v] = min(distance[v], distance[u] + w);
```