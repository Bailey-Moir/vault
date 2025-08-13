---
tags:
  - atom
  - math
---
- *Monotonic sequences* (or *monotone sequences*) are [[Sequences|sequences]] that are either entirely increasing or entirely decreasing, allowing repeated values.
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

> [!note]- Methods of Determining Monotonicity
> A [[Sequences|sequence]] can be shown to be *monotonically* increasing by showing:
> - $\forall n \ge 1, a_{n+1} - a_n \ge 0$
> - $\forall n \ge 1, \dfrac{a_{n+1}}{a_{n}} \ge 1$
> - For some continuous extension $f$ of $\{a_n\}$, $\forall x > 0, f'(x) \ge 0$ (see [[Extending Sequences]])