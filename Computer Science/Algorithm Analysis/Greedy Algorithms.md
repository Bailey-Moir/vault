---
tags:
  - atom
  - comp
---
A *greedy algorithm* is an [[Algorithms|algorithm]] that chooses the option that looks best at the moment, hoping that a locally optimal choice will lead to a globally optional solution. The general *greedy algorithm* is

> [!the greedy algorithm]
> Input: A [[Matroids|matroid]] $M = \left( E, \mathcal{I} \right)$ with a weight [[Functions|function]] $w : E \to \R^+$.
> Output: A [[Maximal vs. Maximum|maximal]]/[[Maximal vs. Maximum|maximum]] [[Matroids|independent set]] $I \in \mathcal{I}$ of [[Maximal vs. Maximum|minimal]] weight, and its weight $w(I)$.
> 1. Set $I = \emptyset$ and $w(I) = 0$.
> 2. Choose an element $x \in E-I$ of minimum weight, $w(x)$, such that $I \cup \{ x \} \in \mathcal{I}$.
> 	- $I \leftarrow I \cup \{ x \}$
> 	- $w(I) \leftarrow w(I) + w(x)$.
> If there is no such element, stop.
> 3. Goto step 2.