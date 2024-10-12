---
tags:
  - atom
  - comp
---
*Prim's algorithm* finds a [[Spanning Trees|minimum spanning tree]] using a [[Priority Queues|priority queue]] given a [[Connectivitiy|connected]] [[Math/Discrete/Graph Theory/Graphs|graph]] and a starting point. It finds this [[Math/Discrete/Graph Theory/Definitions/Trees|tree]] by traversing the minimum discovered [[Math/Discrete/Graph Theory/Definitions/Edges|edge]] [[Weighted Graphs|weights]].

```python
def prim(g, start):
	vertQueue = MinPirorityQueue() # (1)
	vertQueue.enqueue(start, 0)
	while not vertQueue.isEmpty():
		currentVert, currentDistance = vertQueue.dequeue_min()
		for nbr in currentVert.getConnections():
			d = currentVert.getWeight(nbr)
			if nbr.getColor() == 'white':
				nbr.setColor('gray')
				vertQueue.enqueue(nbr, d)
				nbr.pred = currentVert
			elif nbr.getColor() == 'gray' and d < vertQueue.priority(nbr):
				nbr.pred = currentVert

		currentVert.setColor('black')
		currentVert.distance = currentDistance
```
$$\mathcal{O}(\left| V \right| \log\left| V \right| + \left| E \right| )$$