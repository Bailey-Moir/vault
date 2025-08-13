---
tags:
  - atom
  - math
---
Suppose you have a [[Linear Differential Equations|linear]] [[Homogeneous Differential Equations|homogeneous]] second [[Order|order]] [[Ordinary Differential Equations|ODE]] (same as [[Auxiliary Equations|auxiliary]] except not constant coefficient)
$$a_{2}(t)y'' + a_{1}(t)y' + a_{0}(t)y = 0.$$
If you have one solution $y_{1}$, then the other solution can be given by
$$ y_{2}(t) = y_{1}(t) \int \dfrac{1}{y_{1}(t)^2}e^{\Phi(t)} \, dt \hspace{2em} \text{s.t. } \Phi(t) = \int-\dfrac{a_{1}(t)}{a_{2}(t)} \, dt $$

> [!proof]-
> If you have one solution $y_{1}$, then the other solution can be given by
> $$y_{2}(t) = u(t)y_{1}(t)$$
> for some $u(t)$. Plugging this in gives
> $$\begin{align}
> 	a_{2}(uy_{1})'' + a_{1}(uy_{1})' + a_{0}(uy_{1}) &= 0 \\
> 	a_{2}(u''y_{1} + 2u'y_{1}' + uy_{1}'') + a_{1}(u'y_{1} + uy_{1}') + a_{0}(uy_{1}) &= 0 \\
> 	u(a_{2}y_{1}''+a_{1}y_{1}'+ay_{1}) + u'(2a_{2}y_{1}'+a_{1}y_{1})+a_{2}y_{1}u'' &= 0 \\
> 	u(0) + u'(2a_{2}y_{1}'+a_{1}y_{1})+a_{2}y_{1}u'' &= 0  && \text{Original DE}\\
> 	u'(2a_{2}y_{1}'+a_{1}y_{1})+a_{2}y_{1}u'' &= 0 \\
> \end{align}$$
> This second [[Order|order]] [[Ordinary Differential Equations|ODE]] for $u$ has no $u$ term, meaning we can let $w = u'$, reducing it to first [[Order|order]].
> $$\begin{align}
> 	(a_{2}y_{1})w' + (2a_{2}y_{1}'+a_{1}y_{1})w &= 0 \\
> 	\dfrac{w'}{w}w' &= -\dfrac{2a_{2}y_{1}'+a_{1}y_{1}}{a_{2}y_{1}} \\
> 	&= -\dfrac{2y_{1}'}{y_{1}} - \dfrac{a_{1}}{a_{2}} \\
> \end{align}$$
> This can then be solved with [[Separation of Variables|separation of variables]]
> $$\begin{align}
> 	\int \dfrac{w'}{w} \, dw &= -2\int \dfrac{y_{1}'}{y_{1}} \, dt - \int \dfrac{a_{1}(t)}{a_{2}(t)} \, dt \\
> 	\ln \left| w \right| &= -2\ln \left| y_{1} \right| + \Phi(t) + c && \Phi(t) = \int-\dfrac{a_{1}(t)}{a_{2}(t)} \, dt \\
> 	w &= e^{-2\ln \left| y_{1} \right|  + \Phi(t) + c} \\
> 	w &= \dfrac{C}{y_{1}^2}e^{\Phi(t)} \\
> \end{align}$$
> Then,
> $$ y_{2}(t) = y_{1}(t) \int \dfrac{1}{y_{1}(t)^2}e^{\Phi(t)} \, dt \hspace{2em} \text{s.t. } \Phi(t) = \int-\dfrac{a_{1}(t)}{a_{2}(t)} \, dt $$