---
tags:
  - atom
  - math
---
To solve for the [[General vs Particular Solution|particular solution]] $y_p$ of a [[Solving Non-Homogeneous Differential Equations|non-homogeneous DE]] of the form
$$y'' + py' + q = r(x)$$
1. **Use undetermined coefficients**
Set $y_p$ to the RHS ($r(x)$), with coefficients replaced with undetermined coefficients.

>[!example]
> $r(x) = 7x^2 + \sin(2x) + xe^{3x} \implies y_p = Ax^2 + B\sin(2x) + Cxe^{3x}$

2. **Include derivatives of each term**
Include all the derivatives of each term, keeping the coefficients for each term undetermined.

> [!example] Examples
> $r(x) = Ax^2 + Cxe^3x \implies y_p = Ax^2 + Bx + C + Dxe^3x + Ee^3x$
>  $r(x) = A\sin(2x) + Bcos(3x) \implies y_p = A\sin(2x) + B\cos(2x) + C\sin(3x) + D\cos(3x)$

4. **Prevent [[Linear Independence|linearly dependent]] terms**
For terms which are [[Linear Independence|linearly dependent]] on other terms in $y_h$ or $y_p$, multiply them by $x$ until they are [[Linear Independence|linearly independent]].

> [!example]
> $y_h = C_1e^x + C_2e^{-x} \land r(x) = Axe^x + Be^x \implies y_p = Axe^x + Bx^2e^x$

\[[[Solving Non-Homogeneous Differential Equations]]\]