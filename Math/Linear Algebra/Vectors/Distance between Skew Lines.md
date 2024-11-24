---
tags:
  - atom
  - math
---
The shortest line that joins two lines in $\R^3$ meets the two lines at $90^\circ$. Constructing a [[Vector Parametric Planes|vector parametric plane]] from the two [[Direction Vectors|direction vectors]] of the lines that contains one of the lines must be [[Vector Scalar Multiplication|parallel]] to the other.
![500|center](distance-of-skew-lines.excalidraw)

> [!example]-
> $$\begin{array} {rcl}
> 	\vecbf{r}_{1}=\left\langle 4,5,6 \right\rangle+s\left\langle 1,3,2 \right\rangle && \vecbf{r}_{2} = \left\langle 5,6,7 \right\rangle+t\left\langle 1,2,1 \right\rangle
> \end{array}$$
> First, I will construct a plane containing $\vecbf{r}_{2}$ and [[Vector Scalar Multiplication|parallel]] to $\vecbf{r}_{1}$, meaning the distance between the plane and $\vecbf{r}_{1}$ will be constant. Calculating $\vecbf{n}$ as
> $$\vecbf{n}=\begin{bmatrix}
> 	1 \\
> 	2 \\
> 	1
> \end{bmatrix} \times \begin{bmatrix}
> 	1 \\
> 	3 \\
> 	2
> \end{bmatrix} = \begin{bmatrix}
> 	1 \\
> 	-1 \\
> 	1
> \end{bmatrix}$$
> allows me to create the plane in [[Vector Point-Normal Planes|point-normal form]].
> $$\begin{align*}
> 	\left(\begin{bmatrix}
> 		x \\
> 		y \\
> 		z
> 	\end{bmatrix}
> 	-
> 	\begin{bmatrix}
> 		5 \\
> 		6 \\
> 		7
> 	\end{bmatrix}\right)
> 	\cdot
> 	\begin{bmatrix}
> 		1 \\
> 		-1 \\
> 		1
> 	\end{bmatrix} &= 0 && (1) \\
> 	x - y + z &= 6
> \end{align*}$$
> Creating a line at $\vecbf{r}_{0}$ of $\vecbf{r}_{2}$ with $\vecbf{n}$ as the [[Direction Vectors|direction vector]] and plugging it into this plane gives.
> $$\vecbf{r}=\left\langle 4,5,6 \right\rangle+k\left\langle 1,-1,1 \right\rangle$$
> $$\begin{align*}
> 	\left( 4+k \right)-\left( 5-k \right)+\left( 6+k \right) &= 6 \\
> 	3k+5 &= 6 \\
> 	k &= \dfrac{1}{3}\\
> \end{align*}$$
> The distance between $\vecbf{r}_{1}$ and $\vecbf{r}_{2}$ is then 
> $$\begin{align*}
> 	\| k\vecbf{n} \| &= \| \dfrac{1}{3}\left( 1,-1,1 \right) \| \\
> 	&= \dfrac{1}{\sqrt{ 3 }}
> \end{align*}$$

\[[[Vector Parametric Lines]]\]