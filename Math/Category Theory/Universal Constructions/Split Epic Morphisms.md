---
tags:
  - atom
  - math
---
A morphism $\alpha : x \to y$ is *split epic* iff there exists a morphism $\beta : y \to x$ such that $\alpha\beta = 1_{y}$:
```tikz
\usepackage{tikz-cd}
\begin{document}

\begin{tikzcd}
	x \arrow[r, shift right, swap, "\alpha"] & y \arrow[l, shift right, swap, dashed, "\exists \beta"] \arrow[loop right, "1_y"]
\end{tikzcd}

\end{document}
```
*i.e. it has a right inverse.*

> [!-] *This* definition is [[Duality|dual]] to that of [[Split Monic Morphisms|split monic morphisms]].

> [!theorem-1]- *Split epic* $\to$ [[Epic Morphisms|epic]]
> [[Categories|Categories]] are [[Duality|self-dual]], and this theorem is dual to [[Split Monic Morphisms#^split-monic-gives-monic|split monic's equivalent theorem]] that holds for all [[Categories|categories]], so this theorem is given by [[Duality#^statements-in-self-dual-category-classes|duality theorems]].

> [!theorem-2]- In a [[Concrete Categories|concrete category]], every *split epic* morphism is [[Surjective Functions|surjective]].
> Let $\alpha : X \to Y$ be a *split epic* morphism in $\mathcal{C}$, so there exists $\beta : Y \to X$ such that $\alpha\beta = 1_{Y}$.
> For any $y \in Y$,
> $$y = 1_{Y}(y) = \alpha\beta(y) = \alpha(\beta(y)),$$
> meaning $\alpha$ maps $\beta(y)$ to $y$, so $\alpha$ is [[Surjective Functions|surjective]].

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

[^1]: [[Category of Sets]]
