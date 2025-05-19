---
tags:
  - atom
  - comp
---
> [!example] "glorious" and "algorithms" give `["goris", "loris"]`

Let $L_{i,j}$ be a [[Functions|function]] that gives the *longest common subsequence* of the left string up to $i$, and the right string up to $j$. This can be defined [[Recursion|recursively]] by
$$L_{i,j} = \left\{\begin{array}{lll}
	0 & i = 0 \lor j = 0 & \text{Either is empty} \\
	L_{i-1,j-1} + 1 & a_{i} = b_{j} & \text{Same character} \\
	\begin{align}
		\text{max}(&L_{i,j-1}, \\
		&L_{i-1,j})
	\end{align} & a_{i} \ne b_{i} & \begin{matrix}
		\text{Chose character} \\
		\text{to skip}
	\end{matrix} \\
\end{array}\right.$$
> [!example]- "them" and "tim"
> ![500|center](lsc.excalidraw)

\[[[Dynamic Programming]]\]