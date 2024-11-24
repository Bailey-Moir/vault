---
tags:
  - atom
  - math
---
A *Taylor series/polynomial* is a [[Power Series|power series]] approximation of a function near $\alpha$.
$$\begin{array}{c}
	\displaystyle p_k(x) = \sum_{n=0}^k \dfrac{f^{(n)}(\alpha)}{n!} (x-\alpha)^n \\
	\displaystyle f(x) \sim \sum_{n=0}^\infty \dfrac{f^{(n)}(\alpha)}{n!} (x-\alpha)^n \\
\end{array}$$
*Note: the $\sim$ means that it is approximated by, as we don't know if the series converges. If we know that the series converges, the $\sim$ becomes an $=$*

- It can be shown that $f$ exists as a [[Series|series]] iff $\displaystyle\lim_{n\to\infty} R_n(x) = 0$[^1] for all $x$ in the [[Interval of Convergence|interval of convergence]].

[^1]: [[Error of Taylor Series]]