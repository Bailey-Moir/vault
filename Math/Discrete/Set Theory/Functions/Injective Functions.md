---
tags:
  - atom
  - math
  - discrete
---
A [[Math/Discrete/Set Theory/Functions/Functions|function]] is *injective* (*one-to-one*) [[Logical Equivalence|iff]] each element in the [[Math/Discrete/Set Theory/Functions/Range|range]] has a **unique** element in the [[Math/Discrete/Set Theory/Functions/Domain|domain]];
$$\begin{array}{c}
	\forall a_1,a_2 \in A, \left( f(a_1) = f(a_2) \to a_1 = a_2 \right) \\
	\color{gray}{\small{\forall a_1,a_2 \in A, \left( a_1 \ne a_2 \to f(a_1) \ne f(a_2) \right)}}
\end{array}$$
*Note that the reverse [[Implication|implication]] of these two expressions is given by the definition of a [[Math/Discrete/Set Theory/Functions/Functions|function]].*
# Properties of Injections
Let $f: A \to B$ be a *injective [[Math/Discrete/Set Theory/Functions/Functions|function]]*:
- $|A| \le |B|$^[[[Cardinality]]]
> [!proof]- Intuition
> By the [[Math/Discrete/Set Theory/Functions/Functions|definition of a function]], each $a \in A$ can must map to an element $b \in B$, so if $|A| > |B|$, there must be multiple elements in $A$ that map to the same element $B$. An *injective function* can only map one element from $a \in A$ to each $b \in B$, implying a [[Contradictions|contradiction]]. Thus $|A| \le |B|$.