---
tags:
  - atom
  - math
---
A *linear system* (or *system of linear equations*) is a [[Sets|set]] of linear equations which must all be true simultaneously.

The two main ways of representing *linear systems* with [[Matrices|matrices]] are with an augmented matrix (an expression), and with a matrix equation.

$$\begin{array}{c c}
	A\vecbf{x} = \vecbf{b} 
		&
	\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
	\begin{bmatrix} 
		x \\ y 
	\end{bmatrix} = 
	\begin{bmatrix} 
		3 \\ 4
	\end{bmatrix} 
	
		\\
	
	\begin{bmatrix} 
		A \bigm| & \hspace{-2ex} \vecbf{b} \hspace{0.3ex}
	\end{bmatrix}
		&
	\left[
		\begin{matrix} 
			1 & 2 \\
			3 & 4
		\end{matrix}
		\:
		\left|
		\:
		\begin{matrix}
			3 \\
			4
		\end{matrix}
		\right.
	\right]
\end{array}$$
<center>Both of these examples describe the linear system below.</center>

$$\begin{align*}
	 x + 2y &= 3 \\
	3x + 4y &= 4
\end{align*}$$
The first of these methods can be solved for by multiplying both sides by the [[Linear Map Invertibility|inverse]] of the matrix of coefficients ($\vecbf{x} = A^{-1}\vecbf{b}$), while the other can be solved with [[Gaussian Elimination|Gaussian elimination]].

> [!note]
> - $A$ is the **coefficient matrix**.
> - $\vecbf{x}$ is the **unknown column vector**.
> - $\vecbf{b}$ is the **RHS column vector**.