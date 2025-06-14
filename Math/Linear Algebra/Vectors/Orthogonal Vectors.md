---
tags:
  - atom
  - math
  - linear
---
A [[Sets|set]] of non-zero [[Math/Linear Algebra/Vectors/Vectors|vectors]] $\{ \vecbf{u}_{1},\vecbf{u}_{2},\dots,\vecbf{u}_{k} \}$ in an [[Inner Products|inner product space]] is *orthogonal* iff it is pairwise *orthogonal*:
$$\forall i,j, \left( i\ne j \to \left< \vecbf{u}_{i},\vecbf{u}_{j} \right>  = 0 \right)$$
An *orthogonal set* is **orthonormal** iff all its vectors have [[Vector Length|length]] $1$.
$$\forall i,j, \left< \vecbf{u}_{i},\vecbf{u}_{j} \right>  = \left\{\begin{matrix}
	0, & \text{if } i \ne j \\
	1, & \text{if } i = j \\
\end{matrix}\right.$$

> [!proof]- $\vecbf{u} \:\bot\: \vecbf{v} \iff \left< \vecbf{u},\vecbf{v} \right> = 0$
> $$ \begin{align*}
> 	\left< \vecbf{u},\vecbf{v} \right>  &= \| \vecbf{u} \|\,\| \vecbf{v} \| \cos \theta && (1)\\
> 	&= \| \vecbf{u} \|\,\| \vecbf{v} \| \cos \left( \dfrac{\pi}{2} \right) && \text{Perpendicular $(\theta \in [0,\pi])$} \\
> 	&= \| \vecbf{u} \|\,\| \vecbf{v} \| (0) \\
> 	&= 0 \\
> \end{align*}$$
> \[$(1)$ [[Cosine Similarity Formula]]\]

> [!note]- [[Bijective Functions|Bijectivity]] of $\cos\theta$.
> The angle $\theta$ between two [[Math/Linear Algebra/Vectors/Vectors|vectors]] is always in $[0,\pi]$, and thus $\cos \theta$ looks like
> ![400|center](cosine-quadrants-12.excalidraw.md)
> Note that this is [[Bijective Functions|bijective]], meaning that each value of $\cos\theta$ gives exactly one $\theta$, and vice versa. Thus
> $$\begin{align*}
> 	\theta < \dfrac{\pi}{2} &\iff \left< \vecbf{x},\vecbf{y} \right>  > 0 && \text{acute}\\
> 	\theta = \dfrac{\pi}{2} &\iff \left< \vecbf{x},\vecbf{y} \right>  = 0 && \vecbf{x} \:\bot\: \vecbf{y}\\
> 	\theta > \dfrac{\pi}{2} &\iff \left< \vecbf{x},\vecbf{y} \right>  < 0 && \text{obtuse}\\
> \end{align*}$$
> can be derived from the [[Dot Product|cosine definition of the dot product]].

\[[[Dot Product]], [[Cosine Similarity Formula]]\]