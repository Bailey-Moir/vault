---
tags:
  - atom
  - math
  - discrete
---
For a [[Graphs|graph]] $G$, and $\lambda \in \Z^+$, we denote the number of **distinct** ways of [[Graph Colouring|colouring]] $G$ using $\lambda$ colours by $P(G,\lambda)$.

> [!note] What makes a colouring **distinct**?
> Two colourings of a [[Graphs|graph]] are distinct iff they have at least one (fixed) [[Vertices|vertex]] assigned different colours.
> ![200|center](chromatic-polynomials-distinctness.excalidraw)
> (it is not about being distinct up to [[Graph Isomorphism|isomorphism]])

> [!theorem] $\chi(G)$ is the smallest $\lambda$ such that $P(G,\lambda) \ne 0$.
# Base Cases
- **[[Complete Graphs]]**
  $P(K_{n}, \lambda) = \dfrac{\lambda!}{\left( \lambda - n \right)!} = P(\lambda,n) = \lambda(\lambda-1)\cdots\left( \lambda-(n-1) \right)$[^1]
- **[[Graphs|Graph]] of $\mathbf{n}$ Isolated [[Vertices|Vertices]]**
  $P(G,\lambda) = \lambda^n$
- **[[Trees]] on $\mathbf{n}$ [[Vertices|Vertices]]**
  $P(G, \lambda) = \lambda(\lambda-1)^{n-1}$
- **[[Walks|Cycle]] of $\mathbf{n}$ [[Vertices|Vertices]]**
  $P(C_{n},\lambda) = (\lambda - 1)^n + (-1)^n(\lambda-1)$
- **[[Components of Graphs|Components]] $\bf{G_{1},\dots,G_{k}}$**
  $\displaystyle P(G, \lambda) = \prod_{i=1}^kP(G_{i},\lambda) = P(G_{1},\lambda)\cdots P(G_{k},\lambda)$

[^1]: [[Counting Outcomes]]
