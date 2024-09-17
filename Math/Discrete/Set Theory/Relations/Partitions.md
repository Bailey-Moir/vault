---
tags:
  - atom
  - math
  - discrete
---
A *partition* of a [[Sets|set]] $A$ is a collection $\mathcal{C}$ of [[Subsets|subsets]] of $A$ (called cells, parts, or blocks) such that:
- $\forall \mathcal{C}_1, \mathcal{C}_2 \in \mathcal{C}, \left( \mathcal{C}_1 \ne \mathcal{C}_2 \implies C_1 \cap C_2 = \emptyset \right)$
- $\forall a \in A, \exists \mathcal{C}_1 \in \mathcal{C} : a \in \mathcal{C}_1$

# [[Equivalence Classes]] as a Partition
If $\rel$^[[[Relations]]] is an [[Equivalence Relations|equivalence relation]] on $A$, then
$$\begin{align*}
	\mathcal{C} = \left\{ [a] : a \in A \right\} && (1)
\end{align*}$$
is a *partition* of $A$.
\[(1) [[Equivalence Classes]]\]