---
tags:
  - atom
  - math
  - linear
---
The *dual basis* of a [[Vector Bases|basis]] $\vecbf{v}_{1},\dots,\vecbf{v}_{n}$ of $V$ is the [[Vector Bases|basis]] $\varphi_{1},\dots,\varphi_{n}$ of $V'$[^1], where $\varphi_{j}$ is a [[Linear Functionals|linear functional]] on $V$ defined such that
$$\varphi_{j}(\vecbf{v}_{k}) = \left\{\begin{matrix}
	1 & \text{if } j = k \\
	0 & \text{if } j \ne k \\
\end{matrix}\right.,$$
and this is indeed a [[Vector Bases|basis]] of the [[Dual Space|dual space]].

> [!theorem]- A *dual basis* is a [[Vector Bases|basis]] of the [[Dual Space|dual space]].
> Suppose $a_{1},\dots,a_{n} \in \F$ are defined such that
> $$ a_{1}\varphi_{1}+\dots+a_{n}\varphi_{n} = 0. $$
> By the definition of a *dual basis*,
> $$\begin{align}
> 	\left( a_{1}\varphi_{1}+\dots+a_{n}\varphi_{n} \right)\vecbf{v}_{k} &= a_{k}. && \forall k \\
> \end{align}$$
> Thus, $a_{1}=\dots=a_{n}=0$. Thus, by the definition of [[Linear Independence|linear independence]], $\varphi_{1},\dots,\varphi_{n}$ must be [[Linear Independence|linearly independent]].
> 
> Since the *dual basis* is a [[Linear Independence|linearly independent]] [[Subsets|subset]] of $V'$ of length $\dim\,V=\text{dim}\,V'$[^2], it must then be a [[Vector Bases|basis]] of $V'$[^3].

> [!theorem]- **(1)** $\vecbf{v} = \varphi_{1}(\vecbf{v})\vecbf{v}_{1}+\dots+\varphi_{n}(\vecbf{v})\vecbf{v}_{n}$
> Suppose $\vecbf{v} \in V$ and $\vecbf{v}_{1},\dots,\vecbf{v}_{n}$ is a [[Vector Bases|basis]] of $V$. Then there exists $c_{1},\dots,c_{n}\in \F$ such that
> $$\vecbf{v} = c_{1}\vecbf{v}_{1}+\dots+c_{n}\vecbf{v}_{n}.$$
> Applying $\varphi_{j}$ to both sides of this equation gives
> $$\begin{align}
> 	\varphi_{j}(\vecbf{v}) &= \varphi_{j}(c_{1}\vecbf{v}_{1}+\dots+c_{j}\vecbf{v}_{j}+\dots+c_{n}\vecbf{v}_{n}) \\
> 	&= c_{1}\varphi_{j}(\vecbf{v}_{1})+\dots+c_{j}\varphi_{j}(\vecbf{v}_{j})+\dots+c_{n}\varphi_{j}(\vecbf{v}_{n}) \\
> 	&= c_{j} \\
> \end{align}$$
> Substituting these values for $c_{1},\dots,c_{n}$ shows that
> $$\vecbf{v} = \varphi_{1}(\vecbf{v})\vecbf{v}_{1}+\dots+\varphi_{n}(\vecbf{v})\vecbf{v}_{n}$$

[^1]: [[Dual Space]]
[^2]: [[Dual Space]], Theorem 1
[^3]: [[Linear Independence and Span with Dimension]] or [[Dimension Equality Theorem]]
