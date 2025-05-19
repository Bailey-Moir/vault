---
tags:
  - atom
  - math
  - linear
---
A square [[Matrices|matrix]] is *orthogonal* if its columns form an [[Orthogonal Vectors|orthonormal]] [[Sets|set]].

> [!theorem] Every *orthogonal matrix* represents a rotation and/or reflection.

> [!proof]- If $\lambda$ is an [[Eigenvector & Eigenvalues|eigenvalue]] of an *orthogonal matrix* $Q$, $\left| \lambda \right| = 1$.
> Let $\{ \vecbf{v};\lambda \}$ be an [[Eigenvector & Eigenvalues|eigenvector-eigenvalue pair]] of $Q$. Then
> $$\begin{align}
> 	Q\vecbf{v} &= \lambda \vecbf{v} \\
> 	\| Q\vecbf{v} \| &= \| \lambda \vecbf{v} \| \\
> 	\| \vecbf{v} \| &= \left| \lambda \right|  \| \vecbf{v} \| && (4)  \\
> 	\left| \lambda \right| &= 1 && \vecbf{v} \ne \vecbf{0}\\
> \end{align}$$
> \[[[Vector Length#Properties of Vector Length]]\]


For $Q \in \R^{n,n}$, this is equivalent to
1. $Q^TQ = I_{n}$
2. $Q$ is [[Invertibility|invertible]] and $Q^{-1} = Q^T$
3. $\forall \vecbf{x},\vecbf{y} \in \R^n, \left( Q\vecbf{x}\cdot Q\vecbf{y}=\vecbf{x}\cdot \vecbf{y} \right)$
4. $\forall \vecbf{x} \in \R^n, \left( \| Q\vecbf{x} \| = \| \vecbf{x} \| \right)$

> [!proof]- $(0) \to (1)$
> $$\begin{align}
> 	\left( Q^TQ \right)_{ij} &= \vecbf{q}_{i}^T\vecbf{q}_{j} \\
> 	&= \vecbf{q}_{i} \cdot \vecbf{q}_{j} \\
> 	&= \left\{\begin{array}{ll}
> 		0, & \text{if } i \ne j \\
> 		1, & \text{if } i = j \\
> 	\end{array}\right. \\
> \end{align}$$
> Thus, $Q^TQ = I_{n}$

> [!proof]- $(1) \to (2)$
> If $Q^TQ = I_{n}$, since $Q$ is [[Invertibility|invertible]] (as $\text{rank}\,Q = n\to\text{nullity}\,Q = 0\to \left| Q \right| \ne 0$), $Q^T = I_{n}Q^{-1} = Q^{-1}$.

> [!proof]- $(2) \to (3)$
> For all $\vecbf{x},\vecbf{y} \in \R^n,$
> $$\begin{align}
> 	\left( Q\vecbf{x} \right) \cdot \left( Q\vecbf{y} \right) &= \left( Q\vecbf{x} \right)^T\left( Q\vecbf{y} \right) \\
> 	&= \left( \vecbf{x}^TQ^T \right)\left( Q\vecbf{y} \right) \\
> 	&= \vecbf{x}^TQ^TQ\vecbf{y} \\
> 	&= \vecbf{x}^TI_{n}\vecbf{y} && \text{Premise}\\
> 	&= \vecbf{x}^T\vecbf{y}\\
> 	&= \vecbf{x}\cdot\vecbf{y}\\
> \end{align}$$

> [!proof]- $\left( 3 \right) \to \left( 0 \right)$
> Let $\vecbf{x} = \vecbf{q}_{i}$, and $\vecbf{y} = \vecbf{q}_{j}$ (both in $\text{col}(Q)$). Then
> $$\begin{align}
> 	\vecbf{q}_{i} \cdot \vecbf{q}_{j} &= Q\vecbf{\hat{e}}_{i} \cdot Q \vecbf{\hat{e}}_{j} \\
> 	&= \vecbf{\hat{e}}_{i} \cdot \vecbf{\hat{e}}_{j} && \text{Premise} \\
> 	&= \left\{\begin{array}{ll}
> 		0, & \text{if } i \ne j \\
> 		1, & \text{if } i = j \\
> 	\end{array}\right. \\
> \end{align}$$
> Thus, $Q$ must be *orthogonal*.
