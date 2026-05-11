---
tags:
  - atom
  - math
---
An [[Integral Domains|integral domain]] $D$ is a *unique factorisation domain* iff
- every non-zero, non-[[Rings#^unit|unit]] element in $D$ can be factored into a finite number of [[Reduciblity|irreducible factors]].
- if $p_{1},p_{2},\dots,p_{n} = q_{1},q_{2},\dots q_{m}$ where the $p_{i}$'s and $q_{j}$'s are [[Reduciblity#^negation|irreducible]] elements of $D$, then $m = n$, and after renumbering the $q_{j}$'s, you get $p_{i} = u_{i}q_{i}$ for some [[Rings#^unit|unit]] $u_{i} \in D$.

> [!examples] $\F[x]$[^1], $\Z$, and $\Z_{p}[x]$
^examples

[^1]: [[Polynomial Rings]] and [[Fields]]

# Polynomials
 [[Polynomials|Polynomial rings]] over a [[Fields|field]] $\F[x]$ are *unique factorisation domains*, meaning
- every non-zero non-[[Rings#^unit|unit]] can be written in the form $p_{1},p_{2},\dots,p_{n}$, where the $p_{i}$'s are [[Reduciblity#^negation|irreducible factors]] of positive [[Polynomials#Degree|degree]] and
- if $p_{1},p_{2},\dots,p_{n} = q_{1},q_{2},\dots q_{m}$ where the $p_{i}$'s and $q_{j}$'s are [[Reduciblity#^negation|irreducible factors]] of $R$ of positive [[Polynomials#Degree|degree]], then $m = n$, and after renumbering the $s_{j}$'s, you have $p_{i}(x) = cq_{i}(x)$.

> [!proof]- Existence
> By [[Strong Induction|strong induction]] on the [[Polynomials#Degree|degree]],
> **Base Case**
> Suppose $\deg f = 1$. Then $f(x) = c(x-a)$ for some $a,c \in \F$, so $f$ is [[Reduciblity#^negation|irreducible]] by [[Reduciblity#^field-units-are-constant|this lemma]].
> 
> **Induction Step**
> Let $k \in \N_{>1}$ be given. Suppose every [[Polynomial Rings|polynomial]] of [[Polynomials#Degree|degree]] strictly less than $k$ can be factored into [[Reduciblity#^negation|irreducible factors]]. Let $f \in \F[x]$ be any [[Polynomial Rings|polynomial ring]] of [[Polynomials#Degree|degree]] $k$.
> 
> If $f$ is [[Reduciblity#^negation|irreducible]], then we are done.
> If $f$ is [[Reduciblity|reducible]], $f(x) = g(x)h(x)$ for some $0 < \deg g < \deg h < \deg f = k$.
> 
> By our induction hypothesis, we can factor g and h into [[Reduciblity#^negation|irreducible factors]], so we can also factor $f$.

> [!proof]- Uniqueness
> By induction on the [[Polynomials#Degree|degree]],
> **Base Case**
> Suppose $\deg f = 1$. We can write
> $$f(x) = p_{1}(x)\cdots p_{k}(x).$$
> with $\deg p_{i} > 0$ and [[Reduciblity#^negation|irreducible]].
> We must then have $k = 1$ and $\deg p_{1} = 1$, so we have
> $$f(x) = p_{1}(x)$$
> **Base Case**
> Suppose $k = \deg f > 1$, and all assume the uniqueness of factorisation of all [[Polynomial Rings|polynomials]] of [[Polynomials#Degree|degree]] strictly less than $k$. Factor $f$ as
> $$f(x) = p_{1}(x)\cdots p_{k}(x) = q_{1}(x)\cdots q_{l}(x).$$
> Note $p_{1} | \Pi q_{i}$, so by [[Euclid's Lemma|Euclid's lemma]], $p_{1} | q_{j}$ for some $j$.
> Since $q_{j}$ is [[Reduciblity#^negation|irreducible]], we have $\deg p_{1} = \deg q_{j}$, so $p_{1}(x) = cq_{j}(x)$ for some $c \in \F$.
> 
> Removing $p_{1}$ and $q_{j}$ then gives a [[Polynomial Rings|polynomial]] of [[Polynomials#Degree|degree]] $k-1$, which then has a unique factorisation. Thus, $p_{1},\dots,p_{k}$ is completely determined (up till constant coefficients) by $q_{1},\dots,q_{l}$.
