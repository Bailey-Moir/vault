---
tags:
  - atom
  - math
  - discrete
---
A *group* $\left( G,* \right)$ is a [[Sets|set]] $G$ together with a [[Binary Operations|binary operation]] $* : G \times G \to G$ that satisfies the following properties:
1. **Associativity**
  $\begin{array}{l} \forall a,b,c \in G,\\ (a*b)*c = a*(b*c) \end{array}$
2. **Identity**
  $\begin{array}{l} \exists e \in G : \forall a \in G, \\ a*e = a = e*a \end{array}$
3. **Inverse**
  $\begin{array}{l} \forall a \in G, \exists a^{-1} \in G : \\ a * a^{-1} = e = a^{-1} * a \end{array}$
- ***Closure*** (given by $*$ being a [[Functions|function]])
  $\begin{array}{l} \forall a,b \in G, \exists! c \in G : \\ a*b=c \end{array}$
  
> [!definition] Abelian Groups
> An *abelian group* is a *group* with commutativity: $\forall a,b \in G, (a*b = b*a)$.
 ^abelian-groups

\[[[Binary Operations]]\]
# Theorems
> [!proof]- $a*c = b*c \implies a = b$
> $$\begin{align}
> 	a*c &= b*c \\
> 	a*c*c^{-1} &= b*c*c^{-1} && \text{Inverse}\\
> 	a*e &= b*e\\
> 	a &= b && \text{Identity} \\
> \end{align}$$

> [!proof]- Identity is unique
> Let $e_{1}$ and $e_{2}$ be two identities. Then
> $$\begin{align}
> 	a = e_{1}*a &= e_{2}*a \\
> 	e_{1}*a*a^{-1} &= e_{2}*a*a^{-1} && \text{Inverse} \\
> 	e_{1}*e &= e_{2}*e \\
> 	e_{1} &= e_{2} && \text{Identity} \\
> \end{align}$$
> Thus, if there are two identities, they must be the same, meaning the identity is unique.
^identity-uniqueness

> [!proof]- Inverses are unique
> Let $b_{1}$ and $b_{2}$ be two inverses of $a$. Then
> $$\begin{align}
> 	e = a*b_{1} &= a*b_{2} \\
> 	a^{-1}*a*b_{1} &= a^{-1}*a*b_{2} && \text{Inverse} \\
> 	e*b_{1} &= e*b_{2} \\
> 	b_{1} &= b_{2} && \text{Identity} \\
> \end{align}$$
> Thus, if there are two inverses for any element, they must be the same, meaning inverses is unique.
^inverse-uniqueness

> [!proof]- $\left( a^{-1} \right)^{-1} \equiv a$
> $$\begin{align}
> 	e &= a*a^{-1} \\
> 	e*\left( a^{-1} \right) &= a*a^{-1} * \left( a^{-1} \right)^{-1} && \text{Inverse} \\
> 	e*\left( a^{-1} \right) &= a*e \\
> 	\left( a^{-1} \right) &= a && \text{Identity} \\
> \end{align}$$
^inverse-inverse

> [!proof]- $\left( ab \right)^{-1} \equiv b^{-1}a^{-1}$
> $$\begin{align}
> 	(ab)(b^{-1}a^{-1}) &= abb^{-1}a^{-1} && \text{Associativity} \\
> 	&= aea^{-1} && \text{Inverse} \\
> 	&= aa^{-1} && \text{Identity} \\
> 	&= e && \text{Inverse} \\
> \end{align}$$
> Thus, $b^{-1}a^{-1}$ must be the **unique** inverse of $ab$.