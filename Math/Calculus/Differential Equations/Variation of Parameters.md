---
tags:
  - atom
  - math
---
To solve for the [[Solving Non-Homogeneous Differential Equations|particular solution]] of a [[Homogeneous Differential Equations|non-homogeneous]] [[Linear Differential Equations|linear]] [[Ordinary Differential Equations|ODE]]
$$a_{2}(t)y'' + a_{1}(t)y' + a_{0}(t)y = f(t),$$
in the [[Homogeneous Differential Equations|homogeneous solution]], replace the constants of integration with [[Functions|functions]] of the [[Explanatory and Response Variables|independent variable]] ($t$), and solve for these [[Functions|functions]] (non-unique). This gives

$$\begin{array}{ccc}
	\displaystyle u_{1} = -\int \dfrac{y_{2}(s)}{W(s)} \dfrac{f(s)}{a_{2}(s)} \, ds&& 
	\displaystyle u_{2} = \int \dfrac{y_{1}(s)}{W(s)} \dfrac{f(s)}{a_{2}(s)} \, ds.
\end{array}$$

> [!proof]-
> Suppose you have two [[Homogeneous Differential Equations|homogeneous solutions]] $y_{1}(t)$ and $y_{2}(t)$. Then
> $$\begin{align}
> 	a_{2}(t)y_{1}'' + a_{1}(t)y_{1}' + a_{0}(t)y_{1} &= 0 \\
> 	a_{2}(t)y_{2}'' + a_{1}(t)y_{2}' + a_{0}(t)y_{2} &= 0 \\
> \end{align}$$
> We will assume the [[Solving Non-Homogeneous Differential Equations|particular solution]] $y_{p}$ is of the form
> $$y_{p}(t) = u_{1}(t)y_{1}(t)+u_{2}(t)y_{2}(t)$$
> for some $u_{1}(t)$ and $u_{2}(t)$.
> 
> Then
> $$\begin{align}
> 	y_{p}'(t) &= u_{1}'y_{1}+u_{1}y_{1}'+u_{2}'y_{2}+u_{2}y_{2}' \\
> 	y_{p}''(t) &= u_{1}''y_{1}+2u_{1}'y_{1}'+u_{1}y_{1}''+u_{2}''y_{2}+2u_{2}'y_{2}'+u_{2}y_{2}'.
> \end{align}$$
> 
> Plugging these in gives
> $$\begin{align}
> 	a_{2}y_{p}''+a_{1}y_{p}'+a_{0}y_{p} &= a_{2}\left( u_{1}''y_{1}+2u_{1}'y_{1}'+u_{1}y_{1}''+u_{2}''y_{2}+2u_{2}'y_{2}'+u_{2}y_{2}' \right) \\
> 	&\hspace{1em}+ a_{1}\left( u_{1}'y_{1}+u_{1}y_{1}'+u_{2}'y_{2}+u_{2}y_{2}' \right)  + a_{0}(u_{1}y_{1}+u_{2}y_{2}) \\
> 	&= u_{1}(\underbrace{a_{2}y_{1}''+ay_{1}'+a_{0}y_{1}}_{0}) + u_{2}(\underbrace{a_{2}y_{2}''+ay_{2}'+a_{0}y_{2}}_{0}) \\
> 	&\hspace{1em} + a_{2}\left( u_{1}''y_{1}+u_{1}'y_{1}' \right) + a_{2}\left( u_{2}''y_{2}+u_{2}'y_{2}' \right) + a_{2}\left( u_{1}'y_{1}'+u_{2}'y_{2}' \right) + a_{1}\left( u_{1}'y_{1}+u_{2}'y_{2} \right) \\
> 	&= a_{2} \dfrac{d}{dx}\left( u_{1}'y_{1} + u_{2}'y_{2} \right) + a_{2}\left( u_{1}'y_{1}'+u_{2}'y_{2}' \right) + a_{1}\left( u_{1}'y_{1}+u_{2}'y_{2} \right) \\
> \end{align}$$
> Since we can choose $u_{1}(t)$ and $u_{2}(t)$ to be anything that satisfies the [[Differential Equations|DE]], we can choose them such that
> $$u_{1}'y_{1} + u_{2}'y_{2} = 0.$$
> Then the first and last term vanish, giving
> $$ a_{2}y_{p}''+a_{1}y_{p}'+a_{0}y_{p} = f(t) =  a_{2}\left( u_{1}'y_{1}'+u_{2}'y_{2}' \right)$$
> Thus, $u_{1}(t)$ and $u_{2}(t)$ must be solved such that
> $$\begin{align}
> 	u_{1}'y_{1}+u_{2}'y_{2} &= 0 \\
> 	u_{1}'y_{1}'+u_{2}'y_{2}' &= \dfrac{f(t)}{a_{2}(t)} \\
> \end{align}$$
> We can write this as a [[Linear Systems|linear system]]
> $$\begin{bmatrix}
> 	y_{1} & y_{2} \\
> 	y_{1}' & y_{2}'
> \end{bmatrix} \begin{bmatrix}
> 	u_{1}' \\ u_{2}'
> \end{bmatrix} = \begin{bmatrix}
> 	0 \\
> 	\frac{g(t)}{a_{2}(t)}
> \end{bmatrix}.$$
> This [[Linear Systems|system]] can then be solved using the [[inverse-functions.excalidraw|inverse]] of the left matrix:
> $$\begin{align}
> 	\begin{bmatrix}
> 		u_{1}'\\u_{2}'
> 	\end{bmatrix} &=
> 	\dfrac{1}{\begin{vmatrix}
> 		y_{1} & y_{2} \\
> 		y_{1}' & y_{2}'
> 	\end{vmatrix}}
> 	\begin{bmatrix}
> 		y_{2}' & -y_{2} \\
> 		-y_{1}' & y_{1}
> 	\end{bmatrix}
> 	\begin{bmatrix}
> 		0 \\
> 		\frac{f}{a_{2}}
> 	\end{bmatrix} \\
> 	 &=
> 	\dfrac{1}{W(y_{1},y_{2})}
> 	\begin{bmatrix}
> 		y_{2}' & -y_{2} \\
> 		-y_{1}' & y_{1}
> 	\end{bmatrix}
> 	\begin{bmatrix}
> 		0 \\
> 		\frac{f}{a_{2}}
> 	\end{bmatrix}
> \end{align}$$
> which gives
> $$\begin{array}{ccc}
> 	u_{1}' = \dfrac{-y_{2}}{W} \dfrac{f}{a_{2}} && u_{2}' = \dfrac{y_{1}}{W} \dfrac{f}{a_{2}}.
> \end{array}$$
> Integrating these gives
> $$\begin{array}{ccc}
> 	\displaystyle u_{1} = -\int \dfrac{y_{2}(s)}{W(s)} \dfrac{f(s)}{a_{2}(s)} \, ds&& 
> 	\displaystyle u_{2} = \int \dfrac{y_{1}(s)}{W(s)} \dfrac{f(s)}{a_{2}(s)} \, ds.
> \end{array}$$
 
> [!example]- $y'' + 2y' + y = \dfrac{e^t}{1+t^2}$
> By [[Auxiliary Equations|auxiliary equations]], $y_{1} = e^t$ and $y_{2} = te^t$. Then
> $$W = \begin{vmatrix}
> 	e^t & te^t \\
> 	e^t & (1+t)e^t
> \end{vmatrix} = e^{2t}(t-1) - e^{2t}t = e^2t $$
> $$\begin{align}
> 	u_{1}' &= \dfrac{1}{W}(-y_{2}) \dfrac{f}{a_{2}} \\
> 	&= e^{-2t}(-te^t) \dfrac{\dfrac{e^t}{1+t^2}}{1} \\
> 	&= -\dfrac{t}{1+t^2} \\
> \end{align}$$

\[[[Wronskian Determinant]]\]