---
tags:
  - atom
  - math
---
All [[Bounded Sequences|bounded]] [[Monotone Sequences|monotone sequences]] [[Metric Sequence Convergence|converge]]. Specifically,
- if $(a_{n})$ is [[Monotone Sequences|increasing]] and [[Bounded Sequences|bounded above]], $\displaystyle\lim_{ n \to \infty }(a_{n}) = \sup \{ a_{n} \}$, and
- if $(a_{n})$ is [[Monotone Sequences|decreasing]] and [[Bounded Sequences|bounded below]], $\displaystyle\lim_{ n \to \infty }(a_{n}) = \inf \{ a_{n} \}$.

> [!proof]-
> **(Increasing)**
> Suppose $\left( a_{n} \right)$ is a [[Monotone Sequences|increasing sequence]] that is [[Bounded Sequences|bounded above]].
> 
> Let $L = \sup\,\{ a_{n} \}$, and $\varepsilon > 0$ be given. Since $L$ is an [[Bounded Sets|upper bound]], we have
> $$\begin{align}
> 	a_{n} &\le L && \forall n \\
> 	&< L + \varepsilon \\
> 	a_{n} - L &< \varepsilon. && 1 \\
> \end{align}$$
> We also have that $L-\varepsilon < L$, so $L-\varepsilon$ is not an [[Bounded Sets|upper bound]] (by the definition of the [[Supremums and Infimums|supremum]]). Thus, there is an $N \in \N$ such that
> $$a_{N} > L - \varepsilon.$$
> Since $\left( a_{n} \right)$ is [[Monotone Sequences|increasing]], for every $n \ge N$, we have
> $$\begin{array}{c}
> 	a_{n} \ge a_{N} > L - \varepsilon \\
> 	a_{n} > L - \varepsilon \\
> 	a_{n} - L > -\varepsilon. && 2 \\
> \end{array}$$
> Combining $1$ and $2$ gives
> $$\begin{align}
> 	-\varepsilon < \;&a_{n} - L < \varepsilon, \\
> 	\quad&\hspace{-0.5ex}\left| a_{n}-L \right| < \varepsilon.
> \end{align}$$
> Thus, $\lim_{ n \to \infty } (a_{n}) = \sup \{ a_{n} \}$
> 
> **(Decreasing)**
> Suppose $\left( a_{n} \right)$ is a [[Monotone Sequences|decreasing sequence]] that is [[Bounded Sequences|bounded below]].
> 
> Let $b_{n} = -a_{n}$. Then for all $n$,
> $$\begin{align}
> 	a_{n+1} &\le a_{n} \\
> 	-a_{n+1} &\ge -a_{n} \\
> 	b_{n+1} &\ge b_{n}. \\
> \end{align}$$
> Thus, $b_{n}$ is [[Monotone Sequences|increasing]].
> 
> For some $K$, $a_{n} \ge K$ for all $n$, which gives
> $$b_{n} = -a_{n} \le -K,$$
> meaning $\left( b_{n} \right)$ is [[Bounded Sequences|bounded above]].
> 
> Thus, by the first part of this proof, $b_{n}$ [[Metric Sequence Convergence|converges]] to its [[Supremums and Infimums|supremum]], which gives that $a_{n}$ [[Metric Sequence Convergence|converges]] to its [[Supremums and Infimums|infimum]].

> [!note]  Every [[Monotone Sequences|monotonically increasing sequence]] is [[Bounded Sequences|bounded below]] by its first value, and every [[Monotone Sequences|monotonically decreasing sequence]] is [[Bounded Sequences|bounded above]] by its first value.

> [!extended-version] All [[Monotone Sequences|monotone sequences]] [[Metric Sequence Convergence|converge]] iff they are [[Bounded Sequences|bounded]]