---
tags:
  - atom
  - comp
---
A *depth first search* of a [[Math/Discrete/Graph Theory/Graphs|graph]] traverses each [[Vertices|vertex]] using a [[Stacks|stack]]... #TODO 
```
set all vertices to unvisited
stack.push(start)

while stack is not empty:
   v = stack.pop()

   if v is unvisited:
       mark v visited
       for each neighbour u of v:
		   if u is unvisited:
			   stack.push(u)
```
$$\mathcal{O}(\left|V\right|+\left|E\right|)$$
