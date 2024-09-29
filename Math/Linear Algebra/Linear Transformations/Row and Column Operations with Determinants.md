---
tags:
  - atom
  - math
---
Note all of the following rules apply to row operations as well.
- $\left| \vecbf{a}|\vecbf{b}+\vecbf{c} \right|=\left| \vecbf{a}|\vecbf{b} \right|+\left| \vecbf{a}|\vecbf{c} \right|$ (column addition rule)
- $\left| \vecbf{a}|\vecbf{b} \right| = -\left| \vecbf{b}|\vecbf{a} \right|$
- $\left| \vecbf{a} | k\vecbf{b} \right| = k \left| \vecbf{a}|\vecbf{b} \right|$
> [!intuition]-
> Scaling each of the columns in $\begin{bmatrix}1&1\\0&2\end{bmatrix}$ by $2$ gives
> ![500|center](scaling-columns-determinants.excalidraw)
> Note that in both of these cases, the area increases by a factor of $2$.
- $\left| \vecbf{a}|\vecbf{b}+k\vecbf{a} \right| =\left | \vecbf{a}|\vecbf{b} \right|$
> [!proof]-
> $$\begin{align*}
> 	\left| \vecbf{a}|\vecbf{b}+k\vecbf{a} \right| &= \left| \vecbf{a}|\vecbf{b} \right| +\left| \vecbf{a}|k\vecbf{a} \right| && \text{Column addition rule} \\
> 	&= \left| \vecbf{a}|\vecbf{b} \right| + k\left| \vecbf{a}|\vecbf{a} \right|  \\
> 	&= \left| \vecbf{a}|\vecbf{b} \right| + 0k \\
> 	&= \left| \vecbf{a}|\vecbf{b} \right|
> \end{align*}$$ 

\[[[Determinants]]\]