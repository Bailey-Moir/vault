---
tags:
  - atom
  - math
---
An [[Subfields#^extension-field|extension field]] $E$ of $F$ is an *algebraic extension* of $F$ iff every element of $E$ is [[Algebraic Elements|algebraic]] over $F$.

> [!definition] Otherwise, $E$ is called a **transcendetal extension** of $F$.
^transcendetal

[!theorem]- *(Transitivity)* if $K$ is an *algebraic extension* of $E$, and $E$ is an *algebraic extension* of $F$, then $K$ is an *algebraic extension* of $F$.

Let $\alpha \in K$. Thus, $\alpha$ is a root of some $f(x) = c_{n}x^n + \dots + c_{1}x + c_{0} \in E[x]$.
Each $c_{i}$ is [[Algebraic Elements|algebraic]] over $F$.
Look at $F_{n} = F(c_{0},\dots,c_{n}) = F(c_{0})\cdots(c_{n})$.
$F_{0} = F$
$F_{i+1} = F_{i}(c_{i + 1})$.
Each $F_{i+1}$ is [[Extension Degree#^finite-and-infinite|finite]] over $F_{i}$, as $c_{i+1}$ is [[Algebraic Elements|algebraic]] over $F$ and thus the [[Subfields#^extension-field|extension field]] $F_{i}$, so #TODO

By the [[Extension Degree#^tower-theorem|tower theorem]], $[F_{n} : F] = \prod_{i}^{n-1} [F_{i+1},F_{i}]$ is then finite, so $F_{n}$ is [[Extension Degree#^finite-and-infinite|finite]] over $F$.

$E_{n}$ is [[Extension Degree#^finite-and-infinite|finite]] over $F$ #TODO huhhhhh

By the [[Extension Degree#^tower-theorem|tower theorem]] again,
$$ [K:F] = [K:F_{n}][F_{n} : F] $$


^transitivity