---
tags:
  - math
  - atom
---
Inverse matrices are square matrices that satisfy:
$$ A^{-1}A = I = AA^{-1} $$

Inverse matrices are used in the places where $\frac{1}{A}$ would be used in regular algebra (e.g. $AX = B \iff X = A^{-1}B$). This is because matrix division is not possible. Multiplying a matrix by its inverse produces an [[Identity Matrices|identity matrix]]: $AA^{-1} \equiv A^{-1}A \equiv I$.
 
 - $(A^{-1})^{-1} \equiv A$
 - $(AB)^{-1} \equiv B^{-1}A^{-1}$
   $\left(ABC\right)^{-1} = C^{-1}B^{-1}A^{-1}$

\[[[Matrix Invertibility|Matrix Invertibility]]\]
# Inverse of a 2x2 Matrix
$$ A = \begin{bmatrix} a & b \\ c & d\end{bmatrix} \implies A^{-1} = \dfrac{1}{\left|A\right|} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$
The matrix is transposed along the secondary diagonal, and this same diagonal then changes sign, divided by the [[Determinants|determinant]].