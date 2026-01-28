---
tags:
  - atom
  - math
---
A morphism $\alpha : x \to y$ is *monic* iff in the situation
```tikz
\usepackage{tikz-cd}
\begin{document}

\begin{tikzcd}
        z \arrow[r, shift left, "\beta_1"] \arrow[r, shift right, swap, "\beta_2"] & x \arrow[r, "\alpha"] & y
\end{tikzcd},

	
\end{document}
```
$$\alpha\beta_{1} = \alpha \beta_{2} \to \beta_{1} = \beta_{2},$$
*i.e. it can be cancelled on the left.*

> [!-] *This* definition is [[Duality|dual]] to that of [[Epic Morphisms|epic morphisms]].

> [!theorem-1]- In a [[Concrete Categories|concrete category]], every [[Injective Functions|injective]] morphism is *monic*.
> Let $\alpha : X \to Y$ be an [[Injective Functions|injective]] morphism in a [[Concrete Categories|concrete category]] $\mathcal{C}$. Let $Z \in \mathcal{C}$ and $\beta_{1},\beta_{2} : Z \to X$ such that $\alpha\beta_{1} = \alpha\beta_{2}$. For each $z \in Z$,
> $$\alpha(\beta_{1}(z)) = \alpha\beta_{1}(z) = \alpha\beta_{2}(z) = \alpha(\beta_{2}(z)),$$
> meaning $\beta_{1}(z) = \beta_{2}(z)$ by the [[Injective Functions|injectivity]] of $\alpha$. Since this applies for all $z \in Z$, this gives $\beta_{1} = \beta_{2}$.

>[!theorem-2]- In the [[Categories|category]] of [[Category of Sets|sets]], [[Category of Topologies|topologies]], [[Category of Groups|groups]], and [[Rings|rings]], a morphism is [[Injective Functions|injective]] iff it is *monic*.