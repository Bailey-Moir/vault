---
tags:
  - atom
  - math
  - linear
---
Suppose $A \in \R^{n,n}$[^2] is a [[Zero Matrices|non-zero]] [[Diagonalisation|diagonalisable]] [[Matrices|matrix]]. Then, there exists [[Eigenvectors & Eigenvalues|eigenvectors]] $\vecbf{v}_{1},\dots,\vecbf{v}_{n}$ of $A$ (with corresponding [[Eigenvectors & Eigenvalues|eigenvalues]] $\lambda_{1},\dots,\lambda_{n}$) such that there exists $\vecbf{x} \in\text{domain}\,A$ such that (#TODO should this be a for all?)
$$ \vecbf{x} = a_{1}\vecbf{v}_{1} + \dots + a_{n}\vecbf{v}_{n} $$
for some $a_{1},\dots,a_{n} \in \F$. This gives
$$\begin{align}
	A^n\vecbf{x} &= A^n(a_{1}\vecbf{v}_{1} + \dots + a_{n}\vecbf{v}_{n}) \\
	&= \lambda^n_{1}a_{1}\vecbf{v}_{1} + \lambda_{2}^n a_{2}\vecbf{v}_{2} + \dots + \lambda_{n}^n a_{n}\vecbf{v}_{n}.
\end{align}$$
If the [[Eigenvectors & Eigenvalues|eigenvalues]] are ordered such that
$$\left| \lambda_{1} \right| \ge \left| \lambda_{2} \right| \ge \dots \ge \left| \lambda_{n} \right|, $$
then
$$\begin{align}
	\lim_{ k \to \infty } A^k\vecbf{x} &= \lim_{ k \to \infty } \left[ \lambda^k_{1}a_{1}\vecbf{v}_{1} + \lambda_{2}^k a_{2}\vecbf{v}_{2} + \dots + \lambda_{n}^k a_{n}\vecbf{v}_{n} \right]  \\
	&= \lim_{ k \to \infty } \left[ \lambda^k_{1}\left( a_{1}\vecbf{v}_{1} + \left( \dfrac{\lambda_{2}}{\lambda_{1}} \right)^k a_{2}\vecbf{v}_{2} + \dots + \left( \dfrac{\lambda_{n}}{\lambda_{1}} \right)^k a_{n}\vecbf{v}_{n} \right) \right] \\
	&= \lim_{ k \to \infty } \left[ \lambda^k_{1}a_{1}\vecbf{v}_{1} \right] \\
\end{align}$$
Thus, $\vecbf{v}_{1}$ and $\lambda_{1}$ are called *dominant [[Eigenvectors & Eigenvalues|eigenvectors]]* and *dominant [[Eigenvectors & Eigenvalues|dominant eigenvalues]]* respectively. $\triangle$



[^1]: [[Asymptotic Notation]]

[^2]: [[Sets of Matrices]]
