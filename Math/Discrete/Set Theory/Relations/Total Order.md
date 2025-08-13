---
tags:
  - atom
  - math
---
A [[Relations|relation]] $\rel$ on $A$ is a *total order* iff:
- It is a [[Partial Order|partial order]], and
- $\forall a,b \in A, (a,b) \in \rel \lor (b,a) \in \rel$.

> [!theorem]- **Trichotomy Property** ($\le$): $\forall a,b \in A, a < b \underline{\lor} a > b \underline{\lor} a = b$
> For a *total order* $\le$ on a set $A$, if 
> $$ a < b \iff a \le b \land a \ne b $$
> (and same for $>$).
> It can be shown that $a<b \iff \neg(a \geq b)$. Thus, both $a<b$ and $a>b$ are true iff  the negation of the other two are true.
> If $a=b$, then by definition, $a\not< b$ and $a\not>b$.