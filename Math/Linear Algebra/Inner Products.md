---
tags:
  - atom
  - math
  - linear
---
An *inner product* $\left< \vecbf{v},\vecbf{w} \right> : V\times V \to \F$ of a [[Vector Spaces|vector space]] $V$ is defined by the following properties:
1. **Positive Definite**
   $\left< \vecbf{v},\vecbf{v} \right>\ge 0$
   $\left< \vecbf{v},\vecbf{v} \right> = 0 \iff \vecbf{v} = \vecbf{0}$
2. **Commutative**
   $\left< \vecbf{u},\vecbf{v} \right> = \left< \vecbf{v},\vecbf{u} \right>$
3. **[[Linear Maps|Linear]]**
   $\left< a\vecbf{u} + b\vecbf{v},\vecbf{w} \right> = a\left< \vecbf{u},\vecbf{w} \right> + b\left< \vecbf{v},\vecbf{w} \right>$

> [!definition] A [[Vector Spaces|vector space]] with an *inner product* is called an **inner product space**.

> [!note] For a general **inner product space**, [[Vector Length|vector length]] and [[Orthogonal Vectors|orthogonality]] can be defined in terms of the *inner product* (instead of the [[Dot Product|dot product]]).

> [!example] The [[Dot Product|dot product]] is an *inner product* of $\R^n$.

> [!example]- *Inner product* of $\mathcal{C}([a,b])$[^1]
> For $f,g \in \mathcal{C}([a,b])$, the *inner product* of $f$ and $g$, $\left< f,g \right>$, is defined as
> $$\left< f,g \right> = \int_{a}^b f(x)g(x) \,dx $$
> As, it is
> 1. **Positive Definite**
> $$\left< f,f \right> = \int_{a}^b \left( f(x) \right)^{2} \, dx \ge 0$$
>    as $\left( f(x) \right)^2 \ge 0$ for all $x \in \R$ (and $[a,b] \subseteq\R$), and the [[Integration by First Principals|integral]] of a non-negative [[Functions|function]] is non-negative.
>    
>    Further, $\left< f,f \right> = \int_{a}^b \left( f(x) \right)^{2} \, dx = 0$ iff $f(x) = 0$.
> 2. **Symmetric**
> $$\begin{align}
> 	\left< f,g \right> &= \int_{a}^b f(x)g(x) \, dx \\
> 	&= \int_{a}^b g(x)f(x) \, dx = \left< g,f \right> 
> \end{align}$$
> 3. **Linear**
>    If $c,d \in \R$, then
> $$\begin{align}
> 	\left< cf + dg, h \right> &= \int_{a}^b \left( cf(x) + dg(x) \right)h(x) \, dx \\
> 	&= \int_{a}^b cf(x)h(x) \, dx + \int_{a}^b dg(x)h(x) \, dx \\
> 	&= c\int_{a}^b f(x)h(x) \, dx + d\int_{a}^b g(x)h(x) \, dx \\
> 	&= c\left< f,h \right>  + d\left< g,h \right>  \\
> \end{align}$$

[^1]: [[Definition of Continuity]]
