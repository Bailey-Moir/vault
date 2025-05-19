---
tags:
  - atom
  - math
---
Used to approximate values for the first [[Order|order]] [[Initial Value Problem|initial-value problems]].
$$\begin{align*}
	y_{n+1} &= y_{n} + f'(x_n) \Delta x && \Delta x = x_{n+1} - x_n \\
	&= y_{n} + dy\Bigr|_{x = x_n}^{dx = \Delta x} \\
\end{align*}$$
> [!note]- Proof
> This can be proven using [[Differentiation by First Principals|differentiation by first principals]].
> $$\begin{align*}
\dfrac{dy}{dx} &= \lim_{h\to 0} \left[ \dfrac{f(x+h)-f(x)}h \right] \\
\dfrac{dy}{dx}\Biggr|_{x=x_n} &= \lim_{\Delta x \to 0} \left[ \dfrac{y_{n+1}-y_n}{\Delta x} \right] \\
&= \dfrac{y_{n+1}-y_n}{dx}  \\
dy\Bigr|_{x=x_n}^{dx=\Delta x} &= y_{n+1}-y_n \\
y_{n+1} &= y_n + dy\Bigr|_{x=x_n}^{dx=\Delta x} \\
\end{align*}$$