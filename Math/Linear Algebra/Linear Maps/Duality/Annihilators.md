---
tags:
  - atom
  - math
  - linear
---
The *annihilator* of a [[Subspaces|subspace]] $U$ of $V$, denoted $U^0$, is the [[Subspaces|subspace]] of $V$ defined by
$$U^0 = \{ \varphi \in V' : \forall \vecbf{u} \in U, \varphi(\vecbf{u}) = 0 \}$$
> [!note] Just like [[Orthogonal Complements|orthogonal complements]] and [[Complement|set complements]], *annihilators* depend on a containing [[Vector Spaces|vector space]], so sometimes the notation $U^0_{V}$ is used.

> [!theorem]- For a [[Subspaces|subspace]] $U$ of $V$, $U^0$ is a [[Subspaces|subspace]] of $V'$.
> **Additive Identity**
> Since $(0) \vecbf{u} = \vecbf{0}$ for all $\vecbf{u} \in U$, $0 \in U^0$.
> 
> **Closed Under Addition**
> For two [[Linear Functionals|linear functional]] $\varphi,\psi \in U^0$, for all $\vecbf{u} \in U$,
> $$\begin{align*}
> 	(\varphi + \psi)\vecbf{u} &= \varphi\,\vecbf{u}+\psi\,\vecbf{u} \\
> 	&= \vecbf{0} + \vecbf{0} \\
> 	&= \vecbf{0}. \\
> \end{align*}$$
> Thus, $\varphi+\psi \in U^0$.
> 
> **Closed Under Scalar Multiplication**
> For $\varphi \in U^0$ and $\lambda \in \F$, for all $\vecbf{u} \in U$,
> $$\begin{align*}
> 	(\lambda \varphi)\vecbf{u} &= \lambda(\varphi\,\vecbf{u}) \\
> 	&= \lambda\vecbf{0} \\
> 	&= \vecbf{0}. \\
> \end{align*}$$
> Thus, $\lambda \varphi \in U^0$.

\[[[Dual Space]], [[Linear Functionals]]\]