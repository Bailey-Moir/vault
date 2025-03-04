---
tags:
  - atom
  - math
  - linear
---
The *span* of a [[Lists|list]] $\vecbf{v}_{1}, \dots, \vecbf{v}_{n}$ is its [[Sets|set]] of [[Linear Combinations|linear combinations]], denoted by $\text{span}(\vecbf{v}_1, \dots, \vecbf{v}_n)$.
$$ \text{span}(\vecbf{v}_1, \dots, \vecbf{v}_n) = \left\{ a_1\vecbf{v}_1 + \dots + a_n\vecbf{v}_n : a_1,\dots, a_n \in \F \right\} $$
- If $\text{span}(\vecbf{v}_1,\dots,\vecbf{v}_n) = V$, we say that "$\vecbf{v}_{1}, \dots, \vecbf{v}_{n}$ spans $V$", and that "$\vecbf{v}_{1}, \dots, \vecbf{v}_{n}$ is a **spanning set/list** of $V$."
- The *span* of $\vecbf{v}_1, \dots, \vecbf{v}_n \in V$ is the smallest [[Subspaces|subspace]] of $V$ containing $\vecbf{v}_1, \dots, \vecbf{v}_n \in V$.

> [!example]- Determining if a vector is in the span of others requires solving a [[Linear Systems|system of linear equations]].
> 
> Is $\begin{bmatrix}1\\2\\3\end{bmatrix} \in \text{span}\left( \begin{bmatrix}1\\1\\1\end{bmatrix}, \begin{bmatrix}0\\2\\3\end{bmatrix} \right)$?
> 
> This is the case iff there exists $c_{1}$ and $c_{2}$ such that
> $$\begin{bmatrix}1\\2\\3\end{bmatrix} = c_{1}\begin{bmatrix}1\\1\\1\end{bmatrix} + c_{2}\begin{bmatrix}0\\2\\3\end{bmatrix}$$
> This gives the [[Linear Systems|system of linear equations]]
> $$\begin{array}{cccc}
> 	\begin{bmatrix}
> 		1&0\\
> 		1&2\\
> 		1&3
> 	\end{bmatrix}
> 	\begin{bmatrix}
> 		c_{1}\\
> 		c_{2}
> 	\end{bmatrix}
> 	=
> 	\begin{bmatrix}
> 		1\\
> 		2\\
> 		3
> 	\end{bmatrix}
> 	&&&
> 	\left[
> 		\left.\begin{matrix}
> 			1&0\\
> 			1&2\\
> 			1&3
> 		\end{matrix}
> 		\hspace{0.4em}
> 		\right|
> 		\hspace{0.4em}
> 		\begin{matrix}
> 			1\\
> 			2\\
> 			3
> 		\end{matrix}
> 	\right]
> 	
> \end{array}
> $$
> which in [[EF & REF|REF]] is
> $$\left[
> 	\left.\begin{matrix}
> 		1&0\\
> 		0&2\\
> 		0&0
> 	\end{matrix}
> 	\hspace{0.4em}
> 	\right|
> 	\hspace{0.4em}
> 	\begin{matrix}
> 		1\\
> 		1\\
> 		\frac{1}{2}
> 	\end{matrix}
> \right]$$
> which is [[Consistency of Linear Systems|inconsistent]], meaning the vector is **not** in the **span**.


\[[[Set-Builder Notation]]\]