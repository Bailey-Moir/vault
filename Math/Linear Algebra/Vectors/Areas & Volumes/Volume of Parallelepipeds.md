---
tags:
  - atom
  - math
---
![500|center](volume-parallelepipeds.excalidraw)
The *volume* of a *parallelepiped* represented by $\vecbf{x},\vecbf{y},\vecbf{z} \in \R^3$ is given by
$$ \| \vecbf{x} \cdot (\vecbf{y} \times \vecbf{z}) \| $$
> [!proof]-
> $$V = Ah$$
> Where 
> $$\begin{align*}
> 	h &= \| \text{proj}_{\vecbf{y} \times \vecbf{z}} \vecbf{x} \| && (1) \\
> 	&= \left\| \dfrac{\vecbf{x} \cdot(\vecbf{y}\times \vecbf{z})}{\|\vecbf{y}\times \vecbf{z}\|^2} \vecbf{y}\times \vecbf{z} \right\| \\
> 	&= \dfrac{| \vecbf{x} \cdot(\vecbf{y}\times \vecbf{z}) |}{\|\vecbf{y}\times \vecbf{z}\|^2} \| \vecbf{y}\times \vecbf{z} \| \\
> 	&= \dfrac{| \vecbf{x} \cdot(\vecbf{y}\times \vecbf{z}) |}{\|\vecbf{y}\times \vecbf{z}\|} \\
> \end{align*}$$
> Therefore
> $$\begin{align*}
> 	V &= \left( \|\vecbf{y}\times \vecbf{z}\| \right)\left( \dfrac{|\vecbf{x}\cdot(\vecbf{y} \times \vecbf{z})|}{\|\vecbf{y} \times \vecbf{z} \|} \right) \\
> 	V &= |\vecbf{x}\cdot(\vecbf{y} \times \vecbf{z})|
> \end{align*}$$
> \[(1) [[Vector Projection]]\]