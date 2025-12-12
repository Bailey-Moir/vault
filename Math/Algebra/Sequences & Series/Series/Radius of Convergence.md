---
tags:
  - atom
  - math
---
![1000|center](interval-of-convergence.excalidraw.md)
Let $p$ be the [[Statements and Propositions|statement]] that some [[Power Series|power series]] $\Sigma c_{n}\left( x-\alpha \right)^n$ is [[Partial Sums|convergent]]. There are three possibilities:

1. **Convergent Only at Center** $p \leftrightarrow x = \alpha$
2. **Convergent Everywhere** $\forall x, p$
3. **Convergent on Disk** $\exists R \in \R^+ : \left( \left| x-\alpha \right| < R \to p \right) \land \left( \left| x-\alpha \right| > R \to \neg p \right)$

where $R$ is the **radius of convergence** of the [[Power Series|power series]].

> [!theorem]- \- **Radius of Convergence** - Consider a *power series* $\Sigma c_{k}(x-a)^k$ where $c_{k} \ne 0$ and $r = \lim\left| \dfrac{c_{k+1}}{c_{k}} \right|$ [[Metric Sequence Convergence|exists]], then <ul><li>if $r \ne 0$, the [[Series|series]] [[Absolute Convergence|converges absolutely]] when $\left| x-a \right| < \frac{1}{r}$ and [[Partial Sums|diverges]] if $\left| x-a \right| > \frac{1}{r}$, and</li><li>if $r = 0$, the [[Series|series]] [[Absolute Convergence|converges absolutely]] for all $x$.</li></ul>
> $$\rho = \lim \left| \dfrac{c_{k+1}(x-a)^{k+1}}{c_{k}(x-a)^k} \right| = \left| x - a \right| \lim \left| \dfrac{c_{k+1}}{c_{k}} \right| = r\left| x \right|$$
> Then by [[The Ratio Test|the ratio test]], the [[Series|series]] is [[Absolute Convergence|absolutely convergent]] if $\rho = r \left| x-a \right| < 1$, which occurs iff $r = 0$ or $\left| x-a \right| < \dfrac{1}{r}$.
> 
> Similarly, by [[The Ratio Test|the ratio test]], the [[Series|series]] [[Partial Sums|diverges]] if $\rho = r \left| x-a \right| > 1$, which occurs iff $\left| x-a \right| \ge \dfrac{1}{r}$ (which is only possible if $r \ne 0)$.