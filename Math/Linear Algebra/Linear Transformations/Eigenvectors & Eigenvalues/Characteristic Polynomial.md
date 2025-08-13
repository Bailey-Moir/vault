---
tags:
  - atom
  - math
  - linear
---
The *characteristic polynomial* $P_{T}$ for $T \in \mathcal{L}(V)$ is
$$P_{T}(\lambda) := \left| T-\lambda I \right| $$
> [!note] $P(\lambda)$ is always [[Polynomials#Degree|degree]] $n$.

> [!theorem]- $\lambda$ is an [[Eigenvectors & Eigenvalues|eigenvalue]] of $T$ iff $P_{T}(\lambda) = 0$.
> $\lambda$ is an [[Eigenvectors & Eigenvalues|eigenvalue]] of $T \in \mathcal{L}(V)$ iff $T-\lambda I$ is [[Singular Matrices|singular]] (not [[Linear Map Invertibility|invertible]])[^2], which is the case iff
> $$\left| T - \lambda I \right| = P_{T}(\lambda) = 0 $$

> [!example]- Finding the [[Eigenvectors & Eigenvalues|eigenvalues]] of $A=\begin{bmatrix}5&-6\\2&-2\end{bmatrix}$
> $$\begin{align*}
> 	P_{A}(\lambda) &= \begin{vmatrix}
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
[^2]: [[Eigenvectors & Eigenvalues#Theorems]], Theorem 2
