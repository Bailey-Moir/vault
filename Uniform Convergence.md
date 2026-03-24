---
tags:
  - atom
  - math
---
$f \in B(X)$[^1] is *uniformly convergent* to $g \in B(X)$[^1] iff it is [[Metric Convergence|convergent]] to $g$ in $\left( B(X),d_{\infty} \right)$[^1][^2], i.e. iff
$$ \forall \varepsilon > 0, \exists N \in \N : \forall n \ge N, \sup_{x \in X} \left| f(x) - g(x) \right| < \varepsilon. $$
> [!theorem]- *Uniform Convergence* $\to$ [[Point-wise Convergence|Point-wise convergence]]
> Suppose $f \in B(X)$[^1] is *uniformly convergent* to $g\in B(X)$[^1]. Thus, for all $\varepsilon > 0$, there exists $N \in \N$ such that for all $n \ge N$,
> $$\begin{align}
> 	\sup_{x \in X} \left| f(x) - g(x) \right| &< \varepsilon\\
> 	\to \forall x \in X, \left| f(x) - g(x) \right| &< \varepsilon.\\
> \end{align}$$
> Thus, $f$ is [[Point-wise Convergence|point-wise convergent]] to $g$.

> [!theorem]- *(Completeness)* If $X \ne \emptyset$, $\left( B(X),d_{\infty} \right)$[^1][^2] is [[Completeness|complete]].
> Let $\left( f_{n} \right)$ be a [[Cauchy Sequences|Cauchy sequence]] in $\left( B(X),d_{\infty} \right)$ where $X \ne \emptyset$. Then for all $\varepsilon > 0$, there exists $K \in \N$ such that for all $j,k \ge K$,
> $$d_{\infty}(f_{j},f_{k}) = \sup_{x \in X}\left| f_{j}(x) - f_{k}(x) \right| < \varepsilon.$$
> Thus, for any $x_{0} \in X$,
> $$\left| f_{j}(x_{0}) - f_{k}(x_{0}) \right|  \le \sup_{x \in X}\left| f_{j}(x) - f_{k}(x) \right| < \varepsilon.$$
> Thus, $\left( f_{n}(x_{0}) \right)$ is [[Cauchy Sequences|Cauchy]] in $\R$. By the [[Completeness|completeness]] of $\R$, there exists a [[Metric Convergence#^uniqueness|unique]] [[The Real Numbers|real number]], denoted $f_{*}(x_{0})$, that this [[Sequences|sequence]] [[Metric Convergence|converges]] to. Thus, $\left( f_{n} \right)$ is [[Point-wise Convergence|point-wise convergent]] (to this $f_{*}$).
> 
> For all $\varepsilon > 0$, by [[Cauchy Sequences|Cauchy]], there exists $K_{0} \in \N$ such that for all $j,k \ge K_{0}$ and $x_{0} \in X$,
> $$\left| f_{j}(x_{0})-f_{k}(x_{0}) \right| \le \sup_{x \in X} \left| f_{j}(x) - f_{k}(x) \right| < \dfrac{\varepsilon}{4}.$$
> By the [[Point-wise Convergence|point-wise convergence]] of $\left( f_{n} \right)$, there exists $K_{x_{0}} \in \N$ such that for all $j \ge K_{x_{0}}$,
> $$\left| f_{j}(x_{0}) - f_{*}(x_{0}) \right| < \dfrac{\varepsilon}{4}.$$
> Then for $k \ge K_{0}$ and $j \ge \max\{ K_{0}, K_{x_{0}} \}$,
> $$\begin{align}
> 	\left| f_{k}(x_{0}) - f_{*}(x_{0}) \right| &\le \left| f_{k}(x_{0}) - f_{j}(x_{0}) \right| + \left| f_{j}(x_{0}) - f_{*}(x_{0}) \right| \\
> 	&< \dfrac{\varepsilon}{4} + \dfrac{\varepsilon}{4} \\
> 	&= \dfrac{\varepsilon}{2} \\
> 	&< \varepsilon \\
> \end{align}$$
> #TODO ig this proof was messy ah. not my fault
^completeness

> [!theorem]- *(Preserves Continuity)* Suppose $\left( f_{n} \right)$ is a [[Sequences|sequence]] of [[Bounded Functions|bounded]], [[Metric Continuity|continuous]] [[Functions|functions]] that *uniformly converge* on some $I$ to to a [[Functions|function]] $\lambda$. Then $\lambda$ is [[Metric Continuity|continuous]] on $I$.
> #TODO

[^1]: [[Bounded Function Set]]
[^2]:  $\infty$-[[P-Norms|-norm]]