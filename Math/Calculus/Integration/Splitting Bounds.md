---
tags:
  - atom
  - math
---
Let $f$ be a [[Functions|function]] on the [[Intervals|interval]] $\left[ a,b \right]$ and let $c \in \left[ a,b \right]$. Then $f$ is [[Math/Calculus/Integration/Integrability|integrable]] w.r.t $g$ on $\left[ a,b \right]$ iff it is [[Math/Calculus/Integration/Integrability|integrable]] w.r.t $g$ on the [[Intervals|sub-intervals]] $\left[ a,c \right]$ and $\left[ c,b \right]$. In either case,
$$\int_{a}^b f \, dg = \int_{a}^c f \, dg + \int_{c}^b f \, dg.$$
> [!proof]-
> $\left( \implies \right)$
> Suppose $f$ is [[Riemann-Stieltjes Integrals|R-S]] [[Math/Calculus/Integration/Integrability|integrable]] w.r.t $g$ on $\left[ a,b \right]$. Then by the definition of [[Math/Calculus/Integration/Integrability|integrability]], for all $\varepsilon>0$, there exists a [[Interval Partitions|partition]] $P_{\varepsilon}$ of $\left[ a,b \right]$ such that
> $$\overline{S}(P_{\varepsilon};f,g) - \underline{S}(P_{\varepsilon};f,g) < \varepsilon.$$
> Let $c \in \left[ a,b \right]$ be such that $c = x_i$ for some $x_{i} \in P\varepsilon$, and let $P_{\varepsilon}' = \left( x_{0},\dots,x_{i} \right)$ and $P_{\varepsilon}''=\left( x_{i},\dots,x_{n} \right)$. Thus, by the definition of a [[Riemann-Stieltjes Sums|R-S sum]],
> $$S(P_{\varepsilon};f,g) = S(P_{\varepsilon}';f,g) + S(P_{\varepsilon}'';f,g).$$
> Thus,
> $$\begin{align}
> 	\left[ \overline{S}(P_{\varepsilon}';f,g) -\underline{S}(P_{\varepsilon}';f,g) \right] + \left[ \overline{S}(P_{\varepsilon}'';f,g) -\underline{S}(P_{\varepsilon}'';f,g) \right]  \\
> 	= \overline{S}(P_{\varepsilon};f,g) - \underline{S}(P_{\varepsilon};f,g) < \varepsilon
> \end{align}$$
> Since $\overline S > \underline{S}$, the two bracketed terms must be positive, and thus each must respectively be less than $\varepsilon$. Thus, $f$ is [[Math/Calculus/Integration/Integrability|integrable]] w.r.t $g$ on $\left[ a,c \right]$ and $\left[ c,b \right]$ . Then
> $$\begin{array}{cl}
> 	\displaystyle\underline{S}(P_{\varepsilon}';f,g) < \int_{a}^c f\,dg < \overline{S}(P_{\varepsilon}';f,g) && 1 \\
> 	\displaystyle\underline{S}(P_{\varepsilon}'';f,g) < \int_{c}^b f\,dg < \overline{S}(P_{\varepsilon}'';f,g && 2 \\
> 	\displaystyle\underline{S}(P_{\varepsilon};f,g) < \int_{a}^c f\,dg + \int_{c}^b f\,dg < \overline{S}(P_{\varepsilon};f,g) && 1+2 \\
> \end{array}$$
> Thus, since the integral of $f$ w.r.t $g$ on $\left[ a,b \right]$ is unique,
> $$\int_{a}^b f\, dg = \int_{a}^c f\,dg + \int_{c}^b f\,dg$$
> $\left( \impliedby \right)$
> Suppose $f$ is [[Math/Calculus/Integration/Integrability|integrable]] w.r.t $g$ on $\left[ a,c \right]$ and $\left[ c,b \right]$.
> Then for $\varepsilon > 0$, there exists [[Interval Partitions|partitions]] $P_{\varepsilon}'$ and $P_{\varepsilon}''$ of $\left[ a,c \right]$ and $\left[ c,b \right]$ respectively such that
> $$\begin{align}
> 	\overline{S}(P_{\varepsilon}';f,g) - \underline{S}(P_{\varepsilon}';f,g) &< \dfrac{\varepsilon}{2} && 1 \\
> 	\overline{S}(P_{\varepsilon}'';f,g) - \underline{S}(P_{\varepsilon}'';f,g) &< \dfrac{\varepsilon}{2}. && 2 \\
> \end{align}$$
> Take $P_{\varepsilon} = P_{\varepsilon}'\cup P_{\varepsilon}''$, a [[Partitions|partition]] of $\left[ a,b \right]$. Then 
> $$\begin{align}
> 	\overline{S}(P_{\varepsilon};f,g) - \underline{S}(P_{\varepsilon};f,g) &< \varepsilon. && 1+2 \\
> \end{align}$$
> Thus, $f$ is [[Math/Calculus/Integration/Integrability|integrable]] w.r.t $g$ on $\left[ a,b \right]$.
