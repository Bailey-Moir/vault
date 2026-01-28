---
tags:
  - atom
  - math
  - linear
---
$A \in \R^{n,n}$[^1] is *diagonalisable* iff there exists a [[Diagonal Matrices|diagonal matrix]] $D$ and an [[Matrix Invertibility|invertible matrix]] $P$ such that
$$A = PDP^{-1},$$
or [[Logical Equivalence|equivalently]]
$$D = P^{-1}AP$$

> [!theorem]- $A\in \R^{n,n}$ is *diagonalisable* $A$ has $n$ [[Linear Independence|linearly independent]] [[Eigenvectors & Eigenvalues|eigenvectors]] of $A$.
> Suppose $\vecbf{p}_{1},\vecbf{p}_{2},\dots,\vecbf{p}_{n}$ is a [[Vector Bases|basis]] for $\R^n$ consisting of [[Eigenvectors & Eigenvalues|eigenvectors]] of $A$.
> 
> Set $P = \left[ \vecbf{p}_{1} | \cdots | \vecbf{p}_{n} \right]$. Then
> $$\begin{align}
> 	AP &= \left[ A\vecbf{p}_{1} | \cdots | A\vecbf{p}_{n} \right] \\
> 	&= \left[ \lambda_{1}\vecbf{p}_{1} | \cdots | \lambda_{n}\vecbf{p}_{n} \right] \\
> 	&= PD \\
> \end{align}$$
> where
> $$D = \begin{bmatrix}
> 	\lambda_{1} & \cdots  & 0 \\
> 	\vdots & \ddots  & 0 \\
> 	0 & \cdots  & \lambda_{n} \\
> \end{bmatrix}.$$
> Thus, $A = PDP^{-1}$.

> [!note] Generating $P$ and $D$
> 1. Find all [[Eigenvectors & Eigenvalues|eigenvalues]] of $A$ and a [[Vector Bases|basis]] for each [[Eigenspaces|eigenspace]].
> 2. Let $\vecbf{v}_{1},\dots,\vecbf{v}_{k}$ be the [[Vector Bases|basis]] vectors you found (for all of the [[Eigenspaces|eigenspaces]]).
> 3. If $k < n$, $A$ is not *diagonalisable*
> 4. Otherwise, $A = PDP^{-1}$ with
> $$\begin{align}
> 	P &= \left[ \vecbf{v}_{1} | \cdots | \vecbf{v}_{n} \right] \\
> 	D &= \left[ \lambda_{1}\hat{\vecbf{e}}_{1} | \cdots | \lambda_{n}\hat{\vecbf{e}}_{n} \right] \\
> \end{align}$$
> where $\{ \vecbf{v}_{i}; \lambda_{i} \}$ for all $i$.
# Properties
> [!proof]- $A^n = PD^{301}P^{-1}$
> $$\begin{align}
> 	A^n &= (PDP^{-1})^{301} \\ 
> 	&= (PDP^{-1})(PDP^{-1})\dots(PDP^{-1}) \\
> 	&=PD^{301}P^{-1}
> \end{align}$$

[^1]: [[Sets of Matrices]]
