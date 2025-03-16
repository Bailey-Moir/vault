---
tags:
  - atom
  - math
---
A [[Linear Systems|linear system]] is in *echelon-form* (*EF*) iff the first variable in each equation does not appear in the equations below. A matrix in this form is said to be in *row echelon-form* (*REF*).

> [!note] [[Linear Systems|Linear systems]] in this form are always [[Consistency of Linear Systems|consistent]] unless they contain a row of zeros with a non-zero constant on the right-hand side.
# RREF
*Reduced REF* (*RREF*) is *REF* except all [[Pivots and Free Variables|pivots]] are $1$, and all other entries in [[Pivots and Free Variables|pivot]] columns are $0$.
> [!example]-
> $$\begin{bmatrix}
> 	1 & 0 & 0 & 3 \\
> 	0 & 1 & 0 & 3 \\
> 	0 & 0 & 1 & 0 \\
> \end{bmatrix}$$