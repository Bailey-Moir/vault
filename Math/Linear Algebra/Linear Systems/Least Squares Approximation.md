---
tags:
  - atom
  - math
  - linear
---
![400|center](least-square-approximation.excalidraw)
For to the [[Linear Systems|linear system]] $A\vecbf{x} = \vecbf{b}$, the **error** is given by
$$e = \| \vecbf{e}(\vecbf{x}) \| = \| A\vecbf{x} - \vecbf{b} \|.$$
> [!definition] A *least squares approximation* is found by minimising this error.
> For $A \in \R^{m,n}$ and $b \in \R^m$, a *least squares solution* of $A\vecbf{x} = \vecbf{b}$ is a [[Math/Linear Algebra/Vectors/Vectors|vector]] $\vecbf{x}' \in \R^n$ such that
> $$\| A\vecbf{x}' - \vecbf{b} \| \le \| A\vecbf{x} - \vecbf{b} \|$$
> for all $\vecbf{x} \in \R^n$.

> [!lemma]- For $A \in \R^{m,n}$ and $b \in \R^m$, $\vecbf{x}' \in \R^n$ is a *least squares solution* of $A\vecbf{x} = \vecbf{b}$ iff$$A\vecbf{x}' = \text{proj}_{\text{col}\,A}\vecbf{b}$$
> If $\vecbf{x}\in \R^n$, then $A\vecbf{x} \in \text{col}(A)$, and the closest vector in $\text{col}(A)$ to $\vecbf{b}$ is $\text{proj}_{\text{col}(A)}(\vecbf{b})$[^1].
> 
> Thus, $\vecbf{x}'$ is a *least square solution* of $A\vecbf{x} = \vecbf{b}$ iff $A\vecbf{x}' =\text{proj}_{\text{col}(A)}(\vecbf{b})$.

> [!theorem]- For $A \in \R^{m,n}$ and $b \in \R^m$, $\vecbf{x}' \in \R^n$ is a *least squares solution* of $A\vecbf{x} = \vecbf{b}$ iff$$A^TA\vecbf{x}' = A^T\vecbf{b}$$
> By the previous lemma, $\vecbf{x}'$ is a *least squares solution* iff $A\vecbf{x}' =\text{proj}_{\text{col}(A)}(\vecbf{b})$, i.e.
> $$\begin{align}
> 	b - A\vecbf{x}' &= b - \text{proj}_{\text{col}(A)}(\vecbf{b}) \\
> 	&= \text{perp}_{\text{col}(A)}(\vecbf{b}).
> \end{align}$$
> Note $\text{perp}_{\text{col}(A)}(\vecbf{b})$ is in $\text{col}(A)^\perp =\text{null}(A^T)$[^2][^3].
> 
> Therefore, $\vecbf{x}$' is a *least squares solution* iff 
> $$\begin{align}
> 	A^T(\vecbf{b} - A\vecbf{x}') = \vecbf{0} \\
> 	A^TA\vecbf{x}' = A^T\vecbf{b} \\
> \end{align}$$

> [!example]- $A = \begin{bmatrix}1&1\\1&2\\1&3\end{bmatrix}$, $\hspace{0.5em}\vecbf{b} = \begin{bmatrix}2\\2\\4\end{bmatrix}$, $\hspace{1em}A\vecbf{x} = \vecbf{b}$
> $$\begin{array}{ccc}
> 	A^TA = \begin{bmatrix}
> 		1&1&1\\
> 		1&2&3
> 	\end{bmatrix}\begin{bmatrix}
> 		1&1\\
> 		1&2\\
> 		1&3
> 	\end{bmatrix} = \begin{bmatrix}
> 		3 & 6 \\
> 		6 & 14
> 	\end{bmatrix}
> 	&&
> 	A^T\vecbf{b} = \begin{bmatrix}
> 	8 \\
> 	18
> \end{bmatrix}
> \end{array}$$
> Solving the [[Linear Systems|system of linear equations]]  $A^TA\vecbf{x}' = A^T\vecbf{b}$ corresponds to solving the system
> $$\left[
> \left.
> \begin{matrix}
> 	3 & 6\\
> 	6 & 4\\
> \end{matrix}
> \hspace{0.25em}
> \right|
> \hspace{0.1em}
> \begin{matrix}
> 	8\\
> 	18\\
> \end{matrix}
> \right] = \left[
> \left.
> \begin{matrix}
> 	3 & 6\\
> 	0 & 2\\
> \end{matrix}
> \hspace{0.25em}
> \right|
> \hspace{0.1em}
> \begin{matrix}
> 	8\\
> 	2\\
> \end{matrix}
> \right].$$
> This gives $\vecbf{x} = \begin{bmatrix} \frac{2}{3} \\ 1  \end{bmatrix}$, with associated line $h = \dfrac{2}{3} + t$.

> [!example]- [[Parabolas]] with points $\left( -1,1 \right),\left( 0,-1 \right),\left( 1,0 \right),$ and $\left( 2,2 \right)$.[^4]
> 
> The equation of a [[Parabolas|parabola]] is a quadratic, $y = a + bx + cx^2$.
> 
> Substituting the points into this quadratic gives the [[Linear Systems|linear system]]
> $$\begin{align}
> 	a - b + c &= 1 \\
> 	a &= -1 \\
> 	a + b + c &= 0 \\
> 	a + 2b + 4c &= 2. \\
> \end{align}$$
> Writing this in [[Matrices|matrix]] form gives
> $$\begin{bmatrix}
> 	1 & -1 & 1 \\
> 	1 & 0 & 0 \\
> 	1 & 1 & 1 \\
> 	1 & 2 & 4
> \end{bmatrix}\begin{bmatrix}
> 	a \\ b \\ c
> \end{bmatrix} = \begin{bmatrix}
> 	1 \\
> 	-1 \\
> 	0 \\
> 	2
> \end{bmatrix}.$$
> To find a *least squares solution*, we solve the equation
> $$A^TA \vecbf{x}'= A^T\vecbf{b}$$
> $$\begin{array}{ccc}
> 	A^TA = \begin{bmatrix}
> 		4 & 2 & 6 \\
> 		2 & 6 & 8 \\
> 		6 & 8 & 18
> 	\end{bmatrix}
> 	&&
> 	A^T\vecbf{b} = \begin{bmatrix}
> 	2 \\
> 	3 \\
> 	9
> \end{bmatrix}
> \end{array},$$
> giving
> $$\left[
> \left.
> \begin{matrix}
> 	4 & 2 & 6\\
> 	2 & 6 & 8\\
> 	6 & 8 & 18\\
> \end{matrix}
> \hspace{0.25em}
> \right|
> \hspace{0.1em}
> \begin{matrix}
> 	2\\
> 	3\\
> 	9\\
> \end{matrix}
> \right].$$
> Solving this [[Linear Systems|system of linear equations]] gives $\vecbf{x}' = \begin{bmatrix}-\frac{7}{10}\\-\frac{3}{5}\\1\end{bmatrix}$, meaning the *least squares approximation* parabola is
> $$y = x^2 -\dfrac{3}{5}x - \dfrac{7}{10}$$



[^1]: [[Distance to a Subspace]]
[^2]: [[Orthogonal Complements]]
[^3]: [[Four Fundamental Subspaces]]
[^4]: [[Curve Fitting]]
