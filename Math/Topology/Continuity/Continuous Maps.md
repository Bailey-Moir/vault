---
tags:
  - atom
  - math
---
A [[Functions|function]] between two [[Topology|topological spaces]] $f:X\to Y$ is *continuous* iff for any [[Open Sets|open]] $V \subseteq Y$, the [[Range & Image|pre-image]] $f^{-1}(V)$ is [[Open Sets|open]];
$$\forall V \in \mathcal{T}_{Y}, f^{-1}(V) \in \mathcal{T}_{X}.$$
\[[[Continuity]]\]

> [!notation] In these notes, we will denote the [[Sets|set]] of *continuous maps* from [[Topology|topological spaces]] $X$ to $Y$ as $\mathcal{C}_{X}^Y$

> [!theorem-1]- This is [[Logical Equivalence|logically equivalent]] to "for any **[[Closed Sets|closed]]** $V \subseteq Y$, the [[Range & Image|pre-image]] $f^{-1}(V)$ is [[Closed Sets|closed]]."
> $$\begin{align}
> 	&\forall V^c \in \mathcal{T}_{Y}, f^{-1}(V)^c \in \mathcal{T}_{X}  \\
> 	\iff &\forall V^c \in \mathcal{T}_{Y}, f^{-1}(V^c) \in \mathcal{T}_{X} && (1)  \\
> 	\iff &\forall V \in \mathcal{T}_{Y}, f^{-1}(V) \in \mathcal{T}_{X}  \\
> \end{align}$$
> \[$(1)$ [[Injective Functions#Properties of Injections]]\]

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