---
tags:
  - atom
  - math
---
A [[Subrings|subring]] $A$ of a [[Rings|ring]] $R$ is a (two-sided) *ideal* iff
$$\forall a \in A, \forall r \in R, ra \in A \land ar \in A.$$
This is called the **absorbing property**.

> [!theorem]- [[Ring Cosets|Cosets]] of *ideals* are [[Subrings|subrings]].
> This is given directly by [[Ring Cosets#^subring|this theorem]].
^subrings

> [!theorem]- The [[Math/Analysis/Rings & Fields/Kernels|kernels]] of [[Ring Homomorphisms|homomorphisms]] are *ideals*.
> Let $\varphi : R \to S$ be a [[Ring Homomorphisms|homomorphism]]. $A = \ker \varphi$ is a [[Subrings|subring]] by [[Math/Analysis/Rings & Fields/Kernels#^subring|this theorem]].
> 
> Let $a \in \ker \varphi$ and $r \in R$.
> $$\begin{align}
> 	\varphi(ar) &= \varphi(a) \times \varphi(r) \\
> 	&= 0 \times \varphi(r) \\
> 	&= 0 \\
> 	\to ar &\in \ker \varphi. && \square \\
> \end{align}$$
^kernels-are-ideals

> [!example]- The *ideals* of $\Z$ are $n\Z$.
> $\left( \impliedby \right)$ $n\Z$ are *ideals*.
> Let $n \in \Z$. Thus, let $a \in n\Z$, and $r \in \Z$. There exists $c \in \Z$ such that $a = nc$, so
> $$ar = ra = r(nc) = n(rc) \in n\Z$$
> as $rc \in \Z$.
> 
> $\left( \implies \right)$ *Ideals* are $n\Z$.
> We didn't prove this lol. #TODO

> [!example]- $\Z$ is a *non-ideal* [[Subrings|subring]] of $\Q$.
> Let $a = 1 \in \Z$ and $r = 1/2 \in \Q$. Then $ar = 1/2 \notin \Z$.