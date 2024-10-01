---
tags:
  - atom
  - stats
  - math
---
The number of ways to choose an **unordered** subset of $k$ elements from a fixed set of $n$ elements. 
$$\begin{pmatrix}
	n \\ k
\end{pmatrix} = \dfrac{n!}{k! \left( n - k \right)!} $$
There are many different applications of this coefficient:
- The number of arrangements of $k$ successes among $n$ trials^[[[Binomial Random Variable]]].
- Gives the coefficient of the $x^k$ term in $(x + 1)^n$.
- The number of [[Subsets|subsets]] of size $k$ from a [[Sets|set]] of size $n$.


# Properties
- $\forall n,r \in \N, \left( r \le n \implies \begin{pmatrix}n\\r\end{pmatrix}=\begin{pmatrix}n\\n-r\end{pmatrix} \right)$
> [!proof]-
> $$\begin{align*}
> 	\begin{pmatrix}
> 	n\\n-r
> \end{pmatrix}&=\dfrac{n!}{\left( n-r \right)!\left( n-\left( n-r \right) \right)!} \\
> 	&=\dfrac{n!}{\left( n-r \right)!r!} \\
> 	&=\begin{pmatrix}
> 	n\\r
> \end{pmatrix}
> \end{align*}$$