---
tags:
  - atom
  - comp
---
Given a source [[Strings|string]] $A = a_{1}\dots a_{n}$ and $B = b_{1}\dots b_{n}$, what is the minimum number of
- insertions,
- deletions, and
- substitutions

needed to transform $A$ into $B$.

> [!solution]
> Let $D_{{i,j}}$ denote the *edit distance* between two prefixes of $A$ and $B$, given by $a_{1} \dots a_{i}$ and $b_{1}\dots b_{j}$.
> 
> If $a_{i} = b_{i}$, then $D_{i,j} = D_{i-1,j-1}$.
> 
> If $a_{i} \ne b_{i}$, we have to consider the 3 operations:
> - **Deletion**
>   $D_{i,j} = D_{i-1,j} + 1$
> - **Insertion**
>   $D_{i,j} = D_{i,j-1} + 1$
> - **Substitution**
>   $D_{i,j} = D_{i-1,j-1} + 1$
> 
> Thus,
> 
> $$D_{i,j} = \left\{\begin{array}{lll}
> 	\text{max}(i,j) & i = 0 \lor j = 0 & \text{Empty, edit remaining} \\
> 	D_{i-1,j-1} & a_{i} = b_{j} & \text{Same character} \\
> 	\begin{align}
> 		1 + \text{min}(&D_{i-1,j}, \\
> 		&D_{i,j-1}) \\
> 		&D_{i-1,j-1}) \\
> 	\end{align} & a_{i} \ne b_{i} & \text{Choose operation} \\
> \end{array}\right.$$

\[[[Dynamic Programming]]\]