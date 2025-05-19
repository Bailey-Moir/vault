---
tags:
  - atom
  - math
  - linear
---
The *determinant* of a $3\times3$ matrix is
$$\begin{vmatrix}
		a & b & c \\ d & e & f \\ g & h & k
	\end{vmatrix} = a\begin{vmatrix}
	e&f\\h&k
\end{vmatrix}-b\begin{vmatrix}
	d&f\\g&k
\end{vmatrix}+c\begin{vmatrix}
	d&e\\g&h
\end{vmatrix}$$
Note these coefficients ($a,b,c$) can be chosen to be any row/column, with the [[Determinant of a 2x2 Matrix|2x2 determinants]] being their [[Matrix Minors|minors]]. **It is best to do this by [[Co-factor Expansion|co-factor]] expansion than memorization of the formula**.

> [!proof]-
> $$\begin{align*}
> 	\begin{vmatrix}
> 		a&b&c\\d&e&f\\g&h&k
> 	\end{vmatrix}
> 	&= \begin{vmatrix}
> 		a+0+0&0+b+0&0+0+c\\d&e&f\\g&h&k
> 	\end{vmatrix} \\
> 	&= \begin{vmatrix}
> 		a&0&0\\d&e&f\\g&h&k
> 	\end{vmatrix} + \begin{vmatrix}
> 		0&b&0\\d&e&f\\g&h&k
> 	\end{vmatrix} + \begin{vmatrix}
> 		0&0&c\\d&e&f\\g&h&k
> 	\end{vmatrix} \\
> 	&= \underset{\text{0 swaps}}{\begin{vmatrix}
> 		a&0&0\\d&e&f\\g&h&k
> 	\end{vmatrix}} - \underset{\text{1 swap}}{ \begin{vmatrix}
> 		b&0&0\\e&d&f\\h&g&k
> 	\end{vmatrix} } + \underset{\text{2 swaps}}{ \begin{vmatrix}
> 		c&0&0\\f&d&e\\k&g&h
> 	\end{vmatrix} } \\
> 	&= \begin{vmatrix}
> 		a&0&0\\0&e&f\\0&h&k
> 	\end{vmatrix} - \begin{vmatrix}
> 		b&0&0\\0&d&f\\0&g&k
> 	\end{vmatrix} + \begin{vmatrix}
> 		c&0&0\\0&d&e\\0&g&h
> 	\end{vmatrix} \\
> 	&= a\begin{vmatrix}
> 	e&f\\h&k
> \end{vmatrix}-b\begin{vmatrix}
> 	d&f\\g&k
> \end{vmatrix}+c\begin{vmatrix}
> 	d&e\\g&h
> \end{vmatrix}
> \end{align*}$$
> \[[[Row and Column Operations with Determinants]]\]