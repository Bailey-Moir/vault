---
tags:
  - atom
  - comp
  - math
---
Let an finite [[Ordered Sets|ordered]] [[Universal Set|universal set]] $U = \left( u_{1},\dots,u_{m} \right)$ and [[Sets|sets]] $S_{1},\dots,S_{n} \subseteq U$ be given. These [[Sets|sets]]' *characteristic matrix* $A \in \Z_{2}^{m,n}$ is given by
$$a_{i,j} = \begin{cases}
1 & a_{n} \in S_{m} \\
0 & \text{otherwise}.
\end{cases} $$
> [!example] $S_{1} = \{ a,d \}$, $S_{2} = \{ c \}$, $S_{3} = \{ b,d,e \}$, and $S_{4} = \{ a, c, d \}$.
> $$\begin{array}{cc}
> 	& \begin{array}{ccc}
> 		S_{1} \hspace{-0.5em} & S_{2} \hspace{-0.5em} & S_{3} \hspace{-0.5em} & \hspace{-0em} S_{4}
> 	\end{array} \\
> 	\begin{array}{c}
> 		a \\ b \\ c \\ d \\ e
> 	\end{array} \hspace{-0.5em} &
> 	{\begin{bmatrix}
> 		1 & 0 & 0 & 1 \\
> 		0 & 0 & 1 & 0 \\
> 		0 & 1 & 0 & 1 \\
> 		1 & 0 & 1 & 1 \\
> 		0 & 0 & 1 & 0 \\
> 	\end{bmatrix}}
> \end{array}$$

> [!note] Typically these [[Matrices|matrices]] are [[Sparse Matrices|sparse]], and thus are normally stored as [[Ordered Sets|pairs]] $\left( u_{n}, S_{m} \right)$.