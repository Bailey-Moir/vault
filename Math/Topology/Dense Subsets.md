---
tags:
  - atom
  - math
---
$S \subseteq X$ is *dense* iff $\overline{S} = X$[^1]

> [!theorem-1]- $S \subseteq X$ is *dense* iff every non-[[Empty Set|empty]] [[Open Sets|open set]] meets $S$.
> $$\begin{align}
> 	& \overline{S} = X \\
> 	\iff & X \subseteq \overline{S} \\
> 	\iff & \forall p \in X, \forall A \in \mathcal{N}_{p}, S \cap A \ne \emptyset && (1) \\
> 	\iff & \forall A \in \mathcal{T}, \forall p \in A, S \cap A \ne \emptyset \\
> 	\iff & \forall A \in \mathcal{T} \setminus \{ \emptyset \}, S \cap A \ne \emptyset \\
> \end{align}$$
> \[$(1)$ [[Closures]], Characterisation\]

> [!example] $\overline{\Q^n} = \R^n$

[^1]: [[Closures]]