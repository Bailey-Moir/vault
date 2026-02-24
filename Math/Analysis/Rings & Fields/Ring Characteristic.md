---
tags:
  - atom
  - math
---
The *characteristics* of a [[Rings|ring]] $R$ is defined to be
$$\char R  = \min\{ n \in \Z^+ : \forall a \in R, na = 0 \},$$
and if no such integer exists, we say that $\char R = 0$.

> [!example]- $\char \Z_{n} \oplus \Z_{m} = \lcm(n,m)$[^1][^2]
> For $\left( a,b \right) \in \Z_{n} \oplus \Z_{m}$, we have
> $$\begin{align}
> 	\lcm (n,m) \times (n,m) &= (n\lcm(n,m), m\lcm(n,m)) \\
> 	&= (0, 0). \\
> \end{align}$$
> If $\char \Z_{n} \oplus \Z_{m} < \lcm (n,m)$, then it is not a [[Divisibility|multiple]] of $n$ or $m$, meaning $n \char \Z_{n} \oplus \Z_{m} \ne 0$ or $m \char \Z_{n} \oplus \Z_{m} \ne 0$ by the definition of [[Congruence|congruence]].

> [!theorem]- Let $R$ be a [[Rings|ring]] with [[Rings#^unity|unity]]. Then$$\char R = \begin{cases} \left| 1 \right|  & \left| 1 \right| \text{is finite}  \\ 0 & \left| 1 \right| \text{ is infinite} \end{cases}$$where $\left| 1 \right|$ is the [[Order in Groups|order]] of $1$ under addition.
> By definition, $n = \left| 1 \right|$[^3] is the smallest positive integer such that $n1 = 0$ (if one exists, otherwise it will be infinite).
> 
> This gives that $n1a = na = 0a = 0$, meaning $n$ is a member of the [[Sets|set]] that $\char R$ is the minimum of.
> 
> It must be the minimum of that set, as it is the minimum value that gives the case when $a = 0$.
^unity-gives-order-of-1

> [!theorem]- The *characteristic* of an [[Integral Domains|integral domain]] is either $0$ or [[Primes|prime]].
> Let $R$ be an [[Integral Domains|integral domain]] with $\char R = n$.
> If $n = 0$, then we are done.
> 
> Otherwise, $n \ge 1$. Suppose $n$ is [[Primes#Composite Numbers|composite]]. Then we can write
> $$n = ab \quad \text{s.t.} \quad 1 \le a \le b < n$$
> Then since $n1 = 0$, $ab = 0$, but $a$ and $b$ are non-zero, because this would violate the minimality of $n$.
> This [[Contradictions|contradicts]] the fact that $R$ has no [[Zero-divisors|zero-divisors]] (as it is an [[Integral Domains|integral domain]]).
^integral-domains

[^1]: [[Direct Sums of Rings]]
[^2]: [[Lowest Common Multiple]]
[^3]: [[Order in Groups]]
