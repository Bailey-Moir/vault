---
tags:
  - atom
  - math
  - discrete
---
## Encryption
- Alice chooses large [[Primes|primes]] $p,q$ and shares their product $n = pq$.
- Bob encrypts his message $m$ as $c = m^2 \mod n$
## Decryption
- Alice finds the solutions $\pm a$ of $x^2 \equiv c \mod p$.
- Alice finds the solutions $\pm b$ of $x^2 \equiv c \mod q$.
- Alice uses [[Extended Euclidean Algorithm|Euclid's algorithm]] to find $u,v$ such that $pu = qv = 1$.
- Then $m$ is one of the four values of $\pm bpu \pm aqv \mod n$.

\[[[Chinese Remainder Theorem#Alternative Approach]]\]