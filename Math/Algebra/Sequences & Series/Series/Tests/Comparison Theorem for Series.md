---
tags:
  - atom
  - math
---
# The Direct Comparison Test
For all [[Series|series]] $\Sigma a_{k}, \Sigma b_{k}$ such that $\forall k, \left| a_{k} \right| \le b_{k}$, then if $b_{k}$ is [[Partial Sums|convergent]], then $a_k$ is [[Absolute Convergence|absolutely convergent]].

> [!note] the [[Converse, Inverse, and Contrapositive|contrapositive]].

> [!proof]-
> If $\Sigma b_{k}$ [[Partial Sums|converges]], all its [[Partial Sums|partial sums]] are [[Bounded Sequences|bounded]], meaning there exists $B$ such that $\sum_{k=1}^nb_{k} \le B$ for all $n$. Then
> $$\begin{align}
> 	S_{n} = \sum_{k=1}^n \left| a_{k} \right| &= \left| a_{1} \right|  + \left| a_{2} \right| + \dots + \left| a_{n} \right| \\
> 	&\le b_{1} + b_{2} + \dots + b_{n} \\
> 	&= \sum_{k=1}^n b_{k} \\
> 	&= B \\
> \end{align}$$
> Thus, $\Sigma \left| a_{k} \right|$ is [[Bounded Sequences|bounded]], so it is [[Partial Sums|convergent]], so $\Sigma a_{k}$ is [[Absolute Convergence|absolutely convergent]].
> \[[[Partial Sums]], Theorem 3.3\]

> [!example]- Convergence of $\displaystyle\sum_{n=1}^\infty \dfrac{5}{2n^2+4n+3}$
> For sufficiently large $n$ ($n>-\frac{3}{4}$),
> $$\dfrac{5}{2n^2+4n+3} < \dfrac{5}{2n^2}$$
> because the denominator is larger on the $\text{LHS}$.
> $$\sum_{n=1}^\infty \dfrac{5}{2n^2} = \dfrac{5}{2}\sum_{n=1}^\infty \dfrac{1}{n^2}$$
> This is a [[p-series]] where $p=2$, so it converges. By *The Direct Comparison Test*, $\displaystyle\sum_{n=1}^\infty \dfrac{5}{2n^2+4n+3}$ must also converge.

\[[[Comparison Theorem]]\]
# The Limit Comparison Test
For all positive [[Series|series]] $\Sigma a_{n}, \Sigma b_{n}$, if
$$\lim_{ n \to \infty } \dfrac{a_{n}}{b_{n}}=c$$
where $c$ is a finite and $c>0$, then $\Sigma a_{n}$ is convergent iff $\Sigma b_{n}$ is convergent.
> [!proof]-
> Let $m,M \in \Z^+$ such that $m < c < M$. Because $\frac{a_{n}}{b_{n}}$ is close to $c$ for sufficiently large $n$, $\exists N \in \Z : \forall n \in \Z_{>N}$
> $$\begin{array}{c}
> 	m < \dfrac{a_{n}}{b_{n}} < M \\
> 	mb_{n} < a_{n} < Mb_{n}
> \end{array}$$
> - If $\Sigma b_{n}$ converges, so does $\Sigma Mb_{n}$, and by [[#The Direct Comparison Test|the direct comparison test]], so does $\Sigma a_{n}$.
> - If $\Sigma b_{n}$ diverges, so does $\Sigma mb_{n}$, and by [[#The Direct Comparison Test|the direct comparison test]], so does $\Sigma a_{n}$.