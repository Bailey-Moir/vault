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

> [!definition] A **unit** in a *ring* is an element that has a multiplicative inverse. 

[!theorem]- If $R$ is a *ring*, then for all $a,b,c \in R$,
1. $0a = a0 = 0$
2. $a(-b) = (-a)b = -(ab)$
3. $(-a)(-b) = ab$
4. $a\left( b-c \right) = ab - ac$ and $\left( a-b \right)c = ac - bc$.
If $R$ is a *ring* with **unity**, the **unity** is unique, and if $a \in R$ is a **unit**, its multiplicative inverse is unique. Further,
5. $(-1)a = -a$
6. $(-1)(-1) = a$

#TODO
1. Start with $0+0=0$. Then multiplying $a$ on either side gives
$$\begin{array}{rcl}
	(0 + 0)a = 0a && a(0 + 0) = a0 \\
	0a + 0a = 0a && a0 + a0 = a0\\
	0a + 0a + -0a = 0a + -0a && a0 + a0 + -a0 = a0 + -a0 \\
	0a = 0 && a0 = 0. \\
\end{array}$$
2. 

^properties