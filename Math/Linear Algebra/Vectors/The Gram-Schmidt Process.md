---
tags:
  - atom
  - math
  - linear
---
Let $\vecbf{u}_{1},\dots,\vecbf{u}_{k}$ be a [[Vector Bases|basis]] for a [[Subspaces|subspace]] $U \in V$, and define the following
$$\begin{array}{lcll}
	\vecbf{v}_{1} = \vecbf{u}_{1} && U_{1} = \text{span}\{ \vecbf{u}_{1} \}  \\
	&& \phantom{U_{1}} =  \text{span}\{ \vecbf{v}_{1} \}\\
	\vecbf{v}_{2} = \text{perp}_{U_{1}}\vecbf{u}_{2} && U_{2} = \text{span}\{ \vecbf{u}_{1}, \vecbf{u}_{2} \}\\
	\phantom{\vecbf{v}_{2}}= \vecbf{u}_{2} - \text{proj}_{U_{1}}\vecbf{u}_{2} && \phantom{U_{2}} =  \text{span}\{ \vecbf{v}_{1}, \vecbf{v}_{2} \}\\
	\vecbf{v}_{3} = \text{perp}_{U_{2}}\vecbf{u}_{3} && U_{3} = \text{span}\{ \vecbf{u}_{1}, \vecbf{u}_{2}, \vecbf{u}_{3} \} \\
	\phantom{\vecbf{v}_{3}}= \vecbf{u}_{3} - \text{proj}_{U_{2}}\vecbf{u}_{3} && \phantom{U_{3}} =  \text{span}\{ \vecbf{v}_{1}, \vecbf{v}_{2}, \vecbf{v}_{3} \}\\
	\phantom{\vecbf{v}_{3}}\hspace{0.5em}\vdots && \phantom{\vecbf{U}_{3}}\hspace{0.3em}\vdots \\
	\vecbf{v}_{k} = \text{perp}_{U_{k-1}}\vecbf{u}_{k} && U_{k} = \text{span}\{ \vecbf{u}_{1}, \dots, \vecbf{u}_{k} \} \\
	\phantom{\vecbf{v}_{k}}= \vecbf{u}_{k} - \text{proj}_{U_{k-1}}\vecbf{u}_{k} && \phantom{U_{k}} =  \text{span}\{ \vecbf{v}_{1}, \dots, \vecbf{v}_{k} \}\\
\end{array}$$
Then $\vecbf{v}_{1},\dots,\vecbf{v}_{k}$ is an [[Orthogonal Vectors|orthogonal]] [[Vector Bases|basis]] for $U$.

\[[[Orthogonal Projection]], [[Vector Projection]]\]

> [!proof]-
> **Base Case**
If $l = 1$, then $\vecbf{v}_{1} = \vecbf{u}_{1}$ is an [[Orthogonal Vectors|orthogonal]] [[Vector Bases|basis]] for $U_{1} =\text{span}(\vecbf{u}_{1})$.
> 
> **Induction Step**
> Suppose $l \in \{ 2,\dots,k \}$, and $\vecbf{v}_{1},\dots,\vecbf{v}_{l-1}$ is an [[Orthogonal Vectors|orthogonal]] [[Vector Bases|basis]] for $U_{l-1}$.
> $$\begin{align}
> 	\vecbf{v}_l = \vecbf{u}_{l} - \text{proj}_{W_{l-1}}(\vecbf{u}_{l}),
> \end{align}$$
> so, by the definition of [[Orthogonal Projection|orthogonal projection]], $\vecbf{v}_{1},\dots,\vecbf{v}_{l}$ is [[Orthogonal Vectors|orthogonal]].
> 
> This implies that $\vecbf{v}_{l} \notin W_{l-1}$, meaning by the [[Linear Dependence Lemma|linear dependence lemma]], $\vecbf{v}_{1},\dots,\vecbf{v}_{l}$ is [[Linear Independence|linearly independent]].
> 
> \[We didn't prove the [[Span|span]]\]