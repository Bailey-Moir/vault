---
tags:
  - atom
  - math
---
A [[Functions|function]] between two [[Topology|topological spaces]] $f:X\to Y$ is *continuous* iff for any [[Open Sets|open]] $V \subseteq Y$, the [[Range & Image|pre-image]] $f^{-1}(V)$ is [[Open Sets|open]];
$$\begin{align}
& \forall V \in \mathcal{T}_{Y}, f^{-1}(V) \in \mathcal{T}_{X} \\
	{\textcolor{gray}\iff} & \forall B \in \mathcal{B}_{Y}, f^{-1}(B) \in \mathcal{T}_{X} && (1) \\
	{\textcolor{gray}\iff} & \forall V^c \in \mathcal{T}_{Y}, f^{-1}(V)^c \in \mathcal{T}_{X} && (2)
\end{align}$$
> [!notation] In these notes, we will denote the [[Sets|set]] of *continuous maps* from [[Topology|topological spaces]] $X$ to $Y$ as $\mathcal{C}_{X}^Y$

> [!proof]- $(1)$
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
>
> \[[[Topological Bases]]\]

> [!proof]- $\left( 2 \right)$
> $$\begin{align}
> 	&\forall V \in \mathcal{T}_{Y}, f^{-1}(V) \in \mathcal{T}_{X}  \\
> 	\iff &\forall V^c \in \mathcal{T}_{Y}, f^{-1}(V^c) \in \mathcal{T}_{X} && (1)  \\
> 	\iff &\forall V^c \in \mathcal{T}_{Y}, f^{-1}(V)^c \in \mathcal{T}_{X}  \\
> \end{align}$$
> \[$(1)$ [[Bijective Functions#Properties of Bijections]]\]

\[[[Continuity]]\]
# Examples
> [!example]- Constants [[Functions|functions]] are *continuous*
> Let $f : X\to Y$ be any constant [[Functions|function]] between [[Topology|topological spaces]], meaning $f(x) = c$ for some $c \in Y$.
> 
> For any $V \in \mathcal{T}_{Y}$, there are only two cases.
> - **Case** $c \in V$
>   Then $f^{-1}(V) = X$, which is axiomatically defined to be [[Open Sets|open]].
> - **Case** $c \notin V$
>   Then $f^{-1}(V) = \emptyset$, which is also axiomatically defined to be [[Open Sets|open]].
> 
> $\square$

> [!example]- Identity maps are *continuous*
> Let $f : X\to X$ be any identity [[Operators|operator]] on [[Topology|topological space]], meaning $f(x) = x$.
> 
> For any $V \in \mathcal{T}$, $f^{-1}(V) = V \in \mathcal{T}$.