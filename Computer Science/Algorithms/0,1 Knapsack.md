---
tags:
  - atom
  - comp
---
Suppose there is a [[Sets|set]] $S$ of $n$ items: the $i$-th item has value $v_{i}$ and weight $w_{i}$. Find a [[Subsets|subset]] of $S$ that maximises the total weight whilst having at most a total weight of $C$ (the capacity).

> [!idea]
> Let $V(i,C)$ be a [[Functions|function]] that gives the maximum value achievable with the first $i$ items of $S$ and a capacity of $C$. This can be defined [[Recursion|recursively]] by
> $$V(i,C) = \left\{\begin{array}{lll}
> 	0 & i = 0 & \text{No items to chose} \\
> 	V(i-1,C) & i > 0, w_{i} > C & \text{Item too heavy} \\
> 	\begin{align}
> 		\text{max}&(V(i-1,C), \\
> 		&\hspace{-1em}v_{i} + V(i-1,C-w_{i}))
> 	\end{align} & i > 0, w_{i} \le C & \begin{matrix}
> 		\text{Chose whether} \\
> 		\text{to pick item}
> 	\end{matrix} \\
> \end{array}\right.$$

\[[[Dynamic Programming]]\]