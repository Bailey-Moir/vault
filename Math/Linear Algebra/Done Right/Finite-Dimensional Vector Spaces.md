---
tags:
  - atom
  - math
---
A [[Vector Spaces|vector space]] is called a *finite-dimensional* iff it has a finite [[Span|spanning list]].
$$ \exists n \in \Z^+ : \exists \vecbf{v}_1, \dots, \vecbf{v}_n \in V : \text{span}(\vecbf{v}_1 + \dots + \vecbf{v}_n) = V $$
- Every [[Subspaces|subspace]] of a *finite-dimensional vector space* is *finite-dimensional*.
  > [!proof]-
> Suppose $V$ is a *finite-dimensional vector space*, and $U$ is a [[Subspaces|subspace]] of $V$.
> 
> **Base Case**
If $U = \{ \vecbf{0} \}$, then $U$ is *finite-dimensional*, and it is proven. Otherwise, if $U \ne \{ \vecbf{0} \}$, chose a non-zero vector $\vecbf{u}_{1} \in U$.
> 
> **Induction Step**
For some $k \in \Z^+$, let $\vecbf{u}_{1},\dots,\vecbf{u}_{k} \in U$.
> 
> If $U = \text{span}(\vecbf{u}_{1}, \dots, \vecbf{u}_{k})$, $U$ is *finite-dimensional*, and it is proven. Otherwise, If $U \ne \text{span}(\vecbf{u}_{1}, \dots, \vecbf{u}_{k})$, chose a vector $\vecbf{u}_{k+1} \notin \text{span}(\vecbf{u}_{1}, \dots, \vecbf{u}_{k})$, which must exist.
> 
> **Conclusion**
> Note that after each step, no vector in the [[Lists|list]] is in the [[Span|span]] of the previous vectors, and thus the [[Lists|list]] is [[Linear Independence|linearly independent]] by the [[Linear Dependence Lemma|linear dependence lemma]].
> 
> If this process terminates, $U$ is *finite-dimensional*. If this process does not terminate, the length of the [[Linear Independence|linearly independent]] [[Lists|list]] must eventually exceed the size of a [[Span|spanning]] [[Lists|list]] of [[Vectors|vectors]] of $V$, which is a [[Contradictions|contradiction]] by the [[Steinitz Exchange Lemma|Steinitz exchange lemma]]. Thus, this process must terminate, meaning $U$ must be *finite-dimensional*.
> 
> \[[[Induction]]\]



[^1]: [[Steinitz Exchange Lemma]]