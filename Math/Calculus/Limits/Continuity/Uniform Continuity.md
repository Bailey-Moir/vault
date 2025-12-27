---
tags:
  - atom
  - math
---
$$\forall \varepsilon>0, \exists \delta>0: \forall x,y \in \R,  \left|x-y\right| < \delta \to \left|f(x) - f(y)\right| < \varepsilon$$
> [!note] This is the same as regular [[Math/Calculus/Limits/Continuity/Continuity|continuity]], except the $a$ is given after the $\delta$ instead of before the $\varepsilon$: $\mathbf{\delta}$ **cannot depend on** $\mathbf{a}$.

> [!theorem]- \- **4.26** \- If $f \in \mathcal{C}(I)$[^1] for some [[Intervals|closed interval]] $I$, then $f$ is *uniformly continuous* on $I$.
> Let $I = \left[ a,b \right]$, and $f \in \mathcal{C}(I)$, but suppose $f$ is **not** *uniformly continuous* on $I$.
> 
> Let's bisect $I$ with $\left[ a_{n},b_{n} \right]$ such that each iteration, a half that is not *uniformly continuous* is chosen.
> 
> Let $\varepsilon>0$ be given.  Let $a_{0}=a$ and $b_{0}=b$, and take $\left[ a_{n}, \frac{a_{n}+b_{n}}{2} \right]$ and $\left[ \frac{a_{n}+b_{n}}{2}, b_{n} \right]$. 
> 
> We first check what happens at the midpoint $\frac{a_{n}+b_{n}}{2}$. Since $f$ is [[Math/Calculus/Limits/Continuity/Continuity|continuous]] at this point, there exists $\delta > 0$ such that for $\left| z - \frac{a_{n}+b_{n}}{2} \right| < \delta$, $\left| f(z) - f(\frac{a_{n}+b_{n}}{2}) \right| < \varepsilon$.
> 
> Therefore, $f$ has to violate the definition of *uniform continuity* on one of the sub-[[Intervals|intervals]], and such an [[Intervals|interval]] is chosen for $[a_{n+1},b_{n+1}]$.
> 
> Let $x_{n},y_{n} \in \left[ a_{n},b_{n} \right]$ for all $n$[^2]   such that $\left| f(x_{n}) - f(y_{n})  \right| \ge \varepsilon$.
> 
> Since $\left( a_{n} \right)$ and $\left( b_{n} \right)$ and both [[Monotone Sequences|monotone]] and [[Bounded Sequences|bounded]], they [[Metric Sequence Convergence|converge]] by [[Monotone Convergence Theorem|monotone convergence theorem]]. Further, since each iteration bisects the [[Intervals|interval]],
> $$\lim \left( b_{n}-a_{n} \right) = \lim \dfrac{b-a}{2^n} = 0$$
> Thus, by [[Rationals in Intervals|2.21.2]], $\lim x_{n} = \lim y_{n} = x$.
> 
> But $f$ is [[Math/Calculus/Limits/Continuity/Continuity|continuous]]  on $\left[ a,b \right]$, so $\lim f(x_{n}) = \lim f(y_{n}) = f(x)$[^3], but we know that $\left| f(x_{n}) - f(y_{n}) \right| \ge \varepsilon$ for all $n$, which this [[Contradictions|contradicts]].

[^1]: [[Math/Calculus/Limits/Continuity/Continuity]]
[^2]: [[Rationals in Intervals]], Theorem 2.21.1
[^3]: [[Math/Topology/Continuity/Continuity Under Composition]]
