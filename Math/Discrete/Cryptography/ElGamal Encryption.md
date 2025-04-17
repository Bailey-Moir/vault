---
tags:
  - atom
  - math
  - discrete
---
After performing a [[Diffie-Hellman Key Exchange|Diffie-Hellman key exchange]], Bob can send a message $m$ to Alice using *ElGamal encryption*:
1. Bob sends $(B,mK)$
2. Alice computes $m = B^{-a}(mK)$

---

1. Bob sends $mK$
2. Alice computes $m = K^{-1}(mK)$

> [!proof]- Alice recovers $m$
> $$\begin{align}
> 	B^{-a} (mK) &= g^{-ab} m g^{ab} \\
> 	&= g^{-ab} g^{ab} m  (1) \\
> 	&= m \\
> \end{align}$$
> \[$(1)$ [[Cyclic Groups|Commutativity of Cyclic Groups]]\]
