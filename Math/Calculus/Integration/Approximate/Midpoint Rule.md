---
tags:
  - math
  - atom
aliases:
---
The *midpoint rule* is a type of [[Approximate Integration|approximate integration]] by centred [[Riemann Sums|Riemann sum]].
![400|center](midpoint-rule.excalidraw.md)
$$\begin{array}{l}
	\displaystyle\int_a^b f(x) \, dx \approx M_n = \Delta x [ f(\overline x_1) + f(\overline x_2) + \dots + f(\overline x_n) ] \\
	\text{where } \Delta x = (b-a)/n \\
	\begin{alignat}{2}
		\text{and } \overline x_i &= (x_{i-1} + x_i)/2 \\
		&= a + \left(i- \dfrac{1}{2} \right)\Delta x \\ 
		&= \text{midpoint of } \left[ x_{i-1}, x_i \right] \\
	\end{alignat} \\
\end{array}$$
