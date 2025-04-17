---
tags:
  - atom
  - math
  - linear
---
*The inverse power method* is [[The Power Method|the power method]] applied to the [[Matrix Invertibility|inverse]].

> [!proof]- Suppose $A$ is [[Matrix Invertibility|invertible]]. Then $\left\{ \vecbf{v};\lambda \right\}$ is an [[Eigenvector & Eigenvalues|eigenvector-eigenvalue pair]] of $A$ iff $\left\{ \vecbf{v}; \frac{1}{\lambda} \right\}$ is an [[Eigenvector & Eigenvalues|eigenvector-eigenvalue pair]] of $A^{-1}$.
> $$\begin{align}
> 	A\vecbf{v} &= \lambda \vecbf{v} \\
> 	A^{-1}A\vecbf{v} &= A^{-1}\lambda \vecbf{v} \\
> 	\vecbf{v} &= \lambda A^{-1} \vecbf{v} \\
> 	 A^{-1} \vecbf{v} &= \dfrac{1}{\lambda}\vecbf{v} && (1)\\
> \end{align}$$
> Note $(1)$ is allowed as $\lambda \ne 0$, as $A$ is [[Matrix Invertibility|invertible]].