---
tags:
  - atom
  - math
---
From the cosine definition of the [[Dot Product|dot product]], it can be shown that if $\theta$ is the angle between two non-zero vectors $\vecbf{u}$ and $\vecbf{v}$, then:
$$ \cos \theta = \dfrac{\vecbf{u} \cdot \vecbf{v}}{\|\vecbf{u}\|\,\|\vecbf{v}\|} $$
> [!proof]- with Cosine Rule
> Using the [[Cosine Rule|cosine rule]],
> $$\begin{array}{rcl}
> 	c^2 = a^2 + b^2 - 2ab\cos\theta &&
> 	\cos \theta = \dfrac{a^2 + b^2 - c^2}{2ab}
> \end{array}$$
> applying this to vector geometry gives
> $$\begin{align*}
> 	\cos \theta &= \dfrac{\|\vecbf u\|^2 + \|\vecbf v\|^2 - \|\vecbf u - \vecbf v\|^2}{2\|\vecbf u\|\|\vecbf v\|} \\
> 	&= \dfrac{\vecbf u\cdot\vecbf u + \vecbf v\cdot\vecbf v - (\vecbf u - \vecbf v)\cdot(\vecbf u - \vecbf v)}{2\|\vecbf u\|\|\vecbf v\|} \\
> 	&= \dfrac{\vecbf u\cdot\vecbf u + \vecbf v\cdot\vecbf v - \left( \vecbf u\cdot\vecbf u - 2\vecbf u\cdot\vecbf v + \vecbf v\cdot\vecbf v\right)}{2\|\vecbf u\|\|\vecbf v\|} \\
> 	&= \dfrac{2\vecbf u\cdot\vecbf v}{2\|\vecbf u\|\|\vecbf v\|} \\
> 	&= \dfrac{\vecbf u\cdot\vecbf v}{\| \vecbf u \| \| \vecbf v \|} \\
> \end{align*}$$
> \[[[Vector Length]], [[Dot Product#Properties of Dot Product]]\]