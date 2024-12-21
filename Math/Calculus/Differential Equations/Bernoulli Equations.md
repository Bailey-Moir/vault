---
tags:
  - atom
  - math
---
$$ y' + p(x)y = q(x) y^n $$
$$y^{1-n} = \dfrac{1}{\mu} (1-n) \int q(x) \mu \, dx \hspace{2em} \text{s.t. } \mu = e^{(1-n)\int p(x) \, dx}$$
Same as ODE ($n = 0$) with [[Integrating Factor Method|integrating factor method]] except $y \to y^{1-n}$, $\mu \to \mu^{1-n}$, and $\text{RHS} \to (1-n)\text{RHS}$.
> [!proof]
> $$\begin{array}{l}
>	y' + p(x)y = q(x) y^n \\
>	y'y^{-n} + p(x)y^{1-n} = q(x) \\
>	\begin{align*}
>		\text{let } u &= y^{1-n} \\
>		u' &= (1-n)y'y^{-n} \\
>		y'y^{-n} &= \dfrac{u'}{(1-n)} \\
>	\end{align*} \\
>	u' + (1-n)p(x)u = (1-n)q(x) && (1) \text{ Linear}\\
>	\therefore \displaystyle y^{1-n} = \dfrac{1}{\mu} (1-n) \int q(x) \mu \, dx && (2) \\
>	\phantom{\therefore\therefore}\displaystyle \text{where } \mu = e^{(1-n)\int p(x) \, dx} \\
>\end{array}$$
	> \[$(1)$ [[Linear Differential Equations]], $(2)$ [[Integrating Factor Method]]\]