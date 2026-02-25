---
tags:
  - atom
  - math
  - discrete
---
Let $\F$ be a [[Fields|field]] and $f,g \in \F[x]$[^1] with $g \ne 0$. Then there exists **unique** $q,r \in \F[x]$ such that
$$f = qg + r$$
and $\deg r < \deg g$.

> [!definitions] $q$ and $r$ are called the **quotient** and **remainder** respectively.

> [!logical-notation]-
> $$ \forall f \in \F[x], g \in \F[x] \setminus \{ 0 \}, \exists! q,r \in \F[x] : f = qg + r \land \deg r < \deg g. $$

> [!integers]-
> If $a,b \in \Z$ with $b \ne 0$, then there exist **unique** integers $q$ and $r$ such that
> $$ a = qb + r$$
> where $0 \le r < b$
> $$\forall a, b \in \Z \land b > 0, \exists! q,r \in \Z \land 0 \le r < b : a = qb + r$$

> [!corollary]- *(Remainder Theorem)* For all $f \in \F[x]$ and $a \in \F$, then<ol><li>$f(a)$ is the **remainder** of the division of of $f(x)$ by $x-a$, and thus,</li><li>$a$ is a root of $f$ iff $x-a | f(x)$[^2]</li></ol>

The *division algorithm* gives $q,r \in \F[x]$ such that $f = q(x-a) + r$ and $\deg r < \deg (x - a) = 1$, meaning $r$ is constant.
$$\begin{align}
	f(x) &= q(x)(x - a) + r(x) && \forall x \in \F \\
	\to f(a) &= q(a)(a - a) + r(a) \\
	&= q(a)0 + r(a) \\
	&= r(a) && 1 \\
\end{align}$$
Since $r$ is constant, $r(a) = r(x)$. Thus, $f(a)  = r(x)$ $\square_{1}$.

$$\begin{align}
	a \text{ is a root} &\iff r(a) = 0 && \leftarrow 1 \\
	&\iff r = 0 && r \text{ is constant} \\
	&\iff r(a) = 0 \\
\end{align}$$

^remainder-theorem

[^1]: [[Polynomial Rings]]
[^2]: [[Divisibility]]
