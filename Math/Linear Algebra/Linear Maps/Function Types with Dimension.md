---
tags:
  - atom
  - math
  - linear
---
Similar to the corresponding rules with [[Cardinality|cardinality]], for $T \in \mathcal{L}(V,W)$ such that $V$ and $W$ are [[Finite-Dimensional Vector Spaces|finite-dimensional]]:
- $T$ can be [[Injective Functions|injective]] iff $\text{dim}\,V \le \dim\,W$.
  > [!proof]-
> ($\implies$)
> Suppose $T$ is [[Injective Functions|injective]]. By the [[Rank-Nullity Theorem|rank-nullity theorem]],
> $$\begin{align}
> 	\text{dim}\,V &= \text{dim}\,\text{null}\,T + \text{dim}\,\text{range}\,T \\
> 	&= \text{dim}\,\text{range}\,T \\
> 	&\le \text{dim}\,W \\
> \end{align}$$
> 
> ($\impliedby$)
> Suppose $\text{dim}\,V\le\text{dim}\,W$. By the [[Rank-Nullity Theorem|rank-nullity theorem]],
> $$\begin{align}
> 	\text{dim}\,\text{null}\,T &= \text{dim}\,V - \text{dim}\,\text{range}\,T \\
> 	&\le \text{dim}\,W - \text{dim}\,\text{range}\,T \\
> 	&\le \text{dim}\,W - \text{dim}\,W \\
> 	&\le 0. \\
> \end{align}$$
> Thus, $\text{null}\,T = \{ \vecbf{0} \}$, and this is true iff $T$ is [[Injective Functions|injective]][^1].

- $T$ can be [[Surjective Functions|surjective]] iff $\text{dim}\,V \ge \dim\,W$.
  > [!proof]-
> ($\implies$)
> Suppose $T$ is [[Surjective Functions|surjective]]. By the [[Rank-Nullity Theorem|rank-nullity theorem]],
> $$\begin{align}
> 	\text{dim}\,V &= \text{dim}\,\text{null}\,T + \text{dim}\,\text{range}\,T \\
> 	\text{dim}\,V &= \text{dim}\,\text{null}\,T + \text{dim}\,W \\
> 	&\ge \text{dim}\,W \\
> \end{align}$$
> 
> ($\impliedby$)
> Suppose $\text{dim}\,V<\text{dim}\,W$. By the [[Rank-Nullity Theorem|rank-nullity theorem]],
> $$\begin{align}
> 	\text{dim}\,\text{range}\,T &= \text{dim}\,V - \text{dim}\,\text{null}\,T \\
> 	&< \text{dim}\,W - \text{dim}\,\text{null}\,T \\
> 	\text{dim}\,\text{range}\,T &< \text{dim}\,W. \\
> \end{align}$$
Thus, since $\text{range}\,T$ is a [[Subspaces|subspace]] of $W$ and $W$ is [[Finite-Dimensional Vector Spaces|finite-dimensional]], $\text{range}\,T \ne W$[^2], meaning $T$ can not be [[Surjective Functions|surjective]]. Thus, by [[Proof by Contraposition|contraposition]], $T$ can only be [[Surjective Functions|surjective]] if $\text{dim}\,V\ge\text{dim}\,W$.

-  $T$ is [[Bijective Functions|bijective]] (and thus [[Linear Map Invertibility|invertible]]) iff $\text{dim}\,V = \text{dim}\,W$ and $T$ is [[Injective Functions|injective]] or [[Surjective Functions|surjective]].
> [!proof]-
> ($\implies$)
> If $T$ is [[Bijective Functions|bijective]], by the above theorems, $\text{dim}\,V = \text{W}$, and by the definition of [[Bijective Functions|bijectivity]], it must also be [[Injective Functions|injective]] and [[Surjective Functions|surjective]].
> 
> ($\impliedby$)
> If $T$ is [[Injective Functions|injective]], $\text{null}\,T = \{ \vecbf{0} \}$[^1], meaning by the [[Rank-Nullity Theorem|rank-nullity theorem]],
> $$ \text{dim}\,\text{range}\,T = \text{dim}\,V - \text{dim}\,\text{null}\,T = \text{dim}\,V = \text{dim}\,W $$
> Thus, $T$ is [[Surjective Functions|surjective]] (and thus [[Bijective Functions|bijective]]).
> 
> [[Converse, Inverse, and Contrapositive|Conversely]], if $T$ is [[Surjective Functions|surjective]]
> $$ \text{dim}\,\text{null}\,T = \text{dim}\,V - \text{dim}\,\text{range}\,T = \text{dim}\,V - \text{dim}\,W = 0 $$
> Thus, $T$ is [[Injective Functions|injective]] (and thus [[Bijective Functions|bijective]]).

\[[[Dimension]]\]

[^1]: [[Null Space]]
[^2]: [[Dimension Equality Theorem]]