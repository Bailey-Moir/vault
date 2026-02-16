---
tags:
  - atom
  - math
  - linear
---
A *vector space* $V$ is a [[Sets|set]] with a scalar [[Fields|field]] $\F$ with [[Binary Operations|binary operations]] of addition $+$ and scalar multiplication $\times$ such that
- $\left( V,+ \right)$ is an [[Groups#^abelian-groups|abelian group]].
- **Scalar Associativity**
  $(ab)\vecbf{v} \equiv a(b\vecbf{v})$
- **Distributivity**
  $a(\vecbf{u}+\vecbf{v}) \equiv a\vecbf{u} + a\vecbf{v}$
  $(a+b)\vecbf{v} \equiv a\vecbf{v} + b\vecbf{v}$
- **Scalar Multiplicative Identity**
  $1\vecbf{v} \equiv \vecbf{v}$

> [!note]
> - The elements of a *vector space* are called vectors or points.
> - A *vector space* over $A$ is a *vector space* with $A$ as the scalar [[Fields|field]].
> - A *vector space* over $\R$ is called a **real vector space**.
> - A *vector space* over $\C$ is called a **complex vector space**.
# Theorems
> [!theorem]- $(-1)\vecbf{v} = -\vecbf{v}$
> $$\begin{align*}
> 	\vecbf{v} + (-1)\vecbf{v} &= 1\vecbf{v} + (-1)\vecbf{v} && \text{Multiplicative Identity} \\
> 	& = (1 + (-1))\vecbf{v} && \text{Distributive Property} \\
> 	& = 0\vecbf{v} \\
> 	& = \vecbf{0} && \forall \vecbf{v}, 0\vecbf{v} = \vecbf{0} \\
> \end{align*}$$
> Thus, $(-1)\vecbf{v}$ must be the (unique) additive inverse, $-\vecbf{v}$.

> [!theorem]- $0\vecbf{v} = \vecbf{0}$
> $$\begin{align*}
> 	0\vecbf{v} &= (0 + 0)\vecbf{v} \\
> 	0\vecbf{v} &= 0\vecbf{v} + 0\vecbf{v} && \text{Distributive Property} \\
> 	\vecbf{0} &= 0\vecbf{v} && \text{Additive Inverse} \\
> \end{align*}$$

> [!theorem]- $a\vecbf{0} = \vecbf{0}$
> $$\begin{align*}
> 	a\vecbf{0} &= a(\vecbf{0} + \vecbf{0}) && \text{Additive Identity} \\
> 	a\vecbf{0} &= a\vecbf{0} + a\vecbf{0} && \text{Distributive Property} \\
> 	\vecbf{0} &= a\vecbf{0} && \text{Additive Inverse} \\
> \end{align*}$$