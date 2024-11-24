---
tags:
  - atom
  - math
---
A [[Lists|list]] of vectors in a [[Vector Spaces|vector space]] $V$ is *linearly independent* if and only if each vector in the [[Span|span]] of those vectors has a **unique** representation as a [[Linear Combinations|linear combination]] of the [[Lists|list]] of vectors.
i.e.
$v_1, \dots, v_m \in V$ is *linearly independent* if and only if
$$\forall v \in \text{span}(v_1,\dots,v_m), \exists!a_1, \dots, a_m \in \F \ni v = a_1v_1 + \dots + a_mv_m$$

> [!note] Condition for Linear Independence
> $v_1, \dots, v_m \in V$ is *linearly independent* if the only choice of $a_1, \dots, a_m \in \F$[^1] that makes
> $$ a_1 v_1 + \dots + a_m v_m = 0  $$
> is $a_1 = \dots = a_m = 0$.

- All subsets of a *linearly independent* [[Lists|list]] are *linearly independent*.
- If some vector in a [[Lists|list]] of vectors in $V$ is a [[Linear Combinations|linear combination]] of the other vectors, then the list is *linearly dependent*. <br>Thus every [[Lists|list]] of vectors in $V$ containing $0$ is *linearly dependent*.

[^1]: [[Fields]]