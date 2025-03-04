---
tags:
  - atom
  - comp
---
A *breadth first search* of a [[Graphs|graph]] traverses each [[Vertices|vertex]] in ascending order of **depth** using a [[Queues|queue]].
```
set all vertices to undiscovered
mark start as discovered
queue.enqueue(start)

while queue is not empty:
   v = queue.dequeue()
   
   for each neighbour u of v:
	   if u is undiscovered:
	       queue.enqueue(u)
		   mark u as discovered
```
$$\mathcal{O}(\left|V\right|+\left|E\right|)$$
