---
tags:
  - atom
  - math
  - linear
---
![300|center](vector-projections.excalidraw.md)

For an [[Inner Products|inner product space]], the *projection* of $\vecbf{v}$ onto $\vecbf{u}$ can be thought of a the shadow of $\vecbf{v}$ on $\vecbf{u}$.
- The *scalar projection* of $\vecbf{v}$ onto $\vecbf{d}$ (also called the component of $\vecbf{v}$ along $\vecbf{d}$) is defined to the signed magnitude of the *vector projection*.

$$\begin{array}{ccc}
	\textbf{Scalar Projection} && \textbf{Vector Projection} \\
	\text{comp}_\vecbf{u}\,\vecbf{v} = \dfrac{\left< \vecbf{u},\vecbf{v} \right> }{\| \vecbf{u} \|}
	&&
	\text{proj}_\vecbf{u}\,\vecbf{v} = \vecu{u}\, \text{comp}_\vecbf{u}\,\vecbf{v} \\
	&&
	\hspace{2.6em} = \dfrac{\left< \vecbf{u},\vecbf{v} \right>}{\left< \vecbf{u},\vecbf{u} \right>}\vecbf{u}
\end{array}$$

> [!proof]-
> $\text{proj}_{\vecbf{u}}\,\vecbf{v} = c\vecbf{u}$ for some $c \in \R$. The [[Orthogonal Projection|orthogonal projection]] of $\vecbf{v}$ onto $\vecbf{u}$ is defined as
> $$\begin{align}
> 	\text{perp}_{\vecbf{u}}\,\vecbf{v} &= \vecbf{v} - \text{proj}_{\vecbf{u}}\,\vecbf{v} \\
> 	&= \vecbf{v} - c\vecbf{u} \\
> \end{align}$$
> Since $\text{proj}_{\vecbf{u}}\,\vecbf{v}$ and $\text{perp}_{\vecbf{u}}\,\vecbf{v}$ are [[Orthogonal Vectors|orthogonal]] by definition,
> $$\begin{align}
> 	\left< \vecbf{v}-c\vecbf{u},\vecbf{u} \right>  &= 0 \\
> 	\left< \vecbf{v},\vecbf{u} \right>-c\left< \vecbf{u},\vecbf{u} \right>   &= 0 \\
> 	 c &= \dfrac{\left< \vecbf{u},\vecbf{v} \right>}{\left< \vecbf{u},\vecbf{u} \right>} 
> \end{align}$$
> Thus,
> $$\text{proj}_{\vecbf{u}}\,\vecbf{v} = \dfrac{\left< \vecbf{u},\vecbf{v} \right>}{\left< \vecbf{u},\vecbf{u} \right>}\vecbf{u}.$$

\[[[Inner Products]], [[Vector Length]]\]