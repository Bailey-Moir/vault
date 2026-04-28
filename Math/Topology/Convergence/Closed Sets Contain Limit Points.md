---
tags:
  - atom
  - math
---
$S \subseteq X$ is [[Closed Sets|closed]] iff all of its [[Limit Points|limit point]] are contained in $S$.

[!proof]
$\left( \implies \right)$
Let $S\in X$ be [[Closed Sets|closed]] and $p \notin S$.

Then $p \in S^c \in \mathcal{T}$, and since $S \cap S^c = \emptyset$, $p$ is not a [[Limit Points|limit point]] of $S$.

Thus, by [[Proof by Contraposition|contraposition]], if $S$ is [[Closed Sets|closed]] and $p$ is a [[Limit Points|limit point]] of $S$, then $p \in S$.

$\left( \impliedby \right)$
Suppose $S \in X$ is **not** [[Closed Sets|closed]],  and that the limit of every [[Sequence Convergence|convergent sequence]] $\left( x_{n} \right) \subseteq S$ is in $S$.

$S^c \notin X$

> [!corollary] In a [[Hausdorff Spaces|Hausdorff space]], this means $S \subseteq X$ is [[Closed Sets|closed]] iff the limit of every [[Sequence Convergence|convergent sequence]] $\left( x_{n} \right) \subseteq S$ is in $S$