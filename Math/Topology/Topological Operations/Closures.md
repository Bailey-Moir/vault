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
- $\large\overline{S}^c \in \mathcal{T}$[^1]
- $\large S\subseteq\overline{S}$

> [!characterisaion]- $p \in \overline{S} \iff \forall A \in \mathcal{N}_{p}, S \cap A \ne \emptyset$
> $\mathit{p \in \overline{S}}$ *iff every [[Neighbourhoods|neighbourhood]] of $\mathit{p}$ meets $\mathit{S}$.*
>
> $\left( \implies \right)$ [[Proof by Contradiction]]
> Suppose there is a [[Neighbourhoods|neighbourhood]] $A$ of $p\in \overline{S}$ that is [[Disjoint Sets|disjoint]] from $S$. 
> Since $A$ is [[Open Sets|open]], $A^c$ is [[Closed Sets|closed]].
> Further, since $A \subseteq S^c$ ($A$ and $S$ are [[Disjoint Sets|disjoint]]), $S \subseteq A^c$.
> Thus, by definition, $\overline{S}$ is given through [[Unions & Intersections|intersection]] with $A^c$, meaning $\overline{S} \subseteq A^c$ ($\overline{S} \cap A = \emptyset$).
> However, $p \in \overline{S} \cap A  = \emptyset$, a [[Contradictions|contradiction]]. Thus, if $p \in \overline{S}$, every [[Neighbourhoods|neighbourhood]] of $p$ must meet $S$. $\square$
> 
> $\left( \impliedby \right)$ [[Proof by Contraposition]]
> Suppose there is a [[Neighbourhoods|neighbourhood]] $A$ of $p$ that is [[Disjoint Sets|disjoint]] from $S$ ($A \subseteq S^c$). 
> Thus, by the definition of [[Interiors|interiors]], $A \subseteq \text{int}\,S^c = \text{ext}\,S = \overline{S}^c$[^2].
> Finally, since $p \in A$, $p \notin \overline{S}$. $\square$

> [!proof]- $(2)$ & $(1)$
> By the definition of [[Boundaries|boundaries]], 
> $$\begin{align}
> 	\partial S &= \overline{S} \setminus \text{int}\,S \\
> 	&= \overline{S} \cap \left( \text{int}\,S \right)^c.
> \end{align}$$
> Thus,
> $$\begin{align}
> 	\text{int}\,S \cup \partial S &= \text{int}\,S \cup \left( \overline{S} \cap \left( \text{int}\,S \right)^c \right) \\
> 	&= \left( \text{int}\,S \cap \overline{S} \right) \cup \left( \text{int}\,S \cap \text{int}\,S \right)^c \\
> 	&= \overline{S} \cup \emptyset && \text{int}\,S \subseteq S \subseteq \overline{S} \\
> 	&= \overline{S}. \hspace{1em} \square \\
> \end{align}$$
> This gives $(2)$. To derive $(1)$,
> $$\begin{align}
> 	\overline{S} &= \text{int}\,S \cup \partial S && (1) \\
> 	\overline{S} &= S \cup \text{int}\,S \cup \partial S && S \subseteq \overline{S} \\
> 	\overline{S} &= S \cup \partial S. \hspace{1em} \square && \text{int}\,S \subseteq S \\
> \end{align}$$

> [!theorem-1]- $S^c \in \mathcal{T} \iff S = \overline{S}$
> $\left( \implies \right)$
> If $S^c \in \mathcal{T}$ ($S$ is [[Closed Sets|closed]]), then $S \subseteq S$ and $S^c \in \mathcal{T}$, so $\overline{S}$ is given through [[Unions & Intersections|intersection]] with $S$, meaning $\overline{S}\subseteq S$. Since $S \subseteq \overline{S}$ is an identity, together these gives $S = \overline{S}$.
> 
> $\left( \impliedby \right)$
> If $S = \overline{S}$ and $\overline{S}^c \in \mathcal{T}$, $S^c \in \mathcal{T}$. $\square$


\[[[Interiors]]\]

[^1]: [[Closed Sets]]
[^2]: [[Exteriors]], Theorem 1
