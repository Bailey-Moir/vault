---
tags:
  - atom
  - math
---
Suppose $T = \mathcal{L}(V,W)$[^1], $\vecbf{v}_{1},\dots,\vecbf{v}_{n}$ is a [[Basis|basis]] of $V$, and $\vecbf{w}_{1},\dots,\vecbf{w}_{m}$ is a [[Basis|basis]] of $W$. The [[Matrices|matrix]] of $T$ with respect to these [[Basis|bases]] is the $m$-by-$n$ [[Matrices|matrix]] $\mathcal{M}(T)$ whose entries $A_{j,k}$ are defined by
$$T \vecbf{v}_{k} = A_{1,k}\vecbf{w}_{1} + \dots + A_{m,k}\vecbf{w}_{m}$$
- If the [[Basis|bases]] are not clear from the context, then the notation $\mathcal{M}(T,(\vecbf{v}_{1},\dots,\vecbf{v}_{n}), (\vecbf{w}_{1},\dots,\vecbf{w}_{m}))$ is used.

> [!example]-
> Suppose $T \in \mathcal{L}(\F^2,\F^3)$ is defined by
> $$ T\langle x,y \rangle = \left< x + 3y, 2x + 5y, 7x + 9y \right>. $$
> Then
> $$ \mathcal{M}(T) = \begin{bmatrix}
> 	1 & 3 \\
> 	2 & 5 \\
> 	7 & 9
> \end{bmatrix}. $$

[^1]: [[Sets of Linear Maps]]