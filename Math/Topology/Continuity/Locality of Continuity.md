---
tags:
  - atom
  - math
---
$$f \in \mathcal{C}_{X}^Y \iff \forall p \in X, \exists U \in \mathcal{N}_{p} : f\bigr|_{U} \in \mathcal{C}_{U}^Y$$
> [!proof]-
> $\left( \implies \right)$
> For all $f \in \mathcal{C}_{X}^Y$ and $p \in X$, let $U = X$. Obviously $X \in \mathcal{N}_{p}$, and $f\bigr|_{X} = f \in \mathcal{C}_{X}^Y$. $\square$
> 
> $\left( \impliedby \right)$
> Let $V \in \mathcal{T}_{Y}$ and $p \in f^{-1}(V)$. By the premise, there exists $U \in \mathcal{N}_{p}$ such that $f\bigr|_{U} \in \mathcal{C}_{U}^Y$. Note
> $$ f^{-1}\bigr|_{U}(V) {\color{gray}= U \cap f^{-1}(V)} \subseteq f^{-1}(V). $$
> By the [[Continuous Maps|continuity]] of $f\bigr|_{U}$, $f^{-1}\bigr|_{U}(V)$ is a [[Open Sets|open]] [[Subsets|subset]] of $f^{-1}(V)$ containing $p$. Thus, by the [[Interiors|characterisation of interiors]], $p \in \text{int}\left( f^{-1}(V) \right)$.
> 
> Thus, for all $p$ in the [[Range & Image|preimage]], $p$ is in the [[Interiors|interior]] of the [[Range & Image|preimage]], so by \[[[Interiors]], Theorem 1\], $f^{-1}(V) \in \mathcal{T}_{X}$. $\square$