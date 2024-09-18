---
tags:
  - atom
  - math
  - discrete
---
*Functions* are another type of [[Relations|relation]]. For a [[Relations|relation]] $\rel \in A \times B$^[[[Cartesian Product]]] to be a function $f$, it must have the properties:
- The [[Math/Discrete/Set Theory/Functions/Domain|domain]] of $f$ is $A$.
- $\forall a \in A, b_1, b_2 \in B \left( (a,b_1) \in f \land (a,b_2) \in f \implies b_1 = b_2 \right)$ ($f$ is single valued)

Combining these two properties gives $\forall a \in A, \exists! b \in B : f(a) = b$.

# Notations
$$\begin{array}{c}
f(a) = b \iff (a,b) \in f \\
f : A \to B \iff f \in A\times B && (1) \\
\end{array}$$
\[(1) [[Cartesian Product]]\]