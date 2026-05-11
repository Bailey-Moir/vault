---
tags:
  - atom
  - math
---
The *closure* of $S \subseteq X$ is the [[Unions & Intersections|intersection]] of all containing [[Closed Sets|closed sets]]:
$$\begin{align}
	\overline{S} &= \bigcap \{ A\subseteq X : S \subseteq A \land A^c \in \mathcal{T} \} \\
	&= S \cup \partial S && (1) \\
	&= \inte S \cup \partial S && (2) \\
	&= S \cup S' && (3) \\
\end{align}$$
- $\overline{S}^c \in \mathcal{T}$[^1]
- $S\subseteq\overline{S}$

> [!characterisaion]- $p \in \overline{S} \iff \forall A \in \mathcal{N}_{p}, S \cap A \ne \emptyset$.
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

> [!characterisation]- In [[Hausdorff Spaces|Hausdorff spaces]], $p \in \overline{S} \iff  \exists \left( x_{n} \right) \subseteq S : \lim x_{n} = p$.
> $\left( \implies \right)$
> Let $p \in \overline S$.
> Suppose $p \in S$. Then the [[Sequences|sequence]] $x_{n} = p \in S$ [[Sequence Convergence|converges]] to $p$.
> Suppose $p \in S'$. Then $p$ is a [[Limit Points|limit point]] of $S$, implying by [[Limit Points#^distinct-sequence|this theorem]] that there is a [[Sequences|sequence]] in $S$ that [[Sequence Convergence|converges]] to $p$.
> 
> $\left( \impliedby \right)$
> Since [[Closed Sets Contain Limit Points#^hausdorff|closed sets contain their limits]], if there exists $\left( x_{n} \right) \subseteq S \subseteq \overline S$ that converges to $p \in X$, $p \in \overline S$.
^sequence-characterisation

> [!theorem]- $\left( 3 \right)$
> We will prove this by showing 
> 1. $S \cup S'$ is [[Closed Sets|closed]], and that
> 2. it is the smallest [[Closed Sets|closed set]] containing $S$, implying it is $\overline{S}$.
> 
> Take $p \in \left( S' \cup S \right)^c = S'^c \cap S^c$.
> Thus $p \notin S'$, meaning $p$ is not a [[Limit Points|limit point]] of $S$, so there exists $A \in \mathcal{N}_{p}$ such that
> $$\begin{align}
> 	&S \cap A \subseteq \{ p \}. \\
> 	\implies & A \setminus \{ p \} \subseteq S^c \\
> 	\implies & A \subseteq S^c. && p \in S^c
> \end{align}$$
> Since $S'$ [[Limit Points#^closed|is closed]], there also exists $B \in \mathcal{N}_{p}$ such that $B \subseteq S'^c$. Therefore, there exists
> $$\underbrace{A \cap B}_{\in \mathcal{T}} \subseteq S'^c \cap S^c,$$
> meaning $\left( S' \cup S \right)^c \in \mathcal{T}$. $\quad\square_{1}$
> 
> Let $p \in S' \setminus S$. Then there exists a [[Sequences|sequence]] of distinct points $(x_{n}) \subseteq S$ that [[Sequence Convergence|converges]] to $p$.
> Thus, any containing [[Closed Sets|closed set]] must contain this limit $p$, as [[Closed Sets Contain Limit Points|closed sets contain their limits]].
> Therefore, any [[Closed Sets|closed set]] containing $S$ must contain $S'$. Since $S \cup S'$ is also [[Closed Sets|closed]], every [[Closed Sets|closed set]] must contain $S \cup S'$. Therefore, $S \cup S' = \overline S$. $\quad \square_{2}$

> [!theorem]- $S^c \in \mathcal{T} \iff S = \overline{S}$.
> $\left( \implies \right)$
> If $S^c \in \mathcal{T}$ ($S$ is [[Closed Sets|closed]]), then $S \subseteq S$ and $S^c \in \mathcal{T}$, so $\overline{S}$ is given through [[Unions & Intersections|intersection]] with $S$, meaning $\overline{S}\subseteq S$. Together with the identity $S \subseteq \overline{S}$, this gives $S = \overline{S}$.
> 
> $\left( \impliedby \right)$
> If $S = \overline{S}$, since $\overline{S}^c \in \mathcal{T}$, $S^c \in \mathcal{T}$. $\square$
^closedness

> [!properties]- Let $E,F \in X$.<ol><li>$E \subseteq F \to \overline E \subseteq \overline F$.</li><li>$\overline E \cup \overline F = \overline{E \cup F}$.</li><li>$\overline{E \cap F} \subseteq \overline E \cap \overline F$.</li></ol>
> 1. Suppose $E \subseteq F$ and $p \in \overline{E}$. Then there exists $\left( x_{n} \right) \subseteq E$ such that $\lim x_{n} = p$.
>    Since $\left( x_{n} \right) \subseteq F$, $\lim x_{n} = p \in \overline{F}$. Thus, $\overline{E} \subseteq \overline{F}$.
> 2. $\left( \supseteq \right)$
>    $\overline E \cup \overline F$ is a [[Closed Sets|closed set]] containing $E \cup F$, meaning $\overline{E \cup F} \subseteq \overline E \cup \overline F$.
>    $\left( \subseteq \right)$
>    $E \subseteq E \cup F$, and $F \subseteq E \cup F$, so by 1. and basic logic, $\overline E \cup \overline F \subseteq \overline{E \cup F}$.
> 3. $E \cap F \subseteq E$ and $E \cap F \subseteq F$, so by 1. and basic logic, $\overline{E \cap F} \subseteq \overline{E} \cap \overline{F}$.
^properties




\[[[Interiors]], [[Limit Points]]\]

[^1]: [[Closed Sets]]
[^2]: [[Exteriors]], Theorem 1
