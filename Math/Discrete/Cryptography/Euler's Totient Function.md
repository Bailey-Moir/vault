---
tags:
  - atom
  - math
  - discrete
---
For all $n \in \Z^+$, *Euler's totient function*, $\varphi(n)$, is the number of [[Math/Discrete/Number Theory/Modular Arithmetic/Invertibility|invertible]] elements in $\Z_n$[^1].
$$\begin{align*}
	\varphi(n) &= \left|\Z_{n}^\times\right| && (1) \\
	&= n \prod_{p|n} \left( 1 - \dfrac{1}{p} \right)  && \small\begin{array}{c} \text{Euler's Product}\\\text{Formula} \end{array}\\
\end{align*}$$
- If $n \in \mathbb{P}$, $\varphi(n) = n-1$
- If $p,q \in \mathbb{P}$ such that $p \ne q$, $\varphi(pq) = (p-1)(q-1)$

\[$(1)$ [[Invertible Group of Cyclic Groups]]\]

[^1]: [[Cyclic Groups]]