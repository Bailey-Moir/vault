---
tags:
  - atom
  - math
---
$$\displaystyle \lim_{x\to\pm\infty} \dfrac{P(x)}{Q(x)} = \lim_{x\to\pm\infty} \dfrac{\dfrac{P(x)}{x^n}}{\dfrac{Q(x)}{x^n}} \ni n \text{ is the order of } Q$$
<center><b>This only works at infinity</b></center>

If you have the limit of a [[Types of Functions|rational function]] at infinity, then dividing the numerator and denominator by the limit variable with an order of that of the denominator, using [[Limit Laws|limit laws]] to isolate the terms in the fraction will result in most terms being in the form $\displaystyle\lim_{x\to\pm\infty} \dfrac{a}{x^b}$ which evaluate to 0 (see [[Limit Laws|limit law 6]], this is why this only works at infinity).

> [!example]-
> $$\begin{align*}
> 	\lim_{x\to\pm\infty} \dfrac{x^3 - 2x^2 + 10x - 1}{5x^2 + 1} &= \lim_{x\to\pm\infty} \dfrac{x - 2 + \dfrac{10}{x} - \dfrac{1}{x^2}}{5 + \dfrac{1}{x^2}} \\
> 	&= \dfrac{\displaystyle\lim_{x\to\pm\infty} \left( x - 2 + \dfrac{10}{x} - \dfrac{1}{x^2} \right) }{\displaystyle\lim_{x\to\pm\infty} \left( 5 + \dfrac{1}{x^2} \right) } \\
> 	&= \dfrac{\displaystyle \lim_{x\to\pm\infty} \left(x\right) - \lim_{x\to\pm\infty} \left(2\right) + \lim_{x\to\pm\infty} \left(\dfrac{10}{x}\right) - \lim_{x\to\pm\infty} \left(\dfrac{1}{x^2}\right) }{\displaystyle \lim_{x\to\pm\infty} \left(5\right) + \lim_{x\to\pm\infty} \left(\dfrac{1}{x^2}\right) } \\
> 	&= \dfrac{\displaystyle \lim_{x\to\pm\infty} \left(x\right) - 2 }{5} \\
> 	&= \pm\infty
> \end{align*}$$