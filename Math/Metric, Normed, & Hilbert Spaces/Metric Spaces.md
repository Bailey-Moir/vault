---
tags:
  - atom
  - math
---
A *metric* of a [[Sets|set]] $M$ is a [[Functions|function]] $d : M \times M \to \R$ such that ($\forall x,y,z \in M$)
1. $d(x,y) = 0 \leftrightarrow x = y$,
2. $d(x, y) = d(y, x)$
3. $d(x,z) \le d(x,y) + d(y,z)$ ([[Triangle Ineqaulity|triangle inequality]])

> [!definition]  The pair $\left( M,d \right)$ is called a **metric space**.

> [!theorem]- *(Positivity)* $\forall x, y \in M, d(x,y) \ge 0$
> $$\begin{align*}
> 	\forall x,y \in M,\hspace{1em} 0 &= d(x,x) && \text{A1} \\
> 	&\le d(x,y) + d(y,x) && \text{A3} \\
> 	&= 2d(x,y) && \text{A2} \\
> 	\to \hspace{1em} 0 &\le d(x,y). \quad\square
> \end{align*}$$
^positivity