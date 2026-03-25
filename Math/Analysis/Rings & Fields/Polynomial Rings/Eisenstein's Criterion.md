---
tags:
  - atom
  - math
---
Let $f \in \Z[x]$. If there is a [[Primes|prime]] $p \in \P$ such that
- $p$ does not [[Divisibility|divide]] the leading coefficient,
- it [[Divisibility|divides]] all the other coefficients, and
- $p^2$ does not [[Divisibility|divide]] the constant coefficient,

then $f$ is [[Reducible Factors#^negation|irreducible]] over $\Q$.

> [!proof]-
> Let $f \in \Z[x]$ be a polynomial satisfying *Eisenstein's criterion*, and suppose $f$ is [[Reducible Factors|reducible]] in $\Q[x]$.
> 
> Then $f = gh$ for some non-[[Rings#^unit|units]] $g,h \in \Z[x]$ of positive degree by [[Reducible Factors#^rational-reducible-implies-integer-reducible|this theorem]].
> 
> $$\begin{align}
> 	ax^n &\equiv f(x) \mod p \\
> 	&\equiv g(x)h(x) \mod p.
> \end{align}$$
> $\Z_{p}[x]$ is a [[Unique Factorisation Domain|UFD]], so
> $$\begin{array}{cc}
> 	g(x) \equiv bx^k, & h(x) \equiv cx^{n - k},
> \end{array}$$
> so $p$ must [[Divisibility|divide]] the constant coefficients $g_{0}$ and $h_{0}$ of $g$ and $h$. Thus, $p^2$ divides the constant coefficient $g_{0}h_{0}$ of $f$, a [[Contradictions|contradiction]].

> [!example]- $f(x) = 2x^5 + 6x^3 - 9x^2 + 18x + 6$
> Let $p = 3$.
> - $3 \nmid 2$,
> - $3 | 6$, $3|9$, $3| 18$, and $3|6$, and
> - $9 \nmid 6$.
> 
> Thus, $f$ is [[Reducible Factors#^negation|irreducible]] in $\Q[x]$.

> [!example]- $f(x) = 2x^7 - 20x^3 - 10x^2 + 10$
> Let $p = 5$. Reducing the coefficients [[Modular Arithmetic|modulo]] $5$ gives
> $$f(x) \equiv 2x^7 \mod 5,$$
> meaning it divides all coefficients except the leading. Since we also have $25 \nmid 10$, $f$ is [[Reducible Factors#^negation|irreducible]] in $\Q[x]$.