---
tags:
  - atom
  - math
  - linear
---
A [[Subsets|subset]] $U$ of a [[Vector Spaces|vector space]] $V$ is called a *subspace* of $V$ iff $U$ is also a [[Vector Spaces|vector space]] with the same additive identity, addition, and scalar multiplication as on $𝑉$.
- **Identity**
  $\vecbf{0} \in U$
- **Closed Under Addition**
  $\forall \vecbf{u}, \vecbf{v} \in U, \left( \vecbf{u} + \vecbf{v} \in U \right)$
- **Closed Under Scalar Multiplication**
  $\forall \vecbf{u} \in U, \lambda \in \F, \left( \lambda \vecbf{u} \in U \right)$

 > [!note]- This is equivalent to saying a [[Subsets|subset]] $U$ of a [[Vector Spaces|vector space]] is a *subspace* iff $U =\text{span}\,U$.

> [!note]- If $U$ is not [[Empty Set|empty]], **closure under scalar multiplication** implies $\vecbf{0} \in U$.

> [!note] that for the *subspace* to be closed under scalar multiplication, the scalar [[Fields|field]] $\F$ is inherited from the parent [[Vector Spaces|vector space]].

- Every [[Vector Spaces|vector space]] $V$ has the *subspaces* $\{0\}$ and $V$ (which may be the same).