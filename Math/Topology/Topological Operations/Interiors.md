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

> [!theorem-1]- $S \in \mathcal{T} \iff S = \inte S$
> $\left( \implies \right)$
> If $S \in \mathcal{T}$, then $S \in \mathcal{P}(S) \cap \mathcal{T}$. By the definition the [[Power Sets|power set]], all other elements are [[Subsets|subsets]] of $S$, so [[Unions & Intersections|unioning]] them will give $S$. Thus, $\inte S = S$. $\square$
> 
> $\left( \impliedby \right)$
> If $S = \inte S \in \mathcal{T}$, $S \in \mathcal{T}$. $\square$
^openness

\[[[Closures]]\]

[^1]: [[Open Sets]]
