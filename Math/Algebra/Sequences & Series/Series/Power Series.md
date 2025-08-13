---
tags:
  - atom
  - math
---
A *power series* about $\alpha$ is a [[Series|series]] of the form
$$ \sum_{k=0}^\infty c_k\left( x-\alpha \right)^k = c_0 + c_1\left( x-\alpha \right) + c_2\left( x-\alpha \right)^2 + \cdots $$
The sum of a *power series* is a [[Functions|function]] with a [[Domain|domain]] of the [[Interval of Convergence|interval of convergence]].

> [!note]- When $\alpha=0$ and $\exists k : \forall n, c_n = k$, this is a [[Geometric Series|geometric series]] with a ratio of $x$.

> [!note]- Term-by-Term Integration and Differentiation
> For any *power series*,
> - $\displaystyle \dfrac{d}{dx}\left[ \sum _{n=0}^\infty c_{n}(x-\alpha)^n \right] = \sum _{n=0}^\infty \dfrac{d}{dx}\left[ c_{n}(x-\alpha)^n \right]$
> - $\displaystyle \int \left[ \sum _{n=0}^\infty c_{n}(x-\alpha)^n \right] \, dx = \sum _{n=0}^\infty \int \left[ c_{n}(x-\alpha)^n \right] \, dx$

> [!theorem]- **3.14** - Consider a *power series* $\Sigma a_{k}x^k$ where $a_{k} \ne 0$ and $r = \lim\left| \dfrac{a_{k+1}}{a_{k}} \right|$ [[Convergence of Sequences|exists]], then <ul><li>if $r \ne 0$, the [[Series|series]] [[Absolute Convergence|converges absolutely]] when $\left| x \right| < \frac{1}{r}$ and [[Partial Sums|diverges]] if $\left| x \right| > \frac{1}{r}$, and</li><li>if $r = 0$, the [[Series|series]] [[Absolute Convergence|converges absolutely]] for all $x$.</li></ul>
> $$\rho = \lim \left| \dfrac{a_{k+1}x^{k+1}}{a_{k}x^k} \right| = \left| x \right| \lim \left| \dfrac{a_{k+1}}{a_{k}} \right| = r\left| x \right|$$
> Then by [[The Ratio Test|the ratio test]], the [[Series|series]] is [[Absolute Convergence|absolutely convergent]] if $\rho = r \left| x \right| < 1$, which occurs iff $r = 0$ or $\left| x \right| < \dfrac{1}{r}$.
> 
> Similarly, by [[The Ratio Test|the ratio test]], the [[Series|series]] [[Partial Sums|diverges]] if $\rho = r \left| x \right| > 1$, which occurs iff $\left| x \right| \ge \dfrac{1}{r}$.