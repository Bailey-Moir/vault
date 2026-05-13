---
tags:
  - atom
  - math
---
$$\forall f \in \mathcal{C}_{X}^Y, \forall g \in \mathcal{C}_{Y}^Z, g \circ f \in \mathcal{C}_{X}^Z$$
> [!proof]-
> Let $f$, $g$, and $W \in \mathcal{T}_{Z}$ be given.
> 
> By the [[Continuity|continuity]] of $g$, since $W \in \mathcal{T}_{Z}$, there exists $V \in \mathcal{T}_{Y}$ such that $V = g^{-1}(W)$.
> 
> By the [[Continuity|continuity]] of $f$, since $V \in \mathcal{T}_{Y}$, there exists $U \in \mathcal{T}_{X}$ such that $U = f^{-1}(V)$.
> 
> Thus, for all $W \in \mathcal{T}_{Z}$, $(g\circ f)^{-1}(W) = U \in \mathcal{T}_{X}$. $\square$

> [!theorem]- *([[Metric Continuity|Metric]])* $\forall f \in \mathcal{C}_{X}^Y(a),\; \forall g \in \mathcal{C}_{Y}^Z(f(a)),\; g\circ f \in \mathcal{C}_{X}^Y(a)$
> Let $\left( x_{n} \right) \subseteq X$ [[Metric Convergence|converge]] to $a \in X$.
> By the [[Metric Continuity#^sequences|sequence definition of metric continuity]], $\left( f(x_{n}) \right) \subseteq Y$ [[Metric Convergence|converges]] to $f(a)$.
> Applying this again, $\left( g(f(x_{n})) \right) \subseteq Z$ [[Metric Convergence|converges]] to $g(f(a))$.
> 
> Thus, for every $\left( x_{n} \right) \subseteq X$ that [[Metric Convergence|converges]] to $a \in X$, $\left( (g \circ f)(x_{n}) \right) \subseteq Z$ [[Metric Convergence|converges]] to $(g \circ f)(a) \in Z$. Applying this same theorem again for the last time, $(g \circ f)$ is [[Metric Continuity|continuous]]  at $a$.
> 
> > [!alternative-proof]- $\varepsilon$-$\delta$
> > Let $\varepsilon>0$ be given. By the [[Metric Continuity|continuity]] of $g$ at $f(a)$, there is an $\eta>0$ such that for all $y \in Y$,
> > $$d_{Y}( y, f(a) ) < \eta \to d_{Z}( g(y), g(f(a)) ) < \varepsilon.$$
> > Use $\eta$ with the [[Metric Continuity|continuity]] of $f$ at $a$ to give that there exists $\delta>0$ such that for all $x \in X$,
> > $$d_{X}(x, a) < \delta \to d_{Y}( f(x), f(a) ) < \eta.$$
> > Letting $y = f(x)$ gives that for all $\varepsilon > 0$, there exists $\delta > 0$ such that
> > $$\begin{align}
> > 	d_{X}(x, a) < \delta &\to d_{Z}( g(f(x)), g(f(a)) ) < \varepsilon \\
> > 	&\to d_{Z}( (g\circ f)(x), (g\circ f)(a) ) < \varepsilon. \hspace{1em} \square\\
> > \end{align} $$
^metric