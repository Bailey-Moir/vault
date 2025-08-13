---
tags:
  - atom
  - math
---
A [[Series|series]] $\Sigma a_{k}$ is called *absolutely convergent* iff the [[Series|series]] $\Sigma \left| a_{k} \right|$ is [[Partial Sums|convergent]]. 

> [!theorem]- *absolute convergence* $\to$ [[Partial Sums|convergent]]
> Split the series $\Sigma a_{k}$ into its positive and negative parts by letting $b_{k} = \max\{ a_{k},0 \}$, and let $c_{k} =\text{max}\{ 0,-a_{k} \}$. Then
> $$a_{k} = b_{k} - c_{k}.$$
> 
> Let $\sum_{k=1}^\infty \left| a_{k} \right| = L$. Since $\left| a_{k} \right| \ge 0$, for all $n$, $\sum_{k+1}^n\left| a_{k} \right| \le L$.
> 
> Since $0 \le b_{k} \le \left| a_{k} \right|$,
> $$0 \le \sum_{k=1}^n b_{k} \le \sum_{k+1}^n \left| a_{k} \right| \le L.$$
> $\Sigma b_{k}$ is then [[Bounded Sequences|bounded]] and has positive terms ([[Monotone Sequences|increasing]]), so it [[Monotone Convergence Theorem|converges]]. Similarly, since $0 \le c_{k} \le \left| a_{k} \right|$, $\Sigma c_{k}$ [[Monotone Convergence Theorem|converges]].
> 
> By [[Series Limit Laws|theorem 3.4.1]], since $a_{k} = b_{k} - c_{k}$, $\Sigma a_{k} = \Sigma b_{k} - \Sigma c_{k}$, and $\Sigma a_{k}$ [[Partial Sums|converges]].

> [!definition] $\Sigma a_{n}$ is **conditionally convergent** iff it is convergent but not *absolutely convergent.*

> [!note] 
> - $\Sigma a_{k}$ is *absolutely convergent* iff the [[Partial Sums|partial sums]] of both the positive and negative parts [[Convergence of Sequences|converge]], and
> - $\Sigma a_{k}$ is **conditionally convergent** iff the [[Partial Sums|partial sums]] of both the positive and negative parts [[Convergence of Sequences|diverge]], and

- If a [[Series|series]] is *absolutely convergent*, all rearrangements have the same sum. However, if a [[Series|series]] is **conditionally convergent**, it can be rearranged to give any real number.