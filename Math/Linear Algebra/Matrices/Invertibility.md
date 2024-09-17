---
tags:
  - atom
  - math
---
A matrix can be not *invertible* either because it is not square, or because it is [[Singular Matrices|singular]]. 
- A matrix is *invertible* if and only if it is **square**, and not **[[Singular Matrices|singular]]**.
$$ A^{-1} \ne \text{undefined} \iff m=n \land |A| \ne 0  $$
Note that if a row a redundant, the determinant will be 0.
- In a [[Archive/Deatomized/Calculus/Algebra/Linear Algebra/Systems of Linear Equations|system of linear equations]], there is a **unique solution** if and only if the **matrix of coefficients** is *invertible*.
$$ A^{-1} \ne \text{undefined} \iff |S| = 1 $$
- From the above two conditions, you can extrapolate that **if the matrix of coefficients is square and not [[Singular Matrices|singular]], there is a unique solution**.
$$ m = n \land |A| \ne 0 \iff |S| = 1 $$
Thus
$$ m \ne n \lor |A| = 0 \iff |S| \in \{0, \infty\} $$
\[[[Inverting Matrices]]\]