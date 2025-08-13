---
tags:
  - atom
  - math
  - discrete
---
Using [[Fermat's Little Theorem|Fermat's little theorem]], a [[Primality Test|probabilistic primality test]] can be derived:
1. Choose a random $a \in \{2,\dots,n-2\}$ and compute $a^n \mod n$.
2. If $a^n \not\equiv a \mod n$, return $\text{F{\scriptsize ALSE}}$.
3. Repeat steps 1-2 until satisfied, and return $\text{T{\scriptsize{RUE}}}$.

> [!note]- Some [[Primes|non-prime]] integers $n$ pass *the Fermat test* for all $a \in \Z_{n}$. Such numbers are called **Carhmichael numbers**

[^1]: [[Residue Classes]]
