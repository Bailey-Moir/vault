---
tags:
  - atom
  - math
  - linear
---
The *determinant* of a $2\times2$ matrix is the product of the main diagonal minus the product of the secondary diagonal.
$$\begin{vmatrix}
	a & b \\
	c & d \\
\end{vmatrix} = ad-bc$$
> [!proof]- Column Operations
> $$\begin{align*}
> 	\begin{vmatrix}
> 		a&b\\c&d
> 	\end{vmatrix}
> 	&= \begin{vmatrix}
> 		a+0&b\\0+c&d
> 	\end{vmatrix} \\
> 	&= \begin{vmatrix}
> 		a&b\\0&d
> 	\end{vmatrix}+\begin{vmatrix}
> 		0&b\\c&d
> 	\end{vmatrix} \\
> 	&= \begin{vmatrix}
> 		a&b\\0&d
> 	\end{vmatrix}-\begin{vmatrix}
> 		c&d\\0&b
> 	\end{vmatrix} \\
> 	&= ad - bc && (1)
> \end{align*}$$
> \[[[Row and Column Operations with Determinants]], (1) [[Triangular Product of Diagonals]]\]

> [!proof]- [[Co-factor Expansion|Co-factor Expansion]]
> A [[Co-factor Expansion|co-factor expansion]] along row $1$ gives
> $$\begin{align*}
> 	\begin{vmatrix}
> 		a&b\\c&d
> 	\end{vmatrix} &= \left( -1 \right)^{1+1}a\left| d \right| + \left( -1 \right)^{1+2}b\left| c \right| \\
> 	&= ad - bc \\
> \end{align*}$$