---
tags:
  - atom
  - math
---
If $\alpha$ is [[Algebraic Elements#^transcendetal|transcendetal]] over $F$,
$$F(\alpha) \cong F(x) = \left\{ \dfrac{p(x)}{q(x)} : p,q \in F[x] \land q(x) \ne 0 \right\}. $$
If $\alpha$ is [[Algebraic Elements|algebraic]] over $F$, then
$$F(\alpha) \cong F[x] / \left< p(x) \right>, $$
where $p(x)$ is a non-zero [[Polynomial Rings|polynomial]] in $F[x]$ of [[Maximal vs. Maximum|minimum]] [[Polynomials#Degree|degree]] such that $p(\alpha)$.

Further, $p(x)$ is [[Reduciblity#^negation|irreducible]] over $F$ and there is a unique [[Polynomial Rings#^monic|monic]] [[Reduciblity#^negation|irreducible]] [[Polynomial Rings|polynomial]] $p(x) \in F[x]$ such that $p(\alpha) = 0$.

> [!definition] This [[Polynomial Rings|polynimial]] $p(x)$ is called the **minimal polynomial** for $\alpha$ over $F$.
^minimal-polynomial

> [!proof]-
> Consider $\varphi:F[x] \to F(\alpha)$ defined by $f(x) \mapsto f(\alpha)$. Either
> 1. $\alpha$ is [[Algebraic Elements|algebraic]], meaning it is a root of some non-zero [[Polynomial Rings|polynomial]] of $F[x]$, so $\ker \varphi \ne \{ 0 \}$. Because $F(\alpha)$ is a [[Fields|field]], we get that $\ker \varphi$ is [[Maximal Ideals|maximal]]. ( #TODO huh why? ).
>    Thus $F[x] / \ker \varphi$ is a [[Fields|field]], and
> $$ F[x] / \ker \varphi \cong \varphi(F[x]) \subseteq F(\alpha) $$
>    $F \subseteq \varphi(F[x])$ because for all $c \in F$, $\varphi(c) = c$. $\alpha \in \varphi(F[x])$ because $\varphi(x) = \alpha$. Thus,
> $$ F[x] / \ker \varphi \cong F(\alpha), $$
>    and $\ker \varphi = \left< p(x) \right>$ by some theorem #TODO
> 2. If $\alpha$ is [[Algebraic Elements#^transcendetal|transcendetal]].