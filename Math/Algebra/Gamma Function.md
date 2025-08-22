---
tags:
  - atom
  - math
---
The *Euler Gamma Function* is defined by
$$\begin{align*}
	\Gamma(z) &= \int_{0}^\infty e^{-t}t^{z-1} \, dt && \text{Re}(z) > 0 \\ 
	&= \lim_{ n \to \infty } \dfrac{n!n^z}{\prod_{r=0}^n(z+r)} && z \in \C - \Z^- \\ 
\end{align*}$$
- $\Gamma(n+1) = n\Gamma(n)$
  > [!proof]-
> $$\begin{align*}
> 	\Gamma(n + 1) &= \int_{0}^\infty e^{-t} t^n dt \\
> 	&= \left[ -e^{-t}t^{n} \right]_{0}^\infty - n\int_{0}^\infty -e^{-t} nt^{n-1} dt \\
> 	&= n\int_{0}^\infty e^{-t} t^{n-1} dt \\
> 	&= n\Gamma(n) \\
> \end{align*}$$

- $\forall n \in \N, n! = \Gamma(n+1)$
- $\Gamma(\frac{1}{2}) = \sqrt{ \pi }$