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
$$ 
\begin{align*}
	\left( \exists \varepsilon > 0 \ni 0 < |x - a| < \varepsilon \implies g'(x) \ne 0 \land f,g \text{ are differentiable} \right) \land \lim_{x\to a} f(x) = \lim_{x\to a} g&(x) \in \{0, \pm \infty\} \implies \\
	&\lim_{x\to a} \dfrac{f(x)}{g(x)} = \lim_{x\to a} \dfrac{f'(x)}{g'(x)}
\end{align*}$$