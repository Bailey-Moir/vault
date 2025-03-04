---
tags:
  - atom
  - comp
---
Given a [[Connectivitiy|connected]] [[Implementing Graphs|graph]] and a starting [[Vertices|vertex]], *Prim's algorithm* finds a [[Spanning Trees|minimum spanning tree]] by placing discovered [[Edges|edges]] in a [[Priority Queues|minimum priority queue]] based on [[Weighted Graphs|weight]], and traversing the [[Edges|edges]] given by the [[Priority Queues|priority queue]].

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