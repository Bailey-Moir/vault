---
tags:
  - atom
  - math
---
For any $A\in\mathcal{M}(m,n)$[^1] and $\vecbf{v}\in\R^n$,
$$A\vecbf{v}=A\begin{bmatrix}
	v_{1} \\
	v_{2} \\
	\dots \\
	v_{n}
\end{bmatrix} = v_{1}A\vecbf{e}_{1} + v_{2}A\vecbf{e}_{2} + \dots + v_{n}A\vecbf{e}_{n}$$
> [!note]- 2x2 Version
> For any $A \in \mathcal{M}(2,2)$[^1] and $\vecbf{v}\in\R^2$
> $$A\vecbf{v}=A\begin{bmatrix}
> 	v_{1} \\
> 	v_{2}
> \end{bmatrix} = v_{1}A\vecbf{e}_{1} + v_{2}A\vecbf{e}_{2}$$

This is often a much easier way of calculating [[Matrix Addition|matrix]] [[Vectors|vector]] [[Matrix Multiplication|multiplication]], as $Ae_i$ is the $i$-th column of $A$;
$$ A\vecbf{e}_{i}= \begin{bmatrix}
	a_{1i} \\
	a_{2i} \\
	\dots \\
	a_{mi}
\end{bmatrix} $$
> [!example]- Counter-clockwise Rotation
> $$\begin{align*}
> 	\begin{bmatrix}
> 		0&-1\\
> 		1&0\\
> 	\end{bmatrix}\begin{bmatrix}
> 		v_{1}\\
> 		v_{2}
> 	\end{bmatrix} &= v_{1}A\begin{bmatrix} 1\\0 \end{bmatrix} + v_{2}A\begin{bmatrix} 0\\1 \end{bmatrix} \\
> 	&= v_{1}\begin{bmatrix} 0\\1 \end{bmatrix} + v_{2}\begin{bmatrix} -1\\0 \end{bmatrix} \\
> 	&= \begin{bmatrix} -v_{2}\\ v_{1} \end{bmatrix}
> \end{align*}$$

> [!note]- Types of Transformations
> - Scale
> - Rotation
> - Reflection
> - Sheer

\[[[Matrix Multiplication]], [[Basis Vectors]]\]

[^1]: [[Sets of Matrices]]