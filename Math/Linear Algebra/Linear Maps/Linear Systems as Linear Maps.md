---
tags:
  - atom
  - math
  - linear
---
Define $T \in \mathcal{L}(\F^n,\F^m)$[^1] by
$$\begin{align}
	T(\langle v_{1},\dots,v_{n} \rangle) &= \left\langle A_{1,1}v_{1} + \dots + A_{1,k}v_{k}, \dots, A_{m,1}v_{1} + \dots + A_{m,k}v_{k} \right\rangle \\
	&= \left\langle \sum_{k=1}^n A_{1,k}v_{k}, \dots, \sum_{k=1}^n A_{m,k}v_{k} \right\rangle. \\
\end{align}$$
The equation $T(\langle v_{1},\dots,v_{n}\rangle) = 0$ is the same as the [[Homogeneous Systems|homogeneous system]]
$$\begin{array}{cccc}
	A_{1,1}v_{1} &+& \dots &+& A_{1,n}v_{n} &=& 0 \\
	\vdots && \vdots && \vdots && \vdots \\
	A_{m,1}v_{1} &+& \dots &+& A_{m,n}v_{n} &=& 0 \\
\end{array}$$
> [!note]- A homogeneous system with more variables than equations has non-zero solutions
> Given the above notation, a homogeneous system with $n$ variables and $m$ linear equations can be described by $T \in \mathcal{L}(\F^n,\F^m)$[^1]. Thus, if there are more variables than equations, $n > m$, meaning $\dim\text{domain}\;T > \dim\text{range}\;T$, meaning $T$ is not [[Injective Functions|injective]][^2], which implies $\left| \text{null}\,T \right| > 1$[^3].

> [!note]- A system with more equations than variables has no solutions for some choice of constants terms.
> Given the above notation, a system with $n$ variables and $m$ linear equations can be described by $T \in \mathcal{L}(\F^n,\F^m)$[^1]. Thus, if there are more equations than variables, $m > n$, meaning $\dim\text{range}\;T > \dim\text{domain}\;T$, meaning $T$ is not [[Surjective Functions|surjective]][^2], which implies there exist vectors in $\F^m$ that $T$ does not map to.
> #TODO this proof is flawed


[^1]: [[Linear Maps]]
[^2]: [[Function Types with Dimension]]
[^3]: [[Null Space]]