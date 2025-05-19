---
tags:
  - atom
  - math
  - discrete
---
For a [[Simple Graphs|simple]] [[Connectivitiy|connected]] [[Planar Graphs|planar graph]] $G$ with $\left| V(G) \right| \ge 3$,
$$ \left| E(G) \right| \le 3\left| V(G) \right| - 6 $$
> [!proof]-
> The [[Face Degrees|degree of each face]] of $G$ is at least $3$.
> 
> It follows that, if $f$ is the number of faces in $G$, the sum of the [[Face Degrees|face degrees]] is greater than or equal to $3f$.
> 
> Furthermore, every [[Edges|edge]] is counted exactly twice when [[Walks|walking]] the boundary of every face.
> 
> Thus,
> $$3f \le \dfrac{1}{\left|F(G)\right|}\sum_{f \in F(G)} d(f) = 2\left| E(G) \right| \hspace{2em}(1)$$
> 
> Using [[Euler's Formula|Euler's formula]], we find another expression for $3f$:
> $$\begin{align}
> 	3f &= 3(2 - \left| V(G) \right| + \left| E(G) \right| ) \\
> 	3f &= 6 - 3\left| V(G) \right| + 3\left| E(G) \right| \\
> 	2\left| E(G) \right|  &\ge 6 - 3\left| V(G) \right| + 3\left| E(G) \right| && (1) \\
> 	 \left| E(G) \right| &\le 3\left| V(G) \right| - 6 \\
> \end{align}$$

\[to [[Euler's Formula]]\]