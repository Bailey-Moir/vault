---
tags:
  - atom
  - math
---
Let $A\in\mathcal{M}(n,n)$^[[[Sets of Matrices]]]. An *eigenvector* of $A$ is a non-zero [[Vectors|vector]] $\vecbf{v}$ such that
$$A\vecbf{v}=\lambda \vecbf{v}$$
for some scalar $\lambda$. This scalar $\lambda$ is called the *eigenvalue* of $A$ belonging to the *eigenvector* $\vecbf{v}$, and $\{ v;\lambda \}$ is an *eigenvector-eigenvalue pair*.

# Properties of Eigenvector and Eigenvalues
- An $n\times n$ [[Matrices|matrix]] can have up to $n$ *eigenvector-eigenvalue pairs*.
- If $A$ is [[Math/Linear Algebra/Matrices/Invertibility|non-invertible]], then there exists an *eigenvector-eigenvalue pair* $\{ \vecbf{v};0 \}$.
- $\forall n \in\N,\forall A\in\mathcal{M}(n,n),$
  $\{ \vecbf{v};\lambda \}\text{ for } A \iff \left( A-\lambda I \right)\vecbf{v}=\vecbf{0}$
> [!proof]-
> $$\begin{align*}
> 	A\vecbf{v}&=\lambda \vecbf{v} \\
> 	A\vecbf{v} - \lambda \vecbf{v} &= \vecbf{0} \\
> 	A\vecbf{v} - \lambda I \vecbf{v} &= \vecbf{0} && (1)\\
> 	\left(A - \lambda I \right) \vecbf{v} &= \vecbf{0} \\
> \end{align*}$$
> \[(1) [[Identity Matrices]]\]