---
tags:
  - atom
  - math
---
All [[Bounded Sequences|bounded]] [[Monotone Sequences|monotone sequences]] [[Metric Sequence Convergence|converge]] (to its [[Supremums and Infimums|supremum]]/[[Supremums and Infimums|infimum]]).

> [!proof]-
> **(Increasing)**
> Suppose $\left( a_{n} \right)$ is a [[Bounded Sequences|bounded]] [[Monotone Sequences|increasing sequence]].
> 
> Let $L = \sup\,\{ a_{n} : n \in \N \}$, and $\varepsilon > 0$ be given.
> 
> Since $L$ is an [[Bounded Sets|upper bounded]], we have
> $$\begin{align}
> 	a_{n} &\le L && \forall n \\
> 	&< L + \varepsilon \\
> 	a_{n} - L &< \varepsilon. && 2 \\
> \end{align}$$
> Also, $L-\varepsilon < L$, so $L-\varepsilon$ is not an [[Bounded Sets|upper bound]] for the sequence (by the definition of the [[Supremums and Infimums|supremum]]).
> 
> Thus, there is an $N$ such that
> $$a_{N} > L - \varepsilon.$$
> 
> Since $\left( a_{n} \right)$ is [[Monotone Sequences|increasing]], for every $n \ge N$, we have
> $$\begin{array}{c}
> 	a_{n} \ge a_{N} > L - \varepsilon \\
> 	a_{n} > L - \varepsilon \\
> 	a_{n} - L > -\varepsilon. && 2 \\
> \end{array}$$
> Combining $1$ and $2$ gives
> $$-\varepsilon < a_{n} - L < \varepsilon,$$
> meaning
> $$\left| a_{n}-L \right| < \varepsilon.$$
> 
> **(Decreasing)**
> Suppose $\left( a_{n} \right)$ is a [[Bounded Sequences|bounded]] [[Monotone Sequences|decreasing sequence]].
> 
> Let $b_{n} = -a_{n}$. Then for all $n$,
> $$\begin{align}
> 	a_{n} &\ge a_{n+1} \\
> 	-a_{n} &\le -a_{n+1} \\
> 	b_{n} &\le b_{n+1}. \\
> \end{align}$$
> Thus, $b_{n}$ is [[Monotone Sequences|increasing]].
> 
> Also, since $a_{n} \ge K$ for all $n$,
> $$b_{n} = -a_{n} \le -K,$$
> meaning $\left( b_{n} \right)$ is [[Bounded Sequences|bounded]].
> 
> Thus, by the first part of this proof, $a_{n}$ must converge to its [[Supremums and Infimums|infimum]].

> [!note]  Every [[Monotone Sequences|monotonically increasing sequence]] is [[Bounded Sequences|bounded below]] by its first value, and every [[Monotone Sequences|monotonically decreasing sequence]] is [[Bounded Sequences|bounded above]] by its first value.

> [!extended-version] All [[Monotone Sequences|monotone sequences]] [[Metric Sequence Convergence|converge]] iff they are [[Bounded Sequences|bounded]]