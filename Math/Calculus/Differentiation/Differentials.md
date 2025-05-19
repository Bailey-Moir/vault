---
tags:
  - atom
  - math
---
![400|center](differentials.excalidraw.md)
$$dy = f'(x) \,dx$$
$dy$ is a function of $dx$ and $x$. Differentials can be used to linearly approximate a function near its value.
>[!example]-
> Find maximum error of volume of a sphere if its radius is 21 cm with a maximum error or 0.05 cm.
> $$
> \begin{array}{l}
> 	V = \dfrac{4}{3}\pi r^3 \\
> 	\begin{alignat}{3}
> 		\Delta r &= dr &&= 0.05 \\
> 		\Delta V &\approx dV &&= 4\pi r^2 \, dr \\
> 		&&&= 4\pi(21)^2 \, 0.05 \\
> 		&&&= 88.2\pi \\
> 	\end{alignat} \\
> \end{array}
> $$
> Alternatively, the relative error can be used.
> $$
> \begin{align*}
> 	\dfrac{\Delta V}{V} &\approx \dfrac{dV}{V} \\
> 	&\approx \dfrac{4\pi r^2 \, dr}{\frac{4}{3}\pi r^3} \\
> 	&\approx 3\dfrac{dr}{r} \\
> 	&\approx 3\dfrac{0.05}{21} \\
> 	&\approx 0.24\% \\
> \end{align*}
> $$