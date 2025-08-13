---
tags:
  - atom
  - comp
---
![800|center](signed-parallelogram-area.excalidraw.md)
Given two [[Computational Vectors|vectors]] that describe adjacent sides of a *parallelogram*, the ***signed*** *[[Area of Parallelograms|area]]* [[Area of Parallelograms|of the parallelogram]] can be calculated as
$$\begin{align}
	A &= x_{1}y_{2}-x_{2}y_{1} \\
	&= \| \vecbf{x} \| \| \vecbf{y} \| \sin \theta \\
\end{align}$$
The [[Area of Triangles|triangle area]] is half that.
$$\begin{align*}
	A > 0 &\iff ABC \text{ is counter-clockwise} \iff \vecbf{y} \text{ is left of } \vecbf{x} \\
	A = 0 &\iff AB \text{ and } AC \text{ are linearly dependent} \\
	A < 0 &\iff ABC \text{ is clockwise} \iff \vecbf{y} \text{ is right of } \vecbf{x} \\
\end{align*}$$
> [!note]- The `signed_area` function
> ```python
> def signed_area(a, b, c):
> 	p = b - a
> 	q = c - a
> 	return p.x * q.y - q.x * p.y
> ```