---
tags:
  - atom
  - math
---
$$\begin{array}{ccc}
(\forall n \ge 1, a_n < a_{n+1} ) \!\!&\!\!\lor\!\!&\!\! (\forall n \ge 1, a_n > a_{n+1} ) \\
\text{increasing}\!\!&\!\!\text{or}\!\!&\!\! \text{decreasing} \\
\end{array}$$
Increasing sequences that are [[Bounded Sequences|bounded above]] and decreasing sequences that are [[Bounded Sequences|bounded below]] [[Convergence and Divergence of Sequences|converge]], implying that all [[Bounded Sequences|bounded]] monotonic sequences [[Convergence and Divergence of Sequences|converge]].

> [!example]-
> $$\begin{array}{l}
> 	\text{Prove convergency of } \displaystyle\sum_{n=1}^\infty \dfrac{1}{n^2} \\\\
> 	\text{Notice that $s_n$ always increases as $n$}\\
> 	\text{increases, meaning $s_n$ monotonically} \\
> 	\text{increases.} \\
> 	\\
> 	\begin{align*}
> 		0 < \sum_{n=1}^\infty \dfrac{1}{n^2} &< \dfrac{1}{1^2} + \int_1^\infty \dfrac{1}{x^2} \, dx \\
> 		&< 2
> 	\end{align*}
> 	\\
> 	\text{Monotonically increases and bounded} \\
> 	\text{above, therefore convergent}
> \end{array}$$