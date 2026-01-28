---
tags:
  - atom
  - math
  - linear
---
Suppose $T \in \mathcal{L}(V)$[^1] (where $V$ is [[Finite-Dimensional Vector Spaces|finite-dimensional]]), and $J$ and $K$ are [[Vector Bases|bases]] of $V$. Let 
$$\begin{array}{c c c c c}
	A = \mathcal{M}(T,J) && B = \mathcal{M}(T,K) && C= \mathcal{M}(I,J,K).
\end{array}$$
Then,
$$A = C^{-1}BC$$
> [!proof]-
> $$\begin{align}
> 	C^{-1}BC &= \mathcal{M}(I,K,J)\,\mathcal{M}(T,K)\,\mathcal{M}(I,J,K) \\
> 	&= \left( \mathcal{M}(I,K,J)\,\mathcal{M}(T,K) \right)\,\mathcal{M}(I,J,K) \\
> 	&= \mathcal{M}(IT,K,J)\,\mathcal{M}(I,J,K) && (1) \\
> 	&= \mathcal{M}(ITI,J) && (1) \\
> 	&= \mathcal{M}(T,J) && (2) \\
> 	&= A \\
> \end{align}$$
> \[$(1)$ [[Matrix of Product of Linear Maps]]. $(2)$ [[Identity Operator]]/[[Identity Matrices]]\]

[^1]: [[Linear Maps]]
