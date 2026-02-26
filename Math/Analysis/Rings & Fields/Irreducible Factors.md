---
tags:
  - atom
  - math
---
Let $D$ be an [[Integral Domains|integral domain]]. A [[Polynomial Rings|polynomial]] $f \in D[x]$ that is non-zero or a [[Rings#^unit|unit]] is called a *irreducible factor* iff
$$\forall g,h \in D[x], (f = gh \to g \text{ or } h \text{ are units}),$$

> [!definition]- *(Reducible)* $\exists g,h \in D[x], f = gh \land g \text{ and } h \text{ aren't units}$
> i.e. iff it is given by two non-unit factors.
^negation

> [!example]- $f(x) = 3x^2 - 6$
> $$\begin{array}{rl}
> 	\R: & f(x) = 3\left( x-\sqrt{ 2 } \right)\left( x+\sqrt{ 2 } \right) \to \text{reducible} \\
> 	\Q :& f(x) = 3\left( x^2 - 2 \right) \to \text{irreducible} \\
> 	\Z :& f(x) = 3\left( x^2 - 2 \right) \to \text{reducible} \\
> 	\Z_{5} :& f(x) = 3\left( x^2 - 2 \right) \to \text{irreducible} \\
> 	\Z_{7} :& f(x) = 3\left( x - 3 \right)(x+3) \to \text{reducible} \\
> \end{array}$$

[!theorem]- *(Reducibility Test)* If $f \in \F[x]$[^1] is of [[Polynomials#Degree|degree]] $2$ or $3$, then $f$ is *reducible* over $\F$ iff $f$ has a root in $\F$.
$f$ has a root $a$ $\iff$ $\exists g \in \F[x] : f(x) = (x-a)g(x)$
If $f$ is *reducible*, $f = gh$, and $\deg g + \deg h = \deg f$.
#TODO

[^1]: [[Fields]]
