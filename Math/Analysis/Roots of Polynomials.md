---
tags:
  - atom
  - math
---
[[Polynomials|Polynomial]] of [[Polynomials#Degree|degree]] $n$ have at most $n$ distinct real roots.

> [!proof]-
> **Base Case**
> When $n = 1$, $p(x) = a_{1}x+a_{0}$, so its only root must be $x = -\dfrac{a_{0}}{a_{1}}$.
> 
> **Induction Step**
> Suppose all [[Polynomials|polynomials]] of [[Polynomials#Degree|degree]] $k-1$ have at most $k-1$ distinct real roots.
> 
> Suppose $p(x) = a_{k}x^k + \dots + a_{1}x+a_{0}$, such that $f(x)$ has more than $k$ roots.
> 
> Note that by the [[Power Rule|power rule]], $p'$ is a [[Polynomials|polynomial]] of [[Polynomials#Degree|degree]] $k-1$, and thus by the [[Induction|induction hypothesis]], $p'$ has at most $k-1$ distinct real roots.
> 
> However, by [[Rolle's Theorem|Rolle's theorem]], since $p$ has more than $k$ distinct real roots, its [[Differentiation|derivative]] must have more than $k-1$ distinct roots, a [[Contradictions|contradiction]].
> 
> Thus, all [[Polynomials|polynomials]] of [[Polynomials#Degree|degree]] $k$ have at most $k$ distinct real roots.