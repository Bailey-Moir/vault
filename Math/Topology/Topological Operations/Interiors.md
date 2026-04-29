---
tags:
  - atom
  - math
---
The *interior* of $S\subseteq X$ is the [[Unions & Intersections|union]] of all contained [[Closed Sets|open sets]]:
$$\begin{align}
	\inte{S} &= \bigcup \{ A\subseteq X : A \subseteq S \land A \in \mathcal{T} \} \\
	&= \bigcup \left( \mathcal{P}(S) \cap \mathcal{T} \right) \\
\end{align}$$
- $\inte S \in \mathcal{T}$[^1]
- $\inte S \subseteq S$

> [!characterisation]- $p \in \inte S \iff \exists A \in \mathcal{N}_{p} : A \subseteq S$
*$\mathit{p \in \inte S}$ iff $\mathit{p}$ has a [[Neighbourhoods|neighbourhood]] contained in $\mathit{S}$*
> $$\begin{align}
> 	p \in \inte S &\iff \exists A \subseteq X : p \in A \land A \subseteq S \land A \in \mathcal{T} \\
> 	&\iff \exists A \subseteq \mathcal{N}_p : A \subseteq S. \quad \square
> \end{align}$$
^characterisation

> [!theorem]- $\inte S$ is the largerst [[Open Sets|open]] [[Subsets|subset]] of $S$.
> Let $A \in X$ be an [[Open Sets|open]] [[Subsets|subset]] of $S$. Then
> $$\begin{align}
> 	&A \in \mathcal{P}(S) \cap \mathcal{T} \\
> 	\to& A \subseteq \inte S = \bigcup \left( \mathcal{P}(S) \cap \mathcal{T} \right). \\
> \end{align}$$
> Thus, $\inte S$ contains every [[Open Sets|open]] [[Subsets|subset]], meaning it is the largest one.
^largest

> [!theorem-1]- $S \in \mathcal{T} \iff S = \inte S$
> $\left( \implies \right)$
> If $S \in \mathcal{T}$, then $S \in \mathcal{P}(S) \cap \mathcal{T}$. By the definition the [[Power Sets|power set]], all other elements are [[Subsets|subsets]] of $S$, so [[Unions & Intersections|unioning]] them will give $S$. Thus, $\inte S = S$. $\square$
> 
> $\left( \impliedby \right)$
> If $S = \inte S \in \mathcal{T}$, $S \in \mathcal{T}$. $\square$
^openness

> [!properties]- Let $E,F \in X$.<ol><li>$E \subseteq F \to \inte E \subseteq \inte F$.</li><li>$\inte E \cap \inte F = \inte{\left( E \cap F \right)}$.</li><li>$\inte E \cup \inte F \subseteq \inte{\left( E \cup F \right)}$.</li></ol>
> 1. $\;$
> $$\begin{align}
> 	E &\subseteq F \\
> 	\mathcal{P}(E) &\subseteq \mathcal{P}(F) \\
> 	\mathcal{P}(E) \cap \mathcal{T} &\subseteq \mathcal{P}(F) \cap \mathcal{T} \\
> 	\bigcup \left( \mathcal{P}(E) \cap \mathcal{T} \right) &\subseteq \bigcup\left( \mathcal{P}(F) \cap \mathcal{T} \right) \\
> 	\inte E &\subseteq \inte F. \\
> \end{align}$$
> 2.  $\left( \supseteq \right)$
>    By **1.**, $\inte{\left( E \cap F \right)} \subseteq \inte E$ and $\inte{\left( E \cap F \right)} \subseteq \inte F$. Thus, $\inte{\left( E \cap F \right)} \subseteq \inte E \cap \inte F$.
>    $\left( \subseteq \right)$
>    By definition, $\inte E \subseteq E$ and $F^o \subseteq F$, so $\inte E \cap \inte F \subseteq E \cap F$.
>    $\inte E \cap \inte F$ is then an [[Open Sets|open]] [[Subsets|subset]] of $E \cap F$, so $\inte E \cap \inte F \subseteq \inte{\left( E \cap F \right)}$.
> 
> 3. By **1.**, $\inte E \subseteq \inte{\left( E \cap F \right)}$ and $\inte F \subseteq \inte{\left( E \cup F \right)} \subseteq$. Thus, $\inte E \cup \inte F\ \subseteq \inte{\left( E \cup F \right)}$.


^properties

\[[[Closures]]\]

[^1]: [[Open Sets]]
