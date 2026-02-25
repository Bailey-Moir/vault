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

[^1]: [[Polynomial Rings]]
