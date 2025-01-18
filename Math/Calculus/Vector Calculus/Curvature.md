---
tags:
  - atom
  - math
---
The *curvature* of a curve is
$$\begin{align*}
	\kappa &= \left\| \dfrac{d\vecbf{T}}{ds} \right\| \\ 
	&= \dfrac{\left\| \vecbf{T}' \right\|}{\left\| \vecbf{r}' \right\|} && (1)\\
	&= \dfrac{\left\| \vecbf{r}' \times \vecbf{r}'' \right\|}{\left\| \vecbf{r}' \right\|^3} && (2)\\
\end{align*}$$
> [!proof]- (1)
> $$\begin{array}{cc|c}
> 	\begin{array}[t]{rl}
> 		\kappa\hspace{-0.5em} &= \left\| \dfrac{d\vecbf{T}}{ds} \right\| \\
> 		&= \left\| \dfrac{\dfrac{d\vecbf{T}}{dt}}{\dfrac{ds}{dt}} \right\| \\
> 	\end{array} &&
> 	\begin{array}[t]{rl}
> 		 \phantom{\kappa}&= \left\| \dfrac{\vecbf{T}'(t)}{\left\| \vecbf{r}'(t) \right\| } \right\| && (3)\\
> 		 &= \dfrac{\left\| \vecbf{T}'(t) \right\|}{\left\| \vecbf{r}'(t) \right\| } \\
> 	\end{array}
> \end{array}$$
> \[(3) [[Parametric Arc Length]]\]

> [!proof]- (2)
> By the definition of a [[Unit Tangent Vectors|unit tangent vector]] and [[Parametric Arc Length|parametric arc length]],
> $$\begin{align*}
> 	\vecbf{r}' = \left\| \vecbf{r}' \right\| \vecbf{T} &= \dfrac{ds}{dt}\vecbf{T} \\
> 	\vecbf{r}'' &= \dfrac{d^2s}{dt^2} \vecbf{T} + \dfrac{ds}{dt}\vecbf{T}' && \text{(1)}\\
> \end{align*}$$
> \[(1) [[Differentiation Rules#Product Rule]]\]
> By the [[Cross Product#Properties of Cross Product|properties of the cross product]], the cross product of these derivatives gives
> $$\begin{align*}
> 	\vecbf{r}' \times \vecbf{r}'' &= \left( \dfrac{ds}{dt}\vecbf{T} \right) \times \left( \dfrac{d^2s}{dt^2}\vecbf{T} + \dfrac{ds}{dt}\vecbf{T}' \right) \\
> 	&= \left( \dfrac{ds}{dt}\vecbf{T} \right) \times \left( \dfrac{d^2s}{dt^2}\vecbf{T} \right) + \left( \dfrac{ds}{dt}\vecbf{T} \right) \times \left( \dfrac{ds}{dt}\vecbf{T}' \right) \\
> 	&= \dfrac{ds}{dt} \dfrac{d^2s}{dt^2} \left( 0 \right) + \left( \dfrac{ds}{dt} \right)^2 \left( \vecbf{T} \times \vecbf{T}' \right) \\
> 	&= \left( \dfrac{ds}{dt} \right)^2 \left( \vecbf{T} \times \vecbf{T}' \right) \\
> \end{align*}$$
> Thus
> $$\begin{align*}
> 	\left\| \vecbf{r}' \times \vecbf{r}'' \right\| &= \left( \dfrac{ds}{dt} \right)^2 \left\| \vecbf{T} \times \vecbf{T}' \right\| \\
> 	&= \left( \dfrac{ds}{dt} \right)^2 \left\| \vecbf{T} \right\| \left\| \vecbf{T}' \right\| \\
> 	&= \left( \dfrac{ds}{dt} \right)^2 \left\| \vecbf{T}' \right\| && \left\| \vecbf{T} \right\| = 1  \\
> 	\end{align*}$$
> Rearranging gives
> $$\begin{align*}
> 	 \left\| \vecbf{T}' \right\| &= \dfrac{\left\| \vecbf{r}' \times \vecbf{r}'' \right\|}{\left( \dfrac{ds}{dt} \right)^2}  \\
> 	 &= \dfrac{\left\| \vecbf{r}' \times \vecbf{r}'' \right\|}{\left\| \vecbf{r}' \right\|^2} \\
> \end{align*}$$
> Plugging this into the formula for $\kappa$,
> $$ \kappa = \dfrac{\left\| \vecbf{T}' \right\|}{\left\| \vecbf{r}' \right\|} = \dfrac{\left\| \vecbf{r}' \times \vecbf{r}'' \right\|}{\left\| \vecbf{r}' \right\|^3} $$

\[[[Unit Tangent Vectors]], [[Parametric Arc Length]]\]