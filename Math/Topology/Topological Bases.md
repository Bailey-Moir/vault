---
tags:
  - atom
  - math
---
In a [[Topology|topological space]] $\left( X,\mathcal{T} \right)$, a [[Collections|collection]] $\mathcal{B} \subseteq \mathcal{T}$ is called a *basis* on $X$ iff every [[Open Sets|open set]] in the space is a [[Unions & Intersections|union]] of elements of $\mathcal{B}$;
$$\begin{align}
	& \forall A \in \mathcal{T}, \exists \mathcal{C} \subseteq \mathcal{B} : A = \bigcup \mathcal{C} \\
	{\textcolor{gray}\iff} & \mathcal{T} = \left\{ \bigcup \mathcal{C} : \mathcal{C} \subseteq \mathcal{B} \right\}
\end{align}$$

> [!theorem-1]- $S \in \mathcal{T}$ iff $\forall p \in S, \exists B \in \mathcal{B} : p \in B \subseteq S$.
> $$\begin{align}
> 	& S \in \mathcal{T} \\
> 	\iff & S = \text{int}\,S && (1) \\
> 	\iff & \forall p \in S, \exists A \in \mathcal{N}_{p} : A \subseteq S && (2) \\
> 	\iff & \forall p \in S, \exists \mathcal{C} \subseteq \mathcal{B} : p \in \bigcup \mathcal{C} \subseteq S \\
> 	\iff & \forall p \in S, \exists B \in \mathcal{B} :  p \in B \subseteq S. \\
> \end{align}$$
> \[$(1)$ [[Interiors]], Theorem 1, $(2)$ [[Interiors]], Characterisation\]

> [!theorem-2]- $f : X \to Y$ is [[Continuous Maps|continuous]] iff $\forall B \in \mathcal{B}_{Y}, f^{-1}(B) \in \mathcal{T}_{X}$.
> $$\begin{align}
> 	& \forall V \in \mathcal{T}_{Y}, f^{-1}(V) \in \mathcal{T}_{X} \\
> 	\iff & \forall \mathcal{C} \subseteq \mathcal{B}_{Y}, f^{-1}\left( \bigcup \mathcal{C} \right) \in \mathcal{T}_{X} \\
> 	\iff & \forall \mathcal{C} \subseteq \mathcal{B}_{Y}, \bigcup_{B \in \mathcal{C}} f^{-1}\left(  B \right) \in \mathcal{T}_{X} \\
> 	\iff & \forall B \in \mathcal{B}_{Y},  f^{-1}\left(  B \right) \in \mathcal{T}_{X}. && (1) \\
> \end{align}$$
> > $(1)$
> > $\left( \implies \right)$
> > For all $B \in \mathcal{B}$, letting $\mathcal{C} = \{ B \}$ in the premise gives the conclusion.
> > 
> > $\left( \impliedby \right)$
> > This follows directly from the fact that [[Open Sets|open sets]] are closed under arbitrary [[Unions & Intersections|unions]].

> [!theorem-3]- A [[Sequences|sequence]] $\left( a_{n} \right)$ of points *converges* to $L$ iff $\forall B \in \mathcal{B} \cap \mathcal{N}_{L}, \exists N \in \N: \forall n \ge N, a_{n} \in B$.
> $\left( \implies \right)$
> Restricting $A$ in the definition of [[Sequence Convergence|sequence convergence]] to be a *basis element* $B \in \mathcal{B}$ gives the concluision directly.
> 
> $\left( \impliedby \right)$
Let $A \in \mathcal{N}_L$. By definition, there must exist $\mathcal{C} \subseteq \mathcal{B}$ such that $A =\bigcup \mathcal{C}$.
> 
> Since $A$ is a [[Neighbourhoods|neighbourhood]] of $L$, there must exist some $B \in \mathcal{C}$ that is a [[Neighbourhoods|neighbourhood]] of $L$.
> 
> Thus by the premise, there exists $N \in\N$ such that for all $n \ge N$, $a_n \in B \subseteq A$. $\square$

--- 

1. $\mathcal{B}$ covers $X$ ($\forall x \in X, \exists B \in \mathcal{B} : x \in B$)
2. $\forall B_{1},B_{2} \in \mathcal{B}, \forall x \in B_{1} \cap B_{2}, \exists B \in \mathcal{B} : x \in B \subseteq B_{1} \cap B_{2}$.

> [!definition] The **topology generated** by $\mathcal{B}$ is
> $$\large \mathcal{T}_{\mathcal{B}} = \left\{ \cup \mathcal{C} : \mathcal{C} \subseteq \mathcal{B} \right\}$$

> [!proof]- The **topology generated** by a *basis* $\mathcal{B}$ of $X$ is a [[Topology|topology]] of $X$.
> 1. **$\mathbf{\emptyset \in \mathcal{T}_{\mathcal{B}}}$ and $\mathbf{X \in \mathcal{T}_{\mathcal{B}}}$.**
>    Let $\mathcal{C} = \emptyset$. Since $\emptyset \subseteq \mathcal{B}$, $\cup \emptyset = \emptyset \in \mathcal{T}_{\mathcal{B}}$.
>    Let $\mathcal{C} = \mathcal{B}$. By the axiom that $\mathcal{B}$ covers $X$, since $\mathcal{B} \subseteq \mathcal{B}$, $\cup \mathcal{B}=X\in \mathcal{T}_{\mathcal{B}}$.
> 2. **$\mathbf{\mathcal{T}_{\mathcal{B}}}$ is closed under [[Unions & Intersections|unions]].**
>    For all $\alpha \in I$ (for some [[Indexing Set|indexing set]] $I$), let $V_{\alpha} \in \mathcal{T}_{\mathcal{B}}$. We need to show that
>    $$\bigcup_{\alpha \in I} V_{\alpha} \in \mathcal{T}_{\mathcal{B}}$$
>    By the definition of $\mathcal{T}_{\mathcal{B}}$, for each $V_{\alpha}$, there exists some $\mathcal{C}_{\alpha} \subseteq \mathcal{B}$ such that $V_{\alpha} = \cup \mathcal{C}_{\alpha}$. Thus,
>    $$\bigcup_{\alpha \in I} V_{\alpha} = \bigcup_{\alpha \in I} \left( \bigcup \mathcal{C_{\alpha}} \right) = \bigcup \left( \bigcup_{\alpha \in I} \mathcal{C_{\alpha}} \right) \in \mathcal{T}_{\mathcal{B}},$$
>    as $\bigcup_{\alpha \in I} \mathcal{C_{\alpha}} \subseteq \mathcal{B}$.
> 3. **$\mathbf{\mathcal{T}_{\mathcal{B}}}$ is closed under finite [[Unions & Intersections|intersections]].**
>    Let $U,V \in \mathcal{T}_{\mathcal{B}}$. By the definition of $\mathcal{T_{\alpha}}$, there exists $\mathcal{A},\mathcal{C} \subseteq \mathcal{B}$ such that $U = \cup \mathcal{A}$ and $V = \cup \mathcal{C}$. 
>    $$U \cap V = \left( \bigcup \mathcal{A} \right) \cap \left( \bigcup \mathcal{C} \right) = \bigcup \{ A \cap C : A \in \mathcal{A}, C \in \mathcal{C} \}$$
>    We need to show that $U \cap V \in \mathcal{T}_{\mathcal{B}}$, and then the rest is shown by [[Induction|induction]]. From above, by 2, all that remains to be shown is that: for any fixed $A, C \in \mathcal{B}$, $A \cap C \in \mathcal{T_{B}}$.
> 
>    If $A \cap C$ is non-[[Empty Set|empty]], then for any $x \in A \cap C$, there exists a *basis* element $B_{x} \in \mathcal{B}$ such that $x \in B_{x} \subseteq A \cap C$. Thus,
>    $$A \cap C \subseteq \bigcup_{x \in A \cap C} B_{x} \subseteq A \cap C,$$
>    so
>    $$A \cap C = \bigcup_{x \in A \cap C} B_{x} \in \mathcal{T}_{\mathcal{B}}.$$
>    If $A \cap C$ is [[Empty Set|empty]], then $A \cap C \in \mathcal{T}_{\mathcal{B}}$ by 1.