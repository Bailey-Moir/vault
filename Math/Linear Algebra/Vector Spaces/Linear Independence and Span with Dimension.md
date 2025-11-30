---
tags:
  - atom
  - math
  - linear
---
In a [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]] $V$, for all [[Linear Independence|linearly independent]] [[Lists|lists]]/[[Sets|sets]] $I$ and [[Span|spanning list/sets]] $S$,
$$ \left| I \right| \le \text{dim}(V) \le \left| S \right|  $$
- Every $I$ can be extended and every $S$ can be reduced to a [[Vector Basis|basis]] of $V$.
  > [!proof]- Reduction
> Let $S$ be the [[Span|spanning list]] $\vecbf{v}_{1}, \dots, \vecbf{v}_{n}$.
>
> **Base Case**
> If $\vecbf{v}_{1} = 0$, remove $\vecbf{v}_{1}$ from $S$.
> 
> Then the [[Lists|list]] before $\vecbf{v}_{2}$ is [[Linear Independence|linearly independent]], and $S$ still [[Span|spans]] $V$.
> 
> **Induction Step**
> Suppose $\vecbf{v}_{1}, \dots, \vecbf{v}_{k-1}$ in $S$ is [[Linear Independence|linearly independent]]. If $k = n+1$, terminate. 
> 
> If $\vecbf{v}_{k} \in \text{span}(\vecbf{v}_{1}, \dots, \vecbf{v}_{k-1})$, remove $\vecbf{v}_{k}$ from $S$.
> 
> Now $\vecbf{v}_{1}, \dots, \vecbf{v}_{k}$ in $S$ is [[Linear Independence|linearly independent]], and $S$ still [[Span|spans]] $V$, both by the [[Linear Dependence Lemma|linear dependence lemma]].
> 
> **Conclusion**
> Thus, by the principal of [[Induction|mathematical induction]], when this process terminates, $S$ (the original [[Lists|list]] with some vectors potentially removed) [[Span|spans]] $V$ and is [[Linear Independence|linearly independent]], and thus is a *basis* of $V$.

  > [!proof]- Extension
> Suppose $I = \vecbf{u}_{1}, \dots, \vecbf{u}_{n}$. Let $\vecbf{w}_{1}, \dots, \vecbf{w}_{m}$ be a [[Span|spanning list]] of $V$, which must exist as it is a [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]]. Thus the list
> $$\vecbf{u}_{1}, \dots, \vecbf{u}_{n}, \vecbf{w}_{1}, \dots, \vecbf{w}_{m}$$
> [[Span|spans]] $V$. Applying the same procedure as in the above theorem's proof, but starting on $\vecbf{w}_{1}$ instead of $\vecbf{u}_{1}$, will give a [[Linear Independence|linearly independent]] [[Span|spanning list]] of $V$ (a *basis*) containing $\vecbf{u}_{1}, \dots, \vecbf{u}_{n}$.

- If $\left| I \right|$ or $\left| S \right|$ is equal to $\text{dim}(V)$, it must be a [[Vector Basis|basis]].
  > [!proof]- for $I$
> As shown, $I$ can be extended to a [[Vector Basis|basis]], but since the given [[Lists|list]] is already the size of a [[Vector Basis|basis]], this extension must be trivial, and the [[Lists|list]] must already be a [[Vector Basis|basis]].

  > [!proof]- for $S$
> As shown, $S$ can be reduced to a [[Vector Basis|basis]], but since the given [[Lists|list]] is already the size of a [[Vector Basis|basis]], this reduction must be trivial, and the [[Lists|list]] must already be a [[Vector Basis|basis]].

\[[[Dimension]]\]