---
tags:
  - atom
  - math
---
A [[Lists|list]] of vectors in a [[Vector Spaces|vector space]] $V$ is *linearly independent* iff each vector in the [[Span|span]] of those vectors has a **unique** representation as a [[Linear Combinations|linear combination]] of the [[Lists|list]] of vectors. In other words, $v_1, \dots, v_m \in V$ is *linearly independent* iff
$$\forall \vecbf{v} \in \text{span}(\vecbf{v}_1,\dots,\vecbf{v}_m), \exists!a_1, \dots, a_m \in \F : \vecbf{v} = a_1\vecbf{v}_1 + \dots + a_m\vecbf{v}_m$$

> [!note] Condition for Linear Independence
> $\vecbf{v}_1, \dots, \vecbf{v}_m \in V$ is *linearly independent* iff the only choice of $a_1, \dots, a_m \in \F$[^1] that makes
> $$ a_1 \vecbf{v}_1 + \dots + a_m \vecbf{v}_m = \vecbf{0} $$
> is $a_1 = \dots = a_m = 0$.

- All subsets of a *linearly independent* [[Lists|list]] are *linearly independent*.
- If some vector in a [[Lists|list]] of vectors in $V$ is a [[Linear Combinations|linear combination]] of the other vectors, then the list is *linearly dependent*. <br>Thus every [[Lists|list]] of vectors in $V$ containing $\vecbf{0}$ is *linearly dependent*.

[^1]: [[Fields]]