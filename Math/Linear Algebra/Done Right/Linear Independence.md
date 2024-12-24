---
tags:
  - atom
  - math
---
A [[Lists|list]] of vectors is *linearly independent* iff each vector in their [[Span|span]] has a **unique** representation as a [[Linear Combinations|linear combination]] of the [[Lists|list]] of vectors. 
$$\forall \vecbf{v} \in \text{span}(\vecbf{v}_1,\dots,\vecbf{v}_n), \exists!a_1, \dots, a_n \in \F : \vecbf{v} = a_1\vecbf{v}_1 + \dots + a_n\vecbf{v}_n$$
*Each value has a unique linear combination*

> [!note] Condition for Linear Independence
> $\vecbf{v}_1, \dots, \vecbf{v}_n \in V$ is *linearly independent* iff the only choice of $a_1, \dots, a_n \in \F$[^1] that makes
> $$ a_1 \vecbf{v}_1 + \dots + a_n \vecbf{v}_n = \vecbf{0} $$
> is $a_1 = \dots = a_n = 0$.

- All subsets of a *linearly independent* [[Lists|list]] are *linearly independent*.
- If some vector in a [[Lists|list]] of vectors in $V$ is a [[Linear Combinations|linear combination]] of the other vectors, then the list is *linearly dependent*. <br>Thus every [[Lists|list]] of vectors in $V$ containing $\vecbf{0}$ is *linearly dependent*.

[^1]: [[Fields]]