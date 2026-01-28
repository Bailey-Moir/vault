---
tags:
  - atom
  - math
---
An object $c$ in a [[Categories|category]] $C$ is  ^ae602c
- *initial* iff $\forall x \in C: \left|C(c,x)\right| = 1$, and
- *terminal* iff $\forall x \in C: \left|C(x,c)\right| = 1$.

> [!note] *These* two definitions are [[Duality|dual]].

> [!example]- $\mathbf{Set}$[^1] and $\mathbf{Top}$[^2] 
> In $\mathbf{Set}$[^1] and $\mathbf{Top}$[^2], the [[Empty Set|empty set]] $\emptyset$ is the *initial*, since for each object $X$, the empty [[Functions|function]] is the unique morphism from $\emptyset$ to $X$, and the *terminals* are the singletons (one-point [[Sets|sets]]), since for each object $X$, the constant [[Functions|function]] is the unique morphism from $X$ to any given singleton.

> [!theorem]- In any [[Categories|category]], any two *initials* are [[Isomorphism|isomorphic]], and any two *terminals* are [[Isomorphism|isomorphic]].
> Let $c$ and $c'$ be both *initials* or *terminals* in a [[Categories|category]] $C$.
> Let $\alpha : c \to c'$ and $\alpha' : c' \to c$ be the unique morphisms between them.
> - $\alpha\alpha' : c \to c$ must be unique, but by the [[Categories|category]] axioms, there must be a $1_{c} : c \to c$, meaning $\alpha\alpha' = 1_{c}$. Similarly,
> - $\alpha'\alpha : c' \to c'$ must be unique, but by the [[Categories|category]] axioms, there must be a $1_{c'} : c' \to c'$, meaning $\alpha'\alpha = 1_{c'}$.
> 
> Thus, $\alpha$ is an [[Isomorphism|isomorphism]] with $\alpha^{-1} = \alpha'$, meaning $c \cong c'$. $\square$

[^1]: [[Category of Sets]]
[^2]: [[Category of Topologies]]
