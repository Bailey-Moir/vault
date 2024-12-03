---
tags:
  - atom
  - math
---
$$ L = \int_\alpha^\beta \sqrt{r^2 + \left[\dfrac{dr}{d\theta}\right]^2} d\theta $$
> [!proof]-
> $$\begin{align*}
> 	L &= \int_a^b \sqrt{ \left[ \dfrac{dx}{dt} \right]^2 + \left[ \dfrac{dy}{dt} \right]^2} \, dt \phantom{aaaaaaa} (1) \text{ Parametric Arc Length Formula} \\
> 	&= \int_\alpha^\beta \sqrt{ \left[ \dfrac{dx}{d\theta} \right]^2 + \left[ \dfrac{dy}{d\theta} \right]^2} \, d\theta \\
> 	&= \int_\alpha^\beta \sqrt{ \left[ \dfrac{dr}{d\theta}\cos\theta - r\sin\theta \right]^2 + \left[ \dfrac{dr}{d\theta}\sin\theta + r\cos\theta \right]^2} \, d\theta \\
> 	&= \int_\alpha^\beta \sqrt{ \left[ \left(\dfrac{dr}{d\theta}\right)^2\cos^2\theta - 2\dfrac{dr}{d\theta}r\sin\theta\cos\theta + r^2\sin^2\theta \right] + \left[ \left(\dfrac{dr}{d\theta}\right)^2\sin^2\theta + 2\dfrac{dr}{d\theta}r\sin\theta\cos\theta + r^2\cos^2\theta \right]} \, d\theta \\
> 	&= \int_\alpha^\beta \sqrt{ \left[\dfrac{dr}{d\theta}\right]^2\left( \cos^2\theta + \sin^2\theta \right) + r^2\left(\sin^2\theta + \cos^2\theta\right) } \, d\theta \\
> 	&= \int_\alpha^\beta \sqrt{ r^2 + \left[\dfrac{dr}{d\theta}\right]^2 } \, d\theta \\
> \end{align*}$$ 
> \[$(1)$ [[Parametric Arc Length]]\]