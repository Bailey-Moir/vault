---
tags:
  - atom
  - math
---
A morphism $\alpha : x \to y$ is *split epic* iff there exists a morphism $\beta : y \to x$ such that $\alpha\beta = 1_{y}$:
![300|center](split-epic-diagram.excalidraw)
*i.e. it has a left inverse.*

> [!theorem-1]- *Split epic* $\to$ [[Epic Morphisms|epic]]
> Let $\alpha : x \to y$ be a *split epic* morphism in $\mathcal{C}$, so there exists $\beta : y \to x$ such that $\alpha\beta = 1_{y}$.
> 
> For some $z \in \mathcal{C}$, let $\beta_{1},\beta_{2} : y \to z$ such that $\beta_{1}\alpha = \beta_{2}\alpha$. Then
> $$\beta_{1} = \beta_{1}1_{y} = \beta_{1}\alpha\beta = \beta_{2}\alpha\beta = \beta_{2}1_{y} = \beta_{2},$$
> meaning $\alpha$ is [[Epic Morphisms|epic]].

> [!theorem-2]- In a [[Concrete Categories|concrete category]], every *split epic* morphism is [[Surjective Functions|surjective]].
> Let $\alpha : X \to Y$ be a *split epic* morphism in $\mathcal{C}$, so there exists $\beta : Y \to X$ such that $\alpha\beta = 1_{Y}$.
> For any $y \in Y$,
> $$y = 1_{Y}(y) = \alpha\beta(y) = \alpha(\beta(y)),$$
> meaning $\alpha$ maps $\beta(y)$ to $y$, so $\alpha$ is [[Surjective Functions|surjective]].
> *This makes sense, as the identity must be [[Surjective Functions|surjective]], meaning it's last morphism must as well.*

> [!theorem-3]- In $\mathbf{Set}$[^1], a morphism is *split epic* iff it is [[Surjective Functions|surjective]].
> Let $\alpha : X \to Y$ be a morphism in $\mathbf{Set}$.
> ($\implies$)
> This is exactly Theorem 1.
> 
> $\left( \impliedby \right)$
> Suppose $\alpha$ is [[Surjective Functions|surjective]].
> For each $y \in Y$, there exists some $x \in X$ such that $\alpha(x) = y$. Define $\beta(y) = x$.
> This defines $\beta: Y \to X$, which satisfies $\alpha\beta = 1_{Y}$.
> Therefore $\alpha$ is *split epic*.

> [!-] *This* definition is [[Duality|dual]] to that of [[Split Monic Morphisms|split monic morphisms]].

[^1]: [[Category of Sets]]
