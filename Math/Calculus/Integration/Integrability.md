---
tags:
  - atom
  - math
---
We say $f$ is *integrable* with respect to $g$ on $J$ iff there exists a unique number $I$ such that for every $\varepsilon>0$, there exists a [[Interval Partitions|partition]] $P_{\varepsilon}$ on $J$ such that if $P$ is any [[Refinements|refinement]] of $P\varepsilon$ and $S(P;f,g)$ is any [[Riemann-Stieltjes Sums|R-S]] sum corresponding to $P\varepsilon$, then
$$\left| S(P;f,g) - I \right|  < \varepsilon.$$
> [!theorem]- The [[Functions|function]] $f$ is *integrable* with respect to $g$ over $\left[ a,b \right]$ iff for all $\varepsilon > 0$, there exists a [[Interval Partitions|partition]] of $\left[ a,b \right]$ such that$$\overline{S}(P;f,g) - \underline{S}(P;f,g) < \varepsilon \hspace{1em} \left( * \right)$$
> $\left( \impliedby \right)$
> Let $\varepsilon>0$. Assume there exists a [[Interval Partitions|partition]] $P$ such that $\left( * \right)$ holds, giving
> $$\overline{S}(P;f,g) < \underline{S}(P;f,g) + \varepsilon.$$
> Then
> $$\begin{array}{c}
> 	\displaystyle \overline{\int^b_{a}} f\, dg \le \overline{S}(P;f,g) < \underline{S}(P;f,g) + \varepsilon\le \underline{\int_{a}^b}f\,dg + \varepsilon \\
> 	\to \displaystyle \overline{\int^b_{a}} f\, dg \le \underline{\int_{a}^b}f\,dg + \varepsilon \\
> 	\to \displaystyle \overline{\int^b_{a}} f\, dg \le \underline{\int_{a}^b}f\,dg
> \end{array}$$
> But in general,
> $$\begin{array}{c}
> 	\displaystyle \underline{\int^b_{a}} f\, dg \le \overline{\int_{a}^b}f\,dg \\
> 	\to 
> 	\displaystyle \underline{\int^b_{a}} f\, dg = \overline{\int_{a}^b}f\,dg \\
> \end{array}$$
> $\left( \implies \right)$
> Assume $f$ is *integrable* with respect to $g$ on $J$.
> 
> Let $\varepsilon>0$ be given. Then there exists a [[Partitions|partition]] $P$ and $Q$ such that
> $$\overline{S}(P;f,g) < \overline{\int_{a}^b}f\,dg + \dfrac{\varepsilon}{2},$$
> and
> $$\underline{S}(Q;f,g) > \underline{\int_{a}^b}f\,dg - \dfrac{\varepsilon}{2}.$$
> Let $P\varepsilon = P \cup Q$ be the common [[Refinements|refinement]] of $P$ and $Q$. Then $P\varepsilon$ is a [[Interval Partitions|partition]] on $J$, and using the fact that $f$ is *integrable* with respect to $g$ on $J$, we have
> $$\overline{S}(P_{\varepsilon};f,g) - \underline{S}(P_{\varepsilon};f,g)\le \overline{S}(P;f,g) - \underline{S}(Q;f,g) < \varepsilon$$
> by the fact that [[Refinements Refine|refinements refine]].

> [!theorem] The anti-derivative / indefinite integral of a [[Riemann Sums|Riemann]] *integrable* [[Functions|function]] is [[Continuity|continuous]].
 
\[[[Riemann-Stieltjes Integrals]]\]