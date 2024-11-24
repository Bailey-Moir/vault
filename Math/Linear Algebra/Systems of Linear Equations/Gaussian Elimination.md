---
tags:
  - atom
  - math
---
![200|center](gaussian-elimination.excalidraw)
1. **Augmented Matrix**: Write the linear system as an [[Augmented Matrices|augmented matrix]].
2. **Row Reduction**: Use a sequence of elementary row operations to put the matrix in [[EF & REF|REF]].
3. **Solve the System**: Write out the equivalent system in [[EF & REF|EF]] and solve by back-substitution.

- $m < n \implies |S| \ne 1$

> [!example]-
> $$\begin{bmatrix}
> 	1 & 1 & 1 & -1 & : & 2 \\
> 	0 & 0 & 2 & 2 & : & 0 \\
> \end{bmatrix}$$
> Pivots: $x$ and $z$.
> Free variables: $y$ and $w$
> One parameter for each free variable.
> let $y = s$, $w = t$, $s,t \in \R$.
> $$\begin{align*}
> 	2z + 2t &= 0 \\
> 	z &= -t
> \end{align*}$$
> $$\begin{align*}
> 	x + s - t - t &= 2 \\
> 	x &= 2 + 2t - s
> \end{align*}$$
> \[[[Atoms/Calculus/Linear Algebra/Matrices/Matrices]]\]

> [!example]-
> $$\begin{array}{l}
> 	\begin{bmatrix}
> 		1 & 2 & : & 2 \\
> 		3 & 4 & : & 12
> 	\end{bmatrix} \\
> 	R_2 \leftarrow  R_2 - 3R_1 \\
> 	\begin{bmatrix}
> 		1 & 2 & : & 2 \\
> 		0 & -2 & : & 6
> 	\end{bmatrix} \\
> 	\text{In REF, and all variables are pivots.} \\
> 	y = -3 \\
> 	\begin{align*}
> 		x &= 2 - 2y \\
> 		&= -10 \\ 
> 	\end{align*}
> \end{array}$$
> \[[[Atoms/Calculus/Linear Algebra/Matrices/Matrices]]\]