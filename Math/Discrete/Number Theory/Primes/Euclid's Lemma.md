---
tags:
  - atom
  - math
  - discrete
---
For any [[Unique Factorisation Domain|unique factorisation domain]] $D$,
$$\forall a,b \in D, p \in D^\text{irreducible}, \left( p|ab \leftrightarrow p | a \lor \ p | b \right).$$
> [!proof]- for $\F[x]$[^1]
> Suppose $p|ab$ and $p \nmid a$. Let
> $$G(x) = \gcd(p,A),$$
> meaning $G$ is a [[Polynomial Rings|polynomial]] of maximal [[Polynomials#Degree|degree]] which [[Divisibility|divides]] $p$ and $A$.
> Since $p \nmid A$, $G \ne P$. Since $p$ is also [[Reduciblity#^negation|irreducible]], $\deg G = 0$, so $G(x) = c \in \F$, a [[Rings#^unit|unit]] in $\F[x]$.
> Using the [[Extended Euclidean Algorithm|extended Euclidean algorithm]], we write
> $$\begin{align}
> 	c &= p(x)r(x) + A(x)s(x) \\
> 	B(x) &= c^{-1}\left[ B(x)p(x)r(x) + A(x)B(x)s(x) \right]  \\
> 	&= p(x)\left[ c^{-1}B(x)r(x) + \dfrac{A(x)B(x)}{p(x)}s(x) \right]  \\
> \end{align}$$
# Integers
$$ \forall a,b \in \Z^+, p \in \mathbb{P}, \left( p | ab \iff p|a \lor p|b\right) $$
*Note the backwards implication is obvious, and almost need not be stated.*

> [!proof]-
> Suppose $p|ab$ and $p \nmid a$. Since $p \nmid a$, $\gcd(p,a) = 1$,
> 
> By the [[Extended Euclidean Algorithm|extended Euclidean algorithm]], there exists $r,s \in \Z$ such that
> $$\begin{align}
> 	1 = pr + as \\
> 	b = pbr + abs \\
> 	b = p\left( br + \dfrac{ab}{p}s \right). \\
> \end{align}$$
> This right-hand coefficient is an integer, as $p|ab$, so $p|b....$

\[[[Divisibility]]\]

[^1]: [[Polynomial Rings]] and [[Fields]]