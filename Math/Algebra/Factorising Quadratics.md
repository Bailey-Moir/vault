---
tags:
  - atom
  - math
---
$$\huge\begin{array}{c}
	\textbf{Factorize} \\
	ax^2 + bx + c
\end{array}$$
## $a = 1$
Since $\alpha\beta = c$, you can find $\alpha$ and $\beta$ by splitting the factors of $c$ between them. Once you find such a split where $\alpha + \beta = b$, then you have found a valid factorisation:
$$(x-\alpha)(x-\beta).$$

Sometimes, this will not happen, which will be the case when $\alpha$ or $\beta$ are not integers, in which case, you should probably just solve with the quadratic formula.
## $\text{gcd}(a,b,c) \ne 1$
If the [[Greatest Common Divisor|greatest common divisor]] of $a$, $b$, and $c$ is not $1$, then you can factor out their common factor. If this results in $a = 1$, then apply [[#$a = 1$]], otherwise apply [[#The Hard Part]]
## The Hard Part
So $a \ne 1$ and you can't cleanly factor any constants out.

Similar to [[#$a = 1$]], you can find $\alpha$ and $\beta$ by splitting the factors of $ac$ between them.


> [!note]- $ac$ trick
> $$\begin{array}{c}
> 	x^* = \alpha,\beta \longleftrightarrow {x^*}^2 + bx^* + ca = 0 \\
> 	\huge\Updownarrow \\
> 	x = \dfrac{\alpha}{a}, \dfrac{\beta}{a} \longleftrightarrow ax^2 + bx + c = 0 \\
> \end{array}$$
> 
> > [!example] $4x^2 - 19x - 5 = 0$
> > $$\begin{align}
> > 	{x^*}^2 - 19x^* - 20 &= 0 \\
> > 	\left(x^* - 20\right)\left(x^* + 1\right) &= 0 \\
> > 	\left(x - \dfrac{20}{4}\right)\left( x + \dfrac{1}{4} \right) &= 0 \\
> > 	\left(x - 5\right)\left(4x + 1\right) &= 0 \\
> > \end{align}$$