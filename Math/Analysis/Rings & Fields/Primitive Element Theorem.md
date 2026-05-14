---
tags:
  - atom
  - math
---
Suppose $\char F = 0$[^1] and $\alpha$ and $\beta$ are [[Algebraic Elements|algebraic]] over $F$. Then there is an element $\gamma \in F(\alpha,\beta)$[^2] such that
$$F(\alpha,\beta) = F(\gamma).$$
> [!corollary]- Suppose $\char F = 0$. Then every [[Extension Degree#^finite-and-infinite|finite extension]] of $F$ is a [[Simple Field Extensions|simple extension]] $F(\alpha)$.
> Suppose $\char F = 0$ and $[E:F] = n$.
> Since $E$ is [[Extension Degree#^finite-and-infinite|finite]] over $F$, by [[Extension Degree#^structure-finite|this theorem]], there exists $\alpha_{1},\dots,\alpha_{n}$ such that
> $$E = F(\alpha_{1},\dots,\alpha_{n}) = F(\alpha_{1})(\alpha_{2})\cdots(\alpha_{n}).$$
> [[Extension Degree#^finite-implies-algebraic|Finite extensions are algebraic]], so each $\alpha_{i}$ is [[Algebraic Elements|algebraic]] over $F$. Thus, these can be [[Induction|inductively]] combined using the root theorem, giving $E = F(\alpha)$ for some $\alpha \in E$.

> [!definition] $\alpha \in E$ is called a **primitive element** of $E$ over $F$ iff $E = F(\alpha)$.


[^1]: [[Ring Characteristic]]
[^2]: [[Simple Field Extensions]]