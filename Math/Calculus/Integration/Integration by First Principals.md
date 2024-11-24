---
tags:
  - math
  - atom
---
Integration by first principals is done with the [[Archive/Deatomized/Calculus/Algebra/Limits|limit]] of a [[Riemann Sums|Riemann sum]] as $n \to \infty$. It is used very frequently in proofs.
$$\begin{array}{l}
	\displaystyle \lim_{n\to\infty} \sum_{i=1}^n f(x_i^*) \Delta{x} = \int_a^b f(x) \, dx \\
	\text{where } \Delta x = \dfrac{b-a}{n} \\
	\text{and } x_i^* \in [x_{i-1},x_i] \\
	\phantom{\text{and } x_i^*} \in  [a + (i-1)\Delta x, a + i\Delta x] \\
\end{array}$$
