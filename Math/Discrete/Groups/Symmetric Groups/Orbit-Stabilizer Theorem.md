---
tags:
  - atom
  - math
  - discrete
---

For any [[Groups|group action]] of $G$ on $S$, and any position $s$ in $S$, the [[Order in Groups|order]] of $G$ is the product of the [[Cardinality|cardinality]]/[[Order in Groups|order]] of the [[Orbits and Stabilizers|orbits and stabilizers]] of $s$;
$$\left| G \right| = \left| \text{Orb}(s) \right| \times \left| \text{Stab}(s) \right|  $$
> [!proof]-
> Since $\text{Stab}(s)$ is a [[Subgroups|subgroup]], by [[Lagrange's Theorem|Lagrange's theorem]],
> $$\left| G \right| = \left| \text{Stab}(s) \right| \times (\text{Number fo cosests of } \text{Stab}(s)). $$
> So we want to show the number of [[Cosets|cosets]] of $\text{Stab}(s)$ is $\left| \text{Orb}(s) \right|$.
> 
> Consider the function $\phi: G \to\text{Orb}(s)$, where $\phi(g) = g(s)$.
> 
> The [[Orbits and Stabilizers#Lemmas|orbit and stabilizer lemmas]] give that
> - $\phi$ has a constant value on each [[Code|coset]], and that
> - $\phi$ takes a different value on each [[Cosets|coset]].
> 
> Thus, $\phi$ induces a [[Bijective Functions|bijection]] between the [[Cosets|cosets]] of $\text{Stab}(s)$ and $\text{Orb}(s)$.
> 
> Thus, $\left| \text{Orb}(s) \right|$ is the number of [[Cosets|cosets]] of $\text{Stab}(s)$.
