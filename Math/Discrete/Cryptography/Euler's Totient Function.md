---
tags:
  - atom
  - math
  - discrete
---
For all $n \in \Z^+$, *Euler's totient function*, $\phi(n)$, is the number of [[Math/Discrete/Number Theory/Modular Arithmetic/Invertibility|invertible]] elements in $\Z_n$^[[[Cyclic Groups]]].
$$\begin{align*}
	\phi(n) &= \left|\left\{ a \in \Z_n :  \gcd(a,n) = 1 \right\}\right| \\
	&= n \prod_{p|n} \left( 1 - \dfrac{1}{p} \right)  && \small\begin{array}{c} \text{Euler's Product}\\\text{Formula} \end{array}\\
\end{align*}$$
- If $n \in \mathbb{P}$, $\phi(n) = n-1$
- If $p,q \in \mathbb{P}$ such that $p \ne q$, $\phi(n) = (p-1)(q-1)$