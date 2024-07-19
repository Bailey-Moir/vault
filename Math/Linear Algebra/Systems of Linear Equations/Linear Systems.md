---
tags:
  - atom
  - math
---
A **linear equation** is an equation in which each term is either constant or a constant multiplied by a variable to the first power.
$$ a_1x_1 + a_2x_2 + \cdots + a_nx_n = b $$
A **system of linear equations** (or **linear system**) is a set or group of linear equations which must all be true simultaneously.

There are two main ways of representing systems of simultaneous linear equations with matrices: with an augmented matrix (an expression), and with a matrix equation.

$$\begin{array}{c c}
	A\mathbf{\underline{x}} = \mathbf{\underline{b}} 
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
		A \bigm| & \hspace{-2ex} \mathbf{\underline{b}} \hspace{0.3ex}
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
<center>Both of these examples describe the below system of equations.</center>
$$\begin{align*}
	 x + 2y &= 3 \\
	3x + 4y &= 4
\end{align*}$$

Note that:
- $A$ is the **coefficient matrix**.
- $\mathbf{\underline{x}}$ is the **unknown column vector**.
- $\mathbf{\underline{b}}$ is the **RHS column vector**.

The first of these methods can be solved for by multiplying both sides by the [[Inverting Matrices|inverse]] of the matrix of coefficients ($\mathbf{\underline{x}} = A^{-1}\mathbf{\underline{b}}$), while the other can be solved with [[Gaussian Elimination|gaussian elimination]].