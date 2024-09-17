---
tags:
  - atom
  - comp
---
Time taken depends on the language, the device, the external and internal conditions, etc. Big Oh Notation is independent of these.
- Find an operation that is done at least as much as any other.
- Find how often it is done in terms of $n$.
- Take the highest order terms
- Remove constants
For a [[Polynomials|polynomial]], the term of the highest order becomes infinitely larger than the other terms as $n \to \infty$, so the lower order terms are ignored. Coefficients are also ignored.
$$\begin{array}{c}
	a_nx^n + a_{n-1}x^{n-1} + \dots + a_{1}x + a_0 \\
	O(x^n)
\end{array}$$

> [!example]
> $$\begin{array}{c}
> 	T_n \\
> 	O(n^2)
> \end{array}$$