---
tags:
  - atom
  - math
  - linear
---
When given a [[Functions|function]] with $n$ unknown linear coefficients and a [[Sets|set]] of $m$ points it passes through, the coefficients can be solved for plugging in the points, giving a [[Linear Systems|system of]] $m$ [[Linear Systems|linear equations]] which can be solved using [[Gaussian Elimination|Gaussian elimination]].

> [!example]- $$\begin{array}{rl} y = ax^2 + bx + c & (1,16), (2,6), (3,58) \end{array}$$
> $$\begin{align*}
> 	(1)\hspace{1em} &16 = a(1)^2 + b(1) + c \\
> 	\phantom{(1)\hspace{1em}} &\phantom{16} = a + b + c \\\\
> 	(2)\hspace{1em} &6 = a(2)^2 + b(2) + c \\
> 	\phantom{(1)\hspace{1em}} &\phantom{16} = 4a + 2b + c \\\\
> 	(3)\hspace{1em} &58 = a(3)^2 + b(3) + c \\
> 	\phantom{(1)\hspace{1em}} &\phantom{16} = 9a + 3b + c
> \end{align*}$$
> $$\left[
> 	\left.
> 	\begin{matrix}
> 		1&1&1\\
> 		4&2&1\\
> 		9&3&1
> 	\end{matrix}
> 	\hspace{0.4em}
> 	\right|
> 	\hspace{0.4em}
> 	\begin{matrix}
> 		16\\
> 		6\\
> 		58
> 	\end{matrix}
> \right]$$
> Then use [[Gaussian Elimination|Gaussian elimination]].