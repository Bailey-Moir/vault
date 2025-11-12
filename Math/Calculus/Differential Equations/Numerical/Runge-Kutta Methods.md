---
tags:
  - atom
  - math
---
*Runge-Kutta* (*RK*) models are iterative, explicit, single-step methods used for $m$-[[Order|order]] approximations of [[Initial Value Problem|initial-value problems]]. This is done by iteratively computing $m$ slopes:
$$\begin{align}
	k_{1} &= f(t_{i},y_{i}) \\
	k_{2} &= f(t_{i} + \alpha_{1},y_{i} + \left( \beta_{1}k_{1} \right)h) \\
	k_{3} &= f(t_{i} + \alpha_{2},y_{i} + \left( \beta_{2}k_{2} + \beta_{3}k_{3} \right)h) \\
	k_{4} &= f(t_{i} + \alpha_{3},y_{i} + \left( \beta_{4}k_{4} + \beta_{5}k_{5} + \beta_{6}k_{6} \right)h) \\
	&\hspace{0.5em}\vdots \\
	k_{m} &= f\left( t_{i} + \alpha_{m-1},y_{i} + h\sum_{i=T_{m-1}}^{T_{m}}\beta_{i}k_{i} \right) \\
\end{align}$$
The update is then computed as
$$y_{i+1} = y_{i} + h\sum_{i=1}^mw_{i}k_{i},$$
for some weights $w_{1},\dots,w_{m}$.

These $\alpha$s, $\beta$s, and $w$s must be chosen such that $y_{i+1}$ matches the first $m$ terms of the [[Taylor Series|Taylor series]] (which would imply the [[Local Truncation Error|LTE]] is $\mathcal{O}(h^{m+1})$).
