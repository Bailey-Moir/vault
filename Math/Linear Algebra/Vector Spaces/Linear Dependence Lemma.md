---
tags:
  - atom
  - math
  - linear
---
If $\vecbf{v}_{1}, \cdots, \vecbf{v}_{n}$ is [[Linear Independence|linearly dependent]],
$$\exists k \in \{ 1, \dots, n \} : \vecbf{v}_{k} \in \text{span}(\vecbf{v}_{1},\dots \vecbf{v}_{k-1})$$
Further, if $k$ satisfies this condition, the [[Span|span]] of the [[Lists|list]] without $\vecbf{v}_{k}$ is the same as the [[Span|span]] of the [[Lists|list]] with $\vecbf{v}_{k}$.

> [!proof]-
> Since $\vecbf{v}_{1}, \cdots, \vecbf{v}_{n}$ is [[Linear Independence|linearly dependent]], there exists a non-zero [[Lists|list]] $a_{1},\dots,a_{n} \in \F$[^1] such that
> $$a_{1}\vecbf{v}_{1} + \dots + a_{n}\vecbf{v}_{n} = \vecbf{0}.$$
> Let $k$ be the largest non-zero element of $\{ 1,\dots, n \}$. Then
> $$\begin{align*}
> 	\vecbf{0} &= a_{1}\vecbf{v}_{1} + \dots + a_{n}\vecbf{v}_{n} \\
> 	\vecbf{0} &= a_{1}\vecbf{v}_{1} + \dots + a_{k}\vecbf{v}_{k} \\
> 	-a_{k}\vecbf{v}_{k} &= a_{1}\vecbf{v}_{1} + \dots + a_{k-1}\vecbf{v}_{k-1} \\
> 	\vecbf{v}_{k} &= -\dfrac{a_{1}}{a_{k}}\vecbf{v}_{1} - \dots - \dfrac{a_{k-1}}{a_{k}}\vecbf{v}_{k-1}, \\
> \end{align*}$$
> thus $v_{k} \in \text{span}(\vecbf{v}_{1}, \dots, \vecbf{v}_{k-1})$
> 
> ---
> 
> Now suppose $k$ is any element of $\{ 1,\dots,n \}$ such that $\vecbf{v}_{k} \in \text{span}( \vecbf{v}_{1}, \dots, \vecbf{v}_{k-1} )$.
> $$\begin{alignat}{4}
> 	&\hspace{0.5em}& \vecbf{v}_{k} &= b_{1}\vecbf{v}_{1} + \dots + b_{k-1}\vecbf{v}_{k-1} &\hspace{1em}& b_{1},\dots,b_{k-1} \in \F \hspace{0.5em}& (1)\\
> 	
> 	\forall \vecbf{u} \in \text{span}(\vecbf{v}_{1}, \dots, \vecbf{v}_{n}) && \vecbf{u} &= c_{1}\vecbf{v}_{1} + \dots + c_{n}\vecbf{v}_{n} && c_{1},\dots,c_{n} \in \F & (2)\\
> \end{alignat}$$
> In the $\text{RHS}$ of (2), $\vecbf{v}_{k}$ can be replaced with the $\text{RHS}$ of (1), meaning 
> $$\text{span}(\vecbf{v}_{1}, \dots, \vecbf{v}_{k-1}, \vecbf{v}_{k+1}, \dots, \vecbf{v}_{n}) = \text{span}(\vecbf{v}_{1}, \dots, \vecbf{v}_{k-1})$$

[^1]: [[Fields]]