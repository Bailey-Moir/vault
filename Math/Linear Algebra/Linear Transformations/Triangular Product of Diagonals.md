---
tags:
  - atom
  - math
---
A [[Matrices|matrix]] of the form $\begin{bmatrix}a_{11}&a_{12}&a_{13}\\0&a_{22}&a_{23}\\0&0&a_{33}\end{bmatrix}$ has a [[Determinants|determinant]] of $a_{11}a_{22}a_{33}$;
$$\left|\begin{matrix}a_{11}&a_{12}&a_{13}\\0&a_{22}&a_{23}\\0&0&a_{33}\end{matrix}\right| = a_{11}\times a_{22}\times a_{33}$$
> [!proof]-
> Using a [[Co-factor Expansion|co-factor expansion]] along the first column,
> $$\begin{align*}
> 	\left|\begin{matrix}
> 		a_{11} & a_{12} & a_{13} \\
> 		0 & a_{22} & a_{23} \\
> 		0 & 0 & a_{33}
> 	\end{matrix}\right| &= a_{11}\left|\begin{matrix} 
> 		a_{22} & a_{23}\\0 & a_{33}
> 	\end{matrix}\right| - 0 + 0 \\
> 	&= a_{11}(a_{22}a_{33}-0) \\
> 	&= a_{11}a_{22}a_{33} \\
> \end{align*}$$
