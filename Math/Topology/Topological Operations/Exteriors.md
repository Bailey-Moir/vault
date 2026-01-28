---
tags:
  - atom
  - math
---
The *exterior* of $S\subseteq X$ is the [[Complement|complement]] of its [[Closures|closure]]:
$$\begin{align}
	\text{ext}\,S &= \bar{S}^c.
\end{align}$$
- $\text{ext}\,S \in \mathcal{T}$[^1]

> [!characterisation]- $p \in \text{ext}\,S \iff \exists A \in \mathcal{N}_{p} : S \cap A = \emptyset$ ($A \subseteq S^c$)
> This is given directly through the [[Converse, Inverse, and Contrapositive|contrapositives]] of the [[Closures#^characterisation|characterisation of closures]]. $\square$
^characterisation

> [!theorem-1]- $\text{ext}\,S = \text{int}\,S^c$[^2]
> $$\begin{align}
> 	p \in \ext S &\iff \exists A \in \mathcal{N}_p : S \cap A = \emptyset \\
> 	&\iff \exists A \in \mathcal{N}_p : A \subseteq S^c \\
> 	&\iff p \in \inte S^c && (1)
> \end{align}$$
> where (1) is by the [[Interiors#^characterisation|characterisation of interiors]]. $\square$
^interior-of-complement

[^1]: [[Open Sets]]
[^2]: [[Interiors]]
[^3]: [[Closures]], Theorem 1