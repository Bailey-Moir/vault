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
> $$\begin{align*}
> 	0 &= 0 + 0 && \text{Additive Identity} \\
> 	0a &= a\left( 0+0 \right) \\
> 	0a &= 0a + 0a && \text{Distributive Property} \\
> 	0a - 0a &= 0a + 0a - 0a \\
> 	0 &= 0a && \text{Additive Inverse} \\
> \end{align*}$$
- $\forall a\in \F$, its additive inverse is $-a= (-1)a$.
> [!proof]-
> $$\begin{align*}
> 	0 &= 1 + (-1) && \text{Additive Inverse} \\
> 	0a &= 1a + (-1)a && \text{Distributive Property}\\
> 	0 &= a + (-1)a && \forall a \in \F, 0a = 0 \\
> \end{align*}$$
> Therefore, $(-1)a$ is the *unique* additive inverse
- $\forall a,b\in \F, -(ab) = (-a)b = a(-b)$
> [!proof]-
> $$\begin{array}{l}
> 	\begin{align*}
> 		(-a)b &= (-1)ab && \forall a\in \F, -a= (-1)a \\
> 		&= (-1)(ab) && \text{Associativity of Multiplication} \\
> 		&= -(ab) && \forall a\in \F, -a= (-1)a \\
> 		\\
> 		a(-b) &= a(-1)b && \forall a\in \F, -a= (-1)a \\
> 		&= (-1)ab && \text{Commutativity of Multiplication} \\
> 		&= (-1)(ab) && \text{Associativity of Multiplication} \\
> 		&= -(ab) && \forall a\in \F, -a= (-1)a \\
> 	\end{align*} \\
> \end{array}$$