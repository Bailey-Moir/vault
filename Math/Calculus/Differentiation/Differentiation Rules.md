---
tags:
  - atom
  - math
---
# Product Rule
$$ (uv)' = u'v+v'u $$
> [!proof]-
> $$\begin{align}
> 	(fg)'(x) &= \lim_{ h \to 0 } \dfrac{f(x+h)g(x+h) - f(x)g(x)}{h} \\
> 	&= \lim_{ h \to 0 } \dfrac{\left[ f(x+h)-f(x) \right]g(x+h) - f(x)\left[g(x) - g(x+h)\right]}{h} \\
> 	&= \lim_{ h \to 0 } \left[ \dfrac{f(x+h)-f(x)}{h} g(x+h) + f(x) \dfrac{g(x+h) - g(x)}{h} \right] \\
> 	&= f'(x)g(x)+f(x)g'(x) \\
> 	&= (f'g+fg')(x) \\
> \end{align}$$
# Chain Rule Rule
$$\dfrac{dy}{dx} = \dfrac{dy}{du}\dfrac{du}{dx}$$
# Quotient Rule
$$ \left( \dfrac{u}{v} \right)' = \dfrac{u'v - uv'}{v^2} $$