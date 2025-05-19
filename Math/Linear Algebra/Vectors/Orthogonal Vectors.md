---
tags:
  - atom
  - math
  - linear
---
A set of non-zero [[Math/Linear Algebra/Vectors/Vectors|vectors]] $\{ \vecbf{u}_{1},\vecbf{u}_{2},\dots,\vecbf{u}_{k} \}$ is *orthogonal* iff it is pairwise *orthogonal*:
$$\forall i,j, \left( i\ne j \to \vecbf{u}_{i}\cdot \vecbf{u}_{j} = 0 \right)$$
An *orthogonal set* is **orthonormal** iff all its vectors have [[Vector Length|length]] $1$.
$$\forall i,j, \vecbf{u}_{i}\cdot \vecbf{u}_{j} = \left\{\begin{matrix}
	0, & \text{if } i \ne j \\
	1, & \text{if } i = j \\
\end{matrix}\right.$$

> [!proof]- $\vecbf{x} \:\bot\: \vecbf{y} \iff \vecbf{x} \cdot \vecbf{y} = 0$
> $$ \begin{align*}
> 	\vecbf{a} \cdot \vecbf{b} &= \left|\vecbf{a}\right| \left|\vecbf{b}\right| \cos \theta \\
> 	&= \left|\vecbf{a}\right| \left|\vecbf{b}\right| \cos \left( \dfrac{\pi}{2} \right) && \text{Perpendicular $(\theta \in [0,\pi])$} \\
> 	&= \left|\vecbf{a}\right| \left|\vecbf{b}\right| (0) \\
> 	&= 0 \\
> \end{align*}$$

> [!note]- [[Bijective Functions|Bijectivity]] of $\cos\theta$.
> The angle $\theta$ between two [[Math/Linear Algebra/Vectors/Vectors|vectors]] is always in $[0,\pi]$, and thus $\cos \theta$ looks like
> ![400|center](cosine-quadrants-12.excalidraw.md)
> Note that this is [[Bijective Functions|bijective]], meaning that each value of $\cos\theta$ gives exactly one $\theta$, and vice versa. Thus
> $$\begin{align*}
> 	\theta < \dfrac{\pi}{2} &\iff \vecbf{x} \cdot \vecbf{y} > 0 && \text{acute}\\
> 	\theta = \dfrac{\pi}{2} &\iff \vecbf{x} \cdot \vecbf{y} = 0 && \vecbf{x} \:\bot\: \vecbf{y}\\
> 	\theta > \dfrac{\pi}{2} &\iff \vecbf{x} \cdot \vecbf{y} < 0 && \text{obtuse}\\
> \end{align*}$$
> can be derived from the [[Dot Product|cosine definition of the dot product]].

> [!note] *Orthogonality* is an important condition for the [[Subspace Projection|subspace projection formula]]

\[[[Dot Product]], [[Cosine Similarity Formula]]\]