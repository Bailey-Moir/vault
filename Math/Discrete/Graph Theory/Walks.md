---
tags:
  - atom
  - math
  - discrete
---
A *walk* in a [[Graphs|graph]] is an alternating [[Sequences|sequence]] of [[Vertices|vertices]] and [[Edges|edges]].
$$v_{1},e_{1},v_{2},e_{2},v_{3},\dots,v_{k-1},e_{k-1},v_{k}$$
such that $e_i$ joins $v_i$ and $v_{i+1}$.
- A **closed walk** is a *walk* where the first and last [[Vertices|vertices]] are the same.
- A **path** is a *walk* with no repeated [[Vertices|vertices]].
- A **cycle** is a **path**, except it is **closed** (which paths can not be).
- A **trail** is a *walk* with no repeated [[Edges|edges]].
- A **circuit** is a **closed trail**.

> [!note]
> - All **paths** are **trails** 
> - All **cycles** are **circuits** 
