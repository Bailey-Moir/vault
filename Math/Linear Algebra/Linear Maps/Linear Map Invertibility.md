---
tags:
  - atom
  - math
  - linear
---
A [[Linear Maps|linear map]] $T \in \mathcal{L}(V,W)$ is *invertible* iff there exists a (unique) [[Linear Maps|linear map]] $T^{-1} \in \mathcal{L}(W)$, such that
- $T^{-1}T = I \in \mathcal{L}(V)$
- $TT^{-1} = I \in \mathcal{L}(W)$

> [!proof]- of Uniqueness
> Suppose $T \in \mathcal{L}(V,W)$ is *invertible* and $S_{1}$ and $S_{2}$ are *inverses*.
> $$\begin{align}
> 	S_{1} &= S_{1}I && I \in \mathcal{L}(W)\\
> 	&= S_{1}(TS_{2}) \\
> 	&= (S_{1}T)S_{2} \\
> 	&= IS_{2} && I \in \mathcal{L}(V) \\
> 	&= S_{2} \\
> \end{align}$$
> Thus, all *inverses* must be the same.

> [!theorem]- $T \in \mathcal{L}(V,W)$ is *invertible* iff it is [[Bijective Functions|bijective]].<br/> *Note this implies $\mathit{\mathcal{M}(T)}$ and $\mathit{\mathcal{M}(T^{-1})}$ are square*[^1]
> ($\implies$)
> Suppose $T$ is *invertible*.
> 
Suppose $\vecbf{u},\vecbf{v} \in V$ such that $T\,\vecbf{u} =T\,\vecbf{v}$. Then
> $$ \vecbf{u} = T^{-1}(T\,\vecbf{u}) = T^{-1}(T\,\vecbf{v}) = \vecbf{v}. $$
> Thus, $T$ must be [[Injective Functions|injective]].
> 
> Suppose $\vecbf{w} \in W$. Then
> $$\begin{align}
> 	\vecbf{w} &= I\vecbf{w} && I \in \mathcal{L}(W) \\
> 	&= T(T^{-1}\vecbf{w}). \\
> \end{align}$$
> Thus, $W = \text{range}\,T$, meaning $T$ is [[Surjective Functions|surjective]].
> 
> ($\impliedby$)
> Suppose $T$ is [[Injective Functions|injective]] and [[Surjective Functions|surjective]].
> 
> For each $\vecbf{w} \in W$, define $S(\vecbf{w})$ as the unique element of $V$ such that $T(S(\vecbf{w})) = \vecbf{w}$ (existing by [[Surjective Functions|surjectivity]], and unique by [[Injective Functions|injectivity]]). Thus, $TS = I \in \mathcal{L}(W)$.
> 
> Suppose $\vecbf{v} \in V$. Then
> $$\begin{align}
> 	T(ST\,\vecbf{v}) &= (TS)T\,\vecbf{v} \\
> 	&= T\,\vecbf{v}. && \because TS = I \in \mathcal{L}(W)\\
> \end{align}$$
> Thus, by [[Injective Functions|injectivity]], $ST\,\vecbf{v} = \vecbf{v}$, meaning $ST = I \in \mathcal{L}(V)$.
> 
> All that remains is to prove $S$ is a [[Linear Maps|linear map]].
> 
> Suppose $\vecbf{w}_{1},\vecbf{w}_{2} \in W$. Then
> $$\begin{align}
> 	T(S\,\vecbf{w}_{1} + S\,\vecbf{w}_{2}) &= TS\,\vecbf{w}_{1} + TS\,\vecbf{w}_{2} \\
> 	&= \vecbf{w}_{1} + \vecbf{w}_{2}. && \because TS = I \in \mathcal{L}(W)\\
> \end{align}$$
> Thus, by the definition of $S$, $S(\vecbf{w}_{1} + \vecbf{w}_{2}) = S\,\vecbf{w}_{1} + S\,\vecbf{w}_{2}$.
> 
> Suppose $\vecbf{w} \in W$ and $\lambda \in \F$. Then
> $$\begin{align}
> 	T(\lambda S(\vecbf{w})) &= \lambda TS\,\vecbf{w} \\
> 	&= \lambda \vecbf{w}. && \because TS = I \in \mathcal{L}(W)\\
> \end{align}$$
> Thus, by the definition of $S$, $S(\lambda\vecbf{w}) = \vecbf{w}$.
> 
> Thus, $S$ is an *inverse* [[Linear Maps|linear map]] of $T$, meaning $T$ is *invertible*.

> [!theorem]- For $S, \in \mathcal{L}(W,V), T \in \mathcal{L}(V,W)$ where $\text{dim}\,V =\text{dim}\,W<\infty$, <br/> $$ST = I \iff TS = I$$
> ($\implies$)
> Suppose $ST = I$. If $v \in V$ and $T\,\vecbf{v} = \vecbf{0}$, then
> $$ \vecbf{v} = I\,\vecbf{v} = (ST)\vecbf{v} = S(T\,\vecbf{v}) = S\,\vecbf{0} = \vecbf{0} $$
> Thus, $T$ must be [[Injective Functions|injective]]. Since $\text{dim}\,V =\text{dim}\,W$, $T$ must then be invertible[^1].
> 
> Further, multiplying $ST = I$ by $T^{-1}$ on the right gives $S = T^{-1}$, meaning $TS = TT^{-1} = I$.
> 
> ($\impliedby$)
> The same process above can be done with the $S$ and $T$ swapped.

\[[[Identity Operator]], [[Vector Space Isomorphism]]\]
# Properties of Inverses
 - $\left(A^{-1}\right)^{-1} \equiv A$
 - $(AB)^{-1} \equiv B^{-1}A^{-1}$
   $\left(ABC\right)^{-1} = C^{-1}B^{-1}A^{-1}$


[^1]: [[Function Types with Dimension]]
