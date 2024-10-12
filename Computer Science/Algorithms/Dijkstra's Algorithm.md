---
tags:
  - atom
  - comp
---
*Dijkstra's algorithm*

```
initialize each vertex 
add start vertex to min priority queue

while queue is not empty:
	v, cv = queue.dequeue
	for (n, cn) of neighbours of v:
		queue.enqueue(n, cv + cn)

```