---
tags:
  - atom
  - math
  - linear
---
![300|center](vector-projections.excalidraw.md)

The *projection* of $\vecbf{x}$ onto $\vecbf{u}$ can be thought of a the shadow of $\vecbf{x}$ on $\vecbf{u}$.
- The *scalar projection* of $\vecbf{x}$ onto $\vecbf{d}$ (also called the component of $\vecbf{x}$ along $\vecbf{d}$) is defined to the signed magnitude of the *vector projection*.

| Scalar Projection                                                                     | Vector Projection                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $\text{comp}_\vecbf{u}\,\vecbf{x} = \dfrac{\vecbf{u}\cdot\vecbf{x}}{\| \vecbf{u} \|}$ | $\text{proj}_\vecbf{u}\,\vecbf{x} = \vecu{u}\, \text{comp}_\vecbf{u}\,\vecbf{x}$ <br/> $\phantom{\text{proj}_\vecbf{u}\,\vecbf{x}} = \dfrac{\vecbf{u} \cdot \vecbf{x}}{\vecbf{u}\cdot\vecbf{u}} \vecbf{u}$ |
> [!proof]-
> $\text{proj}_{\vecbf{u}}\,\vecbf{x} = c\vecbf{u}$ for some $c \in \R$. The [[Orthogonal Projection|orthogonal projection]] of $\vecbf{x}$ onto $\vecbf{u}$ is defined as
> $$\begin{align}
> 	\text{perp}_{\vecbf{u}}\,\vecbf{x} &= \vecbf{x} - \text{proj}_{\vecbf{u}}\,\vecbf{x} \\
> 	&= \vecbf{x} - c\vecbf{u} \\
> \end{align}$$
> Since $\text{proj}_{\vecbf{u}}\,\vecbf{x}$ and $\text{perp}_{\vecbf{u}}\,\vecbf{x}$ are [[Orthogonal Vectors|orthogonal]] by definition,
> $$\begin{align}
> 	\left( \vecbf{x}-c\vecbf{u} \right) \cdot \vecbf{u} &= 0 \\
> 	\vecbf{x}\cdot \vecbf{u} - c\vecbf{u}\cdot \vecbf{u} &= 0 \\
> 	 c &= \dfrac{\vecbf{u}\cdot \vecbf{u}}{\vecbf{x}\cdot \vecbf{u}} \\
> \end{align}$$
> Thus,
> $$\text{proj}_{\vecbf{u}}\,\vecbf{x} = \dfrac{\vecbf{u} \cdot \vecbf{x}}{\vecbf{u}\cdot\vecbf{u}} \vecbf{u}.$$