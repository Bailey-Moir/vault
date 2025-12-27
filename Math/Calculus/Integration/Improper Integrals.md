---
tags:
  - atom
  - math
---
*Improper integrals* are used when you are
- integrating a [[Math/Calculus/Limits/Continuity/Continuity|continuous]] [[Functions|function]] over an infinite [[Intervals|interval]], or 
- integrating a [[Functions|function]] that becomes infinite (or has a [[Math/Calculus/Limits/Continuity/Continuity|discontinuity]]) over a finite [[Intervals|interval]].

If the corresponding [[Archive/Deatomized/Calculus/Algebra/Limits|limit]] is convergent, the integral is said to converge, otherwise it is said to diverge.
# Integrals on Infinite Intervals
$$\begin{align*}
	\int_a^\infty f(x) \, dx &\equiv \lim_{\ell\to\infty} \int_a^\ell f(x) \, dx \\
	\int_{-\infty}^b f(x) \, dx &\equiv \lim_{\ell\to-\infty} \int_\ell^b f(x) \, dx \\
\end{align*}$$
It should be noted that if both the upper and lower bound are infinite, then the integral is split up and dealt with separately, and **if either of the two integrals diverge, then the original integral diverges**.
$$\begin{align*}
	\int_{-\infty}^\infty f(x) \, dx &\equiv \int_{-\infty}^c f(x) \, dx + \int_c^{\infty} f(x) \, dx && \forall c \in \R  \\
		&\equiv \lim_{\ell\to-\infty} \int_{\ell}^c f(x) \, dx + \lim_{\ell\to\infty} \int_c^{\ell} f(x) \, dx \\ 
\end{align*}$$
# Integrals with Boundary Discontinuities 
If a proper integral has bounds $a$ and $b$, the integrand must be continuous over $\left[a,b\right]$. However, the integrand of improper integral can be continuous over $\left[a,b\right)$, $\left(a,b\right]$ or even $\left(a,b\right)$, meaning they can have discontinuities (including infinite discontinuities) on the bounds.

| [[Math/Calculus/Limits/Continuity/Continuity\|Continuous]] [[Intervals\|Interval]] | Integral Type                                                                                                                                             |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $f \in \mathcal{C}(\,\left[a,b\right]\,)$                        | $\displaystyle \int_a^b f(x) \, dx$ (Proper)                                                                                                              |
| $f \in \mathcal{C}(\,\left[a,b\right)\,)$                        | $\displaystyle \lim_{\ell\to b^-} \int_a^\ell f(x) \, dx$                                                                                                 |
| $f \in \mathcal{C}(\,\left(a,b\right]\,)$                        | $\displaystyle \lim_{\ell\to a^+} \int_\ell^b f(x) \, dx$                                                                                                 |
| $f \in \mathcal{C}(\,\left(a,b\right)\,)$                        | $\displaystyle \lim_{\ell\to a^+} \int_\ell^c f(x) \, dx + \lim_{\ell\to b^-} \displaystyle \int_c^\ell f(x) \, dx \phantom{aaaa} c \in \left(a,b\right)$ |

\[[[Math/Calculus/Limits/Continuity/Continuity|Continuity]]\]