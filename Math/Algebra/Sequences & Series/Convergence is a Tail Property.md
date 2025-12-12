---
tags:
  - atom
  - math
---
The [[Metric Sequence Convergence|convergence]] and [[Metric Sequence Convergence|limit]] of a [[Sequences|sequence]] is unchanged if either
1. we alter finitely many terms, or
2. we add (or remove) finitely many terms at the beginning.

> [!proof]- of **1**
> Let $\left( a_{n} \right)$ be a [[Sequences|sequence]], and $\left( \tilde{a}_{n} \right)$ be a different sequence where
> $$a_{n} = \tilde{a}_{n} \hspace{2em} \forall n \ge N_{0}$$
> for some $N_{0} \in \N$.
> 
> Suppose $\left( a_{n} \right)$ [[Metric Sequence Convergence|converges]].
> 
> Let $\varepsilon>0$ be given. Then there is an $N$ such that for all $n \ge N$,
> $$\left| a_{n} - L \right| < \varepsilon.$$
> Thus, for $n \ge \max\{ N,N_{0} \}$,
> $$\left| \tilde{a}_{n} - L \right| < \varepsilon.$$

> [!proof]- of **2**
> This is basically the same as **1**, just think about it.

# Convergence of Series
The [[Metric Sequence Convergence|convergence]] of a [[Series|series]] is unchanged if either
1. we alter finitely many terms, or
2. we add (or remove) finitely many terms at the beginning.