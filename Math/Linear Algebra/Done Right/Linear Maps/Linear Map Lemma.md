---
tags:
  - atom
  - math
---
If $\vecbf{v}_{1},\dots,\vecbf{v}_{n}$ is a [[Basis|basis]] of $V$, and $\vecbf{w}_{1}, \dots, \vecbf{w}_{n} \in W$, then there exists a **unique** [[Linear Maps|linear map]] $T : V \to W$ such that
$$ \phantom{\forall k \in \{ 1,\dots,n \}\hspace{2em}} T\vecbf{v}_{k} = \vecbf{w}_{k} \hspace{2em}\forall k \in \{ 1,\dots,n \}$$
- The 'existence' part means that we can find a [[Linear Maps|linear map]] that maps the vectors in a [[Basis|basis]] to whatever we want. 
- The 'unique' part means that a [[Linear Maps|linear map]] is completely determined by what it maps the vectors in a [[Basis|basis]] to.

> [!proof]-
> **Existence**
> Define $T: V \to W$ by
> $$T(c_{1}\vecbf{v}_{1} + \dots + c_{n}\vecbf{v}_{n}) = c_{1}\vecbf{w}_{1} + \dots + c_{n}\vecbf{w}_{n},$$
> where $c_{1},\dots,c_{n}$ are arbitrary elements of $\F$, and $\vecbf{v}_{1}, \dots, \vecbf{v}_{n}$ is a [[Basis|basis]] of $V$.
> 
> Thus, $T$ is a [[Functions|function]], as each element of $V$ can be written uniquely as $c_{1}\vecbf{v}_{1},\dots,c_{n}\vecbf{v}_{n}$.
> 
> For each $k$, taking $c_{k} = 1$ and all other $c$'s to be $0$, $T\vecbf{v}_{k} = \vecbf{w}_{k}$.
> 
> If $u,v \in V$, with $u = a_{1}\vecbf{v}_{1} + \dots + a_{n}\vecbf{v}_{n}$ and $v = b_{1}\vecbf{v}_{1} + \dots + b_{n}\vecbf{v}_{n}$,
> $$\begin{align}
> 	T(\vecbf{u}+\vecbf{v}) &= T( (a_{1}+b_{1})\vecbf{v}_{1} + \dots + (a_{n} + b_{n})\vecbf{v}_{n} ) \\
> 	&= (a_{1}+b_{1})\vecbf{w}_{1} + \dots + (a_{n} + b_{n})\vecbf{w}_{n} \\
> 	&= (a_{1}\vecbf{w}_{1} + \dots + a_{n}\vecbf{w}_{n}) + (b_{1}\vecbf{w}_{1} + \dots + b_{n}\vecbf{w}_{n}) \\
> 	&= T\vecbf{u} + T\vecbf{v}.
> \end{align}$$
> Similarly, if $\lambda \in \F$ and $\vecbf{v} = c_{1}\vecbf{v}_{1} + \dots c_{n}\vecbf{v}_{n}$,
> $$\begin{align}
> 	T(\lambda \vecbf{v}) &= T(\lambda c_{1}\vecbf{v}_{1} + \dots \lambda c_{n}\vecbf{v}_{n}) \\
> 	&= \lambda c_{1}\vecbf{w}_{1} + \dots \lambda c_{n}\vecbf{w}_{n} \\
> 	&= \lambda(c_{1}\vecbf{w}_{1} + \dots c_{n}\vecbf{w}_{n}) \\
> 	&= \lambda T\vecbf{v}. \\
> \end{align}$$
> Thus, $T$ is a [[Linear Maps|linear map]] from $V$ to $W$.
> 
> **Uniqueness**
> Suppose that $T \in \mathcal{L}(V,W)$ and that $\forall k \in \{ 1,\dots,n \}, T\vecbf{v}_{k} = \vecbf{w}_{k}$. 
> Let $c_{1},\dots,c_{n} \in \F$. Then the homogeneity of $T$ implies that $\forall k \in \{ 1,\dots,n \}, T(c_{k}\vecbf{v}_{k}) = c_{k}\vecbf{w}_{k}$. The [[Additive Property|additivity]] of $T$ then implies that
> $$ T(c_{1}\vecbf{v}_{1} + \dots + c_{n}\vecbf{v}_{n}) = c_{1}\vecbf{w}_{1}  +\dots + c_{n}\vecbf{w}_{n} $$
> Thus, element in the [[Domain|domain]] has an image completely and uniquely determined by the [[Basis|basis]] vectors, as each $\vecbf{v} \in V$ has a unique [[Linear Combinations|linear combination]] of the [[Basis Vectors|basis vectors]], by the definition of a [[Functions|function]] and each [[Linear Combinations|linear combination]] must have a unique output.