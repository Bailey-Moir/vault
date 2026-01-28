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

>[!theorem-2]- $\mathcal{B} \subseteq \mathcal{P}(X)$ forms a valid [[Topology|topology]] on $X$ as a *basis* iff <ol><li>$\mathcal{B}$ covers $X$ ($\bigcup \mathcal{B} = X$), and</li><li>$\forall B_{1},B_{2} \in \mathcal{B}, \forall p \in B_{1} \cap B_{2}, \exists B \in \mathcal{B} : p \in B \subseteq B_{1} \cap B_{2}$.</li></ol>
> 
> $\left( \implies \right)$
> Let $\left( X,\mathcal{T} \right)$ be a [[Topology|topological space]] with a *basis* $\mathcal{B} \subseteq \mathcal{T}$.
> 1. By the definition of a [[Topology|topology]], $X \in \mathcal{T}$, so by the definition of a *basis*, there exists $\mathcal{C} \subseteq \mathcal{B}$ such that
>    $$\begin{align}
> 	X &= \bigcup \mathcal{C} \subseteq \bigcup \mathcal{B} && \mathcal{C} \subseteq \mathcal{B} \\
> 	X &\supseteq \bigcup \mathcal{B} && \mathcal{B} \subseteq \mathcal{P}(X) \\
> 	\to X &= \bigcup \mathcal{B}
> \end{align}$$
> 2. Let $B_{1},B_{2} \in \mathcal{B}$.
>    Since [[Open Sets|open sets]] are closed under finite [[Unions & Intersections|intersection]], $U = B_{1} \cap B_{2} \in \mathcal{T}$.
>    By \[Theorem 1\], for all $p \in U$, there exists some $B \in \mathcal{B}$ such that $p \in B \subseteq U$.
> 
> $\left( \impliedby \right)$
> Let $\mathcal{B} \subseteq \mathcal{P}(X)$ satisfy properties 1 and 2, and let
> $$\mathcal{T} = \left\{ \bigcup \mathcal{C} : \mathcal{C} \subseteq \mathcal{B} \right\}.$$
> 1. **$\mathbf{\emptyset \in \mathcal{T}}$ and $\mathbf{X \in \mathcal{T}}$.**
>    Let $\mathcal{C} = \emptyset$ since $\emptyset \subseteq \mathcal{B}$. This gives $\cup \emptyset = \emptyset \in \mathcal{T}$.
>    Let $\mathcal{C} = \mathcal{B}$ since $\mathcal{B}\subseteq \mathcal{B}$. By 1, this gives $\cup \mathcal{B}=X\in \mathcal{T}$.
> 2. **$\mathbf{\mathcal{T}}$ is closed under arbitrary [[Unions & Intersections|unions]].**
>    For all $\alpha \in I$ (for some [[Indexing Set|indexing set]] $I$), let $U_{\alpha} \in \mathcal{T}$. We need to show that
>    $$\bigcup_{\alpha \in I} U_{\alpha} \in \mathcal{T}$$
>    By the definition of $\mathcal{T}$, for each $U_{\alpha}$, there exists some $\mathcal{C}_{\alpha} \subseteq \mathcal{B}$ such that $U_{\alpha} = \bigcup \mathcal{C}_{\alpha}$. Thus,
>    $$\bigcup_{\alpha \in I} U_{\alpha} = \bigcup_{\alpha \in I} \left( \bigcup \mathcal{C_{\alpha}} \right) = \bigcup \left( \bigcup_{\alpha \in I} \mathcal{C_{\alpha}} \right) \in \mathcal{T},$$
>    as $\displaystyle \bigcup_{\alpha \in I} \mathcal{C_{\alpha}} \subseteq \mathcal{B}$.
> 3. **$\mathbf{\mathcal{T}}$ is closed under finite [[Unions & Intersections|intersections]].**
>    Let $U,V \in \mathcal{T}$. By the definition of $\mathcal{T}$, there exists $\mathcal{C}_{1},\mathcal{C}_{2} \subseteq \mathcal{B}$ such that $U = \cup \mathcal{C}_{1}$ and $V = \cup \mathcal{C}_{2}$. 
>    $$U \cap V = \left( \bigcup \mathcal{C}_{1} \right) \cap \left( \bigcup \mathcal{C}_{2} \right) = \bigcup \{ B_{1} \cap B_{2} : B_{1} \in \mathcal{C}_{1}, B_{2} \in \mathcal{C}_{2} \}$$
>    We need to show that $U \cap V \in \mathcal{T}$, and then the rest is given by [[Induction|induction]]. From above, since $\mathcal{T}$ has already been shown to be closed under arbitrary [[Unions & Intersections|unions]], all that remains to be shown is that: for any fixed $B_{1}, B_{2} \in \mathcal{B}$, $B \cap B \in \mathcal{T}$.
> 
>    If $B_{1} \cap B_{2}$ is non-[[Empty Set|empty]], then by 2, for any $p \in B_{1} \cap B_{2}$, there exists a *basis* element $B_{p} \in \mathcal{B}$ such that $p \in B_{p} \subseteq B_{1} \cap B_{2}$. Thus,
>    $$B_{1} \cap B_{2} \subseteq \bigcup_{p \in B_{1} \cap B_{2}} B_{p} \subseteq B_{1} \cap B_{2},$$
>    so
>    
>    $$B_{1} \cap B_{2} = \bigcup_{p \in B_{1} \cap B_{2}} B_{p} \in \mathcal{T}.$$
>    If $B_{1} \cap B_{2}$ is [[Empty Set|empty]], then $B_{1} \cap B_{2} = \emptyset \in \mathcal{T}$.