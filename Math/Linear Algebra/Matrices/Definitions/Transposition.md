---
tags:
  - math
  - atom
---
![100](transposing-matrices.gif)
Transposing a matrix flips a matrix across the main diagonal. A transposed matrix is denoted by $\square^T$.
$$\begin{array}{c}
A \in \mathbb{M}_{m \times n} \implies A^T \in \mathbb{M}_{n \times m}\\ \begin{bmatrix} 
	\textcolor{green}a & b & c \\ 
	d & \textcolor{green}e & f 
\end{bmatrix}^T
=
\begin{bmatrix} 
	\textcolor{green}a & d \\
	b & \textcolor{green}e \\
	c & f
\end{bmatrix} 
\end{array}$$
# Properties of Transposition
- $\left(A+B\right)^T = A^T + B^T$
- $\left(A^T\right)^T = A$
- $\left(AB\right)^T = B^TA^T$
  $\left(ABC\right)^T = C^TB^TA^T$