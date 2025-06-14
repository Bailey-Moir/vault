---
tags:
  - atom
  - comp
---
$A$ is *polynomial-time reducible* to $B$, $A \le_{P} B$, iff there is a polynomial-time [[Decidability|computable]] [[Functions|function]] $f : \Sigma^* \to \Sigma^*$ with
$$w \in A \iff f(w) \in B$$
> [!intuition] In other words, iff there is a [[Complexity Classes#Polynomial Time|polynomial-time computable]] [[Algorithms|algorithm]] that allows you to convert the problem of deciding $A$ to the problem of deciding $B$.

> [!note]- If $A \le_{P} B$, A is 'easier' than $B$.
> Not easier in time complexity, but easier as $A$ can be solved with $B$, but not (necessarily) the other way around.