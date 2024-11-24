---
tags:
  - atom
  - math
---
$$\large \forall v \in V, \exists w \in V \ni \left( v + w = 0 \right)$$
Since additive inverse are unique, $\forall v, w \in V$,
- $-v$ denotes the additive inverse of $v$, which is equal to $(-1)v$.
- $w-v = w + (-v)$

> [!proof]- Proof Additive Inverse is Unique
> Suppose $V$ is a vector space. Let $v \in V$. Suppose $w$ and $w'$ are additive inverses. It is then true that:
> $$\begin{align*}
>	w &= w + 0 && (1) \text{ Additive Identity}\\
>	&= w + (v + w') \\
>	&= (w + v) + w' && (2) \text{ Associativity} \\
>	&= 0 + w' && (3) \text{ Commutativity} \\
>	&= w' && (3)(1) \text{ Commutativity and Additive Identity} \\
> \end{align*}$$
> Thus $0' = 0$, proving $V$ has only one additive identity.
> \[$(1)$ [[Additive Identity of Vector Spaces|Additive Identity]], $(2)$ [[Associativity of Vector Spaces|Associativity]], $(3)$ [[Commutativity of Vector Spaces|Commutativity]]\]

> [!proof]- $\bf{\forall v \in V, \left( (-1)v = -v \right)}$
> $$\begin{align*}
> 	v + (-1)v &= 1v + (-1)v && (1) \text{ Multiplicative Identity} \\
> 	& = (1 + (-1))v && (2) \text{ Distributive Property} \\
> 	& = 0v \\
> 	& = 0 && (3) \text{ Zero Scalar Multiplication} \\
> \end{align*}$$
> Thus, $(-1)v$ must be the (unique) additive inverse, $-v$.
> \[$(1)$ [[Multiplicative Identity of Vector Spaces|Multiplicative Identity]], $(2)$ [[Distributive Property of Vector Spaces|Distributive Property]], $(3)$ [[Zero Multiplication for Vector Spaces|Zero Scalar Multiplication]]\]

\[[[Vector Spaces]]\]