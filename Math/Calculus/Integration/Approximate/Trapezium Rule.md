---
tags:
  - math
  - atom
---
[[Approximate Integration|Approximate integration]] by averaging a left handed and right handed [[Riemann Sums|Riemann sum]].
![400|center](trapezium-rule.excalidraw)
$$\begin{array}{l}
	\begin{align*}
		\int_a^b f(x) \, dx \approx T_n  &= \Delta x\left[ \dfrac{1}{2}\left( f(x_0) + f(x_n) \right) + f(x_1) + f(x_2) + \dots + f(x_{n-1}) \right] \\
		&= \Delta x\left[ \dfrac{1}{2}\left( f(x_0) + f(x_1) \right) + \dfrac{1}{2}\left( f(x_1) + f(x_2) \right) + \dots + \dfrac{1}{2}\left( f(x_{n-1}) + f(x_{n}) \right) \right] \\
		&=\dfrac{\Delta x}{2}\left[ \sum_{i=1}^n \left( f(x_{i-1}) + f(x_i) \right) \right] \\
		&= (L_n + R_n)/2 \\
	\end{align*} \\
	\text{where } \Delta x = \left( b-a \right)/2 \\
	\text{and } x_i = a+i\Delta x
\end{array}$$
<iframe src="https://www.desmos.com/calculator/gveuzvqnku?embed" height="300" style="width:100%; margin-bottom: -20px;"></iframe>
