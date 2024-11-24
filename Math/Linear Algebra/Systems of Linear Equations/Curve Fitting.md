---
tags:
  - atom
  - math
---
> [!example]
> $$\begin{array}{rl} 
> 	 y = ax^2 + bx + c & (1,16), (2,6), 3(58)
> \end{array}$$
> $$\begin{align*}
> 	(1)\hspace{1em} &16 = a(1)^2 + b(1) + c \\
> 	\phantom{(1)\hspace{1em}} &\phantom{16} = a + b + c \\\\
> 	(2)\hspace{1em} &6 = a(2)^2 + b(2) + c \\
> 	\phantom{(1)\hspace{1em}} &\phantom{16} = 4a + 2b + c \\\\
> 	(3)\hspace{1em} &58 = a(3)^2 + b(3) + c \\
> 	\phantom{(1)\hspace{1em}} &\phantom{16} = 9a + 3b + c
> \end{align*}$$
> $$\begin{bmatrix}
> 	1 & 1 & 1 & : & 16 \\
> 	4 & 2 & 1 & : & 6 \\
> 	9 & 3 & 1 & : & 58 \\
> \end{bmatrix}$$
> Then use [[Gaussian Elimination]]. This same method can be used for a function with any number of unknown linear coefficients.
> $\hspace{2em}$ e.g. $y = a\sin{x} + c$, $y = ae^x + b\sqrt{x}$