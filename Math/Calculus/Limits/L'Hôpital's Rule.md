---
tags:
  - atom
  - math
---
L'Hôpital's rule is used to evaluate [[Indeterminate Forms|indeterminate forms]] of types $\dfrac{0}{0}$ and $\dfrac{\infty}{\infty}$. If on an open interval containing $a$ (except possibly at $a$), $g'(x) \ne 0$ and $f$ and $g$ are differentiable, then if
$$\begin{array}{lcl}
	\displaystyle\lim_{x\to a} f(x) = 0 &\text{and}& \displaystyle\lim_{x\to a} g(x) = 0 \\
	&\text{or}&\\
	\displaystyle\lim_{x\to a} f(x) = \pm\infty &\text{and}& \displaystyle\lim_{x\to a} g(x) = \pm\infty \\
\end{array}
$$
then
$$ \lim_{x\to a} \dfrac{f(x)}{g(x)} = \lim_{x\to a} \dfrac{f'(x)}{g'(x)} $$
> [!formal definition]-
> $$\begin{array}{l}
> 	\left( \exists \varepsilon > 0 : \forall x \in (a-\varepsilon,0)\cup(0,a+\varepsilon), g'(x) \ne 0 \right) \,\land \\
> 	f,g \text{ are differentiable} \land \lim_{x\to a} f(x) = \lim_{x\to a} g(x) \in \{0, \pm \infty\} \\
> 	\implies \lim_{x\to a} \dfrac{f(x)}{g(x)} = \lim_{x\to a} \dfrac{f'(x)}{g'(x)}
> \end{array}$$