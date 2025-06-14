---
tags:
  - atom
  - math
  - linear
---
For all $\vecbf{u},\vecbf{v}$ in an [[Inner Products|inner product space]] with [[Norms|induced norm]] $\| \cdot \|$,
![500|center](vector-length-identity.excalidraw.md)
$$ \|\vecbf{u} + \vecbf{v}\|^2 + \|\vecbf{u} - \vecbf{v}\|^2 = 2\|\vecbf{u}\|^2 + 2\|\vecbf{v}\|^2 $$
> [!proof]-
> $$\begin{align*}
> 	\text{LHS} &= \|\vecbf u + \vecbf v\|^2 + \|\vecbf u - \vecbf v\|^2 \\ 
> 	&= \left< \vecbf{u}+\vecbf{v},\vecbf{u}+\vecbf{v} \right>  + \left< \vecbf{u}-\vecbf{v},\vecbf{u}-\vecbf{v} \right>  \\ 
> 	&= \left< \vecbf{u},\vecbf{u} \right>  + 2\left< \vecbf{u},\vecbf{v} \right>  + \left< \vecbf{v},\vecbf{v} \right>  + \left( \left< \vecbf{u},\vecbf{u} \right>  - 2\left< \vecbf{u},\vecbf{v} \right>  + \left< \vecbf{v},\vecbf{v} \right>  \right) \\ 
> 	&= 2\left< \vecbf{u},\vecbf{u} \right> + 2\left< \vecbf{v},\vecbf{v} \right> \\ 
> 	&= 2\|\vecbf u\|^2 + 2\|\vecbf v\|^2 
> \end{align*}$$
> \[[[Inner Products]]\]

> [!note] The [[Converse, Inverse, and Contrapositive|contrapositive]] of this gives that if this equation is not satisfied, the given [[Norms|norm]] does not arise from an [[Inner Products|inner product]].

\[[[Vector Length]]\]