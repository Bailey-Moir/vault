---
tags:
  - atom
  - math
---
For every [[Subspaces|subspace]] $U$ of $V$, there exists another [[Subspaces|subspace]] $W$ of $V$ such that
$$U \oplus W = V$$

> [!proof]-
> Since $U$ is a [[Subspaces|subspace]] of the [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]] $V$, $U$ must also be [[Finite-Dimensional Vector Spaces|finite-dimensional]]. Thus, there must exist a [[Basis|basis]] $\vecbf{u}_{1}, \dots, \vecbf{u}_{n}$ of $U$. Since this [[Lists|list]] is [[Linear Independence|linearly independent]] in $V$, this can be extended to be [[Basis|basis]] $\vecbf{u}_{1}, \dots, \vecbf{u}_{n}, \vecbf{w}_{1}, \dots, \vecbf{w}_{m}$ of $V$.
> 
> Let $W = \text{span}(\vecbf{w}_{1},\dots,\vecbf{w}_{m})$.
> 
> For any $\vecbf{v} \in V$, there exists $a_{1},\dots,a_{n},b_{1},\dots, b_{m}\in \F$ such that
> $$\begin{align}
> 	\vecbf{v} &= (a_{1}\vecbf{u}_{1} + \dots + a_{n}\vecbf{u}_{n}) + (b_{1}\vecbf{w}_{1} + \dots + b_{m}\vecbf{w}_{m}) \\
> 	&= \vecbf{u} + \vecbf{w} \hspace{2em}\exists\vecbf{u}\in U,\vecbf{w}\in W. \\
> \end{align}$$
> Thus, $V \subseteq U + W$. This can be done in reverse to show that $U + W \subseteq V$, meaning $V = U + W$.
> 
> Suppose $\vecbf{v} \in U \cap W$. Then there exists $a_{1},\dots,a_{n},b_{1},\dots, b_{m}\in \F$
> $$\begin{array}{l}
> 	\vecbf{v} = a_{1}\vecbf{u}_{1} + \dots + a_{n}\vecbf{u}_{n} = b_{1}\vecbf{w}_{1} + \dots + b_{m}\vecbf{w}_{m} \\
> 	\vecbf{0} = a_{1}\vecbf{u}_{1} + \dots + a_{n}\vecbf{u}_{n} - b_{1}\vecbf{w}_{1} + \dots + b_{m}\vecbf{w}_{m}. \\
> \end{array}$$
> Since $\vecbf{u}_{1}, \dots, \vecbf{u}_{n}, \vecbf{w}_{1}, \dots, \vecbf{w}_{m}$ is [[Linear Independence|linearly independent]], this implies $a_{1}=\dots=a_{n}=b_{1}=\dots=b_{m}=0$, meaning $\vecbf{v} = \vecbf{0}$, and thus that
> $$V = U \oplus W$$

\[[[Direct Sums]]\]