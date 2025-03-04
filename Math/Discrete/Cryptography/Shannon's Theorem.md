---
tags:
  - atom
  - math
  - discrete
  - stats
---
Let $M$ and $C$ be [[Random Variables|random variables]] for the [[Plaintext|plaintext]] and [[Cipher|cipher]] respectively. For a [[The One-Time Pad|one-time pad]],
$$P(M = m_{0} | C = c_{0}) = P(M = m_{0}),$$
in other words, $M$ and $C$ are [[Independent Events|independent]].

> [!proof]-
> Choose the message $M \in \{ 0,1 \}$ according to some [[Density Curve|probability density function]], and $K \in \{ 0, 1 \}$ randomly ([[Uniform Density Curve|uniformly]]). Let $C = M + K \mod 2$ be the [[Key|public key]].
> 
> The [[Probabilities|probabilities]] of each outcome can be given by
> $$\begin{align*}
> 	P(C=0) &= P(M=0\land K=0) + P(M=1 \land K=1) \\
> 	&= P(M=0)P(K=0) + P(M=1)P(K=1) && (1) \\
> 	&= \dfrac{1}{2}\left( P(M=0) + P(M=1) \right) \\
> 	&= \dfrac{1}{2} \\
> 	\\
> 	P(C=1) &= P(M=1\land K=0) + P(M=0 \land K=1) \\
> 	&= P(M=1)P(K=0) + P(M=0)P(K=1) && (1) \\
> 	&= \dfrac{1}{2}\left( P(M=1) + P(M=0) \right) \\
> 	&= \dfrac{1}{2} \\
> \end{align*}$$