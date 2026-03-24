---
tags:
  - atom
  - math
---
A [[Sequences|sequence]] $( \vecbf{a_{n}} )$ in $\R^n$ is said to *converge component-wise* to $\vecbf{\lambda} \in \R^n$ iff
$$ \forall i \in \{ 1,\dots,n \}, \lim_{ n \to \infty } a_{n,i}= \lambda_{i}, $$
using the usual [[Topology|topology]]/[[Metric Spaces|metric]] on $\R$.

> [!theorem]- *Component-wise convergence* on $\R^n$ is equivalent to $\infty$[[P-Norms|-norm]] [[Metric Convergence|convergence]].
> $\left( \implies \right)$
> Suppose $(\vecbf{a_{n}})$ in $\R^n$ is *component-wise convergent* to $\vecbf{\lambda} \in \R^n$. Thus, for any $\varepsilon > 0$ and $i \in \{ 1,\dots,n \}$, there exists $N_{i} \in \N$ such that for all $n \ge N$, 
> $$\left| a_{n,i} - \lambda_{i} \right| < \varepsilon.$$
> 
> Let $\displaystyle N = \max_{i \in \{ 1,\dots,n \}} N_{i}$. Then for all $n \ge N$,
> $$\begin{align}
> 	\forall i \in \{ 1,\dots,n \}, \left| a_{n,i} - \lambda_{i} \right| &< \varepsilon \\
> 	\max_{i \in \{ 1,\dots,n \}} \left| a_{n,i} - \lambda_{i} \right| &< \varepsilon \\
> 	d_{\infty}(a_{n,i}, \lambda_{i}) &< \varepsilon. \\
> \end{align}$$
> Thus, $(\vecbf{a_{n}})$ [[Metric Convergence|converges]] to $\vecbf{\lambda}$ under the $\infty$[[P-Norms|-norm]].
> 
> $\left( \impliedby \right)$
> Suppose $(\vecbf{a_{n}})$ in $\R^n$ is [[Metric Convergence|convergent]] to $\vecbf{\lambda} \in \R^n$ under the $\infty$[[P-Norms-norm]]. Thus, for any $\varepsilon > 0$, there exists $N \in \N$ such that for all $n \ge N$,
> $$\begin{align}
> 	d_{\infty}(a_{n,i}, \lambda_{i}) &< \varepsilon. \\
> 	\max_{i \in \{ 1,\dots,n \}} \left| a_{n,i} - \lambda_{i} \right| &< \varepsilon \\
> 	\forall i \in \{ 1,\dots,n \}, \left| a_{n,i} - \lambda_{i} \right| &< \varepsilon. \\
> \end{align}$$
> Thus, this $N$ satisfies the $N$ for the [[Metric Convergence|convergence]] of each component, meaning $(\vecbf{a_{n}})$ *component-wise converges* to $\vecbf{\lambda}$.