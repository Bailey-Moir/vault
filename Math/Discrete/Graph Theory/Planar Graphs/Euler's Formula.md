---
tags:
  - atom
  - math
  - discrete
---
If $G$ is a [[Connectivitiy|connected]] [[Planar Graphs|planar graph]], then
$$\left| F(G) \right|  = 2 - \left| V(G) \right| + \left| E(G) \right|$$
> [!proof]-
> Let $F(G)$ denote the [[Sets|set]] of faces.
> 
> **Base Case**
> If $\left| E(G) \right| = 0$, then since $G$ is [[Connectivitiy|connected]], $G = K_{1}$[^1], so there will be $1$ face.
> $$\left| F(G) \right|  =  2 - (1) - (0) = 1 $$
> **Induction Step**
> Assume $k \ge 0$, and that the theorem holds for all [[Connectivitiy|connected]] [[Planar Graphs|planar graphs]] with $k$ [[Edges|edges]].
> 
> Let $G$ be a [[Graphs|graph]] such that $\left| E(G) \right| = k$.
> 
> **Case (i)**
> Suppose $G$ has no [[Walks|cycles]]. Then by definition, $G$ is a [[Trees|tree]], meaning $\left| E(G) \right| = \left| V(G) \right| - 1$. A [[Trees|tree]] has only $1$ face, so
> $$\left| F(G) \right|  = 1 = 2 - (\left| E(G) \right| + 1) +  \left| E(G) \right| $$
> **Case (ii)**
> Suppose $G$ has at least one [[Walks|cycle]]. Let $e$ be an [[Edges|edge]] in that cycle. Then by definition, $e$ is not a [[Bridges|bridge]].
> 
> Since $e$ lies on a [[Walks|cycle]] of $G$, then by the [[Planar Graphs|planar graph lemma]], $e$ is on the boundary of $2$ faces, $f_{1}$ and $f_{2}$.
> 
> Removing $e$ disconnects the [[Walks|cycle]], forcing $f_{1}$ and $f_{2}$ to form a single face. decreasing the number of faces by $1$. This gives
>  - $\left| E(G \setminus e)\right| = \left| E(G) \right| - 1$
> -  $\left| V(G \setminus e)\right| = \left| V(G) \right|$
> -  $\left| F(G \setminus e)\right| = \left| F(G) \right|-1$
> 
> Thus, by the [[Induction|induction hypothesis]],
> $$\begin{align}
> 	\left| F(G \setminus e)\right| &= 2 - \left| V(G \setminus e)\right| + \left| E(G \setminus e)\right| \\
> 	\left| F(G)\right| - 1 &= 2 - \left| V(G)\right| + \left| E(G)\right| - 1\\
> 	\left| F(G)\right| &= 2 - \left| V(G)\right| + \left| E(G)\right|\\
> \end{align}$$
> Thus, the theorem holds.

> [!corollary] For [[Connectivitiy|connected]] [[Planar Graphs|planar graphs]], all *planar drawings* of $G$ have the same number of faces.




[^1]: [[Complete Graphs]]
