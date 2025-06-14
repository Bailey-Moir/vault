---
tags:
  - atom
  - math
  - linear
---
In a [[Singular Value Expansion|SVE]], since the $\sigma_{i}$ are decreasing, the first few terms of the expansion provide a good *low-rank approximation* of $A$.

By taking the first $k$ terms/[[Matrices|matrices]] of this expansion, the $m \times n$ [[Matrices|matrix]]
$$A_{k} = \sum_{i=1}^k \sigma_{i}\vecbf{u}_{i}\vecbf{v}_{i}^T$$
is the *best rank-$\mathit{k}$ approximation of $\mathit{A}$*.