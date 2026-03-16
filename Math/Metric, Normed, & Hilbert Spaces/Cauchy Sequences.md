---
tags:
  - atom
  - math
---
A [[Sequences|sequence]] $(a_{n}) : \N \to M$ for some [[Metric Spaces|metric space]] $M$ is called a *Cauchy sequence* iff
$$\forall \varepsilon > 0, \exists N \in \N : \forall m,n \ge N, d(a_{n}, a_{m}) < \varepsilon$$
> [!theorem]- [[Metric Sequence Convergence|Convergent]] $\to$ *Cauchy*.
> Suppose $\left( a_{n} \right) : \N \to M$ [[Metric Sequence Convergence|converges]] to $\lambda$, meaning
> $$\forall \varepsilon > 0, \exists N \in \N : \forall n \ge N, d(a_{n},\lambda) < \varepsilon.$$
> Then for all $\varepsilon/2 > 0$, there exists $N \in \N$ such that for all $m,n \ge N$,
> $$\begin{array}{ccc}
> 	d(a_{m},L) < \dfrac{\varepsilon}{2} & \land & d(a_{n}, L) < \dfrac{\varepsilon}{2}.
> \end{array}$$
> Thus,
> $$\begin{align}
> 	d(a_{m}, L) + d(a_{n}, L) &< \varepsilon, \\
> 	d(a_{m}, a_{n}) \le d(a_{m}, L) + d(L, a_{n}) &< \varepsilon. && \triangle\le \\
> \end{align}$$
> This gives that for all $\varepsilon > 0$, there exists $N \in \N$ such that for all $m,n \ge N$, $d(a_{m}, a_{n}) < \varepsilon$. Thus, $\left( a_{n} \right)$ is a *Cauchy sequence*.
^convergent-to-cauchy

> [!theorem]- In $\R$, *Cauchy* $\to$ [[Metric Sequence Convergence|Convergent]].
> Suppose $\left( a_{n} \right) : \N \to \R$ is a *Cauchy sequence*.
> For $\varepsilon = 1$, there then exists $N \in \N$ such that for all $n \ge N$,
> $$\begin{array}{c}
> 	\left| a_{n} - a_{N} \right| < 1 \\
> 	- 1< a_{n} - a_{N} < 1 \\
> 	a_{N} - 1< a_{n} < a_{N} + 1. \\
> \end{array}$$
> Thus, $\left( a_{n} \right)$ is eventually [[Bounded Sequences|bounded]], meaning it is [[Bounded Sets|bounded]], as there are finitely many points before $N$.
> 
> Therefore, by [[Bolzano-Weierstrass|Bolzano-Weierstrass]], some subsequence $\left( a_{n(k)} \right)_{k=0}^\infty$ [[Metric Sequence Convergence|converges]] to some $\lambda$.
> 
> Let $\varepsilon > 0$ be given.
> By the [[Metric Sequence Convergence|convergence]] of $\left( a_{n(k)} \right)_{k=0}^\infty$, there exists $K \in \N$ such that for all $k \ge K$,
> $$\left| a_{n(k)} - \lambda \right| < \dfrac{\varepsilon}{2}.$$
> Since $\left( a_{n} \right)$ is *Cauchy*, there exists $N \in \N$ such that for all $m, n \ge N$,
> $$ \left| a_{m} - a_{n} \right| < \dfrac{\varepsilon}{2}. $$
> Let $k \ge K$ such that $n(k) \ge N$. Then for all $n \ge N$,
> $$\begin{array}{c}
> 	\begin{array}{ccc}
> 		\left| a_{n} - a_{n(k)} \right| < \dfrac{\varepsilon}{2} 
> 		& \land &
> 		\left| a_{n(k)} - \lambda \right| < \dfrac{\varepsilon}{2}.
> 	\end{array} \\
> 	\to \left| a_{n} - \lambda \right| \le \left| a_{n} - a_{n(k)} \right| + \left| a_{n(k)} - \lambda \right| < \varepsilon. \phantom{\to}
> \end{array}$$
> Thus, $\left( a_{n} \right)$ is [[Metric Sequence Convergence|convergent]].
^R-cauchy-to-convergent