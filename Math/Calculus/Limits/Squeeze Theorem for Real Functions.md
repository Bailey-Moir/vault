---
tags:
  - math
  - atom
---
![500|center](squeeze-theorem.excalidraw.md)
For any $p \in \R$, let $g,f,h$ be [[Functions|functions]] such that $\displaystyle \lim_{ x \to p } g(x) = g(p) = \lim_{x\to p} h(x) = h(p) = L$[^1], and $g(x) \le f(x) \le h(x)$, then $\displaystyle \lim_{ x \to p } f(x) = L$.

> [!proof]- \- **4.6**
> Let $\varepsilon > 0$ be given. Because both $g,h$ are [[Continuity|continuous]] at $p$, there are $\delta_{g},\delta _h > 0$ such that
> $$\begin{align}
> 	\left| x-p \right| < \delta_{g} &\to \left| g(x)-L \right| < \varepsilon \\
> 	\left| x-p \right| < \delta_{h} &\to \left| h(x)-L \right| < \varepsilon.
> \end{align}$$
> Take $\delta =\text{min}\{ \delta_{g},\delta_h \}$. Then if $\left| x-p \right|<\delta$,
> $$\begin{array}{l}
> 	L-\varepsilon < g(x) < L - \varepsilon , \text{ and} \\
> 	L-\varepsilon < h(x) < L - \varepsilon. \\
> \end{array}$$
> meaning
> $$L-\varepsilon < g(x) \leq f(x) \leq h(x) < L + \varepsilon.$$
> for $\left| x-p \right|<\delta$. Thus,
> $$\begin{array}{c}
> 	L - \varepsilon < f(x) < L + \varepsilon \\
> 	\phantom{\hspace{1em}\square}\left| f(x)-L \right| < \varepsilon\hspace{1em}\square
> \end{array}$$

[^1]: [[Continuity]]
