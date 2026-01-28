---
tags:
  - atom
  - math
---
A morphism $\alpha : x \to y$ is *split monic* iff there exists a morphism $\beta : y \to x$ such that $\beta\alpha = 1_{x}$:
![300|center](split-monic-diagram.excalidraw)
*i.e. it has a left inverse.*

> [!theorem-1]- *Split monic* $\to$ [[Monic Morphisms|monic]]
> Let $\alpha : x \to y$ be a *split monic* morphism in $\mathcal{C}$, so there exists $\beta : y \to x$ such that $\beta\alpha = 1_{x}$.
> 
> For some $z \in \mathcal{C}$, let $\beta_{1},\beta_{2} : z \to x$ such that $\alpha\beta_{1} = \alpha\beta_{2}$. Then
> $$\beta_{1} = 1_{x}\beta_{1} = \beta\alpha\beta_{1} = \beta\alpha\beta_{2} = 1_{x}\beta_{2} = \beta_{2},$$
> meaning $\alpha$ is [[Monic Morphisms|monic]].

> [!theorem-2]- In a [[Concrete Categories|concrete category]], every *split monic* morphism is [[Injective Functions|injective]].
> Let $\alpha : X \to Y$ be a *split monic* morphism in $\mathcal{C}$, so there exists $\beta : Y \to X$ such that $\beta\alpha = 1_{X}$.
> 
> Let $x_{1}, x_{2} \in X$ such that $\alpha(x_{1}) = \alpha(x_{2})$. Then
> $$\begin{align}
> 	\alpha(x_{1}) &= \alpha(x_{2}) \\
> 	\beta\alpha(x_{1}) &= \beta\alpha(x_{2}) \\
> 	x_{1} &= x_{2} \\
> \end{align}.$$
> *This makes sense as having a left inverse means it doesn't lose any information, which means it's injective.*

> [!-] *This* definition is [[Duality|dual]] to that of [[Split Epic Morphisms|split epic morphisms]].