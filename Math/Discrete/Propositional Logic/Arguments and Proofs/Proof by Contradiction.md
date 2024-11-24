---
tags:
  - atom
  - math
  - discrete
---
$$ p \to q \iff p \land \neg q \to \F $$
$$A \iff \neg A \to \F$$
You can prove $p \to q$[^1] by proving $p \land \neg q$ is a [[Contradictions|contradiction]], which can be done as as the latter is the [[Negation|negation]] of the former. This is very similar to [[Proof by Contraposition|proof by contraposition]], as both assume $\neg q$.

\[[[Contradictions]]\]

> [!example]- $x^{2}\text{ is even} \to x\text{ is even}$
> Assume that $p \land \neg q$.
> $$x^2 \text{ is even} \land x \text{ is odd}$$
> Since $x$ is odd, $\exists k \in \Z : x = 2k + 1$ (by the definition of odd numbers).
> and since $x^2$ is even, $\exists l \in \Z : x^2 = 2l$ (by the definition of even numbers).
> $$\begin{align*}
> 	x^2 = (2k+1)^2 = 4k^2 + 4k + 1 &= 2l \\
> 	2k^2 + 2k + \dfrac{1}{2} &= l
> \end{align*}$$
> This is a contradiction as the $\text{LHS}$ is not an integer, but the $\text{RHS}$ is.
> 
> \[[[Existential Quantifier]]\]

[^1]: [[Implication]]