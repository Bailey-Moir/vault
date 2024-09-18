---
tags:
  - atom
  - stats
---
$$\begin{align*}
	P(H|E) &= \dfrac{P(H)}{P(E)}P(E|H) && \text{Multiplicative Rule} \\
	P(H_1|E) &= \dfrac{P(H_1)}{P(E|H_1)P(H_1) + P(E|H_0)P(H_0)}P(E|H_1) && \text{Total Probability} \\
	P(H_1|E) &= \dfrac{1}{1 + \dfrac{P(E|H_0)P(H_0)}{P(E|H_1)(H_1)}} \\
\end{align*}$$
This is just a rearrangement of the [[Multiplicative Rule|multiplicative rule]].

> [!example] False Positive of AIDS test
> $P(H_0) = \dfrac{1}{10000}$
> $P(H_1) = 1 - \dfrac{1}{10000}$
>
>$P(E|H_0) = \dfrac{1}{1000}$
>$P(E|H_1) = \dfrac{3}{1000}$
