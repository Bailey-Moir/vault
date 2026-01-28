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

> [!proof]- $(1)$
> By [[De Morgan's Laws|De Morgan's laws]] and the definition of the [[Exteriors|exterior]],
> $$\begin{align}
> 	\partial S &= \left( \text{int}\,S \cup \text{ext}\, S \right)^c \\
> 	&= \left( \text{int}\,S \right)^c \cap \left( \text{ext}\, S \right)^c \\
> 	&= \left( \text{int}\,S \right)^c \cap \left( \overline{S}^c \right)^c \\
> 	&= \left( \text{int}\,S \right)^c \cap \overline{S} \\
> 	&= \overline{S} \setminus \text{int}\,S \\
> \end{align}$$

> [!characterisation]- $p \in \partial S \iff \forall A \in \mathcal{N}_{p}, S \cap A \ne \emptyset \land S^c \cap A \ne \emptyset$
*$\mathit{p \in \partial S}$ iff every [[Neighbourhoods|neighbourhood]] of $\mathit{p}$ meets $\mathit{S}$ and $\mathit{S^c}$*
> 
> $$\begin{align}
> 	p \in \partial S &\iff p \in (\inte S \cup \ext S)^c \\
> 	p \notin \partial S &\iff p \in \inte S \cup \ext S \\
> 	&\iff p \in \inte S \lor p \in \ext S \\
> 	&\iff \left( \exists A \in \mathcal{N}_p : A \subseteq S \right) \lor \left( \exists A \in \mathcal{N}_p : S \cap A = \emptyset \right) && (1) \\
> 	&\iff \exists A \in \mathcal{N}_p : A \subseteq S \lor S \cap A = \emptyset \\
> 	&\iff \exists A \in \mathcal{N}_p : S \cap A = \emptyset \lor S^c \cap A = \emptyset \\
> 	p \in \partial S &\iff \forall A \in \mathcal{N}_p, S \cap A \ne \emptyset \land S^c \cap A \ne \emptyset,
> \end{align}$$
> 
> where (1) is by the [[Interiors#^characterisation|characterisation of interiors]] and [[Exteriors#^characterisation|characterisation of exteriors]]. $\square$
^characterisation

> [!theorem-1]- $\partial S = \partial S^c$
> By [[Exteriors#^interior-of-complement|exteriors, theorem 1]],
> $$\begin{align}
> 	\partial S^c &= \left( \text{int}\,S^c \cup \text{ext}\, S^c \right)^c \\
> 	&= \left( \text{ext}\,S \cup \text{int}\, S \right)^c \\
> 	&= \partial S \\
> \end{align}$$
^closed-complement

> [!theorem-2]- $S \in \mathcal{T} \iff S \cap \partial S = \emptyset$ ($\partial S \subseteq S^c$) 
> $\left( \implies \right)$
> Suppose $S \in \mathcal{T}$. By the definition of *boundaries* and [[Interiors#^openness|interiors, theorem 1]] ,
> $$\begin{align}
> 	\partial S &= \overline{S} \setminus \text{int}\,S \\
> 	&= \overline{S} \setminus S \\
> \end{align}$$
> Thus, $S \cap \partial S = \emptyset$.
> 
> $\left( \impliedby \right)$
> Let $p \in S$. Suppose that for all $A \in \mathcal{N}_p$[^2], $A \not\subseteq S$.
> Then there must exist $z \in A$ such that $z \in S^c$.
> Thus, by the [[#^characterisation|characterisation of boundaries]], $p \in \partial S$.
> Thus, $p \in S \cap \partial S$, so $S \cap \partial S \ne \emptyset$.
> 
> [[Converse, Inverse, and Contrapositive|Contraposing]] this, supposing $S \cap \partial S = \emptyset$ gives that $\forall p \in S, \exists A \in \mathcal{N}_p : A \subseteq S$[^2].
> Thus, by the [[Interiors#^characterisation|characterisation of interiors]], $S \subseteq \inte S$.
Together with the identity $\inte S \subseteq S$, this gives $S = \inte S$, and by [[Interiors#^openness|interiors, theorem 1]], $S \in \mathcal{T}$. $\square$
^openness

> [!theorem-3]- $S^c \in \mathcal{T} \iff \partial S \subseteq S$ 
> Substituting $S$ as $S^c$ in [[#^openness|theorem 2]] gives
> $$\begin{align}
> 	S^c \in \mathcal{T} &\iff \partial (S^c) \subseteq \left( S^c \right)^c \\
> 	&\iff \partial S \subseteq S \\
> \end{align}$$
> as $\partial S^c = \partial S$ by [[#^closed-complement|theorem-1]].
^closedness

[^1]: [[Exteriors]]
[^2]: [[Neighbourhoods]]
