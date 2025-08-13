---
tags:
  - atom
  - math
  - discrete
---
For any [[Graphs|graph]] $G=\left( V,E \right)$, there is a *[[Matchings|matching]] [[Matroids|matroid]]* $(V, \mathcal{I})$, where $U \in \mathcal{I}$ iff there is a [[Matchings|matching]] of $G$ that [[Matchings|matches]] the [[Vertices|vertices]] of $U$.

> [!proof]-
> **Empty Set**
> The [[Empty Set|empty set]] of [[Vertices|vertices]] is matched by the [[Empty Set|empty set]] of [[Edges|edges]], a [[Matchings|matching]] of $G$. Thus, $\emptyset \in \mathcal{I}$.
> 
> **Hereditary Property**
> Suppose $V_{1} \subseteq V$ is [[Matroids|independent]] ($V_{1} \in \mathcal{I}$). Then there exists a [[Matchings|matching]] $M$ that matches each [[Vertices|vertex]] in $V_{1}$. This [[Matchings|matching]] $M$ still matches every [[Subsets|subset]] of $V_{1}$, so every [[Subsets|subset]] of $V_{1}$ is [[Matroids|independent]].
> 
> **Augmentation Property**
> Suppose $V_{1}$ and $V_{2}$ are [[Matchings|independent]] ($V_{1},V_{2} \in \mathcal{I}$), where $\left| V_{1} \right| > \left| V_{2} \right|$. Then there exists [[Matchings|matchings]] $M_{1}$ and $M_{2}$ that match the [[Vertices|vertices]] of $V_{1}$ and $V_{2}$ respectively.

> [!note] This is actually false... cause maximal $\not\to$ maximum.