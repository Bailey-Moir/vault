---
tags:
  - atom
  - math
  - linear
---
$A \in \R^{n,n}$ is [[Orthogonal Diagonalisation|orthogonally diagonalisable]] iff $A$ is [[Symmetric Matrices|symmetric]].

> [!lemma]- **(1)** If $A \in \R^{n,n}$ is [[Orthogonal Diagonalisation|orthogonally diagonalisable]], then $A$ is [[Symmetric Matrices|symmetric]].
> Since $A$ is [[Orthogonal Diagonalisation|orthogonally diagonalisable]], there exists an [[Orthogonal Matrices|orthogonal matrix]] $Q$ and [[Diagonal Matrices|diagonal matrix]] $D$ such that
> $$\begin{align}
> 	A &= QDQ^T \\
> 	A^T &= \left( QDQ^T \right)^T \\
> 	&= \left( Q^T \right)^TD^TQ^T \\
> 	&= QDQ^T \\
> 	&= A \\
> \end{align}$$

> [!lemma]- **(2)** If $A \in \R^{n,n}$ is [[Symmetric Matrices|symmetric]], [[Eigenvectors & Eigenvalues|eigenvectors]] with distinct [[Eigenvectors & Eigenvalues|eigenvalues]] are [[Orthogonal Vectors|orthogonal]].
> Suppose $A\vecbf{v}_{1} = \lambda_{1}\vecbf{v}_{1}$ and $A\vecbf{v}_{2} = \lambda_{2}\vecbf{v}_{2}$, where $\lambda_{1} \ne \lambda_{2}$. Then, as $A$ is [[Symmetric Matrices|symmetric]],
> $$\begin{align}
> 	\lambda_{1}\left( \vecbf{v}_{1} \cdot \vecbf{v}_{2} \right) &= (\lambda_{1}\vecbf{v}_{1})\cdot \vecbf{v}_{2} && (1)\\
> 	&= (A\vecbf{v}_{1})\cdot \vecbf{v}_{2} \\
> 	&= (A\vecbf{v}_{1})^T\vecbf{v}_{2} && (1)\\
> 	&= \vecbf{v}_{1}^TA^T\vecbf{v}_{2} \\
> 	&= \vecbf{v}_{1}^TA\vecbf{v}_{2} && \text{Symmetric}\\
> 	&= \vecbf{v}_{1}^T(\lambda_{2}\vecbf{v}_{2})\\
> 	&= \lambda_{2}(\vecbf{v}_{1}\cdot\vecbf{v}_{2}) && (1)\\
> \end{align}$$
> \[$(1)$ [[Dot Product#Properties of Dot Product]]\]
> 
> Thus, since $\lambda_{1}\ne\lambda_{2}$, $\vecbf{v}_{1}\cdot \vecbf{v}_{2} = 0$, meaning $\vecbf{v}_{1}$ and $\vecbf{v}_{2}$ are [[Orthogonal Vectors|orthogonal]].

> [!lemma]- **(3)** If $A$ is a [[The Real Numbers|real]] [[Symmetric Matrices|symmetric matrix]], then all of its [[Eigenvectors & Eigenvalues|eigenvalues]] are [[The Real Numbers|real]], and each [[Eigenvectors & Eigenvalues|eigenvalue]] has a real [[Eigenvectors & Eigenvalues|eigenvector]].
> $$\begin{align}
> 	\lambda\left( \vecbf{v} \cdot \overline{\vecbf{v}} \right) &= \left( \lambda \vecbf{v} \right) \cdot \overline{\vecbf{v}} && (1) \\
> 	&= \left( A \vecbf{v} \right) \cdot \overline{\vecbf{v}} \\
> 	&= \left( A \vecbf{v} \right)^T\overline{\vecbf{v}}  && (1) \\
> 	&= \vecbf{v}^T A^T \overline{\vecbf{v}} \\
> 	&= \vecbf{v}^T A \overline{\vecbf{v}} && \text{Symmetric} \\
> 	&= \vecbf{v}^T \overline{A\vecbf{v}} && \text{Real} \\
> 	&= \vecbf{v}^T \overline{\lambda \vecbf{v}} \\
> 	&= \overline{\lambda} \left( \vecbf{v} \cdot \overline{\vecbf{v}} \right) \\
> \end{align}$$
> \[$(1)$ [[Dot Product#Properties of Dot Product]]\]
> 
> This gives $\left( \lambda - \overline{\lambda} \right)\left( \vecbf{v}\cdot\overline{\vecbf{v}} \right) = 0$. If the $k$-th column of $\vecbf{v}$ is $a_{k} + b_{k}i$, then
> $$\begin{align}
> 	\vecbf{v}\cdot\overline{\vecbf{v}} &= \sum_{k \in \Z_{n}} (a_{k}+b_{k}i)(a_{k}-b_{k}i) \\
> 	&= \sum_{k \in \Z_{n}} a_{k}^2+b_{k}^2 \\
> \end{align}$$
> Each of these terms if greater than or equal to $0$, so $\vecbf{v}\cdot\overline{\vecbf{v}} = 0$ iff each term is $0$. This is not possible, as this would mean $\vecbf{v} = \vecbf{0}$, which is not an [[Eigenvectors & Eigenvalues|eigenvector]]. Thus, the only possibility is that $\lambda = \overline{\lambda}$.

> [!proof]-
> $\left( \implies \right)$
> See **lemma 1**.
> 
> $\left( \impliedby \right)$
> Suppose $A \in \R^{n.n}$ is [[Symmetric Matrices|symmetric]].
> 
> **Base Case**
> If $n=1$, then $A \in \R^{n,n} = \R^{1,1}$ is [[Orthogonal Diagonalisation|orthogonally diagonalisable]], as $A$ is a [[Diagonal Matrices|diagonal matrix]], and so  it has a [[Orthogonal Diagonalisation|orthogonal diagonalisation]] of
> $$A = I_{1}AI_{1}$$
> **Induction Step**
> Suppose all [[Symmetric Matrices|symmetric matrices]] $A \in \R^{k,k}$ are [[Orthogonal Diagonalisation|orthogonally diagonalisable]] for some $k \in \Z^+$.
> 
> By **lemma 3**, $A$ has a real [[Eigenvectors & Eigenvalues|eigenvector]] $\vecbf{v}_{1}$, which we can take to be [[Unit Vectors|normalised]].
> 
> We can extend $\{ \vecbf{v}_{1} \}$ to an [[Orthogonal Vectors|orthonormal]] [[Basis|basis]] $\{ \vecbf{v}_{1},\dots,\vecbf{v}_{k+1} \}$ of $\R^{k+1}$
> 
> Let $Q_{1} = \left[ \vecbf{v}_{1}\;\cdots\; \vecbf{v}_{k+1} \right]$, meaning $Q_{1}$ is [[Orthogonal Matrices|orthogonal]].
> 
> Thus,
> $$\begin{align}
> 	Q_{1}^TAQ_{1} &= \begin{bmatrix}
> 		\vecbf{v}_{1}^T \\
> 		\vecbf{v}_{2}^T \\
> 		\vdots \\
> 		\vecbf{v}_{k+1}^T \\
> 	\end{bmatrix} A \begin{bmatrix}
> 		\vecbf{v}_{1} & \vecbf{v}_{2} & \cdots & \vecbf{v}_{k+1}
> 	\end{bmatrix} \\
> 	&= \begin{bmatrix}
> 		\vecbf{v}_{1}^T \\
> 		\vecbf{v}_{2}^T \\
> 		\vdots \\
> 		\vecbf{v}_{k+1}^T \\
> 	\end{bmatrix} \begin{bmatrix}
> 		\lambda_{1}\vecbf{v}_{1} & A\vecbf{v}_{2} & \cdots & A\vecbf{v}_{k+1}
> 	\end{bmatrix} \\
> 	&= \begin{bmatrix}
> 		\lambda_{1} \left( \vecbf{v}_{1} \cdot \vecbf{v}_{1} \right) & * & \cdots & *  \\
> 		\lambda_{1} \left( \vecbf{v}_{2} \cdot \vecbf{v}_{1} \right) & \\
> 		\vdots && A_{1} & \\
> 		\lambda_{1} \left( \vecbf{v}_{k+1} \cdot \vecbf{v}_{1} \right)  \\
> 	\end{bmatrix} \\
> 	&= \begin{bmatrix}
> 		\lambda_{1} & * & \cdots & *  \\
> 		0 & \\
> 		\vdots && A_{1}\\
> 		0 & \\
> 	\end{bmatrix} = B\\
> \end{align}$$
> $B$ is [[Symmetric Matrices|symmetric]], as
> $$\begin{align}
> 	B^T &= \left( Q_{1}^TAQ_{1} \right)^T \\
> 	&= Q_{1}^TA^TQ_{1} \\
> 	&= Q_{1}^TAQ_{1} && \text{Induction Hypothesis}\\
> 	&= B \\
> \end{align}$$
> Thus, the $*$s are $0$s, and $A_{1}$ is a $k\times k$ [[Symmetric Matrices|symmetric matrix]], so $A_{1}$ is [[Orthogonal Diagonalisation|orthogonally diagonalisable]].
> 
> Thus, there is an [[Orthogonal Matrices|orthogonal matrix]] $Q_{2}'$ such that
> $$Q_{2}'^TA_{1}Q_{2}' = D_{2}'$$
> 
> is [[Diagonal Matrices|diagonal]].
> 
> Let
> $$Q_{2} = \begin{bmatrix}
> 	1 & 0 & \cdots & 0 \\
> 	0 \\
> 	\vdots && Q_{2}' \\
> 	0
> \end{bmatrix}$$
> Then $Q_{2}$ is [[Orthogonal Matrices|orthogonal]] as well.
> 
> So $Q_{1}Q_{2}$ is [[Orthogonal Matrices|orthogonal]].
> 
> Therefore, as
> $$\begin{align}
> 	\left( Q_{1}Q_{2} \right)^TA\left( Q_{1}Q_{2} \right) &= Q_{2}^T\left( Q_{1}^TAQ_{1} \right)Q_{2} \\
> 	&= Q_{2}^TBQ_{2} \\
> 	&= \begin{bmatrix}
> 		\lambda_{1} & 0 & \cdots & 0 \\
> 		0 \\
> 		\vdots && Q_{2}'^TA_{1}Q_{2}' \\
> 		0 \\
> 	\end{bmatrix} \\
> 		&= \begin{bmatrix}
> 		\lambda_{1} & 0 & \cdots & 0 \\
> 		0 \\
> 		\vdots && D_{2}' \\
> 		0 \\
> 	\end{bmatrix} \\
> \end{align}$$
> This is [[Diagonalisation|diagonal]], so $A$ is [[Orthogonal Diagonalisation|orthogonally diagonalisable]].
