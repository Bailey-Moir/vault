---
tags:
  - atom
  - math
---
$$ \sum_{k=1}^\infty \dfrac{1}{k} = 1 + \dfrac{1}{2} + \dfrac{1}{3} + \dfrac{1}{4}+ \cdots $$
The *harmonic series* is a [[p-series]] with $p=1$, and thus [[Partial Sums|diverges]].

> [!proof]- by [[Bounded Sequences|Boundedness]]
> $$\begin{align}
> 	S_{2^n} &= 1 + \dfrac{1}{2} + \dfrac{1}{3} + \dfrac{1}{4} + \cdots \\
> 	&= 1 && = 1\\
> 	&+\dfrac{1}{2} && = \dfrac{1}{2} \\
> 	&+\dfrac{1}{3} + \dfrac{1}{4} && \ge \dfrac{1}{2} \\
> 	&+\dfrac{1}{5} + \dfrac{1}{6} + \dfrac{1}{7} + \dfrac{1}{8} && \ge \dfrac{1}{2} \\
> 	&+\dfrac{1}{9} + \dfrac{1}{10} + \cdots + \dfrac{1}{16} && \ge \dfrac{1}{2} \\
> 	&\vdots \\
> 	&+\dfrac{1}{2^{n-1}+1} + \dfrac{1}{2^{n-1}+2} + \cdots + \dfrac{1}{2^n} && \ge \dfrac{1}{2} \\
> 	&\ge 1 + \dfrac{n}{2}.\\
> \end{align}$$
> 