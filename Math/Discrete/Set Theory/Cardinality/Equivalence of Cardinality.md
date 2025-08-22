---
tags:
  - atom
  - math
  - discrete
---
For any [[Sets|sets]] $A$ and $B$, $|A| = |B|$ iff there is a [[Bijective Functions|bijection]] from $A$ to $B$. 

>[!note] $|A| = |B|$ is an [[Equivalence Relations|equivalence relation]].

> [!example]- $2\Z = \Z$
> Let $2\Z = \{z \in \Z : 2|z\}$. Note that $f : \Z \to 2\Z$ defined by $f(n) = 2n$ is a [[Functions|function]].
> - For all $b \in 2\Z$,  there exists $a \in \Z$ such that $f(a) = 2a = b$. Thus $f$ is [[Surjective Functions|surjective]].
> - Suppose $f(n_1) = f(n_2)$. Then $2n_1 = 2n_2$, meaning $n_1 = n_2$. Thus $f$ is [[Injective Functions|injective]].
> 
> Thus there is a [[Bijective Functions|bijection]] from $\Z$ to $2\Z$ ($f$), meaning $|\Z| = |2\Z|$.
