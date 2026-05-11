---
tags:
  - atom
  - math
---
A [[Subrings|subring]] $A$ of a [[Rings|ring]] $R$ is a (two-sided) *ideal* iff
$$\forall (a \in A, r \in R), ra \in A \land ar \in A.$$
This is called the **absorbing property**.

> [!theorem]- *(Ideal Test)* A [[Empty Set|non-empty]] [[Subsets|subset]] $A$ of a [[Rings|ring]] $R$ is an *ideal* of $R$ iff<ol><li>$\forall (a,b \in A), a - b \in A$, and</li><li>$\forall (a \in A, r \in R), ra \in A \land ar \in A$.</li></ol>
> $A$ is a [[Subrings|subring]] of $R$, as 1. gives closure under subtraction, and 2. gives closure under multiplication if you restrict $r \in A$. Thus, by the [[Subrings#^subring-test|subring test]], $A$ is a [[Subrings|subring]] of $R$.
> Finally, $A$ is an *ideal* directly by 2.
^ideal-test

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

> [!theorem]- Let $R$ and $S$ be [[Rings|rings]], $\varphi : R \to S$ be a [[Ring Homomorphisms|homomorphism]] between them, and $A$ and $B$ be **[[Ideals|ideals]]** of $R$ and $S$ respectively.<ol><li>if $\varphi$ is [[Surjective Functions|surjective]], $\varphi(A)$ is an [[Ideals|ideal]] of $S$, and</li><li>$\varphi^{-1}(B)$ is an [[Ideals|ideal]] of $R$, and</li></ol>
> 1. Let $a \in A$ and $s \in S$ be given.
>    Since $\varphi$ is [[Surjective Functions|surjective]], $\exists r \in R: s = \varphi(r)$. Thus,
>    $$\begin{align}
> 	\varphi(a) s
> 	&= \varphi(a) \varphi(r) \\
> 	&= \varphi(ar) \\
> 	&\in \varphi(A) && ar \in A. \\
> 	s \varphi(a)
> 	&= \varphi(r) \varphi(a) \\
> 	&= \varphi(ra) \\
> 	&\in \varphi(A) && ra \in A. \\
> \end{align}$$
>    Thus, $\varphi(A)$ is a [[Subrings|subring]] of $S$ ([[Ring Homomorphisms#Properties|as]] $A$ [[Ring Homomorphisms#Properties|is subring of]] $R$) satisfying the [[Ideals|absorbing property]], so $\varphi(A)$ is an [[Ideals|ideal]] of $S$.
> 2. Let $a \in \varphi^{-1}(B)$ and $r \in R$ be given.
>    $$\begin{align}
> 	\varphi(ar)
> 	&= \varphi(a) \times \varphi(r) \\
> 	& \in B && \varphi(a) \in B. \\
> 	\varphi(ra)
> 	&= \varphi(r) \times \varphi(a) \\
> 	& \in B && \varphi(a) \in B
> \end{align}$$
>    Thus, $ar,ra \in \varphi^{-1}(B)$. Then $\varphi^{-1}(B)$ is a [[Subrings|subring]] of $R$ ([[Ring Homomorphisms#Properties|as]] $B$ [[Ring Homomorphisms#Properties|is subring of]] $S$) satisfying the [[Ideals|absorbing property]], so $\varphi^{-1}(B)$ is an [[Ideals|ideal]] of $R$.
^homomorphism-properties

\[[[Ring Cosets]]\]

---

> [!example]- The *ideals* of $\Z$ are $n\Z$.
> $\left( \impliedby \right)$ $n\Z$ are *ideals*.
> Let $n \in \Z$. Thus, let $a \in n\Z$, and $r \in \Z$. There exists $c \in \Z$ such that $a = nc$, so
> $$ar = ra = r(nc) = n(rc) \in n\Z$$
> as $rc \in \Z$.
> 
> $\left( \implies \right)$ *Ideals* are $n\Z$.
> We didn't prove this lol. #TODO
^ideals-of-z-are-nz

> [!example]- $\Z$ is a *non-ideal* [[Subrings|subring]] of $\Q$.
> Let $a = 1 \in \Z$ and $r = 1/2 \in \Q$. Then $ar = 1/2 \notin \Z$.
