---
tags:
  - atom
  - math
  - linear
---
$A \in \R^{m,n}$ can be *singular value decomposed* into
$$ A = U\Sigma V^T$$
where
- $U \in \R^{m,m}$ is [[Orthogonal Matrices|orthogonal]], 
- $\Sigma \in \R^{m,n}$ is non-square "[[Diagonal Matrices|diagonal]]", and
- $V \in \R^{n,n}$ is [[Orthogonal Matrices|orthogonal]].

> [!note]
> $$\begin{align}
> 	A &= U \Sigma V^T \\
> 	&= [ \underbrace{\vecbf{u}_{1} \; \cdots \; \vecbf{u}_{r}}_{\text{col}(A)}  \underbrace{\vecbf{u}_{r+1} \; \cdots \; \vecbf{u}_{m}}_{\text{null}(A^T)} ] \Sigma [ \underbrace{\vecbf{v}_{1} \; \cdots \; \vecbf{v}_{r}}_{\text{row}(A)}  \underbrace{\vecbf{v}_{r+1} \; \cdots \; \vecbf{v}_{n}}_{\text{null}(A)} ]^T \\
> \end{align}$$

> [!construction] Given $A \in \R^{m,n}$ where $\text{rank}(A) = r$,
> 1. Find $n$ [[Orthogonal Vectors|orthonormal]] [[Eigenvectors & Eigenvalues|eigenvectors]] $\{ \vecbf{v}_{1},\dots,\vecbf{v}_{n} \}$ of $A^TA$, and order them such that their [[Eigenvectors & Eigenvalues|eigenvalues]] are in decreasing order:
> $$\lambda_{1} \ge \lambda_{2} \ge \dots \ge\lambda _{n} \ge 0$$
> 2. For $i \in \{ 1,\dots,r \}$, let
> $$\vecbf{u}_{i} = \dfrac{1}{\sigma_{i}} A \vecbf{v}_{i}$$
>    where $\sigma_{i}$ is the $i$-th **singular value**, $\sqrt{ \lambda_{i} }$.
> 3. Extend $\{ \vecbf{u}_{1}, \dots,\vecbf{u}_{r} \}$ to an [[Orthogonal Vectors|orthonormal]] [[Basis|basis]] of $\R^m$.
> 4. Set $U = \begin{bmatrix}\vecbf{u}_{1} & \cdots & \vecbf{u}_{m}\end{bmatrix}$,  $V = \begin{bmatrix}\vecbf{v}_{1} & \cdots & \vecbf{v}_{n}\end{bmatrix}$, and $\Sigma$ to an $m\times n$ [[Diagonal Matrices|diagonal matrix]] with entries $\Sigma_{i,i} = \sigma_{i}$, and zeros elsewhere.

> [!example]- Find an *SVD* of $A = \begin{bmatrix}1 & 1 \\ 0 & 1 \\ 1 & 0\end{bmatrix}$.
> The [[Eigenspaces|eigenspaces]] of
> $$A^TA = \begin{bmatrix}
> 	1 & 0 & 1 \\
> 	1 & 1 & 0
> \end{bmatrix}\begin{bmatrix}
> 	1 & 1 \\
> 	0 & 1 \\
> 	1 & 0
> \end{bmatrix} = \begin{bmatrix}
> 	2 & 1 \\
> 	1 & 2 \\
> \end{bmatrix}$$
> are $E_{3}(A^TA) =\text{span}\{ \vecbf{v}_{1} \}$ and $E_{1}(A^TA) =\text{span}\{ \vecbf{v}_{2} \}$, where
> $$\begin{array}{cc}
> 	\vecbf{v}_{1} = \begin{bmatrix}
> 		\dfrac{1}{\sqrt{ 2 }} \\ \dfrac{1}{\sqrt{ 2 }}
> 	\end{bmatrix} &
> 	\vecbf{v}_{2} = \begin{bmatrix}
> 		\dfrac{1}{\sqrt{ 2 }} \\ -\dfrac{1}{\sqrt{ 2 }}
> 	\end{bmatrix}
> \end{array}.$$
> This gives the columns of $V = \begin{bmatrix}\vecbf{v}_{1},\vecbf{v}_{2}\end{bmatrix}$ (note $\vecbf{v}_{1}$ and $\vecbf{v}_{2}$ are normalised).
> 
> Since the **singular values** of $A$ are $\sigma_{1} = \sqrt{ 3 }$ and $\sigma_{2} = 1$, we also get
> $$\Sigma = \begin{bmatrix}
> 	\sqrt{ 3 } & 0 \\
> 	0 & 1 \\
> 	0 & 0 \\
> \end{bmatrix}.$$
> To find the components of $U$, first compute
> $$\begin{align}
> 	\vecbf{u}_{1} &= \dfrac{1}{\sigma_{1}}A\vecbf{v}_{1} \\
> 	&= \dfrac{1}{\sqrt{ 3 }}\begin{bmatrix}
> 		1 & 1 \\
> 		0 & 1 \\
> 		1 & 0
> 	\end{bmatrix} \begin{bmatrix}
> 		\dfrac{1}{\sqrt{ 2 }} \\
> 		\dfrac{1}{\sqrt{ 2 }}
> 	\end{bmatrix} \\
> 	&= \dfrac{1}{\sqrt{ 6 }}\begin{bmatrix}
> 	2 \\ 1 \\ 1
> \end{bmatrix} \\
> \end{align}$$
> $$\vdots$$
> $$\begin{array}{ccc}
> 	U = \begin{bmatrix}
> 		 \frac{2}{\sqrt{ 6 }} & 0 & -\frac{1}{\sqrt{ 3 }} \\
> 		 \frac{1}{\sqrt{ 6 }} & -\frac{1}{\sqrt{ 2 }} & \frac{1}{\sqrt{ 3 }} \\
> 		 \frac{1}{\sqrt{ 6 }} & \frac{1}{\sqrt{ 2 }} & \frac{1}{\sqrt{ 3 }} \\
> 	\end{bmatrix}
> 	&
> 	\Sigma = \begin{bmatrix}
> 		\sqrt{ 3 } & 0 \\
> 		0 & 1 \\
> 		0 & 0
> 	\end{bmatrix}
> 	&
> 	V = \begin{bmatrix}
> 		\frac{1}{\sqrt{ 2 }} & \frac{1}{\sqrt{ 2 }} \\
> 		\frac{1}{\sqrt{ 2 }} & -\frac{1}{\sqrt{ 2 }}
> 	\end{bmatrix}
> 
> \end{array}$$

> [!theorem]- The [[Images of Linear Maps|image]] of the [[Unit Vectors|unit]] sphere in $\R^n$ under $A$ is an [[Ellipsoid|elipsoid]] in $\R^m$ with principal axes $$\sigma_{1}\vecbf{u}_{1}, \sigma_{2}\vecbf{u}_{2},\dots,\sigma_{r}\vecbf{u}_{r},$$ and the interior [[ellipsoid|ellipsoid]] is contained in the image iff $r < n$.
> i.e.
> $$\begin{array}{cccc}
> 	A\vecbf{v}_{1} = \sigma_{1}\vecbf{u}_{1} & A\vecbf{v}_{2} = \sigma_{2}\vecbf{u}_{2} & \cdots & A\vecbf{v}_{r} = \sigma_{r}\vecbf{u}_{r}
> \end{array}$$
> The second part of this theorem is true because $\Sigma$ flattens one of the dimensions.
