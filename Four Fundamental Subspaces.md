---
tags:
  - atom
  - math
  - linear
---
Each [[Matrices|matrix]] $A \in \R^{m,n}$[^3] is associated with *four fundamental subspaces*:
1. $\text{null}(A)$[^1]
2. $\text{row}(A) =\text{col}(A^T)$[^2]
3. $\text{null}(A^T)$[^1]
4. $\text{col}(A) =\text{row}(A^T)$[^2]

> [!example]-
> $$\begin{array}{cc}
> 	A = \begin{bmatrix}
> 		1 & 3 \\
> 		2 & 6
> 	\end{bmatrix}
> 	&
> 	A^T = \begin{bmatrix}
> 		1 & 2 \\
> 		3 & 6
> 	\end{bmatrix}
> \end{array}$$
> Written in [[EF & REF|REF]], we get
> $$\begin{array}{cc}
> 	\begin{bmatrix}
> 		1 & 3 \\
> 		0 & 0
> 	\end{bmatrix}
> 	&
> 	\begin{bmatrix}
> 		1 & 2 \\
> 		0 & 0
> 	\end{bmatrix}
> \end{array}$$
> 1. $\text{null}(A) =\text{span}\left\{ \begin{bmatrix}-3 \\ 1\end{bmatrix} \right\}$[^1]
> 2. $\text{row}(A) =\text{span}\left\{ \begin{bmatrix}1\\ 3\end{bmatrix} \right\}$[^2]
> 3. $\text{null}(A^T) =\text{span}\left\{ \begin{bmatrix}-2\\ 1\end{bmatrix} \right\}$[^1]
> 4. $\text{col}(A) =\text{span}\left\{ \begin{bmatrix}1\\ 2\end{bmatrix} \right\}$[^2]

> [!theorem] For all $A \in \R^{m,n}$[^3], $\text{null}(A) =(\text{row(A)})^\perp$, and thus $\text{null}(A^T) =(\text{col(A)})^\perp$.

[^1]: [[Null Space]]
[^2]: [[Column Space]]
[^3]: [[Sets of Matrices]]
