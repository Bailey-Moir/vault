---
tags:
  - atom
  - math
---
A *vector space* $V$ s a [[Sets|set]] with a **closed** addition on $V$ and a **closed** scalar multiplication on $V$ with:
- **Commutativity**
  $\vecbf{u} + \vecbf{v} \equiv \vecbf{v} + \vecbf{u}$
- **Associativity**
  $(\vecbf{u} + \vecbf{v}) + \vecbf{w} \equiv \vecbf{u} + (\vecbf{v} + \vecbf{w})$
  $(ab)\vecbf{v} \equiv a(b\vecbf{v})$
- **Distributive Property**
  $a(\vecbf{u}+\vecbf{v}) \equiv a\vecbf{u} + a\vecbf{v}$
  $(a+b)\vecbf{v} \equiv a\vecbf{v} + b\vecbf{v}$
- **Scalar Multiplicative Identity**
  $1\vecbf{v} \equiv \vecbf{v}$
- **Additive Identity**
  $\exists \vecbf{0} \in V : \forall \vecbf{v} \in V, \left( \vecbf{v} + \vecbf{0} = \vecbf{v} \right)$
- **Additive Inverse**
  $\forall \vecbf{v} \in V, \exists (-\vecbf{v}) \in V : \left( \vecbf{v} + \vecbf{w} = \vecbf{0} \right)$


> [!note]
> - The elements of a *vector space* are called vectors or points.
> - A *vector space* over $A$ is a *vector space* with $A$ as the scalar [[Fields|field]].
> - A *vector space* over $\R$ is called a **real vector space**.
> - A *vector space* over $\C$ is called a **complex vector space**.

# Theorems
> [!theorem]- Additive Identity is Unique
> Suppose $\vecbf{0}$ and $\vecbf{0'}$ are both additive identities. Then
> $$\begin{align*}
>	\vecbf{0'} &= \vecbf{0'} + \vecbf{0} && \text{Additive Identity} \\
>	&= \vecbf{0} + \vecbf{0'} && \text{Commutativity} \\
>	&= \vecbf{0} && \text{Additive Identity}
> \end{align*}$$
> Thus $\vecbf{0'} = \vecbf{0}$, proving $V$ has only one additive identity.

> [!theorem]- Additive Inverse is Unique
> For some vector $\vecbf{v}$, suppose $\vecbf{w}$ and $\vecbf{w'}$ are additive inverses. Then
> $$\begin{align*}
> \vecbf{w} &= \vecbf{w} + \vecbf{0} && \text{Additive Identity}\\
> &= \vecbf{w} + (\vecbf{v} + \vecbf{w'}) && \text{Additive Inverse} \\
> &= (\vecbf{w} + \vecbf{v}) + \vecbf{w'} && \text{Associativity} \\
> &= \vecbf{0} + \vecbf{w'} && \text{Commutativity and Additive Inverse} \\
> &= \vecbf{w'} && \text{Commutativity and Additive Identity} \\
> \end{align*}$$
> Thus $\vecbf{w'} = \vecbf{w}$, proving $V$ has only one additive inverse.

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