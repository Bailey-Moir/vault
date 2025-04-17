---
tags:
  - atom
  - math
  - discrete
---
The [[Order in Groups|order]] of a [[Cycle Notation|cycle]] in $S_{n}$[^1] is equal to its length.

> [!theorem]- The [[Order in Groups|order]] of a [[Cycle Notation|product of disjoint cycles]] in $S_{n}$ is the [[GCD with LCM|least common multiple]] of the lengths of the [[Cycle Notation|cycles]].
> Let $\sigma = c_{1}c_{2}\dots c_{n}$, where $c_{1},c_{2},\dots,c_{n}$ are [[Disjoint Sets|disjoint]] [[Cycle Notation|cycles]].
> 
> Suppose $\sigma^k = c_{1}^kc_{2}^k \dots c_{n}^k$. For all $i \in \{ 1,\dots,n \}$, $c_{i}^k = \left( c_{1}^k\dots c_{i-1}^kc_{i+1}^k \dots c_{n}^k \right)^{-1}$ (due to commutativity of [[Cycle Notation|disjoint cycles]]. Since these two [[Cycle Notation|cycles]] are [[Disjoint Sets|disjoint]], this is only the case if $c_{i}^k = e$.
> 
> Thus, $\sigma^k = e$ iff $c_{1}^k = \dots = c_{n}^k = e$.
> 
> For $i \in \{ 1,\dots,n \}$, $c_{i}^k = e$ iff $\left| c_{i} \right| \: |\: k$, i.e., iff $k$ is a [[Divisibility|multiple]] of the length of $c_{i}$.
> 
> Thus, the [[GCD with LCM|least common multiple]] of the lengths gives the smallest positive integer power of $\sigma$ that gives $e$, meaning it is the [[Order in Groups|order]].

[^1]: [[Symmetric Groups]]
