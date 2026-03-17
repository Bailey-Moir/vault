---
tags:
  - atom
  - comp
---
For some [[Universal Set|universal set]] $U$, the *minhash* $h : \mathcal{P}(U) \to \R_{>1}$ maps a [[Sets|set]] to the [[Expected Value|expected]] number of times you need to choose a random element of $U$ without replacement until you choose an element in that [[Sets|set]].

> [!note] In the [[Characteristic Polynomial|characteristic matrix]], this is expected first $1$ row of $S$ after shuffling the order of $U$.

> [!theorem]- Given a specified ordering, $P(h(S_{1}) = h(S_{2})) = \text{SIM}(S_{1},S_{2})$[^1].
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
> If we proceed from the top, the probability that you get to a type $X$ row before we meet a type $Y$ row (and thus $h(S_{1}) = h(S_{2})$) is also $x/(x+y)$, as out of the $X$ and $Y$ rows, you would have to have picked an $X$.


[^1]: [[Jaccard Distance]]
