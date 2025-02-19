---
tags:
  - atom
  - math
  - linear
---
$$\forall A \in \F^{m,n}, \left( c = \text{rank}\,A \ge 1\to \exists C\in\F^{m,c}, R \in \F^{c,n} : A = CR \right)$$
> [!proof]-
> Let $c= \text{column rank}\,A$.
> 
> The columns $A_{\cdot,1},\dots,A_{\cdot,n}$ can be [[Linear Independence and Span with Dimension|reduced]] to a [[Basis|basis]] of their [[Span|span]].
> 
> By the definition of [[Rank|rank]], this basis has length $c$.
> 
> These columns can be put together to form a matrix $C \in \F^{m,c}$.
> 
> Each column $k$ of $A$ is then a [[Linear Combinations|linear combination]] of the columns of $C$.
> 
> Thus, putting the coefficients into the $k$-th column of $R \in \F^{c,n}$ gives
> $$A = CR$$

\[[[Rank]]\]