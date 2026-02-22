---
tags:
  - atom
  - math
---
The *supremum* of a [[Subsets|subset]] $S$ of a [[Partial Order|poset]], denoted $\sup S$, is its smallest [[Bounded Sets|upper bound]].

The *infimum* of a [[Subsets|subset]] $S$ of a [[Partial Order|poset]], denoted $\inf S$, is its largest [[Bounded Sets|lower bound]].

> [!theorem]- The *supremum* and *infimum* are unique. 
> If both $L$ and $K$ are *supremums* of $S$, then $L \le K$ and $K \le L$ (by the minimality of *supremums*), meaning $L = K$ (by the [[Antisymmetric Property|antisymmetric property]] of [[Partial Order|partial order]]).
> This same argument can be made for *infimums* using their maximality.

> [!theorem] $\inf S = -\sup(-S)$

> [!theorem]- $\forall s < \sup S, \exists x \in S: s < x \le \sup S$
> Suppose $\exists s < \sup S : \forall x \in S, x \le s$ (part of the [[Negation|negation]]).
> Then $s$ is an [[Bounded Sets|upper bound]] on $S$ smaller than $\sup S$, a [[Contradictions|contradiction]].
 ^inbetween

\[[[Completeness]]\]