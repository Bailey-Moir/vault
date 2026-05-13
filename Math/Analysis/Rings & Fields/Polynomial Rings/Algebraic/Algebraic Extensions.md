---
tags:
  - atom
  - math
---
An [[Subfields#^extension-field|extension field]] $E$ of $F$ is an *algebraic extension* of $F$ iff every element of $E$ is [[Algebraic Elements|algebraic]] over $F$.

> [!definition] Otherwise, $E$ is called a **transcendetal extension** of $F$.
^transcendetal

> [!theorem]- *(Transitivity)* if $K$ is an *algebraic extension* of $E$, and $E$ is an *algebraic extension* of $F$, then $K$ is an *algebraic extension* of $F$.
> 
> Let $\alpha \in K$. Thus, $\alpha$ is a root of some $f(x) = c_{n}x^n + \dots + c_{1}x + c_{0} \in E[x]$.
> 
> [[Induction|Inductively]] define $F_{n}$ by $F_{-1} = F$ and $F_{k+1} = F_{k}(c_{k + 1})$.
> Each $F_{i+1}$ is [[Extension Degree#^finite-and-infinite|finite]] over $F_{i}$, as $c_{i+1}$ is [[Algebraic Elements|algebraic]] over $F$ and thus the [[Subfields#^extension-field|extension field]] $F_{i}$.
> By the [[Extension Degree#^tower-theorem|tower theorem]], $[F_{n} : F] = \prod_{i}^{n-1} [F_{i+1},F_{i}] < \infty$, so $F_{n}$ is [[Extension Degree#^finite-and-infinite|finite]] over $F$.
> 
> $f(x) \in F_{n}$, so $\alpha$ is [[Algebraic Elements|algebraic]] over $F_{n}$, meaning $F_{n}(\alpha)$ is a [[Extension Degree#^finite-and-infinite|finite]] extension of $F_{n}$[^1]. By the [[Extension Degree#^tower-theorem|tower theorem]],
> $$\left[ F_{n}(\alpha):F \right]  = \left[ F_{n}(\alpha):F_{n} \right]\left[ F_{n} : F \right] < \infty.  $$
> Thus, $F_{n}(\alpha)$ is [[Extension Degree#^finite-and-infinite|finite]] and thus [[Algebraic Extensions|algebraic]] over $F$[^2], meaning $\alpha$ is [[Algebraic Elements|algebraic]] over $F$.
> 
> Thus, every $\alpha \in K$ is [[Algebraic Elements|algebraic]] over $F$, meaning $K$ is an [[Algebraic Extensions|algebraic extension]] of $F$.
^transitivity

[^1]: [[Extension Degree#^simple-extensions]]
[^2]: [[Extension Degree#^finite-implies-algebraic]]