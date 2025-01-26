---
tags:
  - atom
  - math
  - discrete
---
A [[Functions|function]] is *surjective* (*onto*) iff the [[Codomain|codomain]] is **equal** to the [[Range & Image|range]];
$$ \forall b \in B, \exists a \in A : f(a) = b $$
# Properties of Surjections
Let $f: A \to B$ be a *surjective [[Functions|function]]*:
- $|A| \ge |B|$
> [!proof]- Intuition
> By the [[Functions|definition of a function]], each $a \in A$ can only map to one element $b \in B$, so if $|A| < |B|$, there must be elements in $B$ that $A$ does not map to. If $f$ is then also *surjective*, each value in $B$ must be mapped to from $A$ by $f$, which is a [[Contradictions|contradiction]]. Thus $|A| \ge |B|$.
>
> \[[[Proof by Contradiction]]\]
- $|\text{range}(f)| = |B|$ ($\text{range}(f) = B$)

\[[[Cardinality]]\]