---
tags:
  - atom
  - math
---
The *determinant* of a $2\times2$ matrix is the product of the main diagonal minus the product of the secondary diagonal.
$$\begin{vmatrix}
	a & b \\
	c & d \\
\end{vmatrix} = ad-bc$$
> [!proof]-
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