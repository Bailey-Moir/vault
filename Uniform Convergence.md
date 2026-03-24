---
tags:
  - atom
  - math
---
$f \in B(X)$[^1] is *uniformly convergent* to $g \in B(X)$[^1] iff it is [[Metric Sequence Convergence|convergent]] to $g$ in $\left( B(X),d_{\infty} \right)$[^1][^2], i.e. iff
$$ \forall \varepsilon > 0, \exists N \in \N : \forall n \ge N, \sup_{x \in X} \left| f(x) - g(x) \right| < \varepsilon. $$
> [!theorem]- *Uniform Convergence* $\to$ [[Point-wise Convergence|Point-wise convergence]]
> Suppose $f \in B(X)$[^1] is *uniformly convergent* to $g\in B(X)$[^1]. Thus, for all $\varepsilon > 0$, there exists $N \in \N$ such that for all $n \ge N$,
> $$\begin{align}
> 	\sup_{x \in X} \left| f(x) - g(x) \right| &< \varepsilon\\
> 	\to \forall x \in X, \left| f(x) - g(x) \right| &< \varepsilon.\\
> \end{align}$$
> Thus, $f$ is [[Point-wise Convergence|point-wise convergent]] to $g$.

[!theorem] *(Completeness)* If $X \ne \emptyset$, $\left( B(X),d_{\infty} \right)$[^1][^2] is [[Completeness|complete]].
Let $\left( f_{n} \right)$ be a [[Cauchy Sequences|Cauchy sequence]] in $\left( B(X),d_{\infty} \right)$ where $X \ne \emptyset$.
#TODO

[!theorem] *(Preserves Continuity)* Suppose $\left( f_{n} \right)$ is a [[Sequences|sequence]] of [[Bounded Functions|bounded]], [[Metric Continuity|continuous]] [[Functions|functions]] that *uniformly converge* on some $I$ to to a [[Functions|function]] $\lambda$. Then $\lambda$ is [[Metric Continuity|continuous]] on $I$.
#TODO

[^1]: [[Bounded Function Set]]
[^2]:  $\infty$-[[P-Norms|-norm]]