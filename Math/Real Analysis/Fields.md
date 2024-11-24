---
tags:
  - atom
  - math
---
A field $\F$ is a [[Sets|set]] with two [[Binary Operations|binary operations]] $+$ and $\times$ with the properties that:
1. $\F$ is an [[Groups|abelian group]] with $+$.
2. $\F/\{0\}$ is an [[Groups|abelian group]] with $\times$, where $0$ is the additive identity.
3. $\forall a,b,c \in \F, (c(a+b) = ca+cb)$ (distributivity).
# Field Properties
- $\forall a \in \F, 0a = 0$
> [!proof]-
> Starting point, additive identity rule to 0:
> $$0 = 0 + 0$$
> Now multiply by $a$:
> $$\begin{align*}
> 	a\times0 &= a\times(0+0) \\
> \end{align*}$$
> Next, apply the distributive property and the additive inverse of $a\times0$.
> $$\begin{align*}
> a\times0 - a\times0 &= a\times0 + a\times0 - a\times0 \\
> 0 &= a\times0
> \end{align*}$$
- $\forall a\in \F$, its additive inverse is $-a= (-1)a$.
> [!proof]-
> Start with $0 = 1 - 1$ (where $0$ is the additive identity and $1$ is the multiplicative identity), multiply by $a$:
> $$\begin{align*}
> 	a \times 0 &= a \times 1 + a\times (-1) \\
> 	0 &= a + (-1)a \\
> \end{align*}$$
> Therefore, $(-1)a$ is the additive inverse
- $\forall a,b\in \F, -(ab) = (-a)b = a(-b)$
> [!proof]-
> $$\begin{array}{l}
> 	\begin{align*}
> 		(-a)b &= (-1)ab \\
> 		&= (-1)(ab) && \text{Associativity} \\
> 		&= -(ab)\\
> 		\\
> 		a(-b) &= a(-1)b \\
> 		&= (-1)ab && \text{Commutativity} \\
> 		&= (-1)(ab) && \text{Associativity} \\
> 		&= -(ab) \\
> 	\end{align*} \\
> \end{array}$$