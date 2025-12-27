---
tags:
  - atom
  - math
---
For all $f \in \mathcal{C}(\left[ a,b \right])$[^1], $f$ is [[Riemann-Stieltjes Integrals|Riemann-Stieltjes]] [[Math/Calculus/Integration/Integrability|integrable]] w.r.t. any [[Bounded Sets|bounded]] [[Monotone Sequences|monotonically increasing]] $g$ on $\left[ a,b \right]$.

> [!proof]-
> Since $f$ is [[Math/Calculus/Limits/Continuity/Continuity|continuous]] on $\left[ a,b \right]$, $f$ is [[Uniform Continuity|uniformly continuous]] on $\left[ a,b \right]$[^2].
> Thus, for all $\varepsilon > 0$, there exists $\delta(\varepsilon) > 0$ such that for all $x,y \in \left[ a,b \right]$,
> $$\left| x - y \right| < \delta(\varepsilon) \to \left| f(x) - f(y) \right| < \dfrac{\varepsilon}{2(g(b)-g(a))}.$$
> Consider a [[Interval Partitions|partition]] $P$ of $\left[ a,b \right]$ such that $\| P \| < \delta(\varepsilon)$.
> Then, the premise from above is satisfied for all $x,y \in \left[ x_{i-1},x_{i} \right]$ (for all $i$), giving
> $$M_{i} - m_{i} \leq \dfrac{\varepsilon}{2(g(b) - g(a))} < \dfrac{\varepsilon}{g(b)-g(a)}.$$
> Then
> $$\begin{align}
> 	\overline{S}(P;f,g) - \underline{S}(P;f,g) &= \sum_{i=1}^n (M_{i}-m_{i})(g(x_{i})-g(x_{i-1})) \\
> 	&< \dfrac{\varepsilon}{g(b)-g(a)} \sum_{i=1}^n \left[ g(x_{i})-g(x_{i-1}) \right] \\
> 	&= \varepsilon. && (1)
> \end{align}$$
> \[$(1)$ [[Telescoping Series]]\]


[^1]: [[Math/Calculus/Limits/Continuity/Continuity]]
[^2]: [[Uniform Continuity]], Theorem 4.26
