---
tags:
  - atom
  - math
---
The discrete analogue of [[Fundamental Theorem of Calculus|FTC 2]] is
$$\sum_{n=a}^{x-1}\Delta f(n) = f(x) - f(a)$$

> [!proof]-
> $$\begin{alignat}{5}
> 	\sum_{n=a}^{x-1} \Delta f(n) &= \Delta f(a) &&+ \Delta f(a+1) &&+ \dots &&+ \Delta f(x-2) &&+ \Delta f(x-1) \\
> 	&= f(a+1) - f(a) \hspace{-50em}\\
> 	&&&+ f(a+2) - f(a+1) \hspace{-50em}\\
> 	&&&&&+ \cdots\\
> 	&&&&&&&+ f(x-1) - f(x-2) \hspace{-50em}\\
> 	&&&&&&&&&+ f(x) - f(x-1)\\
> 	&= f(x) - f(a) \hspace{-50em}\\
> \end{alignat}$$
> \[[[Telescoping Series]]\]

\[[[Math/Calculus/Operational Calculus/Forward Difference Operation]]\]