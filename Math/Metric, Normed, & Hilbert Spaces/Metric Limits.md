---
tags:
  - atom
  - math
---
![500|center](epsilon-delta-limit.excalidraw.md)
The *limit* of a [[Functions|function]] $f : X \to Y$ - where $X,Y$ are [[Metric Spaces|metric spaces]] - at $a \in X$ is $L \in Y$, i.e. $\lim_{ x \to a } f(x) = L$, iff
$$\begin{align}
	& \forall \varepsilon>0, \exists \delta>0: \forall x \in X, d_{X}(x,a) < \delta \to d_{Y}(f(x), L) < \varepsilon \\
	{\textcolor{gray}\iff} & \forall \varepsilon>0, \exists \delta>0: f(B(a,\delta)) \subseteq B(L, \varepsilon) \\
\end{align}$$

> [!theorem]- *(Uniqueness)* If $f(x) \to L$ and $f(x) \to M$ as $x \to a$, then $L = M$.
> Suppose $f(x)$ *converges* to $L$ and $M$ as $x \to a$.
> Let $\varepsilon > 0$ be given. By the *convergence* of $f(x)$ to $L$ and $M$, there exists $\delta_{L},\delta_{M} > 0$ such that
> $$\begin{align}
> 	d_{X}(x,a) &< \delta_{L} \to d_{Y}(f(x),L) < \dfrac{\varepsilon}{2} \\
> 	d_{X}(x,a) &< \delta_{M} \to d_{Y}(f(x),M) < \dfrac{\varepsilon}{2}. \\
> \end{align}$$
> Let $\delta = \min \{ \delta_{L}, \delta_{M} \}$. Then
> $$\begin{align}
> 	d_{X}(x,a) < \delta \to \;\,
> 	& d_{Y}(f(x),L) + d_{Y}(f(x),M) < \dfrac{\varepsilon}{2} + \dfrac{\varepsilon}{2} \\
> 	d_{Y}(L,M) \le\;\,& d_{Y}(L,f(x)) + d_{Y}(f(x),M) < \varepsilon \\
> 	& d_{Y}(L,M) < \varepsilon. \\
> \end{align}$$
> Thus, for all $\varepsilon > 0$, $0 < d_{Y}(L,M) < \varepsilon$, so by [[Bounding with Epsilon|this theorem]], $d_{Y}(L,M) = 0$, meaning $L = M$. $\quad\square$.



> [!note] For some reason, this wasn't covered in MATH343.

\[[[Limits of Real Functions]]gg\]