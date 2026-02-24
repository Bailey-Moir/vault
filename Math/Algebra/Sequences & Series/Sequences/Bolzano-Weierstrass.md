---
tags:
  - atom
  - math
---
Every [[Bounded Sequences|bounded]] [[Sequences|sequence]] $\left( x_{n} \right)$ in $\R$ has a [[Limit Points#^sequence-limit-points|limit point]].

> [!proof]-
> Let $\left( x_{n} \right)$ be a [[Sequences|sequence]] in $\R$ [[Bounded Sequences|bounded]] within $\left[ a_{1},b_{1} \right]$.
> 
> **Base Case**
> $\left[ a_{1},b_{1} \right]$ contains infinitely many points of $\left\{ x_{n} \right\}$, as $\left\{ x_{n} \right\}$ is infinite and $\left\{ x_{n} \right\} \subseteq \left[ a_{1},b_{1} \right]$. Choose $c_{1}$ to be any point in $\{ x_{n} \}$.
> 
> **Induction Step**
> Let $k \in \N$ such that $\left[ a_{k}, b_{k} \right]$ contains infinitely many points of $\{ x_{n} \}$. Let 
> $$m_{n} = \dfrac{a_{n} + b_{n}}{2}.$$
> At least least one of $\left[ a_{n},m_{n} \right]$ and $\left[ b_{n},m_{n} \right]$ must contain an infinite number of points of $\{ x_{n} \}$ (as their union $\left[ a_{n},b_{n} \right]$ does). Let $\left[ a_{n+1},b_{n+1} \right]$ be such an [[Intervals|interval]]. 
> 
> Let $c_{k+1}$ be any of the infinitely many points of $\left( \{ x_{n} \} \cap \left[ a_{n+1}, b_{n+1} \right] \right) \setminus \{ c_{i} : i \in \Z^+_{i \le k+1} \}$.
> 
> Note that $\left[ a_{k+1},b_{k+1} \right] \subseteq \left[ a_{k},b_{k} \right]$.
> 
> **Conclusion**
> Since $\forall k \in \Z^+, \left[ a_{k+1},b_{k+1} \right] \subseteq \left[ a_{k},b_{k} \right]$, $(a_{n})$ is [[Increasing and Decreasing Functions|increasing]] and $\left( b_{n} \right)$ is [[Monotone Sequences|decreasing]] also, and they are [[Bounded Sets|bounded]] within $\left[ a_{1},b_{1} \right]$. Thus, they both [[Metric Sequence Convergence|converge]] by [[Monotone Convergence Theorem|MCT]].
> 
> Further
> $$\begin{align}
> 	a_{n} - b_{n} &= \dfrac{a_{1} - b_{1}}{2^{n-1}} \\
> 	\lim_{ n \to \infty } \left( a_{n} - b_{n} \right) &= \lim_{ n \to \infty } \dfrac{a_{1} - b_{1}}{2^{n-1}} = 0 \\
> 	\lim_{ n \to \infty } a_{n} &= \lim_{ n \to \infty } b_{n}. \\
> \end{align}$$
> 
> By [[Squeeze Theorem for Sequences|squeeze theorem]], since $a_{n} \le c_{n} \le b_{n}$ for all $n$, $\left( c_{n} \right)$ must also [[Metric Sequence Convergence|converge]].
> 
> Thus, $\lim_{ n \to \infty } (c_{n})$ is a [[Limit Points#^sequence-limit-points|limit point]] of $\left( x_{n} \right)$.

> [!note] This generalises to $\R^n$.