---
tags:
  - atom
  - comp
---
Let $t(M,x)$ be the (maximum) number of steps the ([[Non-Deterministic Turing Machines|N]])[[Turing Machines|TM]] $M$ takes on an input $x$ before halting.

> [!definition]- $T : \N^\N \to \Sigma^*$
> For a [[Functions|function]] $f: \N \to \N$, the [[Sets|set]] of [[Languages|languages]] $T(f)$ is defined by
> $$T(f) = \{ A \subseteq \Sigma^* : \exists M \in \textbf{TMs} : A = L(M) \land \forall x \in \Sigma^*, t(M,x) \le f(\left| x \right| ) \},$$
> giving the [[Sets|set]] of [[Languages|languages]] that can always be solved **deterministically** in a number of steps bounded by $f$.

> [!definition]- $NT : \N^\N \to \Sigma^*$
> For a [[Functions|function]] $f: \N \to \N$, the [[Sets|set]] of [[Languages|languages]] $NT(f)$ is defined by
> $$NT(f) = \{ A \subseteq \Sigma^* : \exists M \in \textbf{NTMs} : A = L(M) \land \forall x \in \Sigma^*, t(M,x) \le f(\left| x \right| ) \}.$$
> giving the [[Sets|set]] of [[Languages|languages]] that can always be solved **non-deterministically** in a number of steps bounded by $f$.

$$\begin{array}{ccc}
	\displaystyle\mathbf{P} = \bigcup_{p \in \mathcal{P}}T(p) \hspace{2em} &
	\displaystyle\mathbf{NP} = \bigcup_{p \in \mathcal{P}}NT(p) \hspace{2em} &
	(1)
\end{array}$$

> [!note]  $T$ and $NT$ are very similar to [[Asymptotic Notation#$O$|Big O]], except
> - they give a set of [[Languages|languages]], not [[Functions|functions]], and
> - they apply for all $x$, and thus are not about asymptotic behaviour.

> [!note]- It is known that $\mathbf{P} \subseteq \mathbf{NP}$, but it is not known if $\mathbf{P} = \mathbf{NP}$.
> If any [[NP-complete|NP-complete]] problem was in $\mathbf{P}$, then it would follow that $\mathbf{P} = \mathbf{NP}$.

> [!intuitive definition]- of $\textbf{NP}$
> $\textbf{NP}$ is the [[Sets|set]] of all decision problems where answers can be verified in polynomial time. 

> [!examples] of $\textbf{NP}$ problems
> - Is a given [[Graphs|graph]] [[Hamiltonian Cycles and Graphs|Hamiltonian]]?
> - Given $A \subset \N$ and $b \in \N$, is there a [[Subsets|subset]] $X \subseteq A$ such that $\sum X = b$?
> - Can $A \subset \N$ be [[Partitions|partitioned]] into $\mathcal{C_{1}},\mathcal{C}_{2}$ such that $\sum\mathcal{C}_{1} =\sum\mathcal{C}_{2}$.
> - Is a logical formula – with boolean variables and operations and, or, not – [[Satisfiability|satisfiable]]?


\[$(1)$ [[Polynomials]]\]