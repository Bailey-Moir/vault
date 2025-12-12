---
tags:
  - atom
  - math
---
A *series* is very similar to a [[Sequences|sequence]], except all of the terms are added to each other.

> [!theorem]- **3.2** - If *series* a [[Partial Sums|converges]], the [[Metric Sequence Convergence|limit]] of its terms is zero.
> Let the *series* $\sum_{k=1}^\infty a_{n}$ be given to converge to $L$, meaning $\lim S_{n} = L$.
> 
> Since [[Convergence is a Tail Property|convergence is a tail property]], this is equivalent to $\lim S_{n+1} = L.$
> 
> Thus,
> $$\begin{align}
> 	\lim a_{n} &= \lim \left[ S_{n} + a_{n} - S_{n} \right] \\
> 	&= \lim \left[ S_{n+1} - S_{n} \right] \\
> 	&= L - L && \text{2.6.1 \& 2.6.2} \\
> 	&= 0 \\
> \end{align}$$