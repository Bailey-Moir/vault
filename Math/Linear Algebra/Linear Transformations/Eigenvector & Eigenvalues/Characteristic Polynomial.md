---
tags:
  - atom
  - math
---
The *characteristic polynomial* $P_{T}$ for $T \in \mathcal{L}(V)$ is
$$P_{T}(\lambda) := \left| T-\lambda I \right| $$
- $P(\lambda)$ is always [[Polynomials#Degree|degree]] $n$.

> [!proof]- $\lambda$ is an [[Eigenvector & Eigenvalues|eigenvalue]] of $T$ iff $P_{T}(\lambda) = 0$.
> $\lambda$ is an [[Eigenvector & Eigenvalues|eigenvalue]] of $T$ iff
> $$\begin{align}
> 	T\,\vecbf{v} &= \lambda \vecbf{v} \\
> 	T\,\vecbf{v} - \lambda \vecbf{v} &= \vecbf{0} \\
> 	T\,\vecbf{v} - \lambda I \vecbf{v} &= \vecbf{0} \\
> 	(T - \lambda I)\vecbf{v}&= \vecbf{0} \\
> \end{align}$$
> has a non-trivial solutions, which happens iff $(T-\lambda I)$ is [[Singular Matrices|singular]] (not invertible), which is the case iff
> $$\left| T - \lambda I \right| = P_{T}(\lambda) = 0 $$

> [!example]-
> For $A=\begin{bmatrix}5&-6\\2&-2\end{bmatrix}$,
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

