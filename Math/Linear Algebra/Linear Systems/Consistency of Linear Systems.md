---
tags:
  - atom
  - math
  - linear
---
A [[Linear Systems|linear system]] is said to be *consistent* iff it has at least one solution, and *inconsistent* otherwise.

> [!proof]- A [[Linear Systems|linear system]] $A\vecbf{x} = \vecbf{b}$ is *consistent* iff $\vecbf{b} \in\text{col}\,A$[^1].
> The columns of $A$ give the vectors that each [[Basis|basis vector]] of the [[Domain|domain]] [[Vector Spaces|vector space]] is mapped to, meaning each vector in $\text{range}\,A$ must be a [[Linear Combinations|linear combination]] of these columns, and thus be in the [[Span|span]] of these columns. Finally, a [[Linear Systems|linear system]] is *consistent* iff $\vecbf{b} \in \text{range}\,A$.

[^1]: [[Column Space]]
