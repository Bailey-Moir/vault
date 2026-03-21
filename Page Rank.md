---
tags:
  - atom
  - comp
---
The [[Internet|web]] can be modelled as a [[Directed Graphs|directed]] [[Graphs|graph]] $G$ with weighted [[Vertices|vertices]] representing the **rank**/importance of each [[Vertices|vertex]]/page. The **rank** of $v \in V(G)$[^1]
$$r(v) = \sum_{u \in N^{-1}(v)} \dfrac{r(u)}{\delta(u)}.$$
\[[[Vertex Degrees]]\]

In a [[Graphs|graph]] with $n$ [[Vertices|vertices]], this gives a [[Homogeneous Systems|homogeneous system]] of $n$ equations of $n$ variables, so there are infinitely many solutions. In order to constrain this to a unique solution, we require
$$\sum_{v \in V(g)}r(v) = 1.$$

[^1]: [[Graphs]]