---
tags:
  - atom
  - math
---
A point $p \in X$ is a *limit point* of $S \subseteq X$ iff every [[Neighbourhoods|neighbourhood]] of $p$ contains a point of $S$ other than $p$ itself; iff
$$\varepsilon$$
$$ \forall A \in \mathcal{N}_{p}, S \cap A \not\subseteq \{ p \} $$

> [!notation]  We denote the set of *limit points* of $S \subseteq X$ as $S'$.

> [!theorem]- $S'$ is [[Closed Sets|closed]]
> Let $p \in S'^c$, meaning there exists $A \in \mathcal{N}_{p}$ such that
> $$\begin{align}
> 	& S \cap A \subseteq \{ p \} \\
> 	\iff & S \cap (A \setminus \{  p \}) \subseteq \emptyset.
> \end{align}$$
> Note $A \setminus \{ p \} = A \cap \{ p \}^c \in \mathcal{T}$.
> 
> Let $q \in A \setminus \{ p \}$. Then there exists $B \in \mathcal{N}_{q}$ such that $B \subseteq A \setminus \{ p \}$.
> Thus, $S \cap B = \emptyset$, meaning $q \notin S'$. Since $q$ is arbitrary,
> $$\begin{align}
> 	A \setminus \{ p \} \subseteq S'^c \\
> 	A = \{ p \} \cup \left( A \setminus \{ p \} \right) \subseteq S'^c && p \in S'^c
> \end{align}$$
> Thus, $S'^c$ is [[Open Sets|open]] by [[Interiors#^characterisation|the characterisation of interiors]].
^closed

> [!theorem] *(Metric Space)* $\forall r > 0, S \cap B(p,r) \not\subseteq \{ p \}.$
^metric-space

> [!theorem]- A point $p \in X$ is a *limit point* of $S \subseteq X$ iff there exists a [[Sequences|sequence]] of distinct points $\left( x_{n} \right)$ in $S$ such that $x_{n} \to p$.
> $\left( \implies \right)$
> Suppose $p \in S'$. Then 
> $$ S \cap (B(p,1) \setminus \{ p \}) \ne \emptyset. $$
> So we may choose $x_{1} \in S \cap \left( B(p,1) \setminus \{ p \} \right)$.
> 
> Suppose $x_{1},\dots,x_{k} \in S$ satisfy
> 1. $d(p,x_{1}) > d(p,x_{2}) > \dots > d(p,x_{k})$
> 2. $0 < d(p,x_{k}) < \dfrac{1}{k}$
> 
> Let $r = \min \left\{ d(p,x_{k}), \dfrac{1}{k+1} \right\}$.
> Since $S \cap \left( B(p,r) \setminus \{ p \} \right) \ne \emptyset$, we may take $x_{k+1}$ from that [[Sets|set]]. Then $x_{k+1} \in S$ and $x_{k+1} \ne p$. Together, we have satisfied the two conditions.
> 
> By [[Induction|induction]], this induces a [[Sequences|sequence]] of distinct points $\left( x_{n} \right) \subseteq S$ (by 1.) that converges to $p$ (by 2. with [[Squeeze Theorem for Sequences|squeeze theorem]]).
> 
> $\left( \impliedby \right)$
^distinct-sequence