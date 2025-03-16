---
tags:
  - atom
  - comp
---
For a [[Graphs|graph]] $G = (V,E)$ where $\left| V \right| = n$ and $\left| E \right| = m$,

| **Aspect**                                                 | **[[Adjacency Matrices\|Adj. Matrix]]** | **[[Adjacency Lists\|Adj. List]]** |
| ---------------------------------------------------------- | --------------------------------------- | ---------------------------------- |
| [[Edges\|Incidence]] of $(i,j)$                            | $\Theta(1)$                             | $O(n)$                             |
| Adding an [[Edges\|edge]] (w/ existence check)             | $\Theta(1)$                             | $O(n)$                             |
| Deleting an [[Edges\|edge]]                                | $\Theta(1)$                             | $O(n)$                             |
| Iterating over [[Edges\|edges]] for a [[Vertices\|vertex]] | $\Theta(n)$                             | $O(n)$                             |
| Iterating over all [[Edges\|edges]]                        | $\Theta(n^2)$                           | $\Theta(n+m)$                      |
| Space                                                      | $\Theta(n^2)$                           | $\Theta(n+m)$                      |
\[[[Asymptotic Notation]]\]