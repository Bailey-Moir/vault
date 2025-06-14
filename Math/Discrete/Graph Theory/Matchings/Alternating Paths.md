---
tags:
  - atom
  - math
  - discrete
---
An *alternating path* of a [[Matchings|matching]] $M$ of $G$ is a [[Walks|path]] in $G$ whose [[Edges|edges]] alternate between being in $M$ and not being in $M$.

> [!theorem] (Berge, 1957) A [[Matchings|matching]] $M$ of $G$ is a [[Matchings|maximum matching]] iff there are no *alternating paths* in $G$ that connect [[Matchings|unmatched]] [[Vertices|vertices]].

> [!induced algorithm]
> Search for an *alternating path* for your [[Matchings|matching]] $M$ in $G$ that **starts and ends with [[Matchings|unmatched]] [[Vertices|vertices]]**. If such an *alternating path* is found, replace $M$ with $P\setminus M$. Repeat this procedure until no *alternating path* exists. 