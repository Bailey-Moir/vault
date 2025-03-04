---
tags:
  - atom
  - math
  - linear
---
A [[Lists|list]] of vectors is *linearly independent* iff each vector in their [[Span|span]] has a **unique** representation as a [[Linear Combinations|linear combination]] of the [[Lists|list]]. 
$$\forall \vecbf{v} \in \text{span}(\vecbf{v}_1,\dots,\vecbf{v}_n), \exists!a_1, \dots, a_n \in \F : \vecbf{v} = a_1\vecbf{v}_1 + \dots + a_n\vecbf{v}_n$$
*Each value has a unique linear combination*

> [!note] Condition for Linear Independence
> $\vecbf{v}_1, \dots, \vecbf{v}_n \in V$ is *linearly independent* iff the only choice of $a_1, \dots, a_n \in \F$[^1] that makes
> $$ a_1 \vecbf{v}_1 + \dots + a_n \vecbf{v}_n = \vecbf{0} $$
> is $a_1 = \dots = a_n = 0$.
> > [!note]- Condition as [[Linear Systems|Linear System]]
> > $\vecbf{v}_1, \dots, \vecbf{v}_n \in V$ is *linearly independent* iff the only solution to the [[Homogeneous Systems|homogeneous system]] of those vectors as columns is the trivial solution; iff the only solution to the [[Linear Systems|linear system]]
> > $$\left[ \vecbf{v}_{1}|\cdots|\vecbf{v}_{n} \right]\vecbf{x} = \vecbf{0} $$
> > is the trivial solution, $\vecbf{x} = \vecbf{0}$.

- All [[Subsets|subsets]] of a *linearly independent* [[Lists|list]]/[[Sets|set]] are *linearly independent*.
- A [[Lists|list]]/[[Sets|set]] of vectors is *linearly independent* iff no vectors in it can be given as a [[Linear Combinations|linear combination]] of the others.

[^1]: [[Fields]]