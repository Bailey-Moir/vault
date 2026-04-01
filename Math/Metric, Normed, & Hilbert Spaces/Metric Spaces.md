---
tags:
  - atom
  - math
---
A *metric* of a [[Empty Set|non-empty]] [[Sets|set]] $X$ is a [[Functions|function]] $d : X \times X \to \R$ such that ($\forall x,y,z \in X$)
1. $d(x,y) = 0 \leftrightarrow x = y$ (and $d(x,y) \ge 0$),
2. $d(x, y) = d(y, x)$,
3. $d(x,z) \le d(x,y) + d(y,z)$ ([[Triangle Ineqaulity|triangle inequality]])

> [!definition]  The pair $\left( X,d \right)$ is called a **metric space**.

> [!theorem]- *(Positivity)* $\forall x, y \in X, d(x,y) \ge 0$
> $$\begin{align*}
> 	\forall x,y \in X,\hspace{1em} 0 &= d(x,x) && \text{X1} \\
> 	&\le d(x,y) + d(y,x) && \text{X3} \\
> 	&= 2d(x,y) && \text{X2} \\
> 	\to \hspace{1em} 0 &\le d(x,y). \quad\square
> \end{align*}$$
 ^positivity