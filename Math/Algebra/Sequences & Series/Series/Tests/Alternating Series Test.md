---
tags:
  - atom
  - math
---
An *alternating series* of the form $\Sigma_{k=1}^\infty(-1)^{k-1} a_k$ where $a_{k} > 0$ must [[Partial Sums|converge]]  if both $\lim a_k = 0$ and $(a_k)$ [[Monotone Sequences|monotonically]] decreases.

> [!proof]-
> Since $\left( a_{n} \right)$ is [[Monotone Sequences|decreasing]], for all $n$,
> $$\begin{align}
> 	a_{n} &\ge a_{n+1} \\
> 	a_{n} - a_{n+1} &\ge 0. \\
> \end{align}$$
> First, consider the even terms.
> $$\begin{align}
> 	S_{2n} &= S_{2(n-1)} + \underbrace{a_{2n-1} - a_{2n}}_{\ge 0} \\
> 	&\le  S_{2(n-1)}, \\
> \end{align}$$
> so the even terms are [[Monotone Sequences|increasing]], and
> $$\begin{align}
> 	S_{2n} &= a_{1} - \underbrace{(a_{2} - a_{3})}_{\ge 0} - \underbrace{(a_{4} - a_{5})}_{\ge 0} - \cdots - \underbrace{(a_{2n-2} - a_{2n-1})}_{\ge 0} - \underbrace{a_{2n}}_{\ge 0} \\
> 	&\le a_{1}, \\
> \end{align}$$
> so the even terms are [[Bounded Sequences|bounded]], so the even terms must [[Sequence Convergence|converge]] by [[Monotone Convergence Theorem|monotone convergence theorem]].
> 
> Similarly, consider the odd terms.
> $$\begin{align}
> 	S_{2n-1} &= S_{2(n-1)-1} - \underbrace{(a_{2n-2} - a_{2n-1})}_{\ge 0} \\
> 	&\ge  S_{2(n-1)}, \\
> \end{align}$$
> so the odd terms are [[Monotone Sequences|decreasing]], and
> $$\begin{align}
> 	S_{2n-1} &= \underbrace{(a_{1} - a_{2})}_{\ge 0} + \underbrace{(a_{3} - a_{4})}_{\ge 0} + \cdots + \underbrace{(a_{2n-2} - a_{2n-1})}_{\ge 0} \\
> 	&\ge 0, \\
> \end{align}$$
> so the odd terms are [[Bounded Sequences|bounded]], so the odd terms must [[Sequence Convergence|converge]] by [[Monotone Convergence Theorem|monotone convergence theorem]].
> 
> The odd and even terms must have the same [[Sequence Convergence|limit]] as [[Convergence is a Tail Property|convergence is a tail property]].