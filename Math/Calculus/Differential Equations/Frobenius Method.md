---
tags:
  - atom
  - math
---
If $t_{0}$ is a [[Ordinary and Singular Points|regular singular point]], solutions of the form
$$y = \sum_{n=0}^\infty c_{n}(t-t_{0})^{n+\gamma}$$
may be found. The power $\gamma$ is fixed by an **indicial equation**.

> [!example]- $2ty'' + y' - y = 0$
> In standard form, this is
> $$\begin{align}
> 	y''+\dfrac{1}{2t}y'-\dfrac{1}{2t}y = 0. && (*)
> \end{align}$$
> Thus, $P(t) = \frac{1}{2t}$, and $Q(t) = -\frac{1}{2t}$. Then $tP(t) = \frac{1}{2}$ and $t^2Q(t) = -\frac{t}{2}$, both of these [[Functions|functions]] are [[Analytic Functions|analytic]], so $t_{0}=0$ is a [[Ordinary and Singular Points|regular singular point]]. Thus, using the *Frobenius method*, we will seek solutions of the form
> $$y = \sum_{n=0}^\infty c_{n}t^{n+\gamma}.$$
> The [[Differentiation|derivatives]] of $y$ are then
> $$\begin{align}
> 	y' &= \sum_{n=0}^\infty c_{n}\left( n+\gamma \right)t^{n-1+\gamma} \\
> 	y'' &= \sum_{n=0}^\infty c_{n}\left( n+\gamma \right)\left( n-1 + \gamma \right)t^{n-2+\gamma}. \\
> \end{align}$$
> Plugging this into $\left( * \right)$ gives
> $$\begin{align}
> 	\sum_{n=0}^\infty c_{n}\left( n+\gamma \right)\left( n-1 + \gamma \right)t^{n-2+\gamma} + \dfrac{1}{2t}\sum_{n=0}^\infty c_{n}\left( n+\gamma \right)t^{n-1+\gamma}-\dfrac{1}{2t}\sum_{n=0}^\infty c_{n}t^{n+\gamma} &= 0 \\
> 	\sum_{n=0}^\infty c_{n}\left[ \left( n+\gamma \right)\left( n-1 + \gamma \right)t^{n-2+\gamma} + \dfrac{1}{2}\left( n+\gamma \right)t^{n-2+\gamma} \right] - \sum_{n=0}^\infty c_{n}\dfrac{1}{2}t^{n-1+\gamma} &= 0 \\
> 	\sum_{n=0}^\infty c_{n} \left( n+\gamma \right)\left( n - \dfrac{1}{2} + \gamma \right)t^{n-2+\gamma} - \sum_{n=0}^\infty c_{n}\dfrac{1}{2}t^{n-1+\gamma} &= 0 \\
> 	c_{0}\gamma\left(\gamma-\frac{1}{2}\right)t^{\gamma-2} + \sum_{n=1}^\infty c_{n} \left( n+\gamma \right)\left( n - \dfrac{1}{2} + \gamma \right)t^{n-2+\gamma} - \sum_{n=0}^\infty c_{n}\dfrac{1}{2}t^{n-1+\gamma} &= 0 \\
> 	c_{0}\gamma\left(\gamma-\frac{1}{2}\right)t^{\gamma-2} + \sum_{n=0}^\infty c_{n+1} \left( n+1+\gamma \right)\left( n + \dfrac{1}{2} + \gamma \right)t^{n-1+\gamma} - \sum_{n=0}^\infty c_{n}\dfrac{1}{2}t^{n-1+\gamma} &= 0 \\
> 	c_{0}\gamma\left(\gamma-\frac{1}{2}\right)t^{\gamma-2} + \sum_{n=0}^\infty \left[ c_{n+1} \left( n+1+\gamma \right)\left( n + \dfrac{1}{2} + \gamma \right) - c_{n}\dfrac{1}{2} \right]t^{n-1+\gamma} &= 0 \\
> 	t^{\gamma-1}\left( c_{0}\gamma\left(\gamma-\frac{1}{2}\right)t^{-1} + \sum_{n=0}^\infty \left[ c_{n+1} \left( n+1+\gamma \right)\left( n + \dfrac{1}{2} + \gamma \right) - c_{n}\dfrac{1}{2} \right]t^{n} \right) &= 0 \\
> \end{align}$$
> 
> 