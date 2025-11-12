---
tags:
  - atom
  - math
---
For $f \in \mathcal{C}(I)$ for any [[Intervals|closed interval]] $I \subseteq \R$, $f$ is [[Bounded Sequences|bounded]] on $I$.

> [!proof]- 4.33
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
> Then both [[Sequences|sequences]] [[Sequence Convergence|converge]] by [[Monotone Convergence Theorem|monotone convergence theorem]], and $\lim\left( b_{n} - a_{n} \right) = \lim \frac{b-a}{2^n} = 0$.
> 
> By [[Rationals in Intervals|theorem 2.22]], there exists a unique $c \in \R$ in the intersection of the intervals of $\left( I_{n} \right)$.
> 
> The [[Continuity|continuity]] of  at $c$ gives an [[Intervals|open interval]] $U$ around $c$ on which $f$ is [[Bounded Sets|bounded]]. However, there must exists an $n$ such that $I_{n} \subset U$, meaning $I_{n}$ must be [[Bounded Sets|bounded]], a [[Contradictions|contradiction]].
> 
> Thus, $I$ must be [[Bounded Sets|bounded]].