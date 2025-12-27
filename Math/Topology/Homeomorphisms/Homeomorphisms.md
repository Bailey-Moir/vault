---
tags:
  - atom
  - math
---
A [[Functions|function]] $\varphi$ between [[Topology|topological spaces]] $X$ and $Y$ is a *homeomorphism* iff it is a [[Bijective Functions|bijection]] and it is [[Continuous Maps|continuous]] in both directions.

> [!note] *Homeomorphisms* are [[Isomorphism|isomorphisms]] in the [[Categories|category]] of [[Topology|topological spaces]].

> [!theorem-1]- For [[Bijective Functions|bijective]] $f : X \to Y$, $f$ is a *homeomorphism* iff $U \in \mathcal{T}_{X} \leftrightarrow f(U) \in \mathcal{T}_{Y}$
> By the [[Bijective Functions|bijectivity]] of $f$,
> $$\begin{align}
> 	& f \in \mathcal{C}_{X}^Y \land f \in \mathcal{C}_{Y}^X  \\
> 	\iff& \left( \forall V \in \mathcal{T}_{Y}, f^{-1}(V) \in \mathcal{T}_{X} \right) \land \left( \forall U \in \mathcal{T}_{X}, f(U) \in \mathcal{T}_{Y} \right) \\
> 	\iff& \left( \forall U \in X, f(U) \in \mathcal{T}_{Y} \to U\in \mathcal{T}_{X} \right) \land \left( \forall U \in \mathcal{T}_{X}, f(U) \in \mathcal{T}_{Y} \right) && \text{Injectivity} \\
> 	\iff& \forall U \in X, \left( f(U) \in \mathcal{T}_{Y} \to U\in \mathcal{T}_{X} \right) \land \left( U \in \mathcal{T}_{X} \to f(U) \in \mathcal{T}_{Y} \right) \\
> 	\iff& \forall U \in X, \left( U \in \mathcal{T}_{X} \leftrightarrow f(U)   \in \mathcal{T}_{Y}\right) \\
> \end{align}$$
> > [!proof-]- Long Version
> > $\left( \implies \right)$
> > Suppose $f$ is a *homeomorphism*.
> > $\left( \leftarrow \right)$
> > If $f(U) \in \mathcal{T}_{Y}$, then by the [[Continuous Maps|continuity]] of $f$, $U = f^{-1}(f(U)) \in \mathcal{T}_{X}$.
> > $\left( \to \right)$
> > If $U \in \mathcal{T}_{X}$, then by the [[Continuous Maps|continuity]] of $f^{-1}$, $f(U) = \left( f^{-1} \right)^{-1}(U) \in \mathcal{T}_{Y}$.
> > 
> > $\left( \impliedby \right)$
> > Suppose $U \in \mathcal{T}_{X} \leftrightarrow f(U) \in \mathcal{T}_{Y}$.
> > 
> > Let $U \in \mathcal{T}_{X}$. Then by the premise, $\left( f^{-1} \right)^{-1}(U) = f(U) \in \mathcal{T}_{Y}$. Thus, $f^{-1}$ (which must exist by the [[Bijective Functions|bijectivity]] of $f$) is [[Continuous Maps|continuous]].
> > 
> > Let $V \in \mathcal{T}_{Y}$, and $U = f^{-1}(V)$. Then $f(U) = f\left( f^{-1}(V) \right) = V \in \mathcal{T}_{Y}$, so by the premise, $f^{-1}(V) = U \in \mathcal{T_{X}}$. Thus, $f$ is [[Continuous Maps|continuous]].