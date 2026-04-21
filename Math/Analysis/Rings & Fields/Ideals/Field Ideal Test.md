---
tags:
  - atom
  - math
---
A [[Groups#^abelian-groups|commutative]] [[Rings|ring]] with [[Rings#^unity|unity]] $R$ is a [[Fields|field]] iff it has no proper non-trivial [[Ideals|ideals]] (i.e. [[Ideals|ideals]] other than $\{ 0 \}$ and $R$).

> [!proof]-
> $\left( \implies \right)$
> Let $I$ be an [[Ideals|ideal]] of a [[Fields|field]] $R$, where $I \ne \left< 0 \right> = \{ 0 \}$.
> 
> Then there exists $a \ne 0 \in I$. Let $r \in R$ be given. Then
> $$a\left( a^{-1}r \right) = r,$$
> so by the [[Ideals|absorbing property of ideals]], since $a^{-1}r \in R$ by $R$ being a [[Fields|field]], $r \in A$.
> 
> Thus, $R \subseteq I$, but $I \subseteq R$, meaning $I = R$, giving that all [[Ideals|ideals]] of $R$ are $\{ 0 \}$ or $R$.
> 
> $\left( \impliedby \right)$
> Let $R$ be a [[Groups#^abelian-groups|commutative]] [[Rings|ring]] with [[Rings#^unity|unity]] that's not a [[Fields|field]] (i.e. it has non-[[Rings#^unit|unit]] elements).
> 
> Let $a \ne 0$ be a non-[[Rings#^unit|unit]] of $R$. Then by definition,
> $$\forall r \in R, ra \ne 1.$$
> Thus, $1\notin \left< a \right> = Ra$, so $\left< a \right> \ne \{ 0 \}$ and $\left< a \right> \ne R$.
> 
> The implication is then proven by [[Proof by Contraposition|contraposition]], as given a [[Groups#^abelian-groups|commutative]] [[Rings|ring]] with [[Rings#^unity|unity]], if its not [[Fields|field]], then it has a proper non-trivial [[Ideals|ideal]] ($\left< a \right>$).

> [!corollary]- If [[Ring Homomorphisms|homomorphism]] $\varphi : \F \to S$ maps from a [[Fields|field]] $\F$ to a [[Rings|ring]] $S$, then$$\ker \varphi \in \{ \F , \{ 0 \} \},$$i.e. it is either the zero map, or it is [[Injective Functions|injective]].
> The only [[Ideals|ideals]] of $\F$ are $\{ 0 \}$ and $\F$ itself, so since [[Ideals#^kernels-are-ideals|kernels are ideals]],  these give the possible kernels.
> 
> If $\ker \varphi = \{ 0 \}$, by [[Math/Analysis/Rings & Fields/Kernels#^injectivity|this theorem]], $\varphi$ is [[Injective Functions|injective]].
> If $\ker \varphi = \F = \text{dom}\, \varphi$, $\varphi$ maps every element to zero, so $\varphi$ is the zero map.