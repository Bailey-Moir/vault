---
tags:
  - atom
  - math
---
$$ L = \int_\alpha^\beta \sqrt{\left(\dfrac{dx}{dt}\right)^2 + \left(\dfrac{dy}{dt}\right)^2} \, dt $$
> [!proof]-
> $$
> \begin{align*}
> 	L &= \int_a^b \sqrt{1 + \left[ \dfrac{dy}{dx} \right]^2} \, dx \\
> 	&= \int_a^b \sqrt{1 + \left[ \dfrac{dy}{dt}\Big/\dfrac{dx}{dt} \right]^2} \, dx && \hspace{-3em}(1) \text{ Cartesian Arc Length Formula} \\
> 	&= \int_a^b \dfrac{1}{\dfrac{dx}{dt}}\sqrt{\left[ \dfrac{dx}{dt} \right]^2 + \left[ \frac{dy}{dt} \right]^2} \, dx \\
> 	&= \int_\alpha^\beta \sqrt{\left[ \dfrac{dx}{dt} \right]^2 + \left[ \frac{dy}{dt} \right]^2} \, dt \\
> \end{align*}
> $$
> \[$(1)$ [[Arc Length Formula|Cartesian Arc length Formula]]\]

\[[[Parametric Form]], [[Atoms/Calculus/Integration/Integration|Integration]]\]