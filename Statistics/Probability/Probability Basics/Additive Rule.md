---
tags:
  - atom
  - stats
  - discrete
  - math
---
For two [[Events|events]] $A$ and $B$,
$$ P(A \cup B) = P(A) + P(B) - P(A \cap B) $$
\[[[Cardinality]], [[Combining Events]]\]

> [!proof]-
> ![530|center](additive-rule.excalidraw.md)
> $A \cup B = A \cup B-A$
> $\implies P(A\cup B) = P(A) + P(B-A)$
> $B = (B - A) \cup A \cap B$
> $\implies P(B) = P(B-A) + P(A \cap B)$
> Combining these two results gives
> $$\begin{align*}
> 	P(A\cup B)-P(A) &= P(B) - P(A\cap B) \\
> 	P(A\cup B) &= P(A) + P(B) - P(A\cap B)
> \end{align*}$$


$$ P(B_{1} \cup B_{2})$$