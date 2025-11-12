---
tags:
  - atom
  - math
---
$$f \in \mathcal{C}\left(\{ g(a) \}\right) \land g \in \mathcal{C}\left(\{ a \}\right) \iff \left(f \circ g\right)(a) \in \mathcal{C}(\{ a \})$$
> [!proof]-
> Let $\varepsilon>0$ be given. By the [[Continuity|continuity]] of $f$ at $g(a)$, there is an $\eta>0$ such that for all $y \in \R$,
> $$\left| y-g(a) \right| < \eta \to \left| f(y) - f(g(a)) \right| < \varepsilon.$$
> Use $\eta$ with the [[Continuity|continuity]] of $f$ to give that there exists $\delta>0$ such that
> $$\left| x - a \right| < \delta  \to\left| g(x)-g(a) \right| < \eta.$$
> If $y = g(x)$, this gives that for all $\varepsilon > 0$, there exists $\delta > 0$ such that
> $$\begin{align}
> 	\left| x-a \right| < \delta &\to \left| f(g(x)) - f(g(a)) \right| < \varepsilon \\
> 	&\to \left| (f\circ g)(x) - (f\circ g)(a) \right| < \varepsilon. \hspace{1em} \square\\
> \end{align} $$


\[[[Continuity]]\]