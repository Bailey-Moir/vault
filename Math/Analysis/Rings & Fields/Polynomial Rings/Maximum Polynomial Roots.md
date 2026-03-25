---
tags:
  - atom
  - math
---
A non-zero [[Polynomials|polynomial]] of [[Polynomials#Degree|degree]] $n$ over a [[Fields|field]] has at most $n$ zeros, counting multiplicity.

> [!proof]-
> **Base Case**
> If $f \in \F[x]$ has [[Polynomials#Degree|degree]] $0$, $f(x) = a \ne 0$, which has no roots.
> 
> **Induction Step**
> Suppose every [[Polynomials|polynomial]] in $\F[x]$ of [[Polynomials#Degree|degree]] $d<k$ has at most $d$ roots.
> 
> Let $f \in \F[x]$ by a [[Polynomials|polynomial]] in $\F[x]$ of [[Polynomials#Degree|degree]] $k$.
> 
> Suppose $a$ is a root of $f$ of multiplicity $m$. We can write
> $$f(x) = (x-a)^m g(x)$$
> for some $g \in \F[x]$.
> 
> Suppose $b \neq a$ is a root of $f$. We then have
> $$\begin{align}
> 	0 &= f(b)  \\
> 	&= \underbrace{(b-a)^m}_{\ne 0} g(b) && (1) \\
> 	\to g(b) &= 0 && (2)
> \end{align}$$
> where $(1)$ is by the [[Groups#^inverse-uniqueness|uniqueness of the additive inverse]], and $(2)$ is by the fact that [[Fields|fields]] have no [[Zero-divisors|zero-divisors]].
> 
> Thus, every root of $f$ other than $a$ is a root of $g$.
> $g$ has at most $\deg g = k - m$ roots by the [[Induction|induction hypothesis]], so $f$ has at most $(k-m) + m = k$ zeros, counting multiplicity.