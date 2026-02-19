---
tags:
  - atom
  - math
---
A *ring* $R$ is a [[Sets|set]] together with two [[Binary Operations|binary operations]] $+$ and $\times$ on $R$ such that
1. $\left( R,+ \right)$ is an [[Groups#^abelian-groups|abelian group]].
2. $\times$ is associative, and
3. it is distributive, meaning $\forall a,b,c \in R,$
   $c(a+b) = ca+cb \;\land$ 
   $(a+b)c = ac+bc$

> [!definition] A **unity** in a *ring* is a non-zero multiplicative identity. 
^unity

> [!definition] A **unit** in a *ring* is an element that has a multiplicative inverse. 
^unit

> [!theorem]- If $R$ is a *ring*, then for all $a,b,c \in R$, <ol><li>$0a = a0 = 0$</li><li>$a(-b) = (-a)b = -(ab)$</li><li>$(-a)(-b) = ab$</li><li>$a\left( b-c \right) = ab - ac$ and $\left( a-b \right)c = ac - bc$</li></ol>If $R$ is a *ring* with **unity**, the **unity** is unique, and if $a \in R$ is a **unit**, its multiplicative inverse is unique. Further,<ol start="5"><li>$(-1)a = -a$</li><li>$(-1)(-1) = 1$</li></ol>
> 1. Start with $0+0=0$. Then multiplying $a$ on either side gives
> $$\begin{array}{rl}
> 	(0 + 0)a = 0a & a(0 + 0) = a0 \\
> 	0a + 0a = 0a & a0 + a0 = a0\\
> 	0a + 0a + -0a = 0a + -0a & a0 + a0 + -a0 = a0 + -a0 \\
> 	0a = 0 & a0 = 0. \\
> \end{array}$$
> 2. Using additive inverses,
> $$\begin{array}{rl}
> 	b + -b = 0  & a + -a = 0 \\
> 	a(b+ -b) = a0 & (a + -a)b = 0b \\
> 	ab + a(-b) = 0 & ab + (-a)b = 0. && 1. \\
> \end{array}$$
>    Then by the [[Groups#^inverse-uniqueness|uniqueness of inverses]] in [[Groups|groups]], $a(-b) = (-a)b = -(ab)$.
> 3. By $2.$, $(-a)(-b) = -(a(-b)) = -(-(ab))$, and since the [[Groups#^inverse-inverse|inverse of an inverse is itself]] in [[Groups|groups]], $(-a)(-b) = ab$.
> 4. Consider
> $$\begin{alignat}{3}
> 	a(b-c) &= ab + a(-c) &\hspace{2em} (a-b)c &= ac + a(-b) \\
> 	&= ab - ac  & &= ac - ab. &\hspace{2em} 2. \\
> \end{alignat}$$
> 5. Consider
> $$\begin{align}
> 	1 + -1  &= 0 \\
> 	(1 + -1)a  &= 0a \\
> 	1a + (-1)a  &= 0 && 1. \\
> 	a + (-1)a  &= 0. \\
> \end{align}$$
>    Then by the [[Groups#^inverse-uniqueness|uniqueness of inverses]] in [[Groups|groups]], $(-1)a = -a$.
> 6. This is a special case of 3. where $a=b=1$.
> 
> All the remains to be shown is that the **unities** and multiplicative inverses are unique.
> 
> Suppose $R$ has two **unities** $1_{1}$ and $1_{2}$ (and $1$ is any **unity**). Then
> $$\begin{array}{c}
> 	1 \times 1_{1} = 1 = 1 \times 1_{2} \\
> 	1_{1} = 1_{2}. \\
> \end{array}$$
> Suppose $a \in R$ has two inverses $a_{1}^{-1}$ and $a_{2}^{-1}$ (and $a^{-1}$ is any of its inverses). Then
> $$\begin{array}{c}
> 	a \times a_{1}^{-1} = 1 = a \times a_{2}^{-1} \\
> 	a^{-1} \times a \times a_{1}^{-1} = a^{-1} \times a \times a_{2}^{-1} \\
> 	1 \times a_{1}^{-1} = 1 \times a_{2}^{-1} \\
> 	a_{1}^{-1} = a_{2}^{-1}. \\
> \end{array}$$
^properties

> [!lemma]- If $a \in R$ is a [[#^unit|unit]], then $a$ is not a [[Zero-divisors|zero-divisor]].
> Suppose $a$ is a [[#^unit|unit]] and $ab = 0$. Then
> $$b = a^{-1}ab = a^{-1}0 = 0$$
^units-and-zero-divisors



not-unit -> zero-divisor
not-zero-divisor -> unit