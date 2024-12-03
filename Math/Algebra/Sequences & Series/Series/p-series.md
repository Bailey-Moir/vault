---
tags:
  - atom
  - math
---
A *p-series* is a [[Series|series]] of the form
$$\sum_{n=1}^\infty \dfrac{1}{n^p}$$
This [[Series|series]] converges iff $p>1$ (diverges if $p\le 1$).

> [!proof]-
> If $p < 0$, $\displaystyle\lim_{ n \to \infty } \dfrac{1}{n^p} = \infty$. If $p = 0$, $\displaystyle\lim_{ n \to \infty } \dfrac{1}{n^p} = 1$. In both cases, the limit of the [[Summand|summand]] is not 0, meaning the series diverges. If $p>0$, the [[Functions|function]]
> $$f(x) = \dfrac{1}{x^p}$$
> is a [[Definition of Continuity|continuous]] positive [[Extending Sequences|extension]] of $\left\{ a_{n} \right\}$ into the real numbers.
> $$\begin{align*}
> 	\int_{1}^\infty \dfrac{1}{x^p} \,dx &= \left[ -\dfrac{1}{(p-1)x^{p-1}} \right]_{1}^\infty \\
> 	&= -\dfrac{1}{p-1}\left[ \dfrac{1}{x^{p-1}} \right]_{1}^\infty \\
> 	&= -\dfrac{1}{p-1}\left[ \lim_{x \to \infty} \left( \dfrac{1}{x^{p-1}} \right) - 1 \right] \\
> 	&= -\dfrac{1}{p-1} \lim_{x \to \infty} \left( \dfrac{1}{x^{p-1}} \right) + \dfrac{1}{p-1}\\
> 	&= -\dfrac{1}{p-1} \lim_{x \to \infty} \left( \dfrac{1}{x^{p-1}} \right) + \dfrac{1}{p-1}\\
> \end{align*}$$
> This [[Improper Integrals|improper integral]] converges iff the $\lim_{ x \to \infty } 1/x^{p-1}$ converges. This limit converges iff $p-1>0$[^1] (if $p-1=0$, division by zero occurs). Applying [[The Integral Test|the integral test]], the series
> $$ \sum_{n=1}^\infty \dfrac{1}{n^p} $$
> converges iff $p > 1$, and otherwise diverges.

[^1]: [[Limit Laws]]