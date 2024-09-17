---
tags:
  - atom
  - math
---
$\mathcal{P}(\F)$ is the set of all polynomials with coefficients in $\F$. 
$$ \mathcal{P}(\F) = \left\{ p : \F \to \F : \left( p(z) = a_0 + a_1 z + \dots + a_mz^m \right) \land z, a_0, \dots, a_m \in \F \right\} $$
$$ \mathcal{P}_m(\F) = \text{span}\left( \lambda z.1, \lambda z.z, \dots, \lambda z.z^m,\right) $$
Thus $\mathcal{P}_m(\F)$ is a [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]] for each $m \in \Z^+$.
# Degree
A polynomial $p \in \mathcal{P}(\F)$ is said to have *degree* $m$ if $m$ is in the same set as above, with the condition that $a_m \ne 0$.
- The polynomial that is identically 0 is said to have degree $-\infty$.
- The degree of a polynomial $p$ is denoted by $\text{deg}\,p$.

For $m \in \Z^+$, $\mathcal{P}_m(\F)$ denotes the set of all polynomials with coefficients in $\F$ and degree at most $m$.
$$ \forall m \in \Z^+, \left( \mathcal{P}_m(\F) = \left\{ p \in \mathcal{P}(\F) : \text{deg}\,p \le m \right\} \right) $$
