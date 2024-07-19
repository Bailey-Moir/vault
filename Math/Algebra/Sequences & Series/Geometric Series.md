---
tags:
  - atom
  - math
---
$$\begin{array}{rl}
	\displaystyle\sum_{n=1}^\infty ar^{n-1} & a \ne 0
\end{array}$$
$$ s_n = \dfrac{a(1-r^n)}{1-r} $$
> [!proof]-
> $$\begin{array}{l}
> 	\begin{alignat}{3}
> 		s_n &= a +\hspace{-.25em}&&\hspace{.5em} ar + ar^2 + \cdots + ar^{n-1} \\
> 		rs_n &= &&\hspace{.5em}ar + ar^2 + \cdots + ar^{n-1} + ar^n
> 	\end{alignat} \\
> 	s_n-rs_n = a-ar^n \\
> 	s_n = \dfrac{a(1-r^n)}{1-r}
> \end{array}$$