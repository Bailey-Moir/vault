---
tags:
  - atom
  - math
---
![400|center](parallelogram-area.excalidraw.md)
Given two [[Vectors|vectors]] that describe adjacent sides of a *parallelogram*, the area can be calculated as
$$ A = \| \vecbf{x} \times \vecbf{y}  \| $$
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


> [! ]- **Lagrange's Identity** $\| \vecbf{x} \times \vecbf{y}  \|^2 = \|\vecbf{x}\|^2\|\vecbf{y}\|^2 - (\vecbf{x} \cdot \vecbf{y})^2$
> Let $\vecbf{x} = \langle x_1, x_2, x_3 \rangle$, $\vecbf{y} = \langle y_1, y_2, y_3 \rangle$, and $\vecbf{n} = \langle n_1, n_2, n_3 \rangle = \vecbf{x} \times \vecbf{y}$.
> $$\begin{align*}
> 	\text{RHS} &= \|\vecbf{x}\|^2\|\vecbf{y}\|^2 - (\vecbf{x} \cdot \vecbf{y})^2 \\
> 	&= (x_1^2 + x_2^2 + x_3^2)(y_1^2 + y_2^2 + y_3^2) - (x_1y_1 + x_2y_2 + x_3y_3)^2 \\
> 	&= \left(\begin{array}{c}
> 		x_1^2y_1^2 + x_2^2y_2^2 + x_3^2y_3^2 \\
> 		\color{red}{+ x_1^2y_2^2 + x_2^2y_1^2} \\
> 		\color{OliveGreen}{+ x_3^2y_1^2 + x_1^2y_3^2} \\
> 		\color{CornflowerBlue}{+ x_3^2y_2^2 + x_2^2y_3^2} \\
> 	\end{array}\right) - \left(\begin{array}{c}
> 		x_1^2y_1^2 + x_2^2y_2^2 + x_3^2y_3^2 \\
> 		\color{red}{+ 2x_1y_1x_2y_2} \\
> 		\color{OliveGreen}{+ 2x_1y_1x_3y_3} \\
> 		\color{CornflowerBlue}{+ 2x_2y_2x_3y_3} \\
> 	\end{array}\right) \\
> 	&= \left(\textcolor{red}{x_1y_2 - x_2y_1}\right)^2 + \left(\textcolor{OliveGreen}{x_3y_1 - x_1y_3}\right)^2 + \left(\textcolor{CornflowerBlue}{x_2y_3 - x_3y_2}\right)^2 \\
> 	&= \left(\textcolor{red}{n_3}\right)^2 + \left(\textcolor{OliveGreen}{-n_2}\right)^2 + \left(\textcolor{CornflowerBlue}{n_1}\right)^2 \\
> 	&= \|\vecbf{x} \times \vecbf{y}\|^2 \\
> 	&= \text{LHS} \hspace{1em}\square
> \end{align*}$$