---
tags:
  - atom
  - math
---
$e \in \R\setminus \Q$.

> [!proof] 
> $$e = 1 + \dfrac{1}{1!} + \dfrac{1}{2!} + \dots + \dfrac{1}{n!} + R_{n}(1)$$
> Note that $R_{n}(1) = \dfrac{e^{\xi_{L}}}{(n+1)!} > 0$ for some $\xi_{L} \in \left( 0,1 \right)$, so
> $$0 < R_{n}(1) < \dfrac{3}{\left( n+1 \right)!}.$$
> Assume $e \in \Q$, meaning $e=\dfrac{a}{b}$ for some $a,b\in\N$. Then for all $n >\text{max}\{ b,3 \}$,
> $$\underbrace{n!e}_{\in\Z} = n! \dfrac{a}{b} = \underbrace{n! + \dfrac{n!}{1!}+ \dfrac{n!}{2!} + \dots + \dfrac{n!}{n!}}_{\in\, \Z} + n!R_{n}(1).$$
> Thus, $n!R_{n}(1) \in \Z$, but
> $$0 < n!R_{n}(1) < \dfrac{3n!}{\left( n+1 \right)!} = \dfrac{3}{n+1} < \dfrac{3}{4} < 1.$$
> This is a [[Contradictions|contradiction]], so $e$ is irrational.