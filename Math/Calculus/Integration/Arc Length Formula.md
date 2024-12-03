---
tags:
  - math
  - atom
---
If $f' \in \mathcal{C}([a,b])$, then the length of it's curve $y = f(x)$, $a \le x \le b$ is
$$\begin{align*}
	L &= \int_a^b \sqrt{1 + \left[f'(x)\right]^2} \, dx \\
	&= \int_{t_1}^{t_2} \sqrt{\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2} \, dt && (1) \text{ Parametric Arc Legnth Formula} \\
	&= \int_\alpha^\beta \sqrt{r^2 + \left[\dfrac{dr}{d\theta}\right]^2} d\theta && (2) \text{ Polar Arc Legnth Formula} \\
\end{align*}$$
\[$(1)$ [[Parametric Arc Length|Parametric Arc Length]], $(2)$ [[Polar Arc Length Formula|Polar Arc Length Formula]]\]
> [!proof]-
> $$
> \begin{align*}
> 	L &= \lim_{n\to\infty} \sum_{i=1}^n \sqrt{ \left[\Delta x\right]^2 + \left[f'(x_i^*)\Delta x\right]^2 } \\
> 	&= \lim_{n\to\infty} \sum_{i=1}^n \sqrt{ 1 + \left[f'(x_i^*)\right]^2 } \Delta x \\
> 	&= \int_a^b \sqrt{ 1 + \left[f'(x)\right]^2 } \, dx && \text{Integration by First Principles}
> \end{align*}
> $$
> \[$(1)$ [[Integration by First Principals]]\]

# Arc Length Function
![300|center](arc-length-differentials.excalidraw)
$$\begin{array}{c}
	\displaystyle s(x) = \int_a^x \sqrt{1 + \left[ f'(t) \right]^2} \, dt \\
	\displaystyle ds = \sqrt{\left[dx\right]^2 + \left[dy\right]^2} \\
	\displaystyle \phantom{ds} = \sqrt{1 + \left[ \dfrac{dy}{dx} \right]^2} \, dx \\
	\displaystyle \phantom{ds} = \sqrt{1 + \left[ \dfrac{dx}{dy} \right]^2} \, dy \\
\end{array}$$
\[[[Differentials|Differentials]]\]