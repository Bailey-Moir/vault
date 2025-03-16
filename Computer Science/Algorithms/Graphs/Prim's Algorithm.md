---
tags:
  - atom
  - comp
---
Given a [[Connectivitiy|connected]] [[Graphs|graph]] and a starting [[Vertices|vertex]], *Prim's algorithm* finds a [[Spanning Trees|minimum spanning tree]] by placing discovered [[Edges|edges]] in a [[Priority Queues|minimum priority queue]] based on [[Weighted Graphs|weight]], and traversing the [[Edges|edges]] given by the [[Priority Queues|priority queue]].
$$\begin{array}{rl}
\hline

\scriptsize1& \textbf{procedure} \; \text{P{\scriptsize RIM}}(Adj,s) \\
\scriptsize2& \hspace{1em} n \leftarrow \left| Adj \right|  \\
\scriptsize3& \hspace{1em} in\text{-}tree \leftarrow n\text{-array filled with F{\scriptsize ALSE}}  \\
\scriptsize3& \hspace{1em} distance \leftarrow n\text{-array filled with } \infty  \\
\scriptsize4& \hspace{1em} parent \leftarrow n\text{-array filled with {\scriptsize NULL}}  \\
\scriptsize6& \hspace{1em} distance[s] \leftarrow 0  \\
\scriptsize2& \hspace{1em} \textbf{while} \; \neg all(in\text{-}tree)  \\
\scriptsize3& \hspace{2em} u \leftarrow \text{N{\scriptsize EXT}-V{\scriptsize ERTEX}}(in\text{-}tree, distance)  \\
\scriptsize3& \hspace{2em} in\text{-}tree[u] \leftarrow \text{T{\scriptsize RUE}} \\
\scriptsize4& \hspace{2em} \textbf{for} \; v, weight \; \textbf{in} \; Adj[u]  \\
\scriptsize5& \hspace{3em} \textbf{if} \; \neg in\text{-}tree[v]  \land weight < distance[v]  \\
\scriptsize6& \hspace{4em} distance[v] \leftarrow weight  \\
\scriptsize7& \hspace{4em} parent[v] \leftarrow u \\
\scriptsize10& \hspace{1em} \textbf{return} \; parent, distance \\

\hline
\end{array}$$

$$\mathcal{O}(\left| V \right| \log\left| V \right| + \left| E \right| )$$

> [!implementation]- Python
> ```python
> def prim(g, start):
> 	vertQueue = MinPriorityQueue() # (1)
> 	vertQueue.enqueue(start, 0)
> 	while not vertQueue.isEmpty():
> 		currentVert, currentDistance = vertQueue.dequeue_min()
> 		for nbr in currentVert.getConnections():
> 			d = currentVert.getWeight(nbr)
> 			if nbr.getColor() == 'white':
> 				nbr.setColor('gray')
> 				vertQueue.enqueue(nbr, d)
> 				nbr.pred = currentVert
> 			elif nbr.getColor() == 'gray' and d < vertQueue.priority(nbr):
> 				nbr.pred = currentVert
> 
> 		currentVert.setColor('black')
> 		currentVert.distance = currentDistance
> ```