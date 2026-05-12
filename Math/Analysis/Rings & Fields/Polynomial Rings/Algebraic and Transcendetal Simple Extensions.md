---
tags:
  - atom
  - math
---
If $\alpha$ is [[Algebraic Elements#^transcendetal|transcendetal]] over $F$,
$$F(\alpha) \cong F(x) = \left\{ \dfrac{p(x)}{q(x)} : p,q \in F[x] \land q(x) \ne 0 \right\}. $$
If $\alpha$ is [[Algebraic Elements|algebraic]] over $F$, then
$$F(\alpha) \cong F[x] / \left< p(x) \right>, $$
where $p(x)$ is a non-zero [[Polynomial Rings|polynomial]] in $F[x]$ of [[Maximal vs. Maximum|minimum]] [[Polynomials#Degree|degree]] such that $p(\alpha) = 0$.

Further, $p(x)$ is [[Reduciblity#^negation|irreducible]] over $F$ and there is a unique [[Polynomial Rings#^monic|monic]] [[Reduciblity#^negation|irreducible]] [[Polynomial Rings|polynomial]] $p \in F[x]$ such that $p(\alpha) = 0$.

> [!definition] This [[Polynomial Rings|polynimial]] $p(x)$ is called the **minimal polynomial** for $\alpha$ over $F$.
^minimal-polynomial

> [!proof]-
> Consider $\varphi:F[x] \to F(\alpha)$ defined by $f(x) \mapsto f(\alpha)$. Either
> 
> **(Algebraic)**
> Suppose $\alpha$ is [[Algebraic Elements|algebraic]] over $F$, meaning $f(\alpha) = 0$ for some non-zero [[Polynomial Rings|polynomial]] $f \in F[x]$.
> 
> Suppose $f(x)$ was [[Reduciblity|reducible]]. Then there exists non-[[Fields#^units|units]] $g,h \in F[x]$ such that
> $$\begin{align}
> 	f(x) &= g(x) h(x) \\
> 	f(\alpha) = 0 &= g(\alpha) h(\alpha). \\
> \end{align}$$
> $F[x]$ has no [[Zero-divisors|zero-divisors]][^1], so $g(\alpha) = 0$. Repeating this process decreases the [[Polynomials#Degree|degree]], until eventually $\deg g = \deg h = 0$, [[Contradictions|contradicting]] $g$ and $h$ being non-[[Rings#^unit|units]].
> 
> Thus, there exists an [[Reduciblity#^negation|irreducible]] $p \in F[x]$ such that $p(\alpha) = 0$. Note $p$ is non-zero as $f$ is non-zero and $p|f$.
> 
> Then $p \in \ker \varphi$, meaning the [[Maximal Ideals|maximal ideal]][^2] $\left< p \right> \subseteq \ker \varphi$.
> For any non-zero constant $c \in F$, $\varphi(c) = c \ne 0$, so $\ker \varphi \ne \varphi(F[x])$, meaning
> $$\ker \varphi = \left< p \right>.$$
> 
> $F \subseteq \varphi(F[x])$ because for all $c \in F$, $\varphi(c) = c$. $\alpha \in \varphi(F[x])$ because $\varphi(x) = \alpha$. Thus,
> $$\varphi(F[x]) =  F(\alpha).$$
> Together, by [[First Isomorphism Theorem for Rings|first isomorphism theorem]],
> $$F(\alpha) \cong F[x] / p(x),$$
> where $p(x) \in F[x]$ is a non-zero [[Polynomial Rings|polynomial]] in $F[x]$ of [[Maximal vs. Maximum|minimal]] [[Polynomials#Degree|degree]] such that $p(\alpha) = 0$. Further, $p$ is [[Reduciblity#^negation|irreducible]] over $F$.
> 
> #TODO Unique monic irreducible.
> 
> **(Transcendetal)**
> Suppose $\alpha$ is [[Algebraic Elements#^transcendetal|transcendetal]] over $F$. Chat I have no clue. #TODO


[^1]: [[Polynomial Rings#^integral-domains]]

[^2]: [[Maximal Ideals#^polynomials]]
