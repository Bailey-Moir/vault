---
tags:
  - atom
  - math
---
From the cosine definition of the [[Dot Product|dot product]], it can be shown that if $\theta$ is the angle between two non-zero vectors $\vecbf{a}$ and $\vecbf{b}$, then:
$$ \cos \theta = \dfrac{\vecbf{a} \cdot \vecbf{b}}{\|\vecbf{a}\|\,\|\vecbf{b}\|} $$
> [!proof]- with Cosine Rule
> Using the [[Cosine Rule|cosine rule]],
> $$\begin{array}{rcl}
> 	c^2 = a^2 + b^2 - 2ab\cos\theta &&
> 	\cos \theta = \dfrac{a^2 + b^2 - c^2}{2ab}
> \end{array}$$
> applying this to vector geometry gives
> $$\begin{align*}
> 	\cos \theta &= \dfrac{\|\vecbf x\|^2 + \|\vecbf y\|^2 - \|\vecbf x - \vecbf y\|^2}{2\|\vecbf x\|\|\vecbf y\|} \\
> 	&= \dfrac{\vecbf x\cdot\vecbf x + \vecbf y\cdot\vecbf y - (\vecbf x - \vecbf y)\cdot(\vecbf x - \vecbf y)}{2(\vecbf x\cdot\vecbf x) \times (\vecbf y\cdot\vecbf y)} \\
> 	&= \dfrac{\vecbf x\cdot\vecbf x + \vecbf y\cdot\vecbf y - \left( \vecbf x\cdot\vecbf x - 2\vecbf x\cdot\vecbf y + \vecbf y\cdot\vecbf y\right)}{2(\vecbf x\cdot\vecbf x)(\vecbf y\cdot\vecbf y)} \\
> 	&= \dfrac{2\vecbf x\cdot\vecbf y}{2(\vecbf x\cdot\vecbf x)(\vecbf y\cdot\vecbf y)} \\
> 	&= \dfrac{\vecbf x\cdot\vecbf y}{\| \vecbf x \| \| \vecbf y \|} \\
> \end{align*}$$
> \[[[Vector Length]], [[Dot Product#Properties of Dot Product]]\]