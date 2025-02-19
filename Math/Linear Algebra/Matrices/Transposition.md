---
tags:
  - math
  - atom
  - linear
---
The *transpose* of a [[Matrices|matrix]] $A$ (denoted by $A^T$) is obtained by swapping rows with columns (flipping across the main diagonal)
$$\begin{array}{c}
\begin{bmatrix} 
	\textcolor{Orchid}a & b & c \\ 
	d & \textcolor{Orchid}e & f 
\end{bmatrix}^T = 
\begin{bmatrix} 
	\textcolor{Orchid}a & d \\
	b & \textcolor{Orchid}e \\
	c & f
\end{bmatrix}  \\

A \in \F^{m,n} \iff A^T \in \F^{n,m} \\
(A^T)_{k,j} = A_{j,k} \\
\end{array}$$
> [!note] $\forall A \in \F^{m,n},\, \begin{array}{c} \forall j \in \{ 1,\dots,m \}, A^T_{\cdot ,j} = A_{j,\cdot} \\ \forall k \in \{ 1,\dots,n \}, A^T_{k,\cdot} = A_{\cdot,k} \end{array}$
# Properties of Transposition
- $\left(A+B\right)^T = A^T + B^T$
- $\left( \lambda A \right)^T = \lambda (A)^T$
- $\left(A^T\right)^T = A$
- $\left(AB\right)^T = B^TA^T$
  $\left(ABC\right)^T = C^TB^TA^T$

  
![100](transposing-matrices.gif)
