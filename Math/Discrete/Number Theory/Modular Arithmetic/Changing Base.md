---
tags:
  - atom
  - math
  - discrete
---
To convert to base $b$ from base $10$, divide the number by $b$, using the remainder as the digit base $b$, and do the same thing with the quotient.

Suppose you have a number $q_{0}$ in base $10$ that you want to covert to base $b$. [[The Division Algorithm|The division algorithm]] gives
$$\begin{array}{r}
	q_{0} = q_{1}b + r_{1} \\
	q_{1} = q_{2}b + r_{2} \\
	q_{2} = q_{3}b + r_{3} \\
	\vdots\hspace{3em} \\
	q_{n-1} = q_{n}b + r_{n}, \\
\end{array}$$
with $r_{1},\dots,r_{n}$ gives the digits of $q_{0}$ base $b$.

> [!example]- $245$ base $16$
> $$\begin{array}{r}
> 	245 = 16 \times 15 + 5 \\
> 	15 = 16 \times 0 + 15 \\
> \end{array}$$
> $$\begin{align}
> 	245 &= (F5)_{16} \\
> 	&= 15 \times 16^1 + 5 \times 16^0 \\
> \end{align}$$

> [!example]- $245$ base $2$
> $$\begin{array}{r}
> 	245 = 2 \times 122 + 1 \\
> 	122 = 2 \times 61 + 0 \\
> 	61 = 2 \times 30 + 1 \\
> 	30 = 2 \times 15 + 0 \\
> 	15 = 2 \times 7 + 1 \\
> 	7 = 2 \times 3 + 1 \\
> 	3 = 2 \times 1 + 1 \\
> 	1 = 2 \times 0 + 1 \\
> \end{array}$$
> $$\begin{align}
> 	245 &= (11110101)_{2} \\
> 	&= 1\times 2^7 + 1\times 2^6 + 1\times 2^5 + 1\times 2^4 + 0\times 2^3 + 1\times 2^2 + 0 \times 2^1 + 1 \times 2^0
> \end{align}$$
