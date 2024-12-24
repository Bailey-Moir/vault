---
tags:
  - atom
  - math
---
Every [[Span|spanning list]] can be reduced to a [[Basis|basis]], and in a **[[Finite-Dimensional Vector Spaces|finite-dimensional vector space]]**, every [[Linear Independence|linearly independent]] list of [[Vectors|vectors]] can be extended to a [[Basis|basis]].

> [!proof]- Reduction
> Let $B$ be the [[Span|spanning list]] $\vecbf{v}_{1}, \dots, \vecbf{v}_{n}$.
>
> **Base Case**
> If $\vecbf{v}_{1} = 0$, remove $\vecbf{v}_{1}$ from $B$.
> 
> Then the [[Lists|list]] before $\vecbf{v}_{2}$ is [[Linear Independence|linearly independent]], and $B$ still [[Span|spans]] $V$.
> 
> **Induction Step**
> Suppose $\vecbf{v}_{1}, \dots, \vecbf{v}_{k-1}$ in $B$ is [[Linear Independence|linearly independent]]. If $k = n+1$, terminate. 
> 
> If $\vecbf{v}_{k} \in \text{span}(\vecbf{v}_{1}, \dots, \vecbf{v}_{k-1})$, remove $\vecbf{v}_{k}$ from $B$.
> 
> Now $\vecbf{v}_{1}, \dots, \vecbf{v}_{k}$ in $B$ is [[Linear Independence|linearly independent]], and $B$ still [[Span|spans]] $V$, both by the [[Linear Dependence Lemma|linear dependence lemma]].
> 
> **Conclusion**
> Thus, by the principal of [[Induction|principal of mathematical induction]], when this process terminates, $B$ (the original [[Lists|list]] with some vectors potentially removed) [[Span|spans]] $V$ and is [[Linear Independence|linearly independent]], and thus is a *basis* of $V$.

> [!proof]- Extension
> Suppose $\vecbf{u}_{1}, \dots, \vecbf{u}_{n}$ is a [[Linear Independence|linear independent]] [[Lists|list]] in a [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]] $V$. Let $\vecbf{w}_{1}, \dots, \vecbf{w}_{m}$ be a [[Span|spanning list]] of $V$, which must exist as it is a [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]]. Thus the list
> $$\vecbf{u}_{1}, \dots, \vecbf{u}_{n}, \vecbf{w}_{1}, \dots, \vecbf{w}_{m}$$
> [[Span|spans]] $V$. Applying the same procedure as in the above theorem's proof, but starting on $\vecbf{w}_{1}$ instead of $\vecbf{u}_{1}$, will give a [[Linear Independence|linearly independent]] [[Span|spanning list]] of $V$ (a *basis*) containing $\vecbf{u}_{1}, \dots, \vecbf{u}_{n}$.

\[[[Steinitz Exchange Lemma]]\]