---
tags:
  - atom
  - math
---
Let $A\in\mathcal{M}(n,n)$[^1]. An *eigenvector* of $A$ is a non-zero [[Vectors|vector]] $\vecbf{v}$ such that
$$A\vecbf{v}=\lambda \vecbf{v}$$
for some scalar $\lambda$. This scalar $\lambda$ is called the *eigenvalue* of $A$ belonging to the *eigenvector* $\vecbf{v}$, and $\{ \vecbf{v};\lambda \}$ is an *eigenvector-eigenvalue pair*.
- An *eigenvector* of $A$ is a [[Vectors|vector]] that does not change direction when the [[Linear Transformations|transformation]] $A$ is applied, and its *eigenvalue* $\lambda$ is how much it is scaled.
# Properties of Eigenvector and Eigenvalues
- An $n\times n$ [[Matrices|matrix]] has $n$ *eigenvalues* (possibly repeated).
- If $\left\{ \vecbf{v};\lambda \right\}$ is an *eigenvector-eigenvalue pair*, then so is $\left\{ t\vecbf{v};\lambda \right\}$ for $t\neq0$.
- $\forall n \in\N, \forall A\in\mathcal{M}(n,n)$
  $\{ \vecbf{v};\lambda \}\text{ for } A \iff \left( A-\lambda I \right)\vecbf{v}=\vecbf{0}$
> [!proof]-
> $$\begin{align*}
> 	A\vecbf{v}&=\lambda \vecbf{v} \\
> 	A\vecbf{v} - \lambda \vecbf{v} &= \vecbf{0} \\
> 	A\vecbf{v} - \lambda I \vecbf{v} &= \vecbf{0} && (1)\\
> 	\left(A - \lambda I \right) \vecbf{v} &= \vecbf{0} \\
> \end{align*}$$
  > \[(1) [[Identity Matrices]]\]
- $\lambda$ is a *eigenvalue* of $A$ iff $A-\lambda I$ is [[Singular Matrices|singular]][^2].

[^1]: [[Sets of Matrices]]
[^2]: [[Characteristic Polynomial]]
