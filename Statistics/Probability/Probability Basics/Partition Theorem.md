---
tags:
  - atom
  - math
  - discrete
  - stats
---
Let $B_{1},B_{2},\dots,B_{n}$ be a [[Partitions|partition]] of some [[Events|event]] $A$ such that $P(B_{i}) > 0$[^1] for all $i$. Then
$$\begin{align*}
	P(A) &= P(A\cap B_{1}) + P(A\cap B_{2}) + \dots + P(A\cap B_{n})   \\
	&= P(A|B_{1})P(B_{1}) + P(A|B_{2})P(B_{2}) \dots + P(A|B_{n})P(B_{n}) && (1)\\
	&= \sum_{i=1}^nP(A|B_{i})P(B_{i})
\end{align*}$$

\[(1) [[Conditional Probability]]\]

[^1]: [[Probability Function]]
