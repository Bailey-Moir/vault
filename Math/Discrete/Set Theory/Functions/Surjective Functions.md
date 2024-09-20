---
tags:
  - atom
  - math
  - discrete
---
A [[Math/Discrete/Set Theory/Functions/Functions|function]] is *surjective* (*onto*) [[Logical Equivalence|iff]] the [[Math/Discrete/Set Theory/Functions/Codomain|codomain]] is **equal** to the [[Math/Discrete/Set Theory/Functions/Range|range]];
$$ \forall b \in B, \exists a \in A : f(a) = b $$
# Properties of Surjections
Let $f: A \to B$ be a *surjective [[Math/Discrete/Set Theory/Functions/Functions|function]]*:
- $|A| \ge |B|$
> [!proof]- Intuition
> By the [[Math/Discrete/Set Theory/Functions/Functions|definition of a function]], each $a \in A$ can only map to one element $b \in B$, so if $|A| < |B|$, there must be elements in $B$ that $A$ does not map to. If $f$ is then also *surjective*, each value in $B$ must be mapped to from $A$ by $f$, which is a [[Contradictions|contradiction]]. Thus $|A| \ge |B|$.
- $|\text{range}(f)| = |B|$

\[[[Cardinality]]\]