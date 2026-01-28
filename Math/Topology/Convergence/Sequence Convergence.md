---
tags:
  - atom
  - math
---
A [[Sequences|sequence]] $\left( a_{n} \right)$ of points in a [[Topology|topological space]] $\left( X,\mathcal{T} \right)$ *converges* to $L$ iff
$$\begin{align}
& \forall A \in \mathcal{N}_{L}, \exists N \in \N: \forall n \ge N, a_{n} \in A \\
	{\textcolor{gray}\iff} & \forall B \in \mathcal{B} \cap \mathcal{N}_{L}, \exists N \in \N: \forall n \ge N, a_{n} \in B && (1)
\end{align}$$
*iff for any [[Neighbourhoods|neighbourhood]] $\mathit{A}$ of $\mathit{L}$, eventually the [[Sequences|sequence]] is contained in $\mathit{A}$.*

> [!proof]-  $(1)$
> $\left( \implies \right)$
> Restricting $A$ in the definition of [[Sequence Convergence|sequence convergence]] to be a [[Topological Bases|basis element]] $B \in \mathcal{B}$ gives the concluision directly.
> 
> $\left( \impliedby \right)$
Let $A \in \mathcal{N}_L$. By definition, there must exist $\mathcal{C} \subseteq \mathcal{B}$ such that $A =\bigcup \mathcal{C}$.
> 
> Since $A$ is a [[Neighbourhoods|neighbourhood]] of $L$, there must exist some $B \in \mathcal{C}$ that is a [[Neighbourhoods|neighbourhood]] of $L$.
> 
> Thus by the premise, there exists $N \in\N$ such that for all $n \ge N$, $a_n \in B \subseteq A$.  $\square$

> [!theorem-1]- For any non-eventually constant [[Sequences|sequence]] $\left( a_{n} \right)$ with *limit* $L$, $L$ is a [[Limit Points|limit point]] of $\{ a_{n}\}$.
> Suppose $L$ is not a [[Limit Points|limit point]] of $\{ a_{n} \}$. Then $L$ must have a [[Neighbourhoods|neighbourhood]] $A$ such that $\{ a_{n} \} \cap A \subseteq \{ L \}$.
> 
> If $\{ a_{n} \} \cap A = \emptyset$, then $\forall n \in \N, a_{n} \notin A$, meaning $\left( a_{n} \right)$ does not converge to $L$.
> 
> If $\{ a_{n} \} \cap A = \{ L \}$, the only way $\lim a_{n} = L$ is if $\exists N \in \N: \forall n \ge N, a_{n} = L$, which would make $\left( a_{n} \right)$ eventually constant, a [[Contradictions|contradiction]].
> 
> Thus, the theorem is [[Proof by Contraposition|proven by contraposition]]. $\square$

> [!theorem-2]- If $\{ a_{n} \} \subseteq S \subseteq X$ with $a_{n} \to L$, then $L \in \bar{S}$.
> $$\begin{align}
> &\forall A \in \mathcal{N}_{L}, \exists N \in \N: \forall n \ge N, a_{n} \in A  \\
> \to &\forall A \in \mathcal{N}_{L}, \exists n \in \N : a_{n} \in A \\
> \to &\forall A \in \mathcal{N}_{L}, \{ a_{n} \} \cap A \ne \emptyset \\
> \to &\forall A \in \mathcal{N}_{L}, S \cap A \ne \emptyset && \{ a_{n} \} \subseteq S
> \end{align}$$
> Thus, by the the [[Closures|characterisation of closures]], $L \in \bar{S}$.

\[[[Metric Sequence Convergence]]\]