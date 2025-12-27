---
tags:
  - atom
  - math
---
 Euler's method* is an iterative, explicit, single-step method used to approximate values for first [[Order|order]] [[Initial Value Problem|initial-value problems]].
$$\begin{align*}
	y_{n+1} &= y_{n} + f'(t_n,y(t_{n})) h && h = t_{n+1} - t_n \\
	&= y_{n} + dy\Bigr|_{t = t_n}^{dt = h} \\
\end{align*}$$
> [!proof*]-
> This can be proven (ish) using [[Differentiation by First Principals|differentiation by first principals]].
> $$\begin{align*}
\dfrac{dy}{dx} &= \lim_{h\to 0} \left[ \dfrac{f(x+h)-f(x)}h \right] \\
\dfrac{dy}{dx}\Biggr|_{x=x_n} &= \lim_{\Delta x \to 0} \left[ \dfrac{y_{n+1}-y_n}{\Delta x} \right] \\
&= \dfrac{y_{n+1}-y_n}{dx}  \\
dy\Bigr|_{x=x_n}^{dx=\Delta x} &= y_{n+1}-y_n \\
y_{n+1} &= y_n + dy\Bigr|_{x=x_n}^{dx=\Delta x} \\
\end{align*}$$

## [[Local Truncation Error]]
$$\begin{align}
	\left| y(t_{n})-y_{n} \right| &\le \dfrac{M(t_{n}-t_{0})}{2}h = \mathcal{O}(h) \\
	\left| y(t_{1})-y_{1} \right| &\le \dfrac{M}{2}h^2 = \mathcal{O}(h^2) \\
\end{align}$$
> [!proof]-
> By [[Taylor Series|Taylor's theorem]] (with [[Taylor's Lagrange Remainder|remainder theorem]]),
> $$y(t_{1})=y(t_{0})+y'(t_{0})h+\dfrac{y''(c)}{2}h^2$$
> for some $c \in \left( t_{0},t_{1} \right)$ (note $t_{1} = t_{0}+h$). Suppose $y''(t)$ is [[Math/Calculus/Limits/Continuity/Continuity|continuous]] on $\left[ t_{0},t_{1} \right]$. Then it is [[Bounded Sets|bounded]][^1], so let $\left| y'' \right| \leq M$ for some $M$ on $(t_{0},t_{1})$. Then
> $$\begin{align}
> 	y(t_{1}) &= \left( y(t_{0})+y'(t_{0})h \right) + \dfrac{y''(c)}{2}h^2 \\
> 	&= y_{1} + \dfrac{y''(c)}{2}h^2 \\
> 	y(t_{1})-y_{1} &= \dfrac{y''(c)}{2}h^2 \\
> 	\left| y(t_{1})-y_{1} \right|  &= \left| \dfrac{y''(c)}{2}h^2 \right|  \\
> 	\left| y(t_{1})-y_{1} \right|  &= \dfrac{\left| y''(c) \right| }{2}h^2 \le \dfrac{M}{2}h^2. \\
> \end{align}$$
> If this $\left| y'' \right|\le M$ on $\left( t_{0},t_{1} \right)$, then summing these [[Local Truncation Error|LTE]]s for $n$ iterations gives
> $$\begin{align}
> 	\left| y(t_{n}) - y_{n} \right| &\le \sum_{i=0}^n \left| y(t_{i})-y_{i} \right| && (1) \text{ Triangle Inequality} \\
> 	&\le \sum_{i=0}^n \dfrac{M}{2}h^2 \\
> 	&= n\dfrac{M}{2}h^2 \\
> 	&= \dfrac{t_{n}-t_{0}}{h}\dfrac{M}{2}h^2 \\
> 	&= \dfrac{\left( t_{n}-t_{0} \right)M}{2}h \\
> \end{align}$$
> \[$(1)$ [[Triangle Ineqaulity]] Corollary 1.12.2\]

\[[[Landua's Big Oh Notation]]\]

[^1]: [[Boundedness of Continuous Functions]]
