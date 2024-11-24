---
tags:
  - atom
  - math
---
Suppose $V_1, \dots, V_m$ are [[Subspaces|subspaces]] of [[Vector Spaces|vector space]] $V$. The sum of these [[Subspaces|subspaces]], denoted by $V_1 + \dots + V_m$, is the set of all possible sums of elements in $V_1, \dots V_m$. More precisely:
$$ V_1 + \dots + V_m = \left\{ v_1 + \dots + v_m : v_1 \in V_1, \dots, V_m \in V_m \right\} $$

>[!proof]- $V_1 + \dots + V_m$ is the smallest subspace of $V$ containing $V_1,\dots,V_m$.
> Suppose $U$ is a [[Subspaces|subspace]] of a [[Vector Spaces|vector space]] $V$, and $V_1, \dots, V_m$ are [[Subspaces|subspaces]] of $U$.
> 
> Since [[Subspaces|subspaces]] are closed under addition, for all $v_1 \in V_1, \dots, v_m \in V_m$, $v_1 + \dots + v_m \in U$. Thus $V_1 + \dots + V_m \subset U$, meaning all [[Subspaces|subspaces]] of $V$ containing $V_1, \dots, V_m$ contain $V_1 + \dots + V_m$.
> i.e. $V_1, \dots, V_m \in U \to V_1 + \dots + V_m \in U$
> 
> There is no [[Subspaces|subspace]] of $V$ containing $V_1, \dots, V_m$ that is smaller than $V_1 + \dots + V_m$, as all [[Subspaces|subspaces]] of $V$ containing $V_1,\dots,V_m$ contain $V_1 + \dots + V_m$.
> 
> Since $V_1 + \dots + V_m$ is known to be a [[Subspaces|subspace]], it then must be the smallest [[Subspaces|subspace]] of $V$ containing $V_1, \dots, V_m$.

Sums of [[Subspaces|subspaces]] in the theory of [[Vector Spaces|vector spaces]] are analogous to [[unions.excalidraw|unions]] of set theory.
\[[[Set Equality]]\]