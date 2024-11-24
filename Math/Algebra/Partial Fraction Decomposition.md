---
tags:
  - atom
  - math
---
Given a [[Types of Functions|rational function]], we can write it as the sum of fractions where the denominators are linear factors or irreducible quadratic factors. This is often used in [[Math/Calculus/Integration/Integration|integration]], but also many other branches of math such as [[Math/Algebra/Sequences & Series/Sequences & Series|sequences and series]].
- $\dfrac{1}{(x-a)(x-b)} = \dfrac{A}{x-a} + \dfrac{B}{x-b}$
- For each repeated linear factor, there are $n$ fractions with denominators of ascending power.
   $\dfrac{1}{(x-a)^n} = \dfrac{A}{(x-a)} + \dfrac{B}{(x-a)^2} + \dots + \dfrac{K}{(x-a)^n}$
- Irreducible factors have numerators with indeterminate polynomials of one order less.
   $\dfrac{1}{(x^2+a)P(x)} = \dfrac{Ax + B}{x^2+a} + \dots$
- Repeating irreducible factors are handled using a combination of the previous two rules.
   $\dfrac{1}{(x^2+a)^n} = \dfrac{Ax + B}{x^2+a} + \dfrac{Cx + D}{(x^2+a)^2} + \dots + \dfrac{Ex + F}{(x^2+a)^n}$