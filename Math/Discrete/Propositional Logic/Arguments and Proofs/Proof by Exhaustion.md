---
tags:
  - atom
  - math
  - discrete
---
*Proof by exhaustion* is used when we want to show $p \to q$ is [[Argument|valid]], and we know $p \iff p_1 \lor p_2 \lor \dots \lor p_n$[^1]. Note that this is the same as a [[Argument|typical form of an argument]], except the $\land$s[^2] are replaced with $\lor$s[^3]. If this is the case, it suffices to show that $(p_1 \implies q) \land (p_2 \implies q) \land \dots \land (p_n \implies q)$.
$$ p_1 \lor p_2 \lor \dots \lor p_n \to q \iff \left((p_1 \to q) \land (p_2 \to q) \land \dots \land (p_n \to q) \right) $$

[^1]: [[Logical Equivalence]]
[^2]: [[Conjunction]]
[^3]: [[Disjunction]]
