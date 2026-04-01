---
tags:
  - atom
  - math
---
A [[Sequences|sequence]] $\left( f_{n} \right) \subseteq B(X)$[^1] is *uniformly convergent* to $f_{*} \in B(X)$[^1] iff it is [[Metric Convergence|convergent]] to $g$ in $\left( B(X),d_{\infty} \right)$[^1][^2], i.e. iff
$$ \forall \varepsilon > 0, \exists N \in \N : \forall n \ge N, \sup_{x \in X} \left| f_{n}(x) - f_{*}(x) \right| < \varepsilon. $$
> [!theorem]- *Uniform Convergence* $\to$ [[Point-wise Convergence|Point-wise convergence]]
> Suppose $f \in B(X)$[^1] is *uniformly convergent* to $g\in B(X)$[^1]. Thus, for all $\varepsilon > 0$, there exists $N \in \N$ such that for all $n \ge N$,
> $$\begin{align}
> 	\sup_{x \in X} \left| f(x) - g(x) \right| &< \varepsilon\\
> 	\to \forall x \in X, \left| f(x) - g(x) \right| &< \varepsilon.\\
> \end{align}$$
> Thus, $f$ is [[Point-wise Convergence|point-wise convergent]] to $g$.
^implies-point-wise

> [!theorem]- *(Completeness)* If $X \ne \emptyset$, $\left( B(X),d_{\infty} \right)$[^1][^2] is [[Completeness|complete]].
> **[[Point-wise Convergence|Point-Wise Limit]]**
> Let $\left( f_{n} \right)$ be a [[Cauchy Sequences|Cauchy sequence]] in $\left( B(X),d_{\infty} \right)$ where $X \ne \emptyset$. Then for all $\varepsilon > 0$, there exists $N_{0} \in \N$ such that for all $j,k \ge N_{0}$,
> $$d_{\infty}(f_{j},f_{k}) = \sup_{x \in X}\left| f_{j}(x) - f_{k}(x) \right| < \varepsilon.$$
> Thus, for any $x_{0} \in X$,
> $$\left| f_{j}(x_{0}) - f_{k}(x_{0}) \right|  \le \sup_{x \in X}\left| f_{j}(x) - f_{k}(x) \right| < \varepsilon.$$
> Thus, $\left( f_{n}(x_{0}) \right)$ is [[Cauchy Sequences|Cauchy]] in $\R$. By the [[Completeness|completeness]] of $\R$, there exists a [[Metric Convergence#^uniqueness|unique]] [[The Real Numbers|real number]], denoted $f_{*}(x_{0})$, that this [[Sequences|sequence]] [[Metric Convergence|converges]] to. Thus, $\left( f_{n} \right)$ is [[Point-wise Convergence|point-wise convergent]] (to this $f_{*}$).
> 
> ***Uniformly Convergent* to [[Point-wise Convergence|Point-Wise Limit]]**
> For all $\varepsilon > 0$, by [[Cauchy Sequences|Cauchy]], there exists $N_{1} \in \N$ such that for all $j,k \ge N_{1}$ and $x_{0} \in X$,
> $$\left| f_{j}(x_{0})-f_{k}(x_{0}) \right| \le \sup_{x \in X} \left| f_{j}(x) - f_{k}(x) \right| < \dfrac{\varepsilon}{4}.$$
> By the [[Point-wise Convergence|point-wise convergence]] of $\left( f_{n} \right)$, there exists $N_{x_{0}} \in \N$ such that for all $j \ge N_{x_{0}}$,
> $$\left| f_{j}(x_{0}) - f_{*}(x_{0}) \right| < \dfrac{\varepsilon}{4}.$$
> Then for $k \ge N_{1}$ and $j \ge \max\{ N_{1}, N_{x_{0}} \}$,
> $$\begin{align}
> 	\left| f_{n}(x_{0}) - f_{*}(x_{0}) \right| &\le \left| f_{n}(x_{0}) - f_{j}(x_{0}) \right| + \left| f_{j}(x_{0}) - f_{*}(x_{0}) \right| \\
> 	&< \dfrac{\varepsilon}{4} + \dfrac{\varepsilon}{4} \\
> 	&= \dfrac{\varepsilon}{2} \\
> \end{align}$$
> Since $x_{0} \in X$ is arbitrary,
> $$\begin{align}
> 	d_{\infty}(f_{n} - f_{*}) &= \sup_{x \in X} \left| f_{n}(x) - f_{*}(x) \right| \\
> 	&\leq \dfrac{\varepsilon}{2} \\
> 	&\le \varepsilon. \\
> \end{align}$$
> Thus, $\left( f_{n} \right)$ *uniformly converges* to $f_{*}$.
> 
> **Limit is [[Bounded Functions|Bounded]]**
> Let $\varepsilon = 1$. Then by the *uniform convergence* of $\left( f_{n} \right)$, there exists $N_{2} \in \N$ such that
> $$\begin{align}
> 	\sup_{x \in X} \left| f_{N_{2}}(x) - f_{*}(x) \right| &< 1 \\
> 	\to \forall x \in X, \quad \left| f_{N_{2}}(x) - f_{*}(x) \right| &< 1. \\
> \end{align}$$
> Since $f_{N_{2}}$ is [[Bounded Functions|bounded]], there exists $M \in \R$ such that
> $$\begin{array}{rc}
> 	\forall x \in X \quad & \left| f_{N_{2}}(x) \right| \le M\\
> 	& -M \le f_{N_{2}}(x) \le M\\
> \end{array}$$
> Combining these two gives
> $$\begin{array}{rc}
> 	\forall x \in X,\hspace{-2em} & \left| f_{N_{2}}(x) - f_{*}(x) \right| < 1 \\
> 	& -\varepsilon < f_{*}(x) - f_{N_{2}}(x) < 1 \\
> 	& -M - 1 \le f_{N_{2}}(x) - 1 < f_{*}(x) < f_{N_{2}}(x) + 1 \le M + 1 \\
> 	& \to \left| f_{*}(x) \right| < M +1. \phantom{\to} \\
> \end{array}$$
> Thus, $f_{*}(x)$ is [[Bounded Functions|bounded]], and thus in $B(X)$.
> 
> 
> Finally, this proves that if any [[Sequences|sequence]] $\left( f_{n} \right)$ in $\left( B(X),d_{\infty} \right)$ is [[Cauchy Sequences|Cauchy]], it is [[Metric Convergence|convergent]] in that metric space, so $\left( B(X),d_{\infty} \right)$ is [[Completeness|complete]].
^completeness

> [!theorem]- *(Preserves Continuity)* Suppose $\left( f_{n} \right)$ is a [[Sequences|sequence]] of [[Bounded Functions|bounded]], [[Metric Continuity|continuous]] [[Functions|functions]] on the [[The Real Numbers|reals]] that *uniformly converge* on some $I$ to to a [[Functions|function]] $f_{*}$. Then $f_{*}$ is [[Metric Continuity|continuous]] on $I$.
> Let $a \in I$ and $\varepsilon > 0$ be given.
> 
> By the *uniform convergence* of $\left( f_{n} \right)$, there exists $N \in \N$ such that
> $$\forall x \in I, \left| f_{N}(x) - f_{*}(x) \right| < \dfrac{\varepsilon}{3}. \hspace{2em} (1)$$
> Further, by the [[Metric Continuity|continuity]] of $f_{N}$, there exists $\delta > 0$ such that
> $$\forall x \in I, \left| x - a \right| < \delta \to \left| f_{N}(x) - f_{N}(a) \right| < \dfrac{\varepsilon}{3}.\hspace{2em} (2)$$
> 
> Thus, for all $a \in I$ and $\varepsilon > 0$, there exists $\delta > 0$ such that for all $x \in I$,
> $$\begin{array}{c}
> \left| x - a \right| < \delta \\
> \downarrow \\
> \begin{align}
> 	\left| f_{*}(x) - f_{*}(a) \right| &\le \underbrace{\left| f_{*}(x) - f_{N}(x) \right| }_{(1)} + \underbrace{\left| f_{N}(x) - f_{N}(a) \right| }_{(2)} + \underbrace{\left| f_{N}(a) - f_{*}(a) \right| }_{(1)} \\
> 	&< \dfrac{\varepsilon}{3} + \dfrac{\varepsilon}{3} + \dfrac{\varepsilon}{3} = \varepsilon.
> \end{align}
> \end{array}$$
> Thus, $f_{*}$ is [[Metric Continuity|continuous]] on $I$ 
^preserves-continuity

> [!corollary]- of *(Preserves Continuity)* $\left( \mathcal{C}(\left[ a,b \right]), d_{\infty} \right)$[^1][^3] is [[Complement|complete]].
> [[Boundedness of Continuous Functions|Continuous functions on closed intervals are bounded]].

[^1]: [[Bounded Function Set]]
[^2]:  $\infty$-[[P-Norms|-norm]]
[^3]: [[Metric Continuity]]
