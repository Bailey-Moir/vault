---
tags:
  - atom
  - math
---
A [[Matrices|matrix]] $A$ is *invertible* iff $\left| A \right| \ne 0$ (i.e. if it is not [[Singular Matrices|singular]]).
- This is [[Logical Equivalence|logically equivalent]] to the columns and rows of the [[Matrices|matrix]] being [[Linear Independence|linearly independent]].

> [!note]- Invertibility and Unique Solutions
> - In a [[Archive/Deatomized/Calculus/Algebra/Linear Algebra/Systems of Linear Equations|system of linear equations]], there is a **unique solution** if and only if the **matrix of coefficients** is *invertible*.
> $$ A^{-1} \ne \text{undefined} \iff |S| = 1 $$
> - From the above two conditions, you can extrapolate that **if the matrix of coefficients is square and not [[Singular Matrices|singular]], there is a unique solution**.
> $$ m = n \land |A| \ne 0 \iff |S| = 1 $$
> Thus
> $$ m \ne n \lor |A| = 0 \iff |S| \in \{0, \infty\} $$

\[[[Inverting Matrices]]\]