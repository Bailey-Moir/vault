---
tags:
  - atom
  - math
---
- *Monotonic sequences* (or *monotone sequences*) are [[Sequences|sequences]] that are either entirely non-decreasing or entirely non-increasing.
$$\begin{array}{ccc}
	(\forall n \ge 1, a_n \le a_{n+1} ) \!\!&\!\!\lor\!\!&\!\! (\forall n \ge 1, a_n \ge a_{n+1} ) \\
	\text{increasing}\!\!&\!\!\text{or}\!\!&\!\! \text{decreasing} \\
\end{array}$$

- ***Strictly*** *monotonic sequences* are [[Sequences|sequences]] that are either entirely **strictly** increasing or entirely **strictly** decreasing.
$$\begin{array}{ccc}
	(\forall n \ge 1, a_n < a_{n+1} ) \!\!&\!\!\lor\!\!&\!\! (\forall n \ge 1, a_n > a_{n+1} ) \\
	\text{strictly increasing}\!\!&\!\!\text{or}\!\!&\!\! \text{strictly decreasing} \\
\end{array}$$

- ***Eventually*** *monotonic sequences* are [[Sequences|sequences]] that are monotonic beyond some element $k$.
$$\begin{array}{ccc}
	(\forall n \ge k, a_n \le a_{n+1} ) \!\!&\!\!\lor\!\!&\!\! (\forall n \ge k, a_n \ge a_{n+1} ) \\
	\text{eventually increasing}\!\!&\!\!\text{or}\!\!&\!\! \text{eventually decreasing} \\
\end{array}$$

> [!note]- Methods of determining whether a sequence is increasing or decreasing
> A [[Sequences|sequence]] can be shown to be *monotonically* increasing by showing either:
> - $\forall n \ge 1, a_{n+1} - a_n \ge 0$
> - $\forall n \ge 1, \dfrac{a_{n+1}}{a_{n}} \ge 1$
> - If the [[Sequences|sequence]] is embedded in $f$, $\forall x > 0, f'(x) \ge 0$ (see [[Extending Sequences]])

\[[[Increasing and Decreasing Functions]]\]