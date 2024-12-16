---
tags:
  - atom
  - math
  - discrete
---
Let $S$ be the [[Sets|set]] of [[Sets|sets]] that don't contain themselves
$$S = \{ A : A \notin A \}$$
Is $S \in S$?

If $S \in S$, the set property requires $S \notin S$, implying a [[Contradictions|contradiction]].
> [!proof]- Propositional Logic
> $$\begin{align}
> 	S\in S \land \forall A \in S, A \not\in A &\implies S \notin S \\
> 	&\implies S \notin S \land S \in S\\
> 	&\implies \F \\
> \end{align}$$
> \[[[Universal Quantifier]]\]

If $S \notin S$, $S$ satisfies the set property, and thus $S \in S$, implying a [[Contradictions|contradiction]].
> [!proof]- Propositional Logic
> $$\begin{align}
> 	S\notin S \land \forall A, \left( A \notin A \to A \in S \right) &\implies S \in S \\
> 	&\implies S \in S \land S \notin S\\
> 	&\implies \F \\
> \end{align}$$
> \[[[Universal Quantifier]]\]

Thus, $S \in S \iff S \notin S$, meaning the existence of $S$ is a [[Contradictions|contradiction]].