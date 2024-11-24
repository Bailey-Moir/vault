---
tags:
  - atom
  - math
---
The angle $\theta$ between two [[Vectors|vectors]] is always in $[0,\pi]$, and thus $\cos \theta$ looks like
![400|center](cosine-quadrants-12.excalidraw)
Note that this is [[Bijective Functions|bijective]], meaning that each value of $\cos\theta$ gives exactly one $\theta$, and vice versa. Thus
$$\begin{align*}
	\theta < \dfrac{\pi}{2} &\iff \vecbf{x} \cdot \vecbf{y} > 0 && \text{acute}\\
	\theta = \dfrac{\pi}{2} &\iff \vecbf{x} \cdot \vecbf{y} = 0 && \vecbf{x} \:\bot\: \vecbf{y}\\
	\theta > \dfrac{\pi}{2} &\iff \vecbf{x} \cdot \vecbf{y} < 0 && \text{obtuse}\\
\end{align*}$$
can derived from the [[Dot Product|cosine definition of the dot product]].

> [!proof]- $\vecbf{x} \:\bot\: \vecbf{y} \iff \vecbf{x} \cdot \vecbf{y} = 0$
> $$ \begin{align*}
> 	\vecbf{a} \cdot \vecbf{b} &= \left|\vecbf{a}\right| \left|\vecbf{b}\right| \cos \theta \\
> 	&= \left|\vecbf{a}\right| \left|\vecbf{b}\right| \cos \left( \dfrac{\pi}{2} \right) && \text{Perpendicular $(\theta \in [0,\pi])$} \\
> 	&= \left|\vecbf{a}\right| \left|\vecbf{b}\right| (0) \\
> 	&= 0 \\
> \end{align*}$$

\[[[Dot Product]], [[Cosine Similarity Formula]]\]