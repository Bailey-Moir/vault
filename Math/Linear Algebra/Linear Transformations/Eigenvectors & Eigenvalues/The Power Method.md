---
tags:
  - atom
  - math
  - linear
---
*The power method* is a method for finding [[Dominant Eigenvectors & Eigenvalues|dominant eigenvectors and eigenvalues]]

> [!motivation]-
>  For an $n\times n$ [[Matrices|matrix]], this is typically done by 
> - calculating the [[Characteristic Polynomial|characteristic polynomial]] (a $n\times n$ [[Determinants|determinant]]),
> - finding the roots of that $n$-th order polynomial, and
> - solving the $n$ different [[Eigenspaces|eigenspaces]] using [[Gaussian Elimination|Gaussian elimination]].
> 
> Each of these steps is $O\hspace{-0.2em}\left( n^3 \right)$[^1], which is very inefficient for large [[Matrices|matrices]].

1. Choose a starting vector $\vecbf{x}_{0}$ (whose largest [[Components|components]] is $1$) and set $k = 0$.
   (typically $\vecbf{x}_{0} = \begin{bmatrix} 1 & 1 & \cdots & 1 \end{bmatrix}^T$)
2. Calculate $\vecbf{y}_{k} = A\vecbf{x}_{k}$.
3. Set $\vecbf{x}_{k+1} = \dfrac{1}{\| \vecbf{y}_{k} \|_{\infty}}\vecbf{y}_{k}$[^3], and increment $k$ be one.
4. Repeat steps 2-4 until the [[Sequences|sequence]] [[Convergence and Divergence of Sequences|converges]].

$\vecbf{x}_{0},\vecbf{x}_{1},\dots$ [[Convergence and Divergence of Sequences|converges]] to the [[Dominant Eigenvectors & Eigenvalues|dominant eigenvector]] and $m_{0}, m_{1},\dots$ [[Convergence and Divergence of Sequences|converges]] to the [[Dominant Eigenvectors & Eigenvalues|dominant eigenvalue]].

> [!proof]- If $A \in \R^{n,n}$ is [[Diagonalisation|diagonalisable]] with a [[Dominant Eigenvectors & Eigenvalues|dominant eigenvalue]] $\lambda_{1}$, there exists a non-zero $\vecbf{x} \in\text{domain}\,A$ such that $\text{lim}_{n\to \infty}A^n\vecbf{x}$ is a [[Dominant Eigenvectors & Eigenvalues|dominant eigenvector]].
> Suppose $A \in \R^{n,n}$[^2] is [[Diagonalisation|diagonalisable]]. Then, there exists [[Eigenvectors & Eigenvalues|eigenvectors]] $\vecbf{v}_{1},\dots,\vecbf{v}_{n}$ of $A$ (with corresponding [[Eigenvectors & Eigenvalues|eigenvalues]] $\lambda_{1},\dots,\lambda_{n}$) such that there exists $\vecbf{x} \in\text{domain}\,A$ such that
> $$ \vecbf{x} = a_{1}\vecbf{v}_{1} + \dots + a_{n}\vecbf{v}_{n} $$
> for some $a_{1},\dots,a_{n} \in \F$ **where $\mathbf{a_{1} \ne 0}$**. This gives
> $$\begin{align}
> 	A^n\vecbf{x} &= A^n(a_{1}\vecbf{v}_{1} + \dots + a_{n}\vecbf{v}_{n}) \\
> 	&= \lambda^n_{1}a_{1}\vecbf{v}_{1} + \lambda_{2}^n a_{2}\vecbf{v}_{2} + \dots + \lambda_{n}^n a_{n}\vecbf{v}_{n}.
> \end{align}$$
> If the [[Eigenvectors & Eigenvalues|eigenvalues]] are ordered such that
> $$\left| \lambda_{1} \right| \ge \left| \lambda_{2} \right| \ge \dots \ge \left| \lambda_{n} \right|, $$
> then
> $$\begin{align}
> 	\lim_{ k \to \infty } A^k\vecbf{x} &= \lim_{ k \to \infty } \left[ \lambda^k_{1}a_{1}\vecbf{v}_{1} + \lambda_{2}^k a_{2}\vecbf{v}_{2} + \dots + \lambda_{n}^k a_{n}\vecbf{v}_{n} \right]  \\
> 	&= \lim_{ k \to \infty } \left[ \lambda^k_{1}\left( a_{1}\vecbf{v}_{1} + \left( \dfrac{\lambda_{2}}{\lambda_{1}} \right)^k a_{2}\vecbf{v}_{2} + \dots + \left( \dfrac{\lambda_{n}}{\lambda_{1}} \right)^k a_{n}\vecbf{v}_{n} \right) \right] \\
> 	&= \lim_{ k \to \infty } \left[ \lambda^k_{1}a_{1}\vecbf{v}_{1} \right] \\
> \end{align}$$
> Thus, $\vecbf{v}_{1}$ and $\lambda_{1}$ are [[Dominant Eigenvectors & Eigenvalues|dominant]]. $\triangle$



[^1]: [[Asymptotic Notation]]
[^2]: [[Sets of Matrices]]
[^3]: [[P-Norms]]
