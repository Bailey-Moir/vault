---
tags:
  - atom
  - comp
---
Any *comparison sort [[Algorithms|algorithm]]* requires $\Omega(n\log n)$[^1] comparisons in the [[Formal Definition of Best and Worst Case|worst case]].

> [!proof]
> Let $n,l,$ and $h$ denote the size of the input, the number of [[Leaf Nodes|leaves]] in the [[Trees|tree]], and the [[Tree Height|height of the tree]] respectively.
> 
> We view $h$ as a function of $n$.
> 
> - The number of possible outputs is $n!$.
> - Thus, $l \ge n!$.
> - $2^h \ge l$.
> - Combining these gives $2^h \ge n!$
> 
> $$\begin{align}
> 	\log 2^h &\ge n! \\
> 	h &\ge \log(n!) \\
> 	&\ge \log(n) + \log(n-1) + \dots + \log 1 \\
> 	&\ge \left\lfloor \dfrac{n}{2} \right\rfloor \log \left\lfloor \dfrac{n}{2} \right\rfloor \\
> 	&\in \Omega(n\log n)
> \end{align}$$

[^1]: [[Asymptotic Notation]]
