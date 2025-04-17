---
tags:
  - atom
  - math
  - discrete
---
In *cycle notation*, each [[Components of Graphs|component]] of the [[Symmetric Groups|symmetric group]] is brackets, with each containing a [[Cycle Notation|cycle]].  

> [!example]
> $$\begin{array}{cccc}
> 	\sigma(1) = 2 &
> 	\sigma(2) = 1 &
> 	\sigma(3) = 6 &
> 	\sigma(4) = 4 &
> 	\sigma(5) = 3 &
> 	\sigma(6) = 5 &
> \end{array}$$
> can be written as
> $$ \sigma = \left( 1 \; 2 \right)\left( 3 \; 6 \; 5 \right), $$
> where $\left( 1\;2 \right)$, $\left( 3\;6\;5 \right)$, and $\left( 4 \right)$ are [[Disjoint Sets|disjoint]] [[Walks|cycles]], each an element in $S_{6}$.

> [!lemma] Each [[Permutations|permutation]] in $S_{n}$[^1] can be written as a product/[[Composite Functions|composition]] of [[Disjoint Sets|disjoint]] [[Walks|cycles]].

[!lemma]- If $\sigma$ and $\tau$ are *cycles* in $S_{n}$[^1] with no common entries, then $\sigma\tau = \tau\sigma$.
Suppose $\sigma$ and $\tau$ are [[Disjoint Sets|disjoint]] [[Walks|cycles]] in $S_{n}$, and let $i \in \{ 1,\dots,n \}$.

If $i$ does not appear in $\sigma$, then $\sigma(i) = i$, and $\tau(i)$ does not appear in $\sigma$ (as they a [[Disjoint Sets|disjoint]]).
$$\begin{align}
	\tau\sigma(i) & = \tau(\sigma(i)) = \tau(i) \\
	\sigma\tau(i) & = \sigma(\tau(i)) = \tau(i)\\
\end{align}$$
If $i$ does not appear in $\tau$, this gives the same result.


> [!note] The [[Inverse Functions|inverse]] in *cycle notation* just reverses the order:
> $$\left( 1\;2\;3 \right)^{-1} = (3\;2\;1)$$

[^1]: [[Symmetric Groups]]