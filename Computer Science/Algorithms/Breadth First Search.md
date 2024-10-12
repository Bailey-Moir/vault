---
tags:
  - atom
  - comp
---
A *breadth first search* of a [[Math/Discrete/Graph Theory/Graphs|graph]] traverses each [[Vertices|vertex]] in ascending order of **depth**.
```
set all vertices to unvisited
choose starting vertex start_V
queue.enqueue(start_V)

while queue is not empty:
   new_V = queue.dequeue()
   
   for each neighbour of new_V:
       enqueue neighbour if unvisited and undiscovered
       mark neighbour as discovered
       
    mark new_V as visited
```
$$\mathcal{O}(\left|V\right|+\left|E\right|)$$
