---
tags:
  - atom
  - math
---
A *Taylor series/polynomial* is a [[Power Series|power series]] approximation of a [[Functions|function]] near $\alpha$.
$$\begin{array}{c}
	\displaystyle p_k(x) = \sum_{n=0}^k \dfrac{f^{(n)}(\alpha)}{n!} (x-\alpha)^n \\
	\displaystyle f(x) \sim \sum_{n=0}^\infty \dfrac{f^{(n)}(\alpha)}{n!} (x-\alpha)^n \\
\end{array}$$
*Note the $\sim$ means that it is approximated by, as we don't know if the [[Series|series]] converges at the given $x$. If we know that the series converges, the $\sim$ becomes an $=$*.

- It can be shown that $f$ exists as a [[Power Series|power series]] representation iff $\displaystyle\lim_{n\to\infty} R_{n}(x) = 0$ for all $x$ in the [[Interval of Convergence|interval of convergence]].
> [!proof]-
> $$\begin{align*}
> 	\lim_{ n \to \infty } R_{n}(x) &= 0 \\
> 	\lim_{ n \to \infty } \left[ f(x) - p_{n}(x) \right] &= 0 \\
> 	\lim_{ n \to \infty } f(x) &= \lim_{ n \to \infty } p_{n}(x) \\
> 	f(x) &= \lim_{ n \to \infty } p_{n}(x)\\
> \end{align*}$$
> Note that $\lim_{ n \to \infty } p_{n}(x)$ is undefined outside of the [[Interval of Convergence|convergence]].

> [!note]- All [[Power Series|Power Series]] Representations are the *Taylor Series* 
If a [[Functions|function]] $f$ has a [[Power Series|power series]] representation at $a$ such that
$$f(x) = \sum_{n=0}^\infty c_{n}\left( x-a \right)^n \hspace{2em} \left| x-a \right| < R$$
then its coefficients are given by
$$c_{n} = \dfrac{f^{(n)}(a)}{n!}$$
