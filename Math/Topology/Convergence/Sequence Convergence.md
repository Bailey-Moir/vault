---
tags:
  - atom
  - math
---
A [[Sequences|sequence]] $\left( a_{n} \right)$ of points in a [[Topology|topological space]] $\left( X,\mathcal{T} \right)$ *converges* to $L$ iff
$$\forall A \in \mathcal{N}_{L}, \exists N \in \N: \forall n \ge N, a_{n} \in A;$$
*iff for any neighbourhood $\mathit{A}$ of $\mathit{L}$, eventually the [[Sequences|sequence]] is contained in $\mathit{A}$.*

\[[[Metric Sequence Convergence]]\]

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