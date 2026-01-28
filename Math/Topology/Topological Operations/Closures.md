---
tags:
  - atom
  - math
---
The *closure* of $S \subseteq X$ is the [[Unions & Intersections|intersection]] of all containing [[Closed Sets|closed sets]]:
$$\begin{align}
	\overline{S} &= \bigcap \{ A\subseteq X : S \subseteq A \land A^c \in \mathcal{T} \} \\
	&= S \cup \partial S && (1) \\
	&= \text{int }S \cup \partial S && (2) \\
\end{align}$$
- $\overline{S}^c \in \mathcal{T}$[^1]
- $S\subseteq\overline{S}$

> [!characterisaion]- $p \in \overline{S} \iff \forall A \in \mathcal{N}_{p}, S \cap A \ne \emptyset$
> $\mathit{p \in \overline{S}}$ *iff every [[Neighbourhoods|neighbourhood]] of $\mathit{p}$ meets $\mathit{S}$.*
> 
> $\left( \implies \right)$ **[[Proof by Contraposition|Proof by Contraposition]]**
> Suppose there is a [[Neighbourhoods|neighbourhood]] $A$ of $p$ that is [[Disjoint Sets|disjoint]] from $S$.
> Then $S\subseteq A^c$ and $A^c$ is [[Closed Sets|closed]].
> Thus, by *definition* $\bar{S}$ is given through [[Unions & Intersections|intersection]] with $A^c$, meaning $\bar{S} \subseteq A^c$, so since $p \in A$, $p \notin \bar{S}$.
> 
> $\left( \impliedby \right)$ **[[Proof by Contraposition|Proof by Contraposition]]**
> Let $p \in \bar{S}^c$.
> $\bar{S}^c \in \mathcal{N}_{p}$, and $S \cap \bar{S}^c = \emptyset$ since $S \subseteq \bar{S}$.
> Thus, $\bar{S}^c$ satisfies $A$ in $\exists A \in \mathcal{N}_{p} : S \cap A = \emptyset$. $\square$
^characterisation

> [!theorem-1]- $S^c \in \mathcal{T} \iff S = \overline{S}$
> $\left( \implies \right)$
> If $S^c \in \mathcal{T}$ ($S$ is [[Closed Sets|closed]]), then $S \subseteq S$ and $S^c \in \mathcal{T}$, so $\overline{S}$ is given through [[Unions & Intersections|intersection]] with $S$, meaning $\overline{S}\subseteq S$. Together with the identity $S \subseteq \overline{S}$, this gives $S = \overline{S}$.
> 
> $\left( \impliedby \right)$
> If $S = \overline{S}$, since $\overline{S}^c \in \mathcal{T}$, $S^c \in \mathcal{T}$. $\square$
^closedness

\[[[Interiors]]\]

[^1]: [[Closed Sets]]
[^2]: [[Exteriors]], Theorem 1
