---
tags:
  - atom
  - math
  - discrete
---
*RSA digital signatures* are done the same as [[RSA]], except instead of computing
$$C \equiv m^e \mod n,$$
using their own **private key**, the signer computes
$$S \equiv m^{e^{-1}} \mod n.$$
To check the signature, the checker must use the signers **public key** to check that
$$m \equiv S^e \mod n.$$

> [!note] In [[RSA]], anyone can send anything to any receiver, but only the receiver can open it. <br/>With *RSA digital signatures*, only one person can sign, but everyone can check the authenticity.
