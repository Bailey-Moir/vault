---
tags:
  - atom
  - math
  - linear
---
The [[Singular Value Decomposition|SVD]] of $A \in \R^{m,n}$ can be rewritten as
$$A = U\Sigma V^T = \sigma_{1}\vecbf{u}_{1}\vecbf{v}_{1}^T + \dots + \sigma_{r}\vecbf{u}_{r}\vecbf{v}_{r}^T$$
where $r =\text{rank}(A)$.

> [!note] Each $\sigma_{i}\vecbf{u}_{i}\vecbf{v}_{i}^T$ is an $m\times n$ [[Matrices|matrix]] with [[Rank|rank]] $1$.

> [!note] This is analogous to the [[Spectral Decomposition|spectral decomposition]] of [[Symmetric Matrices|symmetric matrices]].