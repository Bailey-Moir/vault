---
tags:
  - atom
  - math
  - linear
---
For $T \in \mathcal{L}(V)$[^1] and $\lambda \in \F$, the *$\mathit{\lambda}$-eigenspace* of $T$ is the [[Sets|set]] $E_{\lambda}(T)$ of solutions for $\vecbf{v}$ in the equation
$$T\,\vecbf{v} = \lambda \vecbf{v},$$
giving the [[Eigenvectors & Eigenvalues|eigenvectors]] with [[Eigenvectors & Eigenvalues|eigenvalue]] $\lambda$, and the zero vector.

> [!note] Iff $\lambda$ is **not** an [[Eigenvectors & Eigenvalues|eigenvalue]], $E_{\lambda}(T) = \{ \vecbf{0} \}$.

> [!proof]- The [[Eigenspaces|eigenspace]] is a [[Subspaces|subspace]] of $V$.
> For any vector $\vecbf{v} \in V$, $T(\vecbf{v}) = \lambda \vecbf{v} \iff (T-\lambda I)\vecbf{v} = \vecbf{0}$
> 
> $T,I \in \mathcal{L}(V) \implies (T - \lambda I) \in \mathcal{L}(V)$.
> 
> Thus, $E_{\lambda}(T)$ can be defined as
> $$\begin{align}
> 	E_{\lambda}(T) &= \{ \vecbf{v} \in V : (T - \lambda I)\vecbf{v} = 0 \} \\
> 	&= \text{null}(T-\lambda I) \\
> \end{align}$$
> 
> Thus, $E_{\lambda}(T) =\text{null}(T-\lambda I)$ is a [[Subspaces|subspace]] of $V$, as the [[Null Space|null space]] of a [[Linear Maps|linear map]] is a [[Subspaces|subspace]] of its [[Domain|domain]].

[^1]: [[Linear Maps]]
