---
tags:
  - atom
  - comp
---
*Dijkstra's algorithm* finds the shortest path between [[Vertices|vertices]] on a [[Graphs|graph]] (creates a shortest path tree).

A [[Priority Queues|minimum priority queue]] is created, and the start [[Vertices|vertex]] $v_i$ is [[Queues|enqueued]] with distance $0$.

Until the [[Queues|queue]] is empty, a vertex $v$ is [[Queues|dequeued]] and marked, and all [[Neighbourhood|neighbours]] of $v$ are [[Queues|enqueued]] with a distance of $v$ from $v_{i}$ plus the edge weight from $v$ to the given neighbour #TODO.

```
initialize each vertex with distance infinity
add start vertex to min priority queue
distance[start] = 0

while queue is not empty:
	v, cv = queue.dequeue()
	mark v as visited
	for (n, cn) of neighbours of v:
		queue.enqueue(n, cv + cn)
		if n is unvisited:
			tempDistance = distance[v] + cn
			if tempDistance < distance[n]:
				distance[n] = tempDistance

```

> [!complexity]-
> **Time Complexity** $\mathcal{O}((|V|+|E|)\log |V|)$
> **Space Complexity** $\mathcal{O}(|V|)$
