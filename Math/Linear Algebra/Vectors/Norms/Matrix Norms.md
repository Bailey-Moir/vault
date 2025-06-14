---
tags:
  - atom
  - math
  - linear
---
A *matrix norm* is a [[Norms|norm]] on [[Vector Spaces|vector spaces]] of the form $\R^{m,n}$, where the following **additional** property holds:
- **Submultiplicative**
  $\| AB \| \le \| A \|\| B \|$

> [!definition] A *matrix norm* on $\R^{m,n}$ is **compatible** with a vector [[Norms|norm]] $\| \cdot \|$ on $\R^{n}$ iff
> $$\| A\vecbf{x} \| \le \| A \|\| \vecbf{x} \|$$
> for all $A \in \R^{m,n}$ and $\vecbf{x} \in \R^n$
> > [!note] Intuitively, this gives $$\dfrac{\| A\vecbf{x} \|}{\| \vecbf{x} \|} \le \| A \|$$when $\vecbf{x}\ne 0$.

> [!derivation]- One approach for constructing *matrix norms* is to consider a [[Matrices|matrix]] $A \in \R^{m,n}$ as a [[Math/Linear Algebra/Vectors/Vectors|vector]] in $\R^{mn}$, constructing the vector left to right, top to bottom. The *matrix norm* can then be given as a [[Norms|norm]] on $\R^{mn}$.
> e.g.
> $$\left\| \begin{bmatrix}
> 	a & b \\
> 	c & d
> \end{bmatrix} \right\| = \left\| \begin{bmatrix}
> 	a \\ b \\ c \\ d
> \end{bmatrix} \right\|  $$
> However, this does not always give a **submultiplicative** *matrix norm*, or **compatibility** with the corresponding vector [[Norms|norm]].
> 
> One example of such a [[Norms|norm]] that **does** satisfy these properties is the [[Frobenius Norm]]