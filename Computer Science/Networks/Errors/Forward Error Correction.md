---
tags:
  - atom
  - comp
---
*Forward error correction* (*FEC*) divides messages into blocks of $k$-bits called **data blocks**.
- the *FEC* encoder encodes **data blocks** it into $n$-bit **codewords**.
- the *FEC* decoder decodes **codewords** as their [[Hamming Distance|nearest]] valid **codeword**.

> [!note] Obviously, $n\geq k$.

> [!note] This is done on the [[OSI Seven Layer Model#Link Layer|link layer]].