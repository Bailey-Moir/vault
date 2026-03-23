---
tags:
  - atom
  - comp
---
The [[Internet|web]] can be modelled as a [[Directed Graphs|directed]] [[Graphs|graph]] $G$ with weighted [[Vertices|vertices]] representing the **rank**/importance of each [[Vertices|vertex]]/page. The **rank** of $j \in V(G)$[^1]
$$r_{j} = \sum_{u \in N^{-1}(v)} \dfrac{r_{i}}{\delta(i)}.$$
In a [[Graphs|graph]] with $n$ [[Vertices|vertices]], this gives a [[Homogeneous Systems|homogeneous system]] of $n$ equations of $n$ variables, so there are infinitely many solutions. In order to constrain this to a unique solution, we require
$$\sum_{j \in V(g)}r_{j} = 1.$$
Using a [[Stochastic Adjacency Matrix|Stochastic adjacency matrix]], $M_{ij} = 1/\delta(j)$, these equations can be represented as
$$\begin{array}{c}
\vecbf{r} = M\vecbf{r} &
\sum\vecbf{r}= 1.
\end{array}$$
Then solving for $\vecbf{r}$ simply reduces to finding for an element that sums to $1$ in $E_{1}(M)$[^2].

\[[[Vertex Degrees]]\]

[^1]: [[Graphs]]
[^2]: [[Eigenspaces]]
