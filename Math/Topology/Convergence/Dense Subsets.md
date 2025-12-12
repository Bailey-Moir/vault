---
tags:
  - atom
  - math
---
$S \subseteq X$ is *dense* iff $\bar{S} = X$[^1]

> [!theorem-1]- $S \subseteq X$ is *dense* iff every non-[[Empty Set|empty]] [[Open Sets|open set]] meets $S$.
> By the [[Closures|characterisation of closures]], $p \in \bar{S}$ iff every [[Neighbourhoods|neighbourhood]] of $p$ meets $S$.
> $\left( \implies \right)$
> If $\bar{S} = X$ ($S$ is *dense*), $X \subseteq \bar{S}$, so every [[Neighbourhoods|neighbourhood]] of every $p \in X$ meets $S$. In other words, every [[Open Sets|open set]] that contains some $p \in X$ (every non-[[Empty Set|empty]] [[Open Sets|open set]]) meets $S$.
> 
> $\left( \impliedby \right)$
> Suppose every non-[[Empty Set|empty]] [[Open Sets|open set]] meets $S$. Then for all $p \in X$, every [[Neighbourhoods|neighbourhood]] of $p$ (which is then non-[[Empty Set|empty]]) meets $S$, meaning $p \in \bar{S}$. Thus, $X \subseteq \bar{S}$, and since obviously $\bar{S} \subseteq X$, this gives $\bar{S} = X$.

[^1]: [[Closures]]
