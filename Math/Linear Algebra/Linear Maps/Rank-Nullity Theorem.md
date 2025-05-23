---
tags:
  - atom
  - math
  - linear
---
![600|center](rank-nullity-theorem.excalidraw.md)
If $V$ is [[Finite-Dimensional Vector Spaces|finite-dimensional]] and $T \in \mathcal{L}(V,W)$[^1], then $\text{im}\,T$[^2] is [[Finite-Dimensional Vector Spaces|finite-dimensional]] and
$$\begin{align}
	\text{dim}\,V &= \text{rank}\,T + \text{nullity}\,T \\
	&= \text{dim}\,\text{im}\,T + \text{dim}\,\text{null}\,T && (1) \\
\end{align}$$

> [!proof]-
> Let $\vecbf{u}_{1}, \dots, \vecbf{u}_{n}$ be a [[Basis|basis]] of $\text{null}\,T$; thus $\text{nullity}\,T = n$[^3]G. This list is [[Linear Independence|linearly independent]], and thus can be [[Linear Independence and Span with Dimension|extended]] to a [[Basis|basis]] of $V$:
> $$\vecbf{u}_{1}, \dots, \vecbf{u}_{n}, \vecbf{v}_{1}, \dots, \vecbf{v}_{m}.$$
> Thus $\text{dim}\,V = n + m$. To complete this proof, it must be shown that $\text{im}\,T$[^2] is [[Finite-Dimensional Vector Spaces|finite-dimensional]] and $\text{rank}\,T = m$. This can be done by proving $T\,\vecbf{v}_{1},\dots,T\,\vecbf{v}_{m}$ is a [[Basis|basis]] of $\text{range}\,T$.
> 
> **Spanning List and Finite-Dimensionality**
> Let $\vecbf{v} \in V$. There then exists $a_{1},\dots,a_{n},b_{1},\dots,b_{m}$ such that
> $$\begin{align}
> 	\vecbf{v} &= a_{1}\vecbf{u}_{1} + \dots + a_{n}\vecbf{u}_{n} + b_{1}\vecbf{v}_{1} + \dots + b_{m}\vecbf{v}_{m} \\
> 	T\,\vecbf{v} &= T(a_{1}\vecbf{u}_{1} + \dots + a_{n}\vecbf{u}_{n}) + T(b_{1}\vecbf{v}_{1} + \dots + b_{m}\vecbf{v}_{m}) \\
> 	T\,\vecbf{v} &= b_{1}T\,\vecbf{v}_{1} + \dots + b_{m}T\,\vecbf{v}_{m}. \\
> \end{align}$$
Thus $T\,\vecbf{v}_{1},\dots,T\,\vecbf{v}_{m}$ [[Span|spans]] $\text{im}\,T$[^2] and is [[Finite-Dimensional Vector Spaces|finite-dimensional]].
> 
> **Linear Independence**
> Suppose $c_{1},\dots,c_{m} \in \F$ such that
> $$\begin{align}
> 	c_{1}T\,\vecbf{v}_{1} \dots + c_{m}T\,\vecbf{v}_{m} &= \vecbf{0} \\
> 	T(c_{1}\vecbf{v}_{1} \dots + c_{m}\vecbf{v}_{m}) &= \vecbf{0} \\
> 	\to c_{1}\vecbf{v}_{1} + \dots + c_{m}\vecbf{v}_{m} &\in \text{null}\,T 
> \end{align}$$
> Since $\vecbf{u}_{1},\dots,\vecbf{u}_{n}$ [[Span|spans]] $\text{null}\,T$, we can write
> $$ c_{1}\vecbf{v}_{1} + \dots + c_{m}\vecbf{v}_{m} = d_{1}\vecbf{u}_{1} + \dots + d_{n}\vecbf{u}_{n}$$
> where the $d$'s are in $\F$. Since $\vecbf{u}_{1}, \dots, \vecbf{u}_{n}, \vecbf{v}_{1}, \dots, \vecbf{v}_{m}$ is a [[Basis|basis]], the $c$'s and $d$'s must be $0$. Thus, the original premise implies that the $c$'s are $0$, and thus $\vecbf{v}_{1}, \dots, \vecbf{v}_{m}$ is [[Linear Independence|linearly independent]].


\[$(1)$ [[Rank]], $(1)$ [[Nullity]], [[Dimension]], [[Null Space]]\]

[^1]: [[Linear Maps]]
[^2]: [[Images of Linear Maps]]
[^3]: [[Nullity]]
