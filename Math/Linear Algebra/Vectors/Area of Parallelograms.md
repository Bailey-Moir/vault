---
tags:
  - atom
  - math
  - linear
---
![400|center](parallelogram-area.excalidraw.md)
Given two [[Math/Linear Algebra/Vectors/Vectors|vectors]] that describe adjacent sides of a *parallelogram*, the area can be calculated as
$$\begin{align}
	A &= \| \vecbf{x} \times \vecbf{y}  \| \\
\end{align}$$
> [!proof]-
> ![800|center](parallelogram-area-proof0.excalidraw.md)
> $$\begin{align*}
> 	A &= \|\vecbf{x}\|\|\vecbf{y}\| \sin \theta \\
> 	A^2 &= \|\vecbf{x}\|^2\|\vecbf{y}\|^2 \sin^2 \theta \\
> 	&= \|\vecbf{x}\|^2\|\vecbf{y}\|^2 (1 - \cos^2 \theta) \\
> 	&= \|\vecbf{x}\|^2\|\vecbf{y}\|^2 - (\|\vecbf{x}\|\|\vecbf{y}\|\cos \theta)^2 \\
> 	&= \|\vecbf{x}\|^2\|\vecbf{y}\|^2 - (\vecbf{x} \cdot \vecbf{y})^2 && (1) \\
> 	A^2 &=  \|\vecbf{x} \times \vecbf{y}\|^2 && (2)\\
> 	A &= \|\vecbf{x} \times \vecbf{y}\| \\
> \end{align*}$$
> \[(1) [[Dot Product]], (2) Lagrange's Identity\]