---
tags:
  - atom
  - math
---
A morphism $\alpha : x \to y$ is *epic* iff in the situation
![300|center](epic-diagram.excalidraw)
$$\beta_{1}\alpha = \beta_{2}\alpha \to \beta_{1} = \beta_{2},$$
*i.e. it can be cancelled on the right.*

> [!theorem-1]- In a [[Concrete Categories|concrete category]], every [[Surjective Functions|surjective]] morphism is *epic*.
> Suppose $\alpha : X \to Y$ is [[Surjective Functions|surjective]]. 
> 
> Let $z \in Z \in \mathcal{C}$ and $\beta_{1},\beta_{2} : Y \to Z$ such that $\beta_{1}\alpha = \beta_{2}\alpha$.
> 
> Let $y \in Y$. By the [[Surjective Functions|surjectivity]] of $\alpha$, there exists $x \in X$ such that $\alpha(x) = y$. Thus,
> $$\beta_{1}(y) = \beta_{1}(\alpha(x)) = \beta_{1}\alpha(x) = \beta_{2}\alpha(x) = \beta_{2}(\alpha(x)) = \beta_{2}(y).$$
> Thus, meaning $\beta_{1} = \beta_{2}$. $\square$

> [!theorem-2]- In the [[Categories|category]] of [[Category of Sets|sets]], [[Category of Topologies|topologies]], and [[Category of Groups|groups]], a morphism is *epic* iff it is [[Surjective Functions|surjective]].
> ($\implies$)
> This is exactly Theorem 1.
> 
> $\left( \impliedby \right)$
> Consider $\mathbf{Set}$. Suppose $\alpha : X \to Y$ is *epic*.
> Let $\beta_{1}: Y \to \B$ be the characteristic [[Functions|function]] of $\text{im}\,\alpha$, meaning 
> $$\beta_{1}(y) = \begin{cases}
> 	1 & y \in \text{im}\,\alpha \\
> 	0 & y \notin \text{im}\,\alpha. \\
> \end{cases}$$
> Let $\beta_{2} : Y \to \B$ be constantly $1$.
> Thus $\beta_{1}\alpha=\beta_{2}\alpha$ as both are constantly $1$.
> Since $\alpha$ is *epic*, $\beta_{1}=\beta_{2}$, meaning $\beta_{1}(y) = 1$ for all $y$, so $\text{im}\,\alpha = Y$.
> 
> The proof for $\mathbf{Top}$ is the same as $\mathbf{Set}$, except
> - $\alpha$ is supposed to be [[Continuous Maps|continuous]],
> - $\B$ has the indiscrete topology so that $\beta_{1}$ and $\beta_{2}$ are [[Continuous Maps|continuous]] (as the [[Range & Image|preimage]] of $\emptyset$ is $\emptyset \in \mathcal{T}_{Y}$, and the [[Range & Image|preimage]] of $\B$ is $Y \in \mathcal{T}_{Y}$).
> 
> Consider $\mathbf{Grp}$. I don't actually know what a group homemorphism is so idk.

> [!-] *This* definition is [[Duality|dual]] to that of [[Monic Morphisms|monic morphisms]].