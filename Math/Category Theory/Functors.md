---
tags:
  - atom
  - math
---
Let $\mathcal{C}$ and $\mathcal{D}$ be [[Categories|categories]]. A *functor* $F$ from $\mathcal{C}$ to $\mathcal{D}$ is a [[Functions|function]] that
- maps each object $x \in \mathcal{C}$ to an object $F(x) \in \mathcal{D}$, and
- maps each morphism $\alpha: x \to y$ in $\mathcal{C}$ to a morphism $F(\alpha): F(x) \to F(y)$ in $D$ such that
	- $F(1_{x}) = 1_{F(x)}$ for all $x \in \mathcal{C}$, and
	- $F(\beta \circ \alpha) = F(\beta) \circ F(\alpha)$ for all $\alpha : x \to y$, $\beta : y \to z$ in $\mathcal{C}$,
	
	i.e., it preserves identity morphisms and [[Composite Functions|composition]].

> [!intuition] A *functor* is a mapping between [[Categories|categories]] that preserves structure.