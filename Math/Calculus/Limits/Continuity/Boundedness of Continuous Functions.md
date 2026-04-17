---
tags:
  - atom
  - math
---
For $f \in \mathcal{C}(I)$ for any [[Intervals|closed interval]] $I \subseteq \R$, $f$ is [[Bounded Sequences|bounded]] on $I$.

[!proof]
Suppose $f : \left[ a,b \right] \to M$ is [[Metric Continuity 1|continuous]] but not [[Bounded Functions|bounded]].
Pick any $x_{0} \in \left[ a,b \right]$.
For $n \in \N$, we can find $x_{n+1} \in \left[ a,b \right]$ such that $\left| f(x_{n+1}) \right| \ge \left| f(x_{n}) \right| + 1$.

The [[Sequences|sequence]] $\left( x_{n} \right)$ in $\left[ a,b \right]$ is [[Bounded Sets|bounded]], so by [[Bolzano-Weierstrass|Bolzano-Weierstrass]], there exists a [[Metric Convergence|convergent]] subsequence $\left( x_{n(k)} \right)_{k=0}^\infty$.

Since $\left[ a,b \right]$ is a [[Closed Sets|closed]] [[Intervals|interval]], $\lim_{ k \to \infty } x_{n(k)} \in \left[ a,b \right]$, otherwise as $k$ become sufficiently large, $x_{n(k)}$ will be outside of $\left[ a,b \right]$. (This is not very rigorous).

Since $f \in \mathcal{C}(\left[ a,b \right])$, by the [[Metric Continuity 1#^sequences|sequence definition of continuity]],
$$\lim_{ k \to \infty } f(x_{n(k)}) = f\left( \lim_{ k \to \infty } x_{n(k)} \right). $$
Then since all [[Cauchy Sequences#^convergent-to-cauchy|convergent sequences are Cauchy]], $f$ is [[Cauchy Sequences|Cauchy]]. However, by the [[Triangle Ineqaulity#^reverse|reverse triangle inequality]], for all $n \in \N$
$$\left| f(x_{n+1}) - f(x_{n}) \right| \ge \left| f(x_{n+1}) \right| - \left| f(x_{n}) \right| \ge 1,$$
leading to [[Contradictions|contradiction]].

Thus, $f$ is [[Bounded Functions|bounded]] on $\left[ a,b \right]$.


> [!proof]-
> Let $I = \left[ a,b \right]$, and $f \in \mathcal{C}(I)$, but suppose $f$ is **not** [[Bounded Sets|bounded]] on $I$.
> 
> Let's bisect $I$ with $\left[ a_{n},b_{n} \right]$ such that each iteration, a half that is [[Bounded Sets|unbounded]] is chosen.
> 
> Let  and $b_{0}=b$. For $I_{n} = \left[ a_{n},b_{n} \right]$,
> - if $f$ is [[Bounded Sets|unbounded]] on $\left[ a_{n}, \frac{a_{n}+b_{n}}{2} \right]$, let this be $I_{n+1}$, otherwise
> - let $I_{n+1}$ be $\left[ \frac{a_{n}+b_{n}}{2}, b_{n} \right]$.
> 
> Note that at least one of these [[Intervals|intervals]] must be [[Bounded Sets|unbounded]], as if they were both [[Bounded Sets|bounded]], $I_{n}$ would be [[Bounded Sets|bounded]] by the maximum of their bounds.
> 
> Then both [[Sequences|sequences]] [[Metric Convergence|converge]] by [[Monotone Convergence Theorem|monotone convergence theorem]], and $\lim\left( b_{n} - a_{n} \right) = \lim \frac{b-a}{2^n} = 0$.
> 
> By [[Rationals in Intervals|theorem 2.22]], there exists a unique $c \in \R$ in the intersection of the intervals of $\left( I_{n} \right)$.
> 
> The [[Metric Continuity 1|continuity]] of  at $c$ gives an [[Intervals|open interval]] $U$ around $c$ on which $f$ is [[Bounded Sets|bounded]]. However, there must exists an $n$ such that $I_{n} \subset U$, meaning $I_{n}$ must be [[Bounded Sets|bounded]], a [[Contradictions|contradiction]].
> 
> Thus, $I$ must be [[Bounded Sets|bounded]].