---
tags:
  - atom
  - math
---
You can split [[Order|2nd order]] [[Linear Differential Equations|linear]] DEs into two [[Order|2nd order]] [[Linear Differential Equations|linear]] DEs. This is a more formal version of solving with [[Differential Operators|differential operators]].

> [!example]-
> $$\begin{align*}
> 	y'' + 3y' + 2y &= 0 \\
> 	y'' + + 2y' + y' + 2y &= 0 \\
> 	(y' + 2y)' + (y' + 2y) &= 0 \\
> \end{align*}$$
> Let $z = y' + 2y$
> $$z' + z = 0$$
> First you can solve $z$ by [[Integrating Factor Method|integrating factor method]]:
> $$\begin{align*}
> 	e^xz' + e^xz &= 0e^x \\
> 	\dfrac{d}{dx}\left( e^xz \right) &= 0 \\
> 	e^xz &= \int 0 \, dx \\
> 	z &= ce^{-x} \\
> \end{align*}$$
> Now you can substitute this into the other DE, and again apply [[Integrating Factor Method|integrating factor method]].
> $$\begin{align*}
> 		y' + 2y &= ce^{-x} \\
> 		e^{2x}y' + 2e^{2x}y &= ce^{x} \\
> 		\dfrac{d}{dx}\left( e^{2x}y \right) &= ce^{x} \\
> 		e^{2x}y &= \int ce^{x} \, dx \\
> 		e^{2x}y &= c_1e^{x} + c_2\\
> 		y &= c_1e^{-x} + c_2e^{-2x}\\
> \end{align*}$$