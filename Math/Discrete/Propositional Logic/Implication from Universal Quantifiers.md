---
tags:
  - atom
  - math
  - discrete
---
For any [[Sets|sets]] $A \subseteq B$ and [[Predicates|predicate]] $p$ on $B$,
$$\forall x \in A, p(x) \iff \forall x \in B, \left( x \in A \to p(x) \right)$$
> [!corollary] By [[Proof by Contraposition|contraposing]] this [[Implication|implication]], you get $$\forall x \in A, p(x) \iff \forall x \in B, \left( \neg p(x) \to x \in B \setminus A \right)$$
^contraposing-universal-quantifiers

> [!example] *([[Negation|Negating]] [[Zero-divisors|zero-divisors]])*$$\forall b \in R \setminus \{ 0 \}, ab \ne 0 \iff \forall b \in R, \left( ab = 0 \to b = 0 \right)$$

\[[[Implication]]\]