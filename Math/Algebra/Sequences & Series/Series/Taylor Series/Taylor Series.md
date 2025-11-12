---
tags:
  - atom
  - math
---
A *Taylor series* is a [[Power Series|power series]] approximation of a [[Functions|function]]  around some point $\alpha$ , given by
$$\begin{align}
	\displaystyle f(x) &\sim \sum_{k=0}^\infty \dfrac{f^{(k)}(\alpha)}{k!} (x-\alpha)^k \\
\end{align}$$

> [!note] The $\sim$ means that it is approximated by, as we don't know if the [[Series|series]] converges at the given $x$. If we know that the series converges, the $\sim$ becomes an $=$.

> [!definition]  The [[Partial Sums|partial sums]] of the *Taylor series* of $f$ around $\alpha$ are given by $$p_n(x) = \sum_{k=0}^n \dfrac{f^{(k)}(\alpha)}{k!} (x-\alpha)^k$$

> [!example]- $f(a+b)$
> $$ f(a+b) \sim \sum_{k=0}^\infty \dfrac{f^{(k)}(a)}{k!}b^k $$

---

> [!theorem]- It can be shown that $f$ exists as a [[Power Series|power series]] representation iff $\displaystyle\lim_{n\to\infty} R_{n}(x) = 0$ for all $x$ in the [[Radius of Convergence|interval of convergence]].
> $$\begin{align*}
> 	\lim_{ n \to \infty } R_{n}(x) &= 0 \\
> 	\lim_{ n \to \infty } \left[ f(x) - p_{n}(x) \right] &= 0 \\
> 	\lim_{ n \to \infty } f(x) &= \lim_{ n \to \infty } p_{n}(x) \\
> 	f(x) &= \lim_{ n \to \infty } p_{n}(x)\\
> \end{align*}$$
> Note that $\lim_{ n \to \infty } p_{n}(x)$ is undefined outside of the [[Radius of Convergence|convergence]].

> [!theorem]- All [[Power Series|power series]] representations are the *Taylor Series* 
If a [[Functions|function]] $f$ has a [[Power Series|power series]] representation at $a$ such that
$$f(x) = \sum_{n=0}^\infty c_{n}\left( x-a \right)^n \hspace{2em} \left| x-a \right| < R$$
then its coefficients are given by
$$c_{n} = \dfrac{f^{(n)}(a)}{n!}$$