---
tags:
  - atom
  - math
---
A *field* $\F$ is a [[Sets|set]] together with two [[Binary Operations|binary operations]] $+$ and $\times$ on $\F$ such that
1. $\left( \F,+ \right)$ is an [[Groups#^abelian-groups|abelian group]].
2. $\left( \F\setminus\{0\}, \times \right)$ is an [[Groups|abelian group]], where $0$ is the additive identity.
3. $\forall a,b,c \in \F, (c(a+b) = ca+cb)$ (distributivity).
# Field Theorems
> [!theorem]- **(1)** $0a \equiv 0$
> $$\begin{align*}
> 	0 &= 0 + 0 && \text{Additive Identity} \\
> 	0a &= \left( 0+0 \right)a \\
> 	0a &= 0a + 0a && \text{Distributive Property} \\
> 	0a - 0a &= 0a + 0a - 0a \\
> 	0 &= 0a && \text{Additive Inverse} \\
> \end{align*}$$
 ^zero-mult

> [!theorem]- **(2)** $-a \equiv (-1)a$
> $$\begin{align*}
> 	0 &= 1 + (-1) && \text{Additive Inverse} \\
> 	0a &= 1a + (-1)a && \text{Distributive Property}\\
> 	0 &= a + (-1)a && \mathbf{(1)}\, \forall a \in \F, 0a = 0 \\
> \end{align*}$$
> Therefore, $(-1)a$ is the *unique* additive inverse
 ^negative-times-negative-one

> [!theorem]- **(3)** $(-a)b = -(ab) = a(-b)$
> $$\begin{array}{l}
> 	\begin{align*}
> 		(-a)b &= (-1)ab && \mathbf{(2)}\, \forall a\in \F, -a= (-1)a \\
> 		&= (-1)(ab) && \text{Associativity} \\
> 		&= -(ab) && \mathbf{(2)}\, \forall a\in \F, -a= (-1)a \\
> 		\\
> 		a(-b) &= a(-1)b && \mathbf{(2)}\, \forall a\in \F, -a= (-1)a \\
> 		&= (-1)ab && \text{Commutativity} \\
> 		&= (-1)(ab) && \text{Associativity} \\
> 		&= -(ab) && \mathbf{(2)}\, \forall a\in \F, -a= (-1)a \\
> 	\end{align*} \\
> \end{array}$$
 ^negative-associative

> [!theorem]- **(4)** $(ab)^2 = a^2b^2$
> $$\begin{array}{l}
> 	\begin{align*}
> 		(ab)^2 &= (ab)(ab) && \text{(1)} \\
> 		&= abab && \text{Associativity} \\
> 		&= aabb && \text{Commutativity} \\
> 		&= a^2b^2 && \text{(1)} \\
> 	\end{align*} \\
> \end{array}$$
> \[$(1)$ [[Powers in Groups]]\]
 ^expand-square