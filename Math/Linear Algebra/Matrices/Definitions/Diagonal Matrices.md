---
tags:
  - atom
  - math
  - linear
---
Fairly self-explanatory: the only non-zero entries lie on the main diagonal.
$$\begin{bmatrix} 
	a_{11} & 0 & \dots & 0 \\
	0 & a_{22} & \dots & 0 \\
	\vdots & \vdots & \ddots & \vdots \\
	0 & 0 & \dots & a_{nn} \\
\end{bmatrix} $$
# Properties of [[Diagonal Matrices]]
- **Easy Exponentiation**
$$\begin{bmatrix}
	a_{1} & \cdots  & 0 \\
	\vdots & \ddots  & 0 \\
	0 & \cdots  & a_{i} \\
\end{bmatrix}^n = \begin{bmatrix}
	a_{1}^n & \cdots  & 0 \\
	\vdots & \ddots  & 0 \\
	0 & \cdots  & a_{i}^n \\
\end{bmatrix}$$
- **Easy Vector Multiplication**
$$\begin{bmatrix}
	a_{1} & \cdots  & 0 \\
	\vdots & \ddots  & 0 \\
	0 & \cdots  & a_{i} \\
\end{bmatrix} \begin{bmatrix}
	b_{1} \\ \vdots \\ b_{i}
\end{bmatrix} = \begin{bmatrix}
	a_{1}b_{1} \\ \vdots \\ a_{i}b_{i}
\end{bmatrix}$$
$$\begin{bmatrix}
	b_{1} & \cdots & b_{i}
\end{bmatrix} \begin{bmatrix}
	a_{1} & \cdots  & 0 \\
	\vdots & \ddots  & 0 \\
	0 & \cdots  & a_{i} \\
\end{bmatrix}= \begin{bmatrix}
	a_{1}b_{1} & \cdots & a_{i}b_{i}
\end{bmatrix}$$