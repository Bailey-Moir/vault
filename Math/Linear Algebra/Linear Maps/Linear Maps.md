---
tags:
  - atom
  - math
  - linear
---
A *linear map* from [[Vector Spaces|vector space]] $V$ to $W$ is a [[Functions|function]] $T: V \to W$ which is **linear**, meaning it has the following properties.
- **[[Additive Property]]**
  $\forall \vecbf{u},\vecbf{v} \in V, T(\vecbf{u}+\vecbf{v}) = T\,\vecbf{u} + T\,\vecbf{v}$
- **Homogeneity**
  $\forall \vecbf{v} \in V, \lambda \in \F, T(\lambda \vecbf{v}) = \lambda(T\,\vecbf{v})$

> [!note] $T \vecbf{0} = \vecbf{0}$

> [!notation] The [[Sets|set]] of [[Linear Maps|linear maps]] from $V$ to $W$ is denoted $\mathcal{L}(V,W)$, and $\mathcal{L}(V) := \mathcal{L}(V,V)$.

# Vector Spaces of Linear Maps
Defining addition and scalar multiplication on $\mathcal{L}(V,W)$ as
$$\begin{array}{rcl}
	(S+T)(\vecbf{v}) = S\,\vecbf{v} + T\,\vecbf{v} && (\lambda T)(\vecbf{v}) = \lambda(T\,\vecbf{v})
\end{array}$$
makes $\mathcal{L}(V,W)$ a [[Vector Spaces|vector space]]. 

An additional **product operation** ([[Composite Functions|composition]]) can be defined such that if $T \in \mathcal{L}(U,V)$ and $S \in \mathcal{L}(V,W)$, $ST \in \mathcal{L}(U,W)$ is defined by
$$(ST)(\vecbf{v}) = S(T\,\vecbf{v})$$

> [!note]- $\text{dim}\,\F^{m,n} = mn$
# Properties of Products of Linear Maps
Note all of the below properties have conditions for the [[Domain|domains]] and [[Codomain|codomains]].
- **Associativity**
  $(T_{1}T_{2})T_{3} \equiv T_{1}(T_{2}T_{3})$
- **[[Identity Operator|Identity]]**
  $TI \equiv IT \equiv T$
- **Distributive Properties**
  $(S_{1}+S_{2})T = S_{1}T+S_{2}T$
  $S(T_{1}+T_{2}) = ST_{1}+ST_{2}$
