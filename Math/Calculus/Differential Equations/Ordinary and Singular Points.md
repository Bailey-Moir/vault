---
tags:
  - atom
  - math
tagsa:
---
For a [[Homogeneous Differential Equations|homogeneous]] second [[Order|order]] [[Linear Differential Equations|linear]] [[Differentials|differential equation]] in standard form
$$\begin{align}
	y'' + P(t)y' + Q(t)y = 0. && (*)
\end{align}$$
a point $t_{0}$ is an *ordinary point* if $P$ and $Q$ are [[Analytic Functions|analytic]] at $t_{0}$. Otherwise, $t_{0}$ is said to be a *singular point*.

> [!theorem]- If $t_{0}$ is an *ordinary point* of $(*)$, it has two [[Linear Independence|linearly independent]] [[Power Series|power series]] solutions centred at $t_{0}$.
> e.g. from it giving a [[Recursion|recurrence]] relation that is only in terms of even offsets.

> [!definition] $t_{0}$ is a **regular singular point** of $(*)$ iff $\left( t-t_{0} \right)P(t)$ and $\left( t-t_{0} \right)^2Q(t)$ are [[Analytic Functions|analytic]] at $t_{0}$.