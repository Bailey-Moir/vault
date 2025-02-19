---
tags:
  - atom
  - math
  - linear
---
A *$\mathit{k}$-hyperplane* in $\R^n$ is a [[Subsets|subset]] of the form
$$H = \{ \vecbf{v}_{0} + c_{1}\vecbf{v}_{1} + \dots + c_{k}\vecbf{v}_{k} : c_{1},\dots,c_{k} \in \R \}$$
where $\vecbf{v}_{1},\dots,\vecbf{v}_{k}$ are [[Linear Independence|linearly independent]].

> [!note] An *$\mathit{(n-1)}$-hyperplane* is usually called a *hyperplane* of the [[Vector Spaces|space]].

> [!Theorem] $H$ is a [[Subspaces|subspace]] of $\R^n$ iff $\vecbf{v}_{0}$ is in the [[Span|span]] of $\vecbf{v}_{1},\dots,\vecbf{v}_{k}$

# Hyperplanes and [[Linear Systems|Linear Systems]]
Each [[Linear Systems|system of linear equations]] has a *$\mathit{k}$-hyperplane* as a solution, where $k$ is the number of [[Free Variables|free variables]].
[[Converse, Inverse, and Contrapositive|Conversely]], each *hyperplane* can be given by [[Linear Systems|system of linear equations]].