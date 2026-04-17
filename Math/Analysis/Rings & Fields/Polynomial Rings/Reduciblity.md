---
tags:
  - atom
  - math
---
Let $D$ be an [[Integral Domains|integral domain]]. A element $r \in D$ that is non-zero is called *reducible* iff
$$\exists s,t \in D \setminus D^\times : r = st$$
i.e. iff it is given by two non-[[Rings#^unit|units]] factors.

> [!definition] *(Irreducible)* $\forall s,t \in D, (r = st \to s\in D^\times \lor t \in D^\times).$
^negation
# Polynomials
> [!example]- $f(x) = 3x^2 - 6$
> $$\begin{array}{rl}
> 	\R: & f(x) = 3\left( x-\sqrt{ 2 } \right)\left( x+\sqrt{ 2 } \right) \to \text{reducible} \\
> 	\Q :& f(x) = 3\left( x^2 - 2 \right) \to \text{irreducible} \\
> 	\Z :& f(x) = 3\left( x^2 - 2 \right) \to \text{reducible} \\
> 	\Z_{5} :& f(x) = 3\left( x^2 - 2 \right) \to \text{irreducible} \\
> 	\Z_{7} :& f(x) = 3\left( x - 3 \right)(x+3) \to \text{reducible} \\
> \end{array}$$

> [!lemma]- *(1)* $f \in \F[x]$ is a [[Rings#^unit|unit]] iff it is a non-zero constant.
> $\left( \implies \right)$
> Suppose $f \in \F[x]$ is a [[Rings#^unit|unit]].
> Then there exists $f^{-1} \in \F[x]$ such that
> $$\begin{align}
> 	1 &=  f(x) \times f^{-1}(x) \\
> 	&= \sum_{i = 0}^n a_{i}x^i \times \sum_{i = 0}^m b_{i}x^i  \\
> 	&= \sum_{i = 0}^n \sum_{j=0}^m a_{i}b_{j}x^{i+j}. \\
> \end{align}$$
> Thus, the coefficient of $x^0$ must be $1$ and all other coefficients must be $0$.
> This gives $a_{0}b_{0} = 1$, and for $i>0$ or $j > 0$, $a_{i}b_{j} = 0$.
> Without loss of generality, suppose $i=0$. This gives $\forall j > 0, a_{0}b_{j} = 0$, and since [[Fields|fields]] don't have [[Zero-divisors|zero-divisors]], $b_{j} = 0$. Similarly, $a_{j} = 0$.
> $a_{0} \ne 0$, as $1 = a_{0}b_{0} = 0b_0 = 0$ is a [[Contradictions|contradiction]].
> Thus, $f(x) = a_{0}$, meaning $f$ is non-zero constant.
> 
> $\left( \impliedby \right)$
> Let $f \in \F[x]$ such that $f(x) = c \ne 0$.
> Let $f^{-1} \in \F[x] = f^{-1}(x) = c^{-1}$ (which must exist as this is a [[Fields|field]]).
> Then $f(x) \times f^{-1}(x) = c\times c^{-1} = 1$.
> Thus, $f^{-1}$ is the [[Groups#^inverse|inverse]] of $f$, meaning $f$ is a [[Rings#^unit|unit]].
^field-units-are-constant

> [!theorem]- *(Reducibility Test)* If $f \in \F[x]$[^1] is of [[Polynomials#Degree|degree]] $2$ or $3$, then $f$ is *reducible* over $\F$ iff $f$ has a root in $\F$.
> $\left( \implies \right)$
> Suppose $f \in \F[x]$ is *reducible*, and $\deg f \in \{ 2,3 \}$.
> Then by definition, there exists $g,h \in \F[x]$ that aren't [[Rings#^unit|units]] such that $f = gh$. Thus, both have [[Polynomials#Degree|degree]] larger than $0$, and $\deg f = \deg g + \deg h$. This implies that $g$ or $h$ has [[Polynomials#Degree|degree]] $1$, so by the definition of roots, gives a root of $f$.
> 
> $\left( \impliedby \right)$
> Suppose $f \in \F[x]$ has a root $a \in \F$, and $\deg f > 1$.
> Then there exists $g \in \F[x]$ such that $f(x) = (x-a)g(x)$ by [[Division Algorithm#^remainder-theorem|remainder theorem]].
> Thus, $\deg g = \deg f - 1 > 0$.
> Since $x-a$ and $g$ are non-constant, they are not [[Rings#^unit|units]] by [[#^units-are-constant|lemma 1]].
Thus, $f$ is *reducible*.

> [!theorem] $f$ is *reducible* over $\Q$ $\to$ $f$ is *reducible* over $\Z$
^rational-reducible-implies-integer-reducible

\[[[Polynomial Rings]]\]

[^1]: [[Fields]]
