---
tags:
  - atom
  - math
---
For $T \in \mathcal{L}(V)$[^1], an *eigenvector* of $T$ is a non-zero vector $\vecbf{v} \in V$ such that
$$T\,\vecbf{v}=\lambda \vecbf{v}$$
for some scalar $\lambda \in \F$. This scalar $\lambda$ is called the *eigenvalue* of $T$ belonging to the *eigenvector* $\vecbf{v}$, and $\{ \vecbf{v};\lambda \}$ is an *eigenvector-eigenvalue pair*.
- An *eigenvector* of $A$ is a [[Vectors|vector]] that does not change direction when the [[Linear Transformations|transformation]] $A$ is applied, and its *eigenvalue* $\lambda$ is how much it is scaled.
# Properties of Eigenvector and Eigenvalues
- An $n\times n$ [[Matrices|matrix]] has $n$ *eigenvalues* (possibly repeated).
- If $\left\{ \vecbf{v};\lambda \right\}$ is an *eigenvector-eigenvalue pair*, then so is $\left\{ t\vecbf{v};\lambda \right\}$ for $t\neq0$[^2].
- $\forall n \in\N, \forall A\in\R^{n,n}$
  $\{ \vecbf{v};\lambda \}\text{ for } A \iff \left( A-\lambda I \right)\vecbf{v}=\vecbf{0}$[^2]
> [!proof]-
> $$\begin{align*}
> 	A\vecbf{v}&=\lambda \vecbf{v} \\
> 	A\vecbf{v} - \lambda \vecbf{v} &= \vecbf{0} \\
> 	A\vecbf{v} - \lambda I \vecbf{v} &= \vecbf{0} && (1)\\
> 	\left(A - \lambda I \right) \vecbf{v} &= \vecbf{0} \\
> \end{align*}$$
  > \[(1) [[Identity Matrices]]\]

- $\lambda$ is a *eigenvalue* of $A$ iff $A-\lambda I$ is [[Singular Matrices|singular]][^3]

[^1]: [[Linear Maps]]
[^2]: [[Eigenspaces]]
[^3]: [[Characteristic Polynomial]]
