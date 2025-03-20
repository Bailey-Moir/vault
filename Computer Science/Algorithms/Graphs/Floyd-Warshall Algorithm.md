---
tags:
  - atom
  - comp
---
$$\begin{array}{rl}
\hline

\scriptsize1& \textbf{procedure} \; \text{F{\scriptsize LOYD}}(Distance) \\
\scriptsize2& \hspace{1em} n \leftarrow \text{number of rows (or columns) of matrix } Distance \\
\scriptsize3& \hspace{1em} \textbf{for} \; k \; \textbf{from} \; 0 \; \textbf{to} \; n - 1  \\
\scriptsize4& \hspace{2em} \textbf{for} \; i \; \textbf{from} \; 0 \; \textbf{to} \; n - 1  \\
\scriptsize5& \hspace{3em} \textbf{for} \; j \; \textbf{from} \; 0 \; \textbf{to} \; n - 1  \\
\scriptsize6& \hspace{4em} \textbf{if} \; Distance[i][j] > Distance[i][k] + Distance[k][j]  \\
\scriptsize7& \hspace{5em} Distance[i][j] \leftarrow  Distance[i][k] + Distance[k][j] \\
\scriptsize8& \hspace{1em} \textbf{return} \; Distance \\

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
$$n_i, \dots, n_k, \dots, n_j$$
This path can be split into the sub-paths $n_i, \dots, n_k$ and $n_k, \dots, n_i$, which (as per our assumptions) must be shortest paths themselves.

Thus, if incrementing $k$ changes the result of the function, then
$$d(i,j,k) = d(i,k,k-1) + d(k,j,k-1)$$
If incrementing $k$ does not change the result, then obviously $d(i,j,k) = d(i,j,k-1)$.

$$d(i,j,k) = \left\{ \begin{array}{ll}
	0, & k = -1 \land i = j \\
	\infty, & k = -1 \land (i, j) \notin E \\
	w((i,j)), & k = -1 \land (i, j) \in E \\
	\text{min}(d(i,k,k-1) + d(k,j,k-1), d(i,j,k-1)), & k \geq 0 \\
\end{array} \right. $$