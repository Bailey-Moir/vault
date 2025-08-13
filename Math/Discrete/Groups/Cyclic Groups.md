---
tags:
  - atom
  - math
  - discrete
---
A [[Groups|group]] $G$ is *cyclic* iff there is an element $a \in G$ such that $G = \left< a \right>$[^1].

> [!theorem]- All *cyclic groups* are [[Groups|abelian]].
> Let $x,y \in G$ for some *cyclic group* $G$.
> 
> $x = g^a$ and $y = g^b$ for some $a,b \in \Z_{\left| G \right|}$ (and [[Group Generators|generator]] $g$).
> 
> Thus,
> $$xy = g^ag^b = g^{a+b} = g^{b+a} = g^{b}g^{a} = yx,$$
> meaning $G$ must be commutative (and thus [[Groups|abelian]]).

\[[[Lagrange's Theorem]] Corollary\]

[^1]: [[Generated Subgroups]]
