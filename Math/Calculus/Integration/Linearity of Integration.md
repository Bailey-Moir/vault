---
tags:
  - atom
  - math
---
Let $f$, $y$, $g$ and $h$ be [[Functions|functions]], $c \in \R$, and $\left[ a,b \right] \subseteq \text{dom}\,f \cap\text{dom}\,g$.
If $f$ and $y$ are [[Math/Calculus/Integration/Integrability|integrable]] with respect to $g$ and $h$ on $\left[ a,b \right]$,
 - **Homogeneity**
   then $cf$ is [[Math/Calculus/Integration/Integrability|integrable]] with respect to $g$ on $\left[ a,b \right]$, and
$$\int_{a}^b cf \, dg = c\int_{a}^b f \, dg,$$
   and $f$ is [[Math/Calculus/Integration/Integrability|integrable]] with respect to $cg$ on $\left[ a,b \right]$
$$\int_{a}^b f \, d(cg) = c\int_{a}^b f \, dg,$$
 - **Additive Property**
   then $f+y$ is [[Math/Calculus/Integration/Integrability|integrable]] with respect to $g$ on $\left[ a,b \right]$, and
$$\int_{a}^b f+y \, dg = \int_{a}^b f \, dg + \int_{a}^b y \, dg$$
   and $f$ is [[Math/Calculus/Integration/Integrability|integrable]] with respect to $g+h$ on $\left[ a,b \right]$
$$\int_{a}^b f \, d(g+h) = \int_{a}^b f \, dg + \int_{a}^b f \, dh$$

> [!proof]- Homogenity
> Assume $c>0$, and $f$ is [[Math/Calculus/Integration/Integrability|integrable]] with respect to $g$.
> 
> Let $P$ be a [[Interval Partitions|partition]] of $\left[ a,b \right]$. Then by the definition of [[Riemann-Stieltjes Sums#Upper and Lower Riemann-Stieltjes Sums|upper and lower Riemann-Stieltjes sums]],
> $$\begin{array}{c}
> \displaystyle M_{i}(cf) = \hspace{-0.8em}\sup_{x \in \left[ x_{k-1},x_{k} \right] }\hspace{-0.8em} cf(x) = c\hspace{-0.8em}\sup_{x \in \left[ x_{k-1},x_{k} \right] }\hspace{-0.8em} f(x) = cM_{i}\phantom{.} \\
> \displaystyle m_{i}(cf) = \hspace{-0.8em}\inf_{x \in \left[ x_{k-1},x_{k} \right] }\hspace{-0.8em} cf(x) = c\hspace{-0.8em}\inf_{x \in \left[ x_{k-1},x_{k} \right] }\hspace{-0.8em} f(x) = cm_{i}, \\
> \end{array}$$
> and
> $$\overline{S}(P;cf,g) - \underline{S}(P;cf,g) = c\left( \overline{S}(P;f,g) - \underline{S}(P;f,g) \right).$$
> By the [[Math/Calculus/Integration/Integrability|integrability]] of $f$ w.r.t $g$ on $\left[ a,b \right]$, we know that for all $\varepsilon>0$,
> $$\begin{align}
> 	\overline{S}(P;cf,g) - \underline{S}(P;cf,g) &< \dfrac{\varepsilon}{c} \\
> 	c(\overline{S}(P;cf,g) - \underline{S}(P;cf,g)) &< \varepsilon.
> \end{align}$$
> Thus, $cf$ is [[Math/Calculus/Integration/Integrability|integrable]] w.r.t $g$ on $\left[ a,b \right]$.
> 
> Note that
> $$\begin{array}{c}
> 	\displaystyle\underline{S}(P;cf,g) \le \int_{a}^b f \, dg \le \overline{S}(P;cf,g) \\
> 	c\displaystyle\underline{S}(P;cf,g) \le c\int_{a}^b f \, dg \le c\overline{S}(P;cf,g) \\
> 	\displaystyle\underline{S}(P;cf,g) \le c\int_{a}^b f \, dg \le \overline{S}(P;cf,g). \\
> \end{array}$$
> Since $cf$ is [[Math/Calculus/Integration/Integrability|integrable]] w.r.t $g$ on $\left[ a,b \right]$, its value must be unique, so
> $$\int_{a}^b cf\,dg = c \int_{a}^b f \,dg$$

> [!proof]- Additive Property
> Let $P = (x_{0},\dots,x_{n})$ be a [[Interval Partitions|partition]] of $\left[ a,b \right]$. Then by the definition of [[Riemann-Stieltjes Sums#Upper and Lower Riemann-Stieltjes Sums|upper and lower Riemann-Stieltjes sums]],
> $$\begin{array}{c}
> \displaystyle M_{i}(f+y) = \hspace{-0.8em}\sup_{x \in \left[ x_{k-1},x_{k} \right] }\hspace{-0.8em} (f+y)(x) \le \hspace{-0.8em}\sup_{x \in \left[ x_{k-1},x_{k} \right] }\hspace{-0.8em} f(x) + \hspace{-0.8em}\sup_{x \in \left[ x_{k-1},x_{k} \right] }\hspace{-0.8em} y(x)= M_{i}(f) + M_{i}(y) \\
> \displaystyle m_{i}(f+y) = \hspace{-0.8em}\inf_{x \in \left[ x_{k-1},x_{k} \right] }\hspace{-0.8em} (f+y)(x) \ge \hspace{-0.8em}\inf_{x \in \left[ x_{k-1},x_{k} \right] }\hspace{-0.8em} f(x) + \hspace{-0.8em}\inf_{x \in \left[ x_{k-1},x_{k} \right] }\hspace{-0.8em} y(x)= m_{i}(f) + m_{i}(y), \\
> \end{array}$$
> and
> $$\begin{array}{c}
> 	\overline{S}(P;f+y,g) \le \overline{S}(P;f,g) + \overline{S}(P;y,g) \\
> 	\underline{S}(P;f+y,g) \ge \underline{S}(P;f,g) + \underline{S}(P;y,g). \\
> \end{array}$$
> By the [[Math/Calculus/Integration/Integrability|integrability]] of $f$ and $y$ w.r.t. $g$ over $\left[ a,b \right]$, for all $\varepsilon>0$, there exists [[Partitions|partitions]] $P_{1}$ and $P_{2}$ such that
> $$\begin{align}
> 	\overline{S}(P_{1};f,g) - \underline{S}(P_{1};f,g) &< \dfrac{\varepsilon}{2} \\
> 	\overline{S}(P_{2};y,g) - \underline{S}(P_{2};y,g) &< \dfrac{\varepsilon}{2}. \\
> \end{align}$$
> Combining these gives [[Partitions|partitions]] to get $P=P_{1}\cup P_{2}$, we get
> $$\overline{S}(P;f,g) + \overline{S}(P;y,g) - \left[ \underline{S}(P;f,g) + \underline{S}(P;y,g) \right] < \varepsilon.$$
> Therefore,
> $$\overline{S}(P;f+y,g) - \underline{S}(P;f+y,g) < \varepsilon.$$
> Thus, $f+y$ is [[Math/Calculus/Integration/Integrability|integrable]] w.r.t $g$ on $\left[ a,b \right]$. Thus, for any [[Interval Partitions|partition]] $P$ of $\left[ a,b \right]$,
> $$\begin{array}{c}
> \underline{S}(P;f,g) + \underline{S}(P;y,g) \le \underline{S}(P;f+y,g) \le \\ 
> \displaystyle\int_{a}^b f+y \, dg \\
> \le  \overline{S}(P;f+y,g) \le \overline{S}(P;f,g) + \overline{S}(P;y,g) \\
> \end{array}$$
> Since the value of the integral is unique,
> $$\int_{a}^b f+y\,dg = \int_{a}^b f \,dg + \int_{a}^b y \,dg$$

\[[[Linear Maps]]\]