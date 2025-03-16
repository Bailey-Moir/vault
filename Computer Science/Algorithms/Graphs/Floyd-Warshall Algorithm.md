---
tags:
  - atom
  - comp
---
$$\begin{array}{rl}
\hline

\scriptsize1& \textbf{procedure} \; \text{F{\scriptsize LOYD}}(Distance) \\
\scriptsize2& \hspace{1em} n \leftarrow \text{number of rows (or columns) of matrix } Distance \\
\scriptsize4& \hspace{1em} \textbf{for} \; k \; \textbf{from} \; 0 \; \textbf{to} \; n - 1  \\
\scriptsize4& \hspace{2em} \textbf{for} \; i \; \textbf{from} \; 0 \; \textbf{to} \; n - 1  \\
\scriptsize4& \hspace{3em} \textbf{for} \; j \; \textbf{from} \; 0 \; \textbf{to} \; n - 1  \\
\scriptsize5& \hspace{4em} \textbf{if} \; Distance[i][j] < Distance[i][k] + Distance[k][j]  \\
\scriptsize6& \hspace{5em} Distance[i][j] \leftarrow  Distance[i][k] + Distance[k][j] \\
\scriptsize10& \hspace{1em} \textbf{return} \; Distance \\

\hline
\end{array}$$

The *Floyd-Warshall algorithm* is an exact all-pairs [[Shortest Paths|shortest path]] algorithm that works for [[Graphs|graphs]] containing negative [[Weighted Graphs|weightings]] and no negative [[Walks|cycles]]. This algorithm relies on two key assumptions:
1. There are no repeated nodes. This is because if a node is repeated then it is not a shortest path as, as repeating a node has no benefit as there can not be negative cycles.
2. If you have a shortest path, then all of its sub-paths are shortest paths.

This algorithm works with a theoretical [[Functions|function]] $d(i,j,k)$. First we consider $d(i,j)$, where $i$ is the index of the starting [[Vertices|vertex]], and $j$ is the index of the destination [[Vertices|vertex]], and the [[Functions|function]] gives the shortest distance between those two [[Vertices|vertices]]. We then add an argument $k$, which constrains which intermediate [[Vertices|vertices]] can be used, only allowing [[Vertices|vertices]] in the [[Sets|set]] $\{0,1,\dots,k\}$.

Consider $d(i,j,-1)$. This [[Functions|function]] allows no intermediate [[Vertices|vertices]], meaning that the distance is either:
- $0$ if $i=j$,
- $\infty$ if there is no [[Edges|edge]] from $i$ to $j$,
- and if they are [[Edges|adjacent]], then it is the [[Weighted Graphs|weight]] of the [[Edges|edge]] between them: $w(i,j)$.

We now have a [[Types of Functions|piecewise function]] for $d(i,j,-1)$. If we increment $k$, either
- the output will remain the same, meaning that allowing the intermediate [[Vertices|vertex]] $k$ did not give a shorter path, or 
- the result of the function will be smaller, meaning that using the intermediate [[Vertices|vertex]] $k$ gave a shorter path.

If the $d(i,j,k) \ne d(i,j,k-1)$, then we can think of the resulting shortest path as:
$$d(i,j,k) = \left\{ \begin{array}{ll}
	0, & k = -1 \land i = j \\
	\infty, & k = -1 \land (i, j) \notin E \\
	w((i,j)), & k = -1 \land (i, j) \in E \\
	\text{min}(d(i,k,k-1) + d(k,j,k-1), d(i,j,k-1)), & k \geq 0 \\
\end{array} \right. $$
$$n_i, \dots, n_k, \dots, n_j$$
This path can be split into the sub-paths $n_i, \dots, n_k$ and $n_k, \dots, n_i$, which (as per our assumptions), must be shortest paths in an of themselves.

This means that if incrementing $k$ changes the result of the function, then $d(i,j,k) = d(i,k,k-1) + d(k,j,k-1)$. If incrementing $k$ does not change the result, then obviously $d(i,j,k) = d(i,j,k-1)$.
# Implementations
## Non-Recursive
$O(n^3)$
```
let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
for each edge (u, v) do
    dist[u][v] ← w(u, v)  // The weight of the edge (u, v)
for each vertex v do
    dist[v][v] ← 0
for k from 1 to |V|
    for i from 1 to |V|
        for j from 1 to |V|
            if dist[i][j] > dist[i][k] + dist[k][j] 
                dist[i][j] ← dist[i][k] + dist[k][j]
            end if
```

```python
# N is number of nodes
cache = np.full((N,N,N), np.iinfo(np.int32).max, dtype=np.int32)

for i in range(N):
	for j in range(N):
		for k in range(N):
			cache[i,j,k] = min(d(i,k,k-1) + d(k,j,k-1), d(i,j,k-1))

# I can't remember how to make this verison work.
```
## Recursive
$O(3^n)$
```python
def d(i,j):
	# N is number of nodes
	return d(i,j,N-1)

def d(i,j,k):
	""" Finds shortest path form i to j, allowing intermediate nodes {0,1,...,k} """
	if k == -1:
		if i == j:
			return 0
		
		return w(i,j) # note if no edge, returns np.inf
	
	return min(d(i,k,k-1) + d(k,j,k-1), d(i,j,k-1))
```
## Mixed
$<O(n^3)$
```python
# N is number of nodes
defined = np.full((N,N,N), False, dtype=bool)
cache = np.full((N,N,N), np.iinfo(np.int32).max, dtype=np.int32)

def d(i,j):
	return d(i,j,N-1)

def d(i,j,k):
	""" Finds shortest path form i to j, allowing intermediate nodes {0,1,...,k} """
	if not defined[i][j][k]:
		if k == -1:
			if i == j:
				cache[i][j][k] = 0
			else: 
				cache[i][j][k] = w(i,j) # note if no edge, returns np.inf
		else:
			cache[i][j][k] = min(d(i,k,k-1) + d(k,j,k-1), d(i,j,k-1))

		defined[i][j][k] = True

	return cache[i][j][k]
`