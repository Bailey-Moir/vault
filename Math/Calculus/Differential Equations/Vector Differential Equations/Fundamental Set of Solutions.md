---
tags:
  - atom
  - math
---
A [[Sets|set]] of solutions of a given [[Linear Homogeneous Differential Equations|linear homogeneous DE]] $\{ \vecbf{x}_{1},\dots,\vecbf{x}_{n} \}$ is a *fundamental set of solutions* (*FSS*) iff every solution of can be written as
$$\vecbf{x}(t) = c_{1}\vecbf{x}_{1}(t) + \dots + c_{n}\vecbf{x}_{n}(t)$$
for a unique choice of $c_{1},\dots,c_{n}$.
*iff $\it{S}$* *is a [[Basis|basis]] of the solution space of [[Functions|functions]]*.

> [!theorem]- **(1)** $\{ \vecbf{x}_{1}(t),\dots,\vecbf{x}_{n}(t) \}$ is a *FSS* iff $\{ \vecbf{x}_{1}(t_{0}),\dots,\vecbf{x}_{n}(t_{0}) \}$ is a [[Basis|basis]] for $\R^m$ for some $t_{0}$.
> $\left( \implies \right)$
> Suppose $S$ is a *FSS*.
> 
> Let $c_{1},\dots,c_{n}$ be the unique choice of constants that solve some [[Initial Value Problem|IVP]] with $\vecbf{x}(t_{0}) = \vecbf{x}_{0}$. Then
> $$\vecbf{x}(t_{0})= c_{1}\vecbf{x}_{1}(t_{0})+\dots+c_{n}\vecbf{x}_{n}(t_{0}) = \vecbf{x}_{0}.$$
> Since every $\vecbf{x}_{0} \in \R^m$ can be written as a **unique** [[Linear Combinations|linear combination]] of $\{ \vecbf{x}_{1}(t_{0}),\dots,\vecbf{x}_{n}(t_{0}) \}$, it must then be a [[Basis|basis]] of $\R^m$.
> 
> $\left( \impliedby \right)$
> Let $\vecbf{x}_{1}(t),\dots,\vecbf{x}_{n}(t)$ solve $\vecbf{x}' = A(t)\vecbf{x}$, and suppose that $\{ \vecbf{x}_{1}(t_{0}),\dots,\vecbf{x}_{n}(t_{0}) \}$ is a [[Basis|basis]] of $\R^m$.
> 
> Then there is a unique $c_{1},\dots,c_{n}$such that $\vecbf{x}_{0} = c_{1}\vecbf{x}_{1}(t_{0}) + \dots + c_{n}\vecbf{x}_{n}(t_{t_{0}})$.
> 
> Further, $\vecbf{x}(t)=c_{1}\vecbf{x}_{1}(t) + \dots + c_{n}\vecbf{x}_{n}(t)$ solves the [[Initial Value Problem|IVP]] since
> $$\begin{align}
> 	\vecbf{x}'(t) &= \left( c_{1}\vecbf{x}_{1}(t) + \dots + c_{n}\vecbf{x}_{n}(t) \right)' \\
> 	&= c_{1}\vecbf{x}_{1}'(t) + \dots + c_{n}\vecbf{x}_{n}'(t) \\
> 	&= c_{1}A(t)\vecbf{x}_{1}(t) + \dots + c_{n}A(t)\vecbf{x}_{n}(t) \\
> 	&= A(t)\left( c_{1}\vecbf{x}_{1}(t) + \dots + c_{n}\vecbf{x}_{n}(t) \right) \\
> 	&= A(t)\vecbf{x}(t) \\
> \end{align}$$

> [!theorem]- **(2)** There exists a *FSS*.
> Let $\{ \vecbf{v}_{1},\dots,\vecbf{v}_{m} \}$ be a [[Basis|basis]] for $\R^m$ and choose $\vecbf{x}_{k}(t)$ solve $\vecbf{x}'(t) = A(t)\vecbf{x}(t)$, where
> $$\vecbf{x}_{k}(0) = \vecbf{v}_{k}$$
> Why can you necessarily do this?

> [!theorem]- **(3)** $n = m$
> Let $c_{1},\dots,c_{n}$ be the unique choice of constants that solve some [[Linear Homogeneous Differential Equations|linear homogeneous]] [[Initial Value Problem|IVP]] with $\vecbf{x}(t_{0}) = \vecbf{x}_{0}$. Then
> $$\vecbf{x}(t_{0})= c_{1}\vecbf{x}_{1}(t_{0})+\dots+c_{n}\vecbf{x}_{n}(t_{0}) = \vecbf{x}_{0}.$$
> Since every $\vecbf{x}_{0} \in \R^m$ can be written as a **unique** [[Linear Combinations|linear combination]] of $\{ \vecbf{x}_{1}(t_{0}),\dots,\vecbf{x}_{n}(t_{0}) \}$, it must then be a [[Basis|basis]] of $\R^m$, meaning it is of length $m$. Thus, $n = m$.