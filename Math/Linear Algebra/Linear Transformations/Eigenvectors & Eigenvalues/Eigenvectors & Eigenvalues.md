---
tags:
  - atom
  - math
  - linear
---
For some [[Operators|operator]] $T \in \mathcal{L}(V)$[^1], an *eigenvector* of $T$ is a non-zero vector $\vecbf{v} \in V$ such that
$$T\,\vecbf{v}=\lambda \vecbf{v}$$
for some scalar $\lambda \in \F$, called its *eigenvalue*.

> [!intuition]-
> An *eigenvector* of $T$ is a non-zero [[Math/Linear Algebra/Vectors/Vectors|vector]] that does not change direction when the [[Linear Maps|map]] $T$ is applied, and its *eigenvalue* $\lambda$ is how much it is scaled.

> [!theorem]- A 1[[Dimension|-dimensional]] [[Subspaces|subspace]] $U$ of $V$ is [[Invariant Subspaces|invariant]] iff it is a [[Subspaces|subspace]] of an [[Eigenspaces|eigenspace]].
> Every 1[[Dimension|-dimensional]] [[Subspaces|subspace]] $U$ of $V$ is of the form
> $$U = \text{span}(\vecbf{v}) = \{ \lambda \vecbf{v} : \lambda \in \F \}$$
> for some $\vecbf{v} \in U$. Thus, if $U$ is [[Invariant Subspaces|invariant]] under $T$, then
> $$T\,\vecbf{v} = \lambda \vecbf{v}$$
> for some $\lambda \in \F$. Thus, due to [[Linear Maps|homogeneity of linear maps]], $U$ is a [[Subspaces|subspace]] of an [[Eigenspaces|eigenspace]] of $T$.
# Theorems
> [!theorem]- **(1)** $\lambda \in \F$ and $\vecbf{v} \in V\setminus \{ \vecbf{0} \}$ form an *eigenvector-eigenvalue pair* of $T \in \mathcal{L}(V)$ iff $\left( T-\lambda I \right)\vecbf{v}=\vecbf{0}$.
> For all $\vecbf{v} \in V \setminus \{ \vecbf{0} \}$ and $\lambda \in \F$, $\vecbf{v}$ is an *eigenvector* and $\lambda$ is its *eigenvalue* iff
> $$\begin{align*}
> 	A\vecbf{v}&=\lambda \vecbf{v} \\
> 	A\vecbf{v} - \lambda \vecbf{v} &= \vecbf{0} \\
> 	A\vecbf{v} - \lambda I \vecbf{v} &= \vecbf{0} && (1)\\
> 	\left(A - \lambda I \right) \vecbf{v} &= \vecbf{0} \\
> \end{align*}$$
  > \[(1) [[Identity Matrices]]\]

> [!theorem]- **(2)** $\lambda \in \F$ is a *eigenvalue* of $T \in \mathcal{L}(V)$ iff $T-\lambda I$ is [[Singular Matrices|singular]]
> $\left( \implies \right)$
> Suppose $\lambda \in \F$ is an *eigenvalue* of $T \in \mathcal{L}(V)$. 
> Then, by **(1)**, there exists some $\vecbf{v} \in V \setminus \{ \vecbf{0} \}$ such that $\left( T - \lambda I \right)\vecbf{v} = \vecbf{0}$.
> Thus, $\vecbf{v} \in \text{null}(T-\lambda I)$[^2], meaning $\text{nullity}(T-\lambda I) > 0$[^2], so $T-\lambda I$ is not [[Linear Map Invertibility|invertible]][^3], meaning $T -\lambda I$ is [[Singular Matrices|singular]].
> 
> $\left( \impliedby \right)$
> Suppose $T-\lambda I$ is singular (not [[Linear Map Invertibility|invertible]]) for some $T \in \mathcal{L}(V)$ and $\lambda \in \F$.
> Then, since $T - \lambda I$ is an [[Operators|operator]], it is [[Bijective Functions|bijective]] ([[Linear Map Invertibility|invertible]]) iff it is [[Injective Functions|injective]][^4]. Thus, $T - \lambda I$ must not be [[Injective Functions|injective]].
> This means there must exist $\vecbf{v} \in V \setminus \{ \vecbf{0} \}$ such that $\left( T - \lambda I \right) \vecbf{v} = \vecbf{0}$[^3], so by **(1)**, $\lambda$ must be an *eigenvalue* of $T$ (with *eigenvector* $\vecbf{v}$).

> [!theorem]- **(3)** Every [[Lists|list]] of *eigenvectors* of $T\in \mathcal{L}(V)$ corresponding to distinct *eigenvalues* is [[Linear Independence|linearly independent]].
> Suppose the [[Negation|negation is true]]. Let $k$ be the smallest positive integer such that there exists a [[Linear Independence|linearly dependent]] [[Lists|list]] $\vecbf{v}_{1},\dots,\vecbf{v}_{k}$ of [[Eigenvectors & Eigenvalues|eigenvectors]] of $T \in \mathcal{L}(V)$ corresponding to distinct eigenvalues $\lambda_{1},\dots,\lambda_{k}$.
> Then, there must exist $a_{1},\dots,a_{k} \in \F$ (none of which are zero by the minimality of $k$) such that
> $$a_{1}\vecbf{v}_{1} + \dots + a_{k}\vecbf{v}_{k} = \vecbf{0}.$$
> Applying $T-\lambda_{k}I$ to both sides of this equation gives
> $$\begin{align}
> 	(T-\lambda_{k}I)\left( a_{1}\vecbf{v}_{1} + \dots + a_{k}\vecbf{v}_{k} \right) &= (T-\lambda_{k}I)\,\vecbf{0} \\
> 	a_{1}(T-\lambda_{k}I)\,\vecbf{v}_{1} + \dots + a_{k}(T-\lambda_{k}I)\,\vecbf{v}_{k} &= \vecbf{0} && (1) \\
> 	a_{1}(\lambda_{1}-\lambda_{k})\vecbf{v}_{1} + \dots + a_{k}(\lambda_{k}-\lambda _{k})\,\vecbf{v}_{k} &= \vecbf{0}\\
> 	a_{1}(\lambda_{1}-\lambda_{k})\vecbf{v}_{1} + \dots + a_{k-1}(\lambda_{k-1}-\lambda _{k})\,\vecbf{v}_{k-1} &= \vecbf{0}\\
> \end{align}$$
> Since the *eigenvalues* are distinct, $\lambda_{i}-\lambda_{j}\ne 0$ iff $i\ne j$, so all of scalars above are non-zero. Thus, $\vecbf{v}_{1},\dots,\vecbf{v}_{k-1}$ is [[Linear Independence|linearly dependent]]. This [[Contradictions|contradicts]] the minimality of $k$, so no such [[Linear Independence|linearly dependent]] [[Lists|list]] can exist.
> \[$(1)$ [[Linear Maps]]\]

> [!theorem]- **(4)** For a [[Finite-Dimensional Vector Spaces|finite-dimensional]] $V$, each $T \in \mathcal{L}(V)$ has at most $\text{dim}\,V$ distinct *eigenvalues*.
> For some [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]] $V$ and [[Operators|operator]] $T \in \mathcal{L}(V)$, suppose $T$ has $k$ distinct *eigenvalues* $\lambda_{1},\dots,\lambda_{k}$.
> Then, there must exist *eigenvectors* $\vecbf{v}_{1},\dots,\vecbf{v}_{k}$ corresponding to these *eigenvalues*.
> By **(3)**, this [[Lists|list]] of *eigenvectors* must be [[Linear Independence|linearly independent]], and since each *eigenvector* is in $V$, their [[Span|span]] must be a [[Subspaces|subspace]] of $V$, meaning
> $$\begin{align}
> 	\text{dim}\,\text{span}\left( \vecbf{v}_{1},\dots,\vecbf{v}_{k} \right) &\leq \text{dim}\,V && \text{Subspace of } V \\
> 	k &\leq \text{dim}\,V && \text{Linear indepence} \\
> \end{align}$$
> Thus, $T$ must have at most $\text{dim}\,V$ distinct *eigenvalues*.

[^1]: [[Linear Maps]]
[^2]: [[Null Space]] and [[Nullity]]
[^3]: [[Null Space]], Theorem 2
[^4]: [[Function Types with Dimension]], Theorem 3