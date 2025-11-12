---
tags:
  - atom
  - math
---
$$\mathcal{L}\left\{ y(t) \right\} = \int_{0}^\infty e^{-st}y(t) \, dt = Y(s)$$
> [!example]- $y'=y+4$, $y(0) = 1$
> Take the *Laplace transform* of both sides.
> **LHS** ($y'$)
> $$\begin{align}
> 	\mathcal{L}\left\{ y' \right\} &= \int_{0}^\infty e^{-st}y'(t) \, dt  \\
> 	&= e^{-st}y(t)\Bigr|_{0}^\infty + s\int_{0}^\infty e^{-st}y(t) \, dt  \\
> 	&= \lim_{ t \to \infty } e^{-st}y(t) - e^{0s}y(0) + s\int_{0}^\infty e^{-st}y(t) \, dt  \\
> 	&= -y(0) + s\int_{0}^\infty e^{-st}y(t) \, dt && s > 0 \\
> 	&= -1 + sY \\
> \end{align}$$
> **RHS** $(y+4)$
> $$\begin{align}
> 	\mathcal{L}\left\{ y+4 \right\} &= \int_{0}^\infty e^{-st}\left( y(t) + 4 \right)\,dt \\ 
> 	&= \int_{0}^\infty e^{-st}y(t) \,dt + 4\int_{0}^\infty e^{-st} \, dt \\ 
> 	&= \int_{0}^\infty e^{-st}y(t) \,dt - \dfrac{4}{s}\left[ \lim_{ t \to \infty } e^{-st} - e^{0s} \right] \\ 
> 	&= Y + \dfrac{4}{s} && s >0\\ 
> \end{align}$$
> 
> Thus, 
> $$\begin{align}
> 	\mathcal{L}\left\{ \text{LHS} \right\} &= \mathcal{L}\left\{ \text{RHS} \right\} \\
> 	-1+sY &= Y+\dfrac{4}{s} \\
> 	sY - Y &= \dfrac{4}{s} + 1 \\
> 	(s-1)Y &= \dfrac{4}{s} + 1 \\
> 	Y &= \dfrac{4}{s(s-1)} + \dfrac{1}{s-1} \\
> 	Y &= \dfrac{4}{s-1} - \dfrac{4}{s} + \dfrac{1}{s-1} && \text{(1)} \\
> 	Y &= \dfrac{5}{s-1} - \dfrac{4}{s} \\
> \end{align}$$
> \[$(1)$ [[Partial Fraction Decomposition]]\]
> 
> To solve for $y(t)$,
> $$\begin{align}
> 	\mathcal{L}\left\{ y \right\} &= Y \\
> 	y &= \mathcal{L}^{-1}\left\{ Y \right\} \\
> 	y &= \mathcal{L}^{-1}\left\{ \dfrac{5}{s-1} - \dfrac{4}{s} \right\} \\
> 	y &= 5\mathcal{L}^{-1}\left\{ \dfrac{1}{s-1} \right\} - 4^{-1}\mathcal{L}\left\{ \dfrac{1}{s} \right\} \\
> 	y &= 5e^t - 4, \\
> \end{align}$$
> using the [[Laplace Transforms Table|Laplace transforms table]].

> [!theorem] *Laplace transforms* are [[Linear Maps|linear maps]].

> [!method]-
> Convert a [[Differential Equations|differential equation]] for $y(t)$ to an algebraic equation for $Y(s) = \mathcal{L}\left\{ y(t) \right\}$. After solving for $Y$, the solution to the original [[Differential Equations|DE]] is given by $y(t) = \mathcal{L}^{-1}\left\{ Y(s) \right\}$.

> [!theorem]- If $f : \left[ 0,\infty \right)$ is [[Piecewise Continuity|piecewise continuous]] and for some constant $c$,  $f(t) \in \mathcal{O}(e^{ct})$, then $\mathcal{L}\left\{ f(t) \right\}$ exists for sufficiently large $s$.
> Suppose the premise. Then
> $$\begin{align}
> 	\left| \mathcal{L}\left\{ f(t) \right\} \right| 
> 	&= \left| \int_{0}^\infty e^{-st}f(t) \, dt \right|  \\
> 	&\le \int_{0}^\infty e^{-st} \left| f(t) \right|  \, dt && \text{(1)} \\
> 	&\le \int_{0}^\infty e^{-st} Me^{ct}  \, dt \\
> 	&= M\int_{0}^\infty e^{(c-s)t} \, dt \\
> 	&= \dfrac{M}{c-s}e^{(c-s)t}\Bigr|_{0}^\infty \\
> 	&= \dfrac{M}{c-s}\left[ \lim_{ t \to \infty } e^{(c-s)t} - e^0 \right]  \\
> 	&= \dfrac{M}{c-s}\left[ 0 - 1 \right] && s > c \\
> 	&= \dfrac{M}{s-c} \\
> \end{align}$$
> Thus, for all $s>c$, $\mathcal{L}\{ f(t) \} \le \dfrac{M}{s-c}$ exists.
\[$(1)$ [[Triangle Ineqaulity]]\]