---
tags:
  - atom
  - comp
---
A *depth first search* of a [[Math/Discrete/Graph Theory/Graphs|graph]] traverses each [[Vertices|vertex]] ...
```
set all vertices to unvisited
choose starting vertex start_V
stack.push(start_V)

while stack is not empty:
   new_V = stack.pop()

   if new_V is unvisited:
       mark new_V visited
       for each neighbour of new_V:
           push neighbour if unvisited
```
$$\mathcal{O}(\left|V\right|+\left|E\right|)$$
