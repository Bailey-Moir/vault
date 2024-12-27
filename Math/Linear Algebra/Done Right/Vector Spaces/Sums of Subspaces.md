---
tags:
  - atom
  - math
---
The *sum of [[Subspaces|subspaces]]* $U$ and $W$ of $V$ is defined as
$$ U + V = \left\{ \vecbf{u} + \vecbf{w} : \vecbf{u} \in U \land \vecbf{w} \in W \right\} $$

>[!proof]- $V_1 + \dots + V_m$ is the smallest subspace of $V$ containing $V_1,\dots,V_m$.
> Suppose $U$ is a [[Subspaces|subspace]] of $V$, and $V_1, \dots, V_m$ are [[Subspaces|subspaces]] of $U$.
> 
> Since $U$ is closed under addition, and $V_{i} \subseteq U$
> $$\forall \vecbf{v}_1 \in V_1, \dots, \vecbf{v}_{m} \in V_{m}, \left(\vecbf{v}_1 + \dots + \vecbf{v}_m \in U\right)$$
> Thus $V_1 + \dots + V_m \subseteq U$, meaning all [[Subspaces|subspaces]] of $V$ containing $V_1, \dots, V_m$ contain $V_1 + \dots + V_m$.
> $$ V_1, \dots, V_m \in U \to V_1 + \dots + V_m \subseteq U $$
> Thus, there cannot be a [[Subspaces|subspace]] of $V$ smaller than $V_{1} + \cdots + V_{m}$ that contains $V_{1}, \dots, V_{m}$, as if a [[Subspaces|subspace]] of $V$ contains $V_{1}, \dots, V_{m}$, it must contain $V_{1} + \cdots + V_{m}$.

Sums of [[Subspaces|subspaces]] in the theory of [[Vector Spaces|vector spaces]] are analogous to [[unions.excalidraw|unions]] of set theory.