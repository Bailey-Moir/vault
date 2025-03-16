---
tags:
  - atom
  - math
  - linear
---
For any [[Linear Systems|linear system]] $A\vecbf{x} = \vecbf{b}$ over the [[Fields|field]] of [[The Real Numbers|real numbers]], there are either
1. no solutions,
2. a unique solution, or
3. infinitely many solutions.

> [!proof]-
> If there are no solutions or a unique solution, then the theorem holds.
> 
> Suppose the negation is true, and thus that there are multiple solutions. Then there exists $\vecbf{x}_{1}$ and $\vecbf{x}_{2}$ such that $\vecbf{x}_{1} \ne \vecbf{x}_{2}$ and
> $$A\vecbf{x}_{1} = \vecbf{b} = A\vecbf{x}_{2}.$$
> Then,
> $$\begin{align}
> 	A\vecbf{x}_{1} - A\vecbf{x}_{2} &= \vecbf{b}-\vecbf{b} \\
> 	A\left( \vecbf{x}_{1} - \vecbf{x}_{2} \right) &= \vecbf{0} \\
> \end{align}$$
> Thus, $(\vecbf{x}_{1} - \vecbf{x}_{2} \ne \vecbf{0} )\in\text{null}\,A$, meaning $\text{nullity}A \ge 1$. Then
> $$\begin{align}
> 	\forall \vecbf{x}_{0} \in \text{null}\,A,\, A(\vecbf{x}_{1} + \vecbf{x}_{0}) &= A\,\vecbf{x}_{1} + A\,\vecbf{x}_{0} \\
> 	&= \vecbf{b} + \vecbf{0} \\
> 	&= \vecbf{b}, \\
> \end{align}$$
> and since $\left| \text{null}\,A \right| = \infty$, the set of solutions is infinite.