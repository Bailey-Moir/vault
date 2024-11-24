---
tags:
  - atom
  - comp
---
An exact shortest path finding algorithm that works for negative weightings. This algorithm only works if there are no negative cycles. This algorithm relies on two key assumptions:
1. There are no repeated nodes. This is because if a node is repeated then it is not a shortest path as, as repeating a node as no benefit as there can not be negative cycles.
2. If you have a shortest path, then all of its sub-paths are shortest paths.

This algorithm works with a theoretical (but not so theoretical) function called $d(i,j,k)$. First we consider $d(i,j)$, where $i$ is the index of the starting node, and $j$ is the index of the destination node, and the function gives the shortest distance between these two nodes. We then add an argument $k$, which constrains which intermediate nodes can be used, only allowing nodes in the set $\{0,1,\dots,k\}$.

Consider $d(i,j,-1)$. This function allows no intermediate nodes, meaning that the distance is either:
- $0$ if $i=j$
- $\infty$ if there is no e from $i$ to $j$ (wrong terminology).
- and if there is a connection between then, then it is the weighting of the connection between them: $w(i,j)$.

We now have a [[Functions_#Types of Functions|piecewise function]] for $d(i,j,-1)$. If we increment $k$, either the result of the function will remain the same, meaning that allowing another intermediate node didn't find a shorter path, or the result of the function will be smaller, meaning that using the new intermediate node found a shorter path.
If the value changes when changing $d(i,j,k-1)$ to $d(i,j,k)$, then we can think of the resulting shortest path as:
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