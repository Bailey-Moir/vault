---
tags:
  - atom
  - math
  - linear
---
Suppose $U$ is a [[Subspaces|subspace]] of $V$, and $\vecbf{v},\vecbf{w} \in V$. Then
$$ \vecbf{v}-\vecbf{w} \in U \iff \vecbf{v} + U = \vecbf{w} + U \iff \left(\vecbf{v} + U\right) \cap \left(\vecbf{w} + U\right) \ne \emptyset.$$
> [!proof]-
> $\left( 1\implies 2 \right)$
> Suppose $\vecbf{v}-\vecbf{w} \in U$. Then for all $u \in U$,
> $$\vecbf{v} + \vecbf{u} = \vecbf{w} + \left( (\vecbf{v} - \vecbf{w}) + \vecbf{u}\right) \in \vecbf{w} + U,$$
> meaning $\vecbf{v} + U \subseteq \vecbf{w} + U$. Similarly, $\vecbf{w} + U \subseteq \vecbf{v} + U$, thus $\vecbf{v} + U = \vecbf{w} + U$.
> 
> $\left( 2\implies 3 \right)$
> Suppose $\vecbf{v} + U = \vecbf{w} + U$. Then,
> $$\left(\vecbf{v} + U\right) \cap \left(\vecbf{w} + U\right) = \vecbf{v} + U.$$
> Since this is a [[Subspaces|subspace]]/[[Vector Spaces|vector space]], it can not be the [[Empty Set|empty set]], as it must contain the identity. Thus, $\left(\vecbf{v} + U\right) \cap \left(\vecbf{w} + U\right) \ne \emptyset$.
> 
> $\left( 3\implies 1 \right)$
> Suppose $\left(\vecbf{v} + U\right) \cap \left(\vecbf{w} + U\right) \ne \emptyset$. Then, there exists $\vecbf{u}_{1},\vecbf{u}_{2} \in U$ such that
> $$\begin{align}
> 	\vecbf{v} + \vecbf{u}_{1} &= \vecbf{w} + \vecbf{u}_{2} \\
> 	\vecbf{v} - \vecbf{w} &= \vecbf{u}_{2} - \vecbf{u}_{1} \in U. \\
> \end{align}$$
> Thus, $\vecbf{v}-\vecbf{w} \in U$.