---
tags:
  - atom
  - math
---
![550|center](heaviside.excalidraw)
The *Heaviside* (or *unit step*) *[[Functions|function]]* is defined as
$$H(t) = \begin{cases}
	0 & t < 0 \\
	1 & t \ge 0
\end{cases}$$

> [!example]- $\mathcal{L}\{ H(t-a) \}$[^1]
> $$\begin{align}
> 	\mathcal{L}\{ H(t-a) \} \\
> 	&= \int_{0}^\infty e^{-st}H(t-a)dt \\
> 	&= \int_{0}^a e^{-st}0 dt + \int_{a}^\infty e^{-st}1 dt \\
> 	&= \int_{a}^\infty e^{-st} dt \\
> 	&= -\dfrac{1}{s}e^{-st}\Bigr|_{a}^\infty \\
> 	&= -\dfrac{1}{s}\left[ 0-e^{-as} \right] \\
> 	&= \dfrac{e^{-as}}{s} \\
> \end{align}$$

[^1]: [[Laplace Transforms]]
