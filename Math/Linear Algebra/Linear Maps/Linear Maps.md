---
tags:
  - atom
  - math
  - linear
---
A *linear map* from [[Vector Spaces|vector spaces]] $V$ to $W$ is a [[Functions|function]] $T: V \to W$ which is **linear**, meaning it has the following properties.
- **[[Additive Property]]**
  $\forall \vecbf{u},\vecbf{v} \in V, T(\vecbf{u}+\vecbf{v}) = T\,\vecbf{u} + T\,\vecbf{v}$
- **Homogeneity**
  $\forall \vecbf{v} \in V, \lambda \in \F, T(\lambda \vecbf{v}) = \lambda(T\,\vecbf{v})$

> [!note] $T \vecbf{0} = \vecbf{0}$

> [!notation] The [[Sets|set]] of [[Linear Maps|linear maps]] from $V$ to $W$ is denoted $\mathcal{L}(V,W)$, and $\mathcal{L}(V) := \mathcal{L}(V,V)$.