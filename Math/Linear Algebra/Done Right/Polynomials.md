---
tags:
  - atom
  - math
---
$\mathcal{P}(\mathbb{F})$ is the set of all polynomials with coefficients in $\mathbb{F}$. 
$$ \mathcal{P}(\mathbb{F}) = \left\{ p : \mathbb{F} \to \mathbb{F} : \left( p(z) = a_0 + a_1 z + \cdots + a_mz^m \right) \land z, a_0, \dots, a_m \in \mathbb{F} \right\} $$
$$ \mathcal{P}_m(\mathbb{F}) = \text{span}\left( \lambda z.1, \lambda z.z, \dots, \lambda z.z^m,\right) $$
Thus $\mathcal{P}_m(\mathbb{F})$ is a [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]] for each $m \in \mathbb{Z}^+$.
# Degree
A polynomial $p \in \mathcal{P}(\mathbb{F})$ is said to have *degree* $m$ if $m$ is in the same set as above, with the condition that $a_m \ne 0$.
- The polynomial that is identically 0 is said to have degree $-\infty$.
- The degree of a polynomial $p$ is denoted by $\text{deg}\,p$.

For $m \in \mathbb{Z}^+$, $\mathcal{P}_m(\mathbb{F})$ denotes the set of all polynomials with coefficients in $\mathbb{F}$ and degree at most $m$.
$$ \forall m \in \mathbb{Z}^+, \left( \mathcal{P}_m(\mathbb{F}) = \left\{ p \in \mathcal{P}(\mathbb{F}) : \text{deg}\,p \le m \right\} \right) $$
