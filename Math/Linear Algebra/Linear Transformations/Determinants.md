---
tags:
  - math
  - atom
---
The *determinant* of a [[Matrices|matrix]] $A$, $|A|$, is the **scale factor** of its [[Linear Transformations|linear transformation]]. This can be calculated as the area of the unit square after applying the [[Linear Transformations|transformation]].
- If $A$ reflects the unit square, then $|A| < 0$.
- If any rows or columns are redundant (a [[Linear Combinations|linear combination]] of other rows) then the *determinant* is always zero.
# Properties of Determinants
- $\left| AB \right|\equiv \left| A \right|\left| B \right|$
> [!intuition]-
> By the [[Matrix Multiplication#Properties of Matrix Multiplication|associative property of matrix multiplication]], 
> $$\left( AB \right)\vecbf{v}=A\left( B\vecbf{v} \right)$$
> Thus the [[Linear Transformations|transformation]]
> $$\vecbf{v}\to \left( AB \right)\vecbf{v}$$
> with a scaling factor of $\left| AB \right|$ is the same as
> $$\vecbf{v}\to B\vecbf{v}$$
> with a scaling factor of $\left| B \right|$ followed by
> $$\vecbf{v}\to A\left( B\vecbf{v} \right) $$
> with a scaling factor of $\left| A \right|$. Thus
> $$\left| AB \right| = \left| A \right| \left| B \right| $$
- $\left| A^{-1} \right|=\dfrac{1}{\left| A \right|}$
> [!proof]-
> We know that $\left| I \right|=1$, and $AA^{-1}=I$[^1]. So
> $$\begin{align*}
> 	\left| AA^{-1} \right| &= \left| A \right| \left| A^{-1} \right| \\
> 	1 &= \left| A \right| \left| A^{-1} \right| \\
> \end{align*}$$
> Therefore
> $$\left| A^{-1} \right| =\dfrac{1}{\left| A \right| }$$
- $\left| A^T \right|=\left| A \right|$[^2]
- If $A$ is $n\times n$, $\left| kA \right|=k^n\left| A \right|$.
> [!proof]-
> $$\begin{align*}
> 	\left| kA \right| &= k\left| \vecbf{c}_{1} | \vecbf{c}_{2} | \dots | \vecbf{c}_{n} \right|  \\
> 	&= \left| k\vecbf{c}_{1} | k\vecbf{c}_{2} | \dots | k\vecbf{c}_{n} \right|  \\
> 	&= k\left| \vecbf{c}_{1} | k\vecbf{c}_{2} | \dots | k\vecbf{c}_{n} \right|  \\
> 	&= k^2\left| \vecbf{c}_{1} | \vecbf{c}_{2} | \dots | k\vecbf{c}_{n} \right|  \\
> 	&\dots \\
> 	&= k^n\left| \vecbf{c}_{1} | \vecbf{c}_{2} | \dots | \vecbf{c}_{n} \right|  \\
> 	&= k^n\left| A \right|  \\
> \end{align*}$$
> \[[[Row and Column Operations with Determinants]]\]

[^1]: [[Identity Matrices]]
[^2]: [[Transposition]]
