---
tags:
  - atom
  - math
  - discrete
sr-due: 2026-04-05
sr-interval: 4
sr-ease: 276
---
A [[Sets|set]] $A$ is a *subset* of a [[Sets|set]] $B$, denoted $A \subseteq B$, iff every element of $A$ is also an element of $B$. 
If $A$ is a *subset* of $B$, but $A$ is [[Set Equality|not equal]] to $B$ then $A$ is a ***proper subset*** of $B$, written $A \subset B$.
$$\begin{align*}
	A \subseteq B &\iff \forall x \in A, x \in B \\
	A \subset B &\iff A \ne B \land \forall x \in A, x \in B
\end{align*}$$
\[[[Universal Quantifier]], [[Set Equality]]\]

> [!note] **Properties of Subsets** $\forall A, B, C$
> - **[[Reflexive Property]]**
>   $A \subseteq A$
> - **[[Transitive Property]]**
>   $A \subseteq B \land B \subseteq C \implies A \subseteq C$
> - **[[Antisymmetric Property]]**
>   $A \subseteq B \land B \subseteq A \implies A = B$
> 
> Thus, this is a [[Partial Order|partial order]].