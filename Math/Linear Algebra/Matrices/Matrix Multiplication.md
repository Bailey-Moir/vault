---
tags:
  - atom
  - math
  - linear
---
If $A \in \F^{m,n}$ and $B \in \F^{n,p}$, then $AB \in \F^{m,p}$ is defined by
$$\begin{align}
	(AB)_{j,k} &= \sum_{r=1}^n A_{j,r}B_{r,k} \\
	&= A_{j,\cdot} \cdot B_{\cdot,k} && (1)\\
\end{align}$$
> [!example] $4\times 3$ with $3\times 2$ gives $4\times 2$.
> $$\begin{bmatrix} 
> 	\textcolor{lightgray}{A_{1,1}} & \textcolor{darkgray}{A_{1,2}} & \textcolor{gray}{A_{1,3}} \\
> 	A_{2,1} & A_{2,2} & A_{2,3} \\
> 	A_{3,1} & A_{3,2} & A_{3,3} \\
> 	A_{4,1} & A_{4,2} & A_{4,3} \\
> \end{bmatrix}
> 
> \begin{bmatrix} 
> 	\textcolor{lightgray}{B_{1,1}} & B_{1,2} \\
> 	\textcolor{darkgray}{B_{2,1}} & B_{2,2} \\
> 	\textcolor{gray}{B_{3,1}} & B_{3,2} \\
> \end{bmatrix}
> 
> =
> 
> \begin{bmatrix}
> 	\textcolor{Orchid}{C_{1,1}} & C_{1,2} \\
> 	C_{2,1} & C_{2,2} \\
> 	C_{3,1} & C_{3,2} \\
> 	C_{4,1} & C_{4,2} \\
> \end{bmatrix}$$
> $$ \textcolor{Orchid}{C_{1,1}} = \textcolor{lightgray}{A_{1,1}B_{1,1}} + \textcolor{darkgray}{A_{1,2}B_{2,1}} + \textcolor{gray}{A_{1,3}B_{3,1}} $$

> [!proof]- $\forall T \in \mathcal{L}(U,V), S \in \mathcal{L}(V,W), \mathcal{M}(ST) = \mathcal{M}(S) \mathcal{M}(T)$
> *Note [[Finite-Dimensional Vector Spaces|finite-dimensionality]] is assumed*.
> 
> Suppose $\vecbf{u}_{1},\dots,\vecbf{u}_{p}$, $\vecbf{v}_{1},\dots,\vecbf{v}_{n}$, and $\vecbf{w}_{1},\dots,\vecbf{w}_{m}$ are [[Vector Basis|basis']] of $U$, $V$, and $W$ respectively.
> 
> Suppose $\mathcal{M}(S) = A$ and $\mathcal{M}(T) = B$. For $1 \le k \le p$, we have
> $$\begin{align}
> 	(ST)\vecbf{u}_{k} &= S\left( \sum_{r=1}^n B_{r,k} \vecbf{v}_{r} \right) \\
> 	&= \sum_{r=1}^n B_{r,k} S\vecbf{v}_{r} \\
> 	&= \sum_{r=1}^n B_{r,k} \sum_{j=1}^m A_{j,r} \vecbf{w}_{j} \\
> 	&= \sum_{j=1}^m \left( \sum_{r=1}^n A_{j,r} B_{r,k} \right) \vecbf{w}_{j} \\
> \end{align}$$
> Thus, $\mathcal{M}(ST)$ is the $m\times p$ whose entry in row $j$, column $k$, equals
> $$ \sum_{r=1}^n A_{j,r} B_{r,k} $$

> [!note] $A\vecbf{v} = v_{1}A_{\cdot,1} + \dots + v_{n}A_{\cdot,n}$

\[$(1)$ [[Dot Product]], [[Matrices|Matrices]]\]

# Properties of Matrix Multiplication
- **Associative**
	$A(BC) \equiv (AB)C$
	$k(AB) \equiv (kA)B \equiv A(kB)$
- **Distributive**
	$A(B+C) \equiv AB + AC$
- **NOT** Commutative
	$AB \hspace{.1em}\not{\hspace{-.3em}\equiv}\hspace{.3em} BA$