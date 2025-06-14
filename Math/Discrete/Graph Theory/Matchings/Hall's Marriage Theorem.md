---
tags:
  - atom
  - math
  - discrete
---
Let $G$ be a [[Bipartite Graphs|bipartite graph]] with [[Vertices|vertex]] [[Partitions|parts]] $V_{1}$ and $V_{2}$. Then $G$ has a **complete [[Matchings|matching]]** from $V_{1}$ to $V_{2}$ iff
$$\forall X \subseteq V_{1}, \left| X \right| \le \left| N(X) \right| $$
\[[[Neighbourhood]]\]

> [!definition] For a [[Bipartite Graphs|bipartite graph]] $G$ with [[Vertices|vertex]] [[Partitions|parts]] $V_{1}$ and $V_{2}$, a **complete [[Matchings|matching]]** from $V_{1}$ to $V_{2}$ is a [[Matchings|matching]] that matches all [[Vertices|vertices]] in $V_{1}$.

> [!proof]-
> $\left( \implies \right)$
> Suppose a [[Bipartite Graphs|bipartite graph]] $G$ with [[Vertices|vertex]] [[Partitions|parts]] $V_{1}$ and $V_{2}$, and it has a **complete [[Matchings|matching]]** from $V_{1}$ to $V_{2}$.
> 
> Let $X \subseteq V_{1}$. Since $X$ is [[Matchings|matched]] with $\left| X \right|$ distinct [[Vertices|vertices]], there are at least as many [[Neighbourhood|neighbours]] of $X$ as there are [[Vertices|vertices]] in $X$, i.e.,
> $$\left| X \right| \le \left| N(X) \right|.$$
> 
> $\left( \impliedby \right)$
> Suppose a [[Bipartite Graphs|bipartite graph]] $G$ with [[Vertices|vertex]] [[Partitions|parts]] $V_{1}$ and $V_{2}$, and for all $X\subseteq V_{1}$, $\left| X \right| \le \left| N(X) \right|$.
> 
> By the definition of a [[Bipartite Graphs|bipartite graph]], $V_{1}$ is a [[Coverings|covering]] of $G$.
> 
> Let $W$ be a [[Coverings|minimum covering]] of $G$. Let $S_{1} = W \cap V_{1}$ and $S_{2} = V_{1} - S_{1}$.
> 
> By the premise, $\left| S_{2} \right| \le\left| N(S_{2}) \right|$. But $N(S_{2}) \subseteq W \cap V_{2}$, as $S_{2}$ is by definition not part of the [[Coverings|covering]] $W$, so all of its [[Neighbourhood|neighbours]] must be.
> 
> Thus, $\left| S_{2} \right| \le \left| W \cap V_{2} \right|$, so
> $$\begin{align}
> 	\left| V_{1} \right| &= \left| S_{1} \right| + \left| S_{2} \right| \\
> 	&\le \left| W \cap V_{1} \right| + \left| W\cap V_{2} \right|  \\
> 	&\le \left| W \right|  \\
> \end{align}$$
> Thus, $V_{1}$ must be a **[[Coverings|minimum]]** [[Coverings|covering]] of $G$, so by \[[[Matchings & Coverings with Bipartite Graphs]]\], there is a [[Matchings|matching]] of size $\left| V_{1} \right|$.
> 
> Thus, there is a complete matching from $V_{1}$ into $V_{2}$.

> [!corollary] If $G$ is a $k$[[Regularity|-regular]] [[Bipartite Graphs|bipartite graph]] with $k > 0$, then $G$ has a [[Matchings|perfect matching]].