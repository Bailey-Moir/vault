---
tags:
  - atom
  - math
---
A *fundamental matrix* of [[Linear Homogeneous Differential Equations|linear homogeneous DE]] is a [[Matrices|matrix]] 
$$\Phi(t)  =\left[ \vecbf{x}_{1}(t)\;|\; \cdots \;|\; \vecbf{x}_{m}(t) \right] $$
such that $\{ \vecbf{x}_{1},\dots,\vecbf{x}_{m} \}$  is a [[Fundamental Set of Solutions|FSS]].

> [!definition] $W(t) = \left| \Phi(t) \right|$[^1]

> [!note] $\Phi(t)\vecbf{c} = c_{1}\vecbf{x}_{1}(t) + \dots + c_{m}\vecbf{x}_{m}(t)$

> [!theorem]- A [[Matrices|matrix]] $\Phi(t)$ whose columns solve $\vecbf{x}' = A(t)\vecbf{x}$ is a *fundamental matrix* iff $\Phi (t)$ is [[Matrix Invertibility|invertible]] for all $t$ ($\forall t, W(t) \ne 0$ ).
> 
> $\Phi(t)$ is a *fundamental matrix* iff the columns of $\Phi(t)$ are a [[Fundamental Set of Solutions|FSS]], which is true iff the columns of $\Phi(0)$ form a [[Basis|basis]] for $\R^m$, meaning $\Phi(0)$ is [[Matrix Invertibility|invertible]].
> 
> $\left( \impliedby \right)$
> If $\Phi(t)$ is [[Matrix Invertibility|invertible]] for all $t$, then clearly $\Phi(0)$ is [[Invertibility|invertible]].
> 
> $\left( \implies \right)$
> Suppose $\Phi(0)$ is [[Matrix Invertibility|invertible]], and let $T\in R$ and $\vecbf{c}\in\R^m$ be such that $\Phi(T)\vecbf{c}=0$.
> 
> Set $\vecbf{x}(t) = \Phi(t)\vecbf{c}$, meaning $\vecbf{x}(t)$ is a solution to the [[Differential Equations|DE]].
> 
> Because solutions are unique (by the definition of the [[Fundamental Set of Solutions|FSS]]),
> #TODO ????
> 
> $\left( \implies \right)$
> Suppose $\Phi(t)$ is a *fundamental matrix* of $\vecbf{x}'=A(t)\vecbf{x}$.
> 
> The columns of $\Phi(t)$ form a [[Basis|basis]] of the solution [[Vector Spaces|space]], meaning $\Phi(t)$ is [[Injective Functions|injective]].
> 
> Since $\Phi(t)$ is square[^3] and [[Injective Functions|injective]], it must be [[Bijective Functions|bijective]] ([[Matrix Invertibility|invertible]])[^2]. #TODO this line is incorrect
> 
> $\left( \impliedby \right)$
> Suppose $\Phi(t)$ is [[Matrix Invertibility|invertible]], and its columns solve $\vecbf{x}' = A(t)\vecbf{x}$.
> 
> Since $\Phi(t)$ is [[Matrix Invertibility|invertible]], it is [[Injective Functions|injective]], meaning its columns are [[Linear Independence|linearly independent]].
> 
> Since $\Phi(t)$ is [[Matrix Invertibility|invertible]], it is square, so since each column of $\Phi(t)$ is of length $m$, there must be $m$ ([[Linear Independence|linearly independent]]) columns.
> 
> The [[Dimension|dimension]] of the solution [[Vector Spaces|space]] is $m$[^3], so since the columns of $\Phi(t)$ are a [[Linear Independence|linearly independent]] [[Sets|set]] of [[Vectors|vectors]] in the solution [[Vector Spaces|space]] of length $m$, they must be a [[Basis|basis]] of it[^4].
> 
> Thus, the columns form a [[Fundamental Set of Solutions|FSS]] for $\vecbf{x}' = A(t)\vecbf{x}$, meaning $\Phi(t)$ is a *fundamental matrix* .

> [!theorem]- $\Phi(t) = \Phi(0)\text{diag}(e^{\lambda_{k}t})$.
> $$\begin{align}
> 	\Phi(t) &= \left[ e^{\lambda_{1}}\vecbf{v}_{1} \;|\; \cdots \;|\; e^{\lambda_{m}}\vecbf{v}_{m} \right] \\
> 	&= \left[ \vecbf{v}_{1}\;|\;\cdots\;|\;\vecbf{v}_{m} \right] \begin{bmatrix}
> 		e^{\lambda_{1}} & \cdots & 0 \\
> 		\vdots & \ddots & \vdots \\
> 		0 & \cdots & e^{\lambda_{m}}
> 	\end{bmatrix} \\
> 	&= \Phi(0)\text{diag}(e^{\lambda_{k}t})
> \end{align}$$

[^1]: [[Wronskian Determinant]]
[^2]: [[Function Types with Dimension]], Theorem 3
[^3]: [[Fundamental Set of Solutions]], Theorem 3
[^4]: [[Linear Independence and Span with Dimension]]
