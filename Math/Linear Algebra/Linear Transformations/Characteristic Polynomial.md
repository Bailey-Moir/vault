---
tags:
  - atom
  - math
---
Let $A\in \R^{n,n}$[^1]. The *characteristic polynomial* $p$ for $A$ is
$$p(\lambda) := \left| A-\lambda I \right| $$
- $\lambda$ is an [[Eigenvectors & Eigenvalues|eigenvalue]] of $A$ iff $p(\lambda) = 0$.
- $p(\lambda)$ is always [[Polynomials#Degree|degree]] $n$.

> [!example]-
> For $A=\begin{bmatrix}5&-6\\2&-2\end{bmatrix}$,
> $$\begin{align*}
> 	p(\lambda) &= \begin{vmatrix}
> 		5-\lambda&-6\\2&-2-\lambda
> 	\end{vmatrix} \\
> 	&= \left( 5-\lambda \right)\left( -2-\lambda \right) - (-6)2 \\
> 	&= \left( \lambda-5 \right)\left( \lambda+2 \right) + 12 \\
> 	&= \lambda^2-3\lambda-10 + 12 \\
> 	&= \lambda^2-3\lambda+2\\
> 	&= \left( \lambda-2 \right)\left( \lambda-1 \right)\\
> \end{align*}$$
> $\therefore \lambda=1,\lambda=2$

[^1]: [[Sets of Matrices]]
