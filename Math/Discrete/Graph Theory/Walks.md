---
tags:
  - atom
  - math
  - discrete
---
A *walk* in a [[Graphs|graph]] is an alternating [[Sequences|sequence]] of [[Vertices|vertices]] and [[Math/Discrete/Graph Theory/Definitions/Edges|edges]].
$$v_{1},e_{1},v_{2},e_{2},v_{3},\dots,v_{k-1},e_{k-1},v_{k}$$
such that $e_i$ joins $v_i$ and $v_{i+1}$.
- A **closed walk** is a *walk* where the first and last [[Vertices|vertices]] are the same.
- A **path** is a *walk* with no repeated [[Vertices|vertices]].
- A **trail** is a *walk* with no repeated [[Math/Discrete/Graph Theory/Definitions/Edges|edges]].
- A **cycle** is **path**, except it is **closed** (which paths can not be).
- A **circuit** is a **closed trail**.

> [!note]
> - All **paths** are **trails** 
> - All **cycles** are **closed trails** 