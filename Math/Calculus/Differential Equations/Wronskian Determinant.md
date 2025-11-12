---
tags:
  - atom
  - math
---
$$W(y_{1},\dots,y_{n}) = \begin{vmatrix}
	y_{1} & y_{2} & \dots & y_{n} \\
	y'_{1} & y'_{2} & \dots & y'_{n} \\
	\vdots & \vdots & \ddots & \vdots \\
	y^{(n-1)}_{1} & y^{(n-1)}_{2} & \dots & y^{(n-1)}_{n} \\
\end{vmatrix}$$
For some [[Intervals|interval]] $I$, let $y_{1},\dots,y_{n}$ be [[Functions|functions]] that map $I$ into a [[Fields|field]] that are $n-1$ [[_Differentiability|differentiable]] on $I$. Then if $\exists t \in I, W(y_{1},\dots,y_{n}) \ne 0$, these [[Functions|functions]] are [[Linear Independence|linearly independent]] on $I$.

> [!intuition] If the *Wronskian* is not identically zero on $I$, the [[Functions|functions]] are [[Linear Independence|linearly independent]] on $I$.

> [!proof]-
> If $y_{1},\dots,y_{n}$ is [[Linear Independence|linearly dependent]], by the [[Linear Dependence Lemma|linear dependence lemma]], there exists $k$ such that
> $$y_{k} \in \text{span}(y_{1},\dots,y_{k-1}).$$
> Thus, there exists $a_{1},\dots,a_{k-1}$ such that
> $$\begin{align}
> 	y_{k} &= a_{1}y_{1}+\dots+a_{k-1}y_{k-1} \\
> 	(y_{k})^{(i)} &= \left( a_{1}y_{1}+\dots+a_{k-1}y_{k-1} \right)^{(i)} &&\forall i \in \Z_{n}\\
> 	y^{(i)}_{k} &= a_{1}y^{(i)}_{i}+\dots+a_{k-1}y^{(i)}_{k-1}.  \\
> \end{align}$$
> Note this requires each $y_{1},\dots,y_{n}$ to be $n-1$ [[_Differentiability|differentiable]].
> 
> Thus, $$\begin{bmatrix}
> 	y_{k} \\
> 	y'_{k} \\
> 	\vdots \\
> 	y^{(n-1)}_{k} \\
> \end{bmatrix} = a_{1}\begin{bmatrix}
> 	y_{1} \\
> 	y'_{1} \\
> 	\vdots \\
> 	y^{(n-1)}_{1} \\
> \end{bmatrix} + \dots + a_{k-1}\begin{bmatrix}
> 	y_{k-1} \\
> 	y'_{k-1} \\
> 	\vdots \\
> 	y^{(n-1)}_{k-1} \\
> \end{bmatrix}$$
> By the [[Linear Dependence Lemma|linear dependence lemma]], since each of these [[Math/Linear Algebra/Vectors/Vectors|vectors]] is a column of the [[Matrices|matrix]] determined by $W(y_{1},\dots,y_{n})$, the columns must be [[Linear Independence|linearly dependent]], meaning $W(y_{1},\dots,y_{n}) = 0$.
> Thus, the theorem is [[Proof by Contraposition|proven by contraposition]].

\[[[Linear Homogeneous Differential Equations]]\]