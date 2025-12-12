---
tags:
  - atom
  - math
---
The *exterior* of $S\subseteq X$ is the [[Complement|complement]] of its [[Closures|closure]]:
$$\begin{align}
	\text{ext}\,S &= \bar{S}^c.
\end{align}$$
- $\large \text{ext}\,S \in \mathcal{T}$[^1]

> [!characterisation]- $p \in \text{ext}\,S \iff \exists A \in \mathcal{N}_{p} : S \cap A = \emptyset$ ($A \subseteq S^c$)
*$\mathit{p \in \text{ext}\,S}$ iff $\mathit{p}$ has a [[Neighbourhoods|neighbourhood]] [[Disjoint Sets|disjoint]] from $\mathit{S}$*
>
> The [[Closures|characterisation of closures]] states "$p \in \bar{S}$ iff every [[Neighbourhoods|neighbourhood]] of $p$ meets $S$." Taking the [[Converse, Inverse, and Contrapositive|converse]] of this [[Statements and Propositions|statement]] gives
"$p \in \bar{S}^c = \text{ext}\,S$ iff $p$ has a [[Neighbourhoods|neighbourhood]] [[Disjoint Sets|disjoint]] from $S$"

> [!theorem-1]- $\text{ext}\,S = \text{int}\,S^c$[^2]
> *This is easy to prove from the characterisation, but that would lead to circular logic in my notes*
> 
> $\left( \text{ext}\,S \subseteq \text{int}\,S^c \right)$
> By [[Converse, Inverse, and Contrapositive|contraposition]], since $S\subseteq \bar{S}$, $\text{ext}\,S = \bar{S}^c \subseteq S^c$. Since $\text{ext}\,S \in \mathcal{T}$ as well, by the definition of an [[Interiors|interior]], $\text{ext}\,S \subseteq \text{int}\,S^c$
> 
> $\left( \text{int}\,S^c \subseteq \text{ext}\,S \right)$
> Let $x \in \text{int}\,S^c$. By definition, there exists an [[Open Sets|open set]] $A$ such that $x \in A \subseteq S^c$. Thus $A \cap S = \emptyset$. Thus, not every [[Neighbourhoods|neighbourhood]] of $x$ meets $S$, so $x \notin \bar{S}$ (i.e. $x \in \bar{S}^c = \text{ext},S$)[^3]. Thus, $\text{int}\,S^c \subseteq \text{ext}\,S$.

[^1]: [[Open Sets]]
[^2]: [[Interiors]]
[^3]: [[Closures]], Theorem 1