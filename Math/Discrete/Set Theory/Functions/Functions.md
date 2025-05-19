---
tags:
  - atom
  - math
  - discrete
---

![400|center](function-sets.excalidraw.md)
*Functions* are another type of [[Relations|relation]]. For a [[Relations|relation]] $\rel \in A \times B$[^1] to be a *function* $f$, it must have the following properties:
- The [[Domain|domain]] of $f$ is $A$;
  $\forall a \in A, \exists  b \in B : f(a) = b$
- $\mathcal{f}$ is single valued;
  $\forall a \in A, b_1, b_2 \in B, \left( f(a) = b_1 \land f(a) = b_2 \implies b_1 = b_2 \right)$

These properties combined imply $\forall a \in A, \exists! b \in B : f(a) = b$.
# Notations
$$\begin{array}{c}
f(a) = b \implies (a,b) \in f \\
f : A \to B \implies f \subset A\times B && (1) \\
\end{array}$$

\[(1) [[Cartesian Product]]\]

[^1]: [[Cartesian Product]]
