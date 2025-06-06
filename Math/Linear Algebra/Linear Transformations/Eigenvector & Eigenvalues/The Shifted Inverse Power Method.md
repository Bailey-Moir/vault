---
tags:
  - atom
  - math
  - linear
---
*The shifted inverse power method* allows you to approximate any [[Eigenvector & Eigenvalues|eigenvalue]] given an approximation of that [[Eigenvector & Eigenvalues|eigenvalue]] by using the [[The Power Method|power method]] on the [[The Inverse Power Method|inverse]] of the [[The Shifted Power Method|shifted]] matrix.

> [!proof]- Suppose $A$ is [[Matrix Invertibility|invertible]]. Then $\left\{ \vecbf{v};\lambda \right\}$ is an [[Eigenvector & Eigenvalues|eigenvector-eigenvalue pair]] of $A$ iff $\left\{ \vecbf{v}; \frac{1}{\lambda-c} \right\}$ is an [[Eigenvector & Eigenvalues|eigenvector-eigenvalue pair]] of $(A-cI)^{-1}$.
> Suppose $\lambda$ is an [[Eigenvector & Eigenvalues|eigenvalue]] of $A$, and $c$ is close to $\lambda$ but $c \ne \lambda$.
> 
> Then $A-cI$ is a matrix with an [[Eigenvector & Eigenvalues|eigenvalue]] close to $0$.
> 
> [[The Inverse Power Method|The inverse power method]] will find this small eigenvalue, and undoing this shift will give an approximation for $\lambda$.
