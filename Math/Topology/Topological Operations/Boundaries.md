---
tags:
  - atom
  - math
---
The *boundary* of $S \subseteq X$ is its [[Closures|closure]] without its [[Interiors|interior]]:
$$\begin{align}
	\partial S &= \left( \text{int}\,S \cup \text{ext}\, S \right)^c \\
	&= \overline{S} \setminus \text{int}\,S && (1)\\
\end{align}$$
- $\left( \partial S \right)^c \in \mathcal{T}$[^1]

> [!characterisation]- $p \in \partial S \iff \forall A \in \mathcal{N}_{p}, S \cap A \ne \emptyset \land S^c \cap A \ne \emptyset$
*$\mathit{p \in \partial S}$ iff every [[Neighbourhoods|neighbourhood]] of $\mathit{p}$ meets $\mathit{S}$ and $\mathit{S^c}$*
> 
> $\left( \implies \right)$
> Let p be in the *boundary* of $S$ ($p \in \partial S$) and $A$ be any [[Neighbourhoods|neighbourhood]] of $p$ ($p \in A \in \mathcal{T}$).
> 
> Suppose $A \subseteq S$. Since $A \in \mathcal{T}$, by the definition of [[Interiors|interiors]], $A \subseteq \text{int}\,S$. Thus, $A \cap \partial S = \emptyset$, a [[Contradictions|contradiction]] as $p \in \partial S$ and $p \in A$.
> Thus, $A \not\subseteq S$, so $A$ contains at least one point of $S^c$.
> 
> Similarly, suppose $A$ and $S$ are [[Disjoint Sets|disjoint]] ($A \subseteq S^c$). Since $A \in \mathcal{T}$, by the definition of [[Interiors|interiors]], $A \subseteq \text{int}\,S^c = \text{ext}\,S$[^1]. Thus, $A \cap \partial S = \emptyset$, a [[Contradictions|contradiction]] as $p \in \partial S$ and $p \in A$.
> Thus, $A$ and $S$ are not [[Disjoint Sets|disjoint]], so $A$ contains at least one point of $S$.
> 
> $\left( \impliedby \right)$
> BRO HOW

> [!theorem-1]- $S \in \mathcal{T} \iff S \cap \partial S = \emptyset$ ($\partial S \subseteq S^c$) 
> $\left( \implies \right)$
> Suppose $S \in \mathcal{T}$. By the definition of [[Boundaries|boundaries]] and \[[[Interiors]], Theorem 1\] 
> $$\begin{align}
> 	\partial S &= \overline{S} \setminus \text{int}\,S \\
> 	&= \overline{S} \setminus S \\
> \end{align}$$
> Thus, $S \cap \partial S = \emptyset$.
> 
> $(\impliedby)$
> Suppose $S \cap \partial S = \emptyset$. Further, suppose that for all [[Neighbourhoods|neighbourhoods]] $A$ of $p \in S$, $A \not\subseteq S$. Then there must exists $z \in A$ such that $z \in S^c$.
> 
> Thus, by the *characterisation of boundaries*, $p \in \partial S$. This is a [[Contradictions|contradiction]] though, because $p \in S$ and $S \cap \partial S = \emptyset$.
> 
> Thus, if $S \cap \partial S = \emptyset$, then each point $p \in S$ must have a [[Neighbourhoods|neighbourhood]] contained in $S$.
> 
> Thus, by the [[Interiors|characterisation of interiors]], every $p \in S\to p \in \text{int}\,S$, meaning $S \subseteq \text{int}\,S$.
> 
> Since $\text{int}\,S \subseteq S$ is an identity, this gives $S = \text{int}\,S$, so by \[[[Interiors]], Theorem 1\], $S \in \mathcal{T}$.

> [!theorem-2]- $S^c \in \mathcal{T} \iff \partial S \subseteq S$ 
> Substituting $S$ as $S^c$ in **theorem 1** gives
> $$\begin{align}
> 	S^c \in \mathcal{T} &\iff \partial (S^c) \subseteq \left( S^c \right)^c \\
> 	&\iff \partial S \subseteq S && \textbf{Th. 3} \\
> \end{align}$$

> [!theorem-3]- $\partial S = \partial S^c$
> By \[[[Exteriors]], Theorem 1\],
> $$\begin{align}
> 	\partial S^c &= \left( \text{int}\,S^c \cup \text{ext}\, S^c \right)^c \\
> 	&= \left( \text{ext}\,S \cup \text{int}\, S \right)^c \\
> 	&= \partial S \\
> \end{align}$$

> [!proof]- $(1)$
> By [[De Morgan's Laws|De Morgan's laws]] and the definition of the [[Exteriors|exterior]],
> $$\begin{align}
> 	\partial S &= \left( \text{int}\,S \cup \text{ext}\, S \right)^c \\
> 	&= \left( \text{int}\,S \right)^c \cap \left( \text{ext}\, S \right)^c \\
> 	&= \left( \text{int}\,S \right)^c \cap \left( \overline{S}^c \right)^c \\
> 	&= \left( \text{int}\,S \right)^c \cap \overline{S} \\
> 	&= \overline{S} \setminus \text{int}\,S \\
> \end{align}$$

[^1]: [[Exteriors]]
