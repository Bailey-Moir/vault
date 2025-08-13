---
tags:
  - atom
  - math
---
The *partial sums* of a [[Series|series]] is a [[Sequences|sequence]] $\left( S_{n} \right)$, where each term is the sum of the terms before it in the [[Series|series]].
$$\begin{array}{cc}
	\begin{array}{l}
		S_0 = a_0 \\
		S_1 = a_0 + a_1 \\
		S_2 = a_0 + a_1 + a_2 \\
		S_3 = a_0 + a_1 + a_2 + a_3 \\
		\dots
	\end{array}
	&
	\begin{array}{rcl}
		S_n = \displaystyle\sum_{k=0}^n a_k
	\end{array}
\end{array}$$
$$\sum_{k=0}^\infty a_k = \lim_{k\to\infty} S_k = S_\infty$$

> [!inductive-definition] **3.1** - For any [[Series|series]] $\sum_{k=0}^\infty a_{n}$,  $S_{0} = a_{0}$, and for all $n \in \N$,$$S_{n+1} = S_{n} + a_{n+1}$$

> [!theorem] A [[Series|series]] **converges** iff its *partial sums* [[Convergence of Sequences|converges]] .

> [!theorem]- **3.3** - A [[Series|series]] $\sum_{k=0}^\infty a_{k}$ with $a_{k_{2}} \ge 0$ is convergent iff the *partial sums* $(S_{n})$ are [[Bounded Sequences|bounded]].
> Note that
> $$\begin{align}
> 	S_{n+1} &= S_{n} + a_{n+1} \\
> 	&\ge S_{n}.
> \end{align}$$
> Thus, the [[Sequences|sequence]] of *partial sums* is [[Monotone Sequences|increasing]]. Since it is also [[Bounded Sequences|bounded]], by [[Monotone Convergence Theorem|monotone convergence theorem]], it must [[Convergence of Sequences|converge]].