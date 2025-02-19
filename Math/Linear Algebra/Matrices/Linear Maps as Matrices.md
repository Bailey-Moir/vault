---
tags:
  - atom
  - math
  - linear
---
Suppose $T = \mathcal{L}(V,W)$[^1], $\vecbf{v}_{1},\dots,\vecbf{v}_{n}$ is a [[Basis|basis]] of $V$, and $\vecbf{w}_{1},\dots,\vecbf{w}_{m}$ is a [[Basis|basis]] of $W$. The [[Matrices|matrix]] of $T$ with respect to these [[Basis|bases]] is the $m$-by-$n$ [[Matrices|matrix]] $\mathcal{M}(T)$ whose entries $A_{j,k}$ are defined by
$$T \vecbf{v}_{k} = A_{1,k}\vecbf{w}_{1} + \dots + A_{m,k}\vecbf{w}_{m}$$
$$\begin{align}
	&\color{gray}\hspace{1.2em}\begin{matrix}
		\vecbf{v}_{1}\hspace{0.5em} & \dots & \hspace{0.5em}\vecbf{v}_{n} \\
	\end{matrix} \\
	\color{gray}\hspace{1em}\begin{matrix}
		\vecbf{w}_{1} \\ \vdots \\ \vecbf{w}_{m} \\
	\end{matrix} &
	\begin{bmatrix}
		A_{1,1} & \dots & A_{1,n} \\
		\vdots & \ddots & \vdots \\
		A_{m,1} & \dots & A_{m,n} \\
	\end{bmatrix}
\end{align}$$
- If the [[Basis|bases]] are not clear from the context, then the notation $\mathcal{M}(T,(\vecbf{v}_{1},\dots,\vecbf{v}_{n}), (\vecbf{w}_{1},\dots,\vecbf{w}_{m}))$ is used.

> [!example]-
> Suppose $T \in \mathcal{L}(\F^2,\F^3)$ is defined by
> $$ T\langle x,y \rangle = \left< x + 3y, 2x + 5y, 7x + 9y \right>. $$
> Then
> $$ \mathcal{M}(T) = \begin{bmatrix}
> 	1 & 3 \\
> 	2 & 5 \\
> 	7 & 9
> \end{bmatrix}. $$

> [!proof]- All [[Finite-Dimensional Vector Spaces|finite-dimensional]] [[Linear Maps|linear maps]] can be represented as a [[Matrices|matrix]] (and vice versa).
> Let $\vecbf{v}_{1}, \dots, \vecbf{v}_{n}$ be a [[Basis|basis]] of $V$. By the [[Linear Map Lemma|linear map lemma]], $T \in \mathcal{L}(V,W)$ can be uniquely defined by specifying vectors in $W$ that these [[Basis|basis]] vectors are mapped to. Thus, for each $k \in \{ 1,\dots,n \}$, a $\vecbf{w} \in W$ must be chosen such that
> $$ T\,\vecbf{v}_{k} = \vecbf{w}. $$
> If $\vecbf{w}_{1},\dots,\vecbf{w}_{m}$ is a [[Basis|basis]] of $W$, then this can be rewritten as
> $$ T\,\vecbf{v}_{k} = a_{1}\vecbf{w}_{1} + \dots + a_{m}\vecbf{w}_{m}, $$
> where $a_{1},\dots,a_{n} \in \F$.
> 
> Thus, if $\vecbf{v}_{1},\dots,\vecbf{v}_{n}$ and $\vecbf{w}_{1},\dots,\vecbf{w}_{m}$ are [[Basis|basis]]' of $V$ and $W$ respectively, $T \in \mathcal{L}(V,W)$ can be uniquely defined by
> $$\begin{array}{ccccccc}
> 	T\,\vecbf{v}_{1} &= &A_{1,1}\vecbf{w}_{1} &+ &\dots &+ &A_{m,1}\vecbf{w}_{m} \\
> 	\vdots &= &\vdots &+ &\ddots &+ &\vdots \\
> 	T\,\vecbf{v}_{n} &= &A_{1,n}\vecbf{w}_{1} &+ &\dots &+ &A_{m,n}\vecbf{w}_{m} \\
> \end{array}$$
> where $A_{j,k} \in \F$. Extracting these coefficients, flipping across the diagonal, and adding the brackets gives the [[Matrices|matrix]] form of the [[Linear Maps|linear map]].
> $$\begin{align}
> 	&\color{gray}\hspace{1.2em}\begin{matrix}
> 		\vecbf{v}_{1}\hspace{0.5em} & \dots & \hspace{0.5em}\vecbf{v}_{n} \\
> 	\end{matrix} \\
> 	\color{gray}\hspace{1em}\begin{matrix}
> 		\vecbf{w}_{1} \\ \vdots \\ \vecbf{w}_{m} \\
> 	\end{matrix} &
> 	\begin{bmatrix}
> 		A_{1,1} & \dots & A_{1,n} \\
> 		\vdots & \ddots & \vdots \\
> 		A_{m,1} & \dots & A_{m,n} \\
> 	\end{bmatrix}
> \end{align}$$

# Intuition for Rows and Columns

- **Columns**
  $$\mathcal{M}(T)_{\cdot,k} = \mathcal{M}(T\,\vecbf{v}_{k})$$
  $T\,\vecbf{v}_{k}$ is given by $k$-th column (using the basis of $W$).
 $$ T\vecbf{v}_{k} = \begin{bmatrix}
	A_{1,1} \\
	\vdots \\
	A_{m,1} \\
\end{bmatrix} $$ 
- **Rows**
  The coefficient of $\vecbf{w}_{k}$ in $T\, \vecbf{v}$ is given by the [[Dot Product|dot product]] of $\vecbf{v}$ and the $k$-th row.
$$ T\begin{bmatrix}
	v_{1} \\
	\vdots \\
	v_{n} \\
\end{bmatrix} = \begin{bmatrix}
	A_{1,1}v_{1} + \dots + A_{1,n}v_{n} \\
	\vdots \\
	A_{m,1}v_{1} + \dots + A_{m,n}v_{n} \\
\end{bmatrix} $$

[^1]: [[Linear Maps]]
