---
tags:
  - atom
  - math
  - discrete
---
Let $G$ be a [[Cyclic Groups|cyclic group]] with [[Group Generators|generator]] $g$. Then for all $m \in \Z$,
$$\left| g^m \right| = \dfrac{\left| g \right|}{\gcd(m,\left| g \right| )}$$

> [!proof]-
> Let $G$ be a [[Cyclic Groups|cyclic group]] with [[Group Generators|generator]] $g$, and $m \in \Z$.
> 
> Since $g^\left| g \right| = e$ and $\left( g^m \right)^{\left| g^{m} \right|} = g^{m\left| g^{m} \right|} = e$,
> $$\begin{align}
> 	& \left| g \right| \: {\big|}\; m\left| g^m \right| \\
> 	\iff& m\left| g^m \right| = k\left| g \right| && k \in \Z  \\
> 	\iff& \left| g^m \right| =  \dfrac{k\left| g \right|}{m} \\
> \end{align}.$$
> $\left| g^m \right|$ must be the **smallest positive integer** satisfying this equation, and since $k$ is the only free variable, it must be chosen to be the smallest value such that $\frac{k\left| g \right|}{m} \in \Z^+$.
> 
> Thus, $k$ must be greatest divisor of $m$ without its common factors with $\left| g \right|$, meaning
> $$k = \dfrac{m}{\gcd(m,\left| g \right| )}.$$
> Thus,
> $$\left| g^m \right| = \dfrac{\left| g \right|}{\gcd(m,\left| g \right| )}$$