---
tags:
  - atom
  - math
  - linear
---
To find two [[Eigenvectors & Eigenvalues|eigenvector-eigenvalue pairs]] of a [[Diagonalisation|diagonalisable]] [[Matrices|matrix]] $A \in \R^{n,n}$[^1],
1. use [[The Power Method|the power method]] on $A$, giving $\{ \vecbf{v}_{1}; \lambda_{1}\}$ of $A$, and
2. use [[The Power Method|the power method]] on $A - \lambda_{1}$, giving $\{ \vecbf{v}_{2}; \mu \}$ of $A-\lambda_{1}$, and thus $\{ \vecbf{v}_{2}; \mu + \lambda_{1}\}$ of $A$.

> [!lemma]- $\{ \vecbf{v}, \lambda \}$ is an [[Eigenvectors & Eigenvalues|eigenvector-eigenvalue pair]] of $A$ iff $\{ \vecbf{v}, \lambda - c \}$ is an [[Eigenvectors & Eigenvalues|eigenvector-eigenvalue pair]] of $\left( A - cI \right)$.
> $$\begin{align}
> 	A\vecbf{v} &= \lambda \vecbf{v} \\
> 	A\vecbf{v} - c\vecbf{v} &= \lambda \vecbf{v} - c\vecbf{v} \\
> 	(A - cI)\vecbf{v} &= (\lambda - c)\vecbf{v} \\
> \end{align}$$

\[[[Eigenvectors & Eigenvalues]]\]

[^1]: [[Sets of Matrices]]

