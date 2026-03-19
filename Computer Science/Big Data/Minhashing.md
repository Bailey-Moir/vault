---
tags:
  - atom
  - comp
---
For some [[Ordered Sets|ordered]] [[Universal Set|universal set]] $U = \left( u_{1},u_{2},\dots \right)$, the *minhash* $h : \mathcal{P}(U) \to \Z^+$ gives the index of the first element of $U$ in the given [[Sets|set]] (using one-indexing);
$$h(S) = \min_{{u_{i} \in U }} \{ i : u_{i} \in S \}.$$
> [!note] In the [[Characteristic Set Matrices|characteristic matrix]], this is the first row with $1$ in the $S$ column.

> [!theorem]- $P(h(S_{1}) = h(S_{2})) = \text{SIM}(S_{1},S_{2})$[^1].
> The rows of the corresponding [[Characteristic Set Matrices|characteristic matrix]] can be [[Partitions|partitioned]] into 3 types:
> - type $X$ rows with $1$ in both columns,
> - type $Y$ rows with $1$ in one column and $0$ in the other, and
> - type $Z$ rows with $0$ in both columns.
> 
> Let $x$ be the number of rows of type $X$, and $y$ be the number of rows of type $Y$. Then
> $$\begin{align}
> 	\text{SIM}(S_{1},S_{2})
> 	&= \dfrac{\left| S_{1} \cap S_{2} \right|}{\left| S_{1} \cup S_{2} \right| } \\
> 	&= \dfrac{x}{x + y}. \\
> \end{align}$$
> If we proceed from the top, the probability that you get to a type $X$ row before we meet a type $Y$ row (and thus $h(S_{1}) = h(S_{2})$) is also $x/(x+y)$, as out of the $X$ and $Y$ rows, you would have had to pick an $X$.
^theorem

[^1]: [[Jaccard Distance]]
