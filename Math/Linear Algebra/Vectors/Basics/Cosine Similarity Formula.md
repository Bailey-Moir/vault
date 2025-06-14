---
tags:
  - atom
  - math
  - linear
---
For any [[Inner Products|inner product space]] $V$ and $\vecbf{u},\vecbf{v} \in V$,
$$ \cos \theta = \dfrac{\left< \vecbf{u},\vecbf{v} \right> }{\|\vecbf{u}\|\,\|\vecbf{v}\|} $$

> [!proof]- with Cosine Rule
> Applying the [[Cosine Rule|cosine rule]]
> $$\begin{array}{rcl}
> 	c^2 = a^2 + b^2 - 2ab\cos\theta &&
> 	\cos \theta = \dfrac{a^2 + b^2 - c^2}{2ab}
> \end{array}$$
> to vector geometry gives
> $$\begin{align*}
> 	\cos \theta &= \dfrac{\|\vecbf u\|^2 + \|\vecbf v\|^2 - \|\vecbf u - \vecbf v\|^2}{2\|\vecbf u\|\|\vecbf v\|} \\
> 	&= \dfrac{\left< \vecbf{u},\vecbf{u} \right>  + \left< \vecbf{v},\vecbf{v} \right>  - \left< \vecbf{u}-\vecbf{v},\vecbf{u}-\vecbf{v} \right> }{2\|\vecbf u\|\|\vecbf v\|} \\
> 	&= \dfrac{\left< \vecbf{u},\vecbf{u} \right> + \left< \vecbf{v},\vecbf{v} \right>  - \left( \left< \vecbf{u},\vecbf{u} \right> - 2\left< \vecbf{u},\vecbf{v} \right> + \left< \vecbf{v},\vecbf{v} \right>  \right) }{2\|\vecbf u\|\|\vecbf v\|} \\
> 	&= \dfrac{2\left< \vecbf{u},\vecbf{v} \right> }{2\|\vecbf u\|\|\vecbf v\|} \\
> 	&= \dfrac{\vecbf u\cdot\vecbf v}{\| \vecbf u \| \| \vecbf v \|} \\
> \end{align*}$$
> \[[[Vector Length]], [[Inner Products]]\]