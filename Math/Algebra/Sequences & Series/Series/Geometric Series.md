---
tags:
  - atom
  - math
---
A *geometric series* is a [[Power Series|power series]] where the terms have **common ratio** $r$, with the standard form
$$ \sum_{k=0}^\infty ar^k = a+ar+ar^2+\cdots, \hspace{2em} a\ne 0$$
*Note that the $\mathit{n}$-th term is $\mathit{ar^{n-1}}$*
## Partial Sum Formula
$$ S_n = \dfrac{a(1-r^n)}{1-r} $$
> [!proof]-
> $$\begin{array}{l}
> 	\begin{alignat}{3}
> 		S_n &= a +\hspace{-.25em}&&\hspace{.5em} ar + ar^2 + \dots + ar^{n-1} \\
> 		rS_n &= &&\hspace{.5em}ar + ar^2 + \dots + ar^{n-1} + ar^n
> 	\end{alignat} \\
> 	S_n-rS_n = a-ar^n \\
> 	S_n = \dfrac{a(1-r^n)}{1-r}
> \end{array}$$

As can be [[Scientific Method#Deductive vs Inductive Reasoning|deduced]], iff $\left| r \right|<1$[^1], 
$$ S_\infty = \dfrac{a}{1-r} $$

[^1]: [[Intervals]]