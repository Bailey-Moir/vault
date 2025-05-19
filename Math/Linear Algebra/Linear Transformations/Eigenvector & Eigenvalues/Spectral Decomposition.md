---
tags:
  - atom
  - math
  - linear
---
$$\begin{align}
	A &= QDQ^T \\
	&= \begin{bmatrix}
		\vecbf{q}_{1} & \cdots & \vecbf{q}_{n}
	\end{bmatrix} \begin{bmatrix}
		\lambda_{1} & \cdots & 0 \\
		\vdots & \ddots & \vdots \\
		0 & \cdots & \lambda_{n} \\
	\end{bmatrix} \begin{bmatrix}
		\vecbf{q}_{1}^T \\
		\vdots \\
		\vecbf{q}_{n}^T \\
	\end{bmatrix} \\
	&= \begin{bmatrix}
		\lambda_{1}\vecbf{q}_{1} & \cdots & \lambda _{n}\vecbf{q}_{n}
	\end{bmatrix} \begin{bmatrix}
		\vecbf{q}_{1}^T \\
		\vdots \\
		\vecbf{q}_{n}^T \\
	\end{bmatrix} \\
	&= \lambda_{1}\vecbf{q}_{1}\vecbf{q}_{1}^T + \cdots + \lambda _{n}\vecbf{q}_{n}\vecbf{q}_{n}^T \\
	&= \lambda_{1}\,\text{proj}_{\vecbf{q}_{1}} + \cdots + \lambda _{n}\,\text{proj}_{\vecbf{q}_{n}} && \text{Lemma 1} \\
	&= \sum \lambda\,\text{proj}_{E_{\lambda}(A)} \\
\end{align}$$

> [!lemma] **(1)** $\forall \vecbf{q},\vecbf{v} \in \R^n, \left( \| \vecbf{q} \| = 1 \to \text{proj}_{\vecbf{q}} = \vecbf{q}\vecbf{q}^T \right)$

> [!example]- $A = \begin{bmatrix}1&2\\2&-2\end{bmatrix}$, with [[Eigenvector & Eigenvalues|eigenvectors]] $\vecbf{q}_{1} = \begin{bmatrix} \frac{1}{\sqrt{ 5 }}\\-\frac{2}{\sqrt{ 5 }} \end{bmatrix}$, and $\vecbf{q}_{2} = \begin{bmatrix} \frac{2}{\sqrt{ 5 }} \\ \frac{1}{\sqrt{ 5 }} \end{bmatrix}$.
> The *spectral decomposition* of $A$ is
> $$\begin{align}
> 	A &= \lambda_{1}\vecbf{q}_{1}\vecbf{q}_{1}^T + \lambda \vecbf{q}_{2}\vecbf{q}_{2}^T \\
> 	&= -3 \begin{bmatrix}
> 		\dfrac{1}{\sqrt{ 5 }} \\
> 		-\dfrac{2}{\sqrt{ 5 }}
> 	\end{bmatrix}\begin{bmatrix}
> 		\dfrac{1}{\sqrt{5}} & -\dfrac{2}{\sqrt{ 5 }}
> 	\end{bmatrix}
> 	+
> 	2\begin{bmatrix}
> 		\dfrac{2}{\sqrt{ 5 }} \\
> 		\dfrac{1}{\sqrt{ 5 }}
> 	\end{bmatrix}\begin{bmatrix}
> 		\dfrac{2}{\sqrt{5}} & \dfrac{1}{\sqrt{ 5 }}
> 	\end{bmatrix}\\
> 	&= -3 \begin{bmatrix}
> 		\dfrac{1}{\sqrt{ 5 }} & -\dfrac{2}{\sqrt{ 5 }} \\
> 		-\dfrac{2}{\sqrt{ 5 }} & \dfrac{4}{\sqrt{ 5 }} \\
> 	\end{bmatrix}
> 	+ 2 \begin{bmatrix}
> 		\dfrac{4}{\sqrt{ 5 }} & \dfrac{2}{\sqrt{ 5 }} \\
> 		\dfrac{2}{\sqrt{ 5 }} & \dfrac{1}{\sqrt{ 5 }} \\
> 	\end{bmatrix} \\
> 	&= -3\,\text{proj}_{\vecbf{q}_{1}} + 2\,\text{proj}_{\vecbf{q}_{2}}
> \end{align}$$

\[[[Orthogonal Decomposition]], [[Vector Projection]]\]