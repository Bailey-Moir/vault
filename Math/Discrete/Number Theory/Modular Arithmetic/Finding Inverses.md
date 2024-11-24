---
tags:
  - atom
  - math
  - discrete
---
To *find the inverse* of $a$ in $\Z_n$,
1. Find $\gcd(a,n)$[^1] to determine [[Math/Discrete/Number Theory/Modular Arithmetic/Invertibility|invertibility]] using [[The Euclidean Algorithm|the Euclidean algorithm]].
2. Express $1$ as a [[Linear Combinations|linear combination]] of $a$ and $n$ (over the integers) using the [[Extended Euclidean Algorithm|extended Euclidean algorithm]].
3. Working with this [[Linear Combinations|linear combination]] as a [[Congruence|congruence]] modulo $n$, solve for the *inverse*.

> [!example]-
> **Find $\bf{17^{-1}}$ in $\bf{\Z_{43}}$**
> 1. Find $\gcd(17,43)$ to determine [[Math/Discrete/Number Theory/Modular Arithmetic/Invertibility|invertibility]].
> $$\begin{align*}
> 	43 = 2\times17 + 9 \\
> 	17 = 1\times9 + 8 \\
> 	9 = 1\times8 + 1 \\
> \end{align*}$$
> Therefore $\gcd(17,43) = 1$
> 2. Use [[Extended Euclidean Algorithm]] to find [[Linear Combinations|linear combination]].
> $$\begin{align*}
> 	1 &= 9 - 1\times8 \\
> 	1 &= 9 - (17 - 1 \times 9) \\
> 	1 &= 2\times9 - 17 \\
> 	1 &= 2\times(43 - 2\times17) - 17 \\
> 	1 &= -5\times17 + 2\times43 \\
> \end{align*}$$
> 3. Solve inverse with [[Congruence|congruence]] modulo $43$
> $$\begin{align*}
> 	1 &\equiv -5 \times 17 + 2\times43 \pmod {43} \\
> 	1 &\equiv -5 \times 17 \pmod {43} \\
> \end{align*}$$
> Since $-5 \equiv 38 \pmod {43}$, $17^{-1} = 38$ in $\Z_{43}$.

[^1]: [[Greatest Common Divisor]]