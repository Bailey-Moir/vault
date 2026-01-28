---
tags:
  - atom
  - math
  - discrete
---
A [[Functions|function]] is *injective* (*one-to-one*) iff each element in the [[Range & Image|range]] has a **unique** element in the [[Domain|domain]];
$$\begin{array}{c}
	\forall a_1,a_2 \in A, \left( f(a_1) = f(a_2) \to a_1 = a_2 \right) \\
	\color{gray}{\small{\forall a_1,a_2 \in A, \left( a_1 \ne a_2 \to f(a_1) \ne f(a_2) \right)}}
\end{array}$$
*Note that the reverse [[Implication|implication]] of these two expressions is given by the definition of a [[Functions|function]].*
# Properties of Injections
Let $f: A \to B$ be a *injective [[Functions|function]]*:
- $|A| \le |B|$
  > [!proof]- Intuition
> By the [[Functions|definition of a function]], each $a \in A$ must map to an element $b \in B$, so if $|A| > |B|$, there must be multiple elements in $A$ that map to the same element in $B$. An *injective function* can map at most one element from $a \in A$ to each $b \in B$, implying a [[Contradictions|contradiction]]. Thus $|A| \le |B|$.
> 
> \[[[Proof by Contradiction]]\]

- $|\text{range}(f)| = |A|$
- $f(X^c) = \text{range}(f) \setminus X$

\[[[Cardinality]]\]