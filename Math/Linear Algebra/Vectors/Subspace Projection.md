---
tags:
  - atom
  - math
  - linear
---
Let $\vecbf{x} \in V$, and suppose $U$ is a [[Subspaces|subspace]] of an [[Inner Products|inner product space]] $V$ with a **[[Orthogonal Vectors|orthogonal]]** [[Vector Basis|basis]] $\vecbf{u}_{1},\dots,\vecbf{u}_{k}$. Then
$$\begin{align}
	\text{proj}_{U}\,\vecbf{x} &= \text{proj}_{\vecbf{u}_{1}}\,\vecbf{x} + \dots + \text{proj}_{\vecbf{u}_{k}}\,\vecbf{x} \\
	&= \sum_{i=1}^k \dfrac{\left\langle\vecbf{u}_{i},\vecbf{x}\right\rangle}{\left\langle\vecbf{u}_{i}, \vecbf{u}_{i}\right\rangle} \vecbf{u}_{i} \\
\end{align}$$