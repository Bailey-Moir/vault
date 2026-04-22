---
tags:
  - atom
  - math
---
A [[Subsets|proper]] [[Ideals|ideal]] $A$ of a [[Rings|ring]] R is a *maximal ideal* iff there is no [[Ideals|ideal]] $B$ of $R$ s.t.
$$A \subset B \subset R.$$

> [!lemma]- There is a [[Bijective Functions|bijection]] between the [[Ideals|ideals]] of $R$ containin $A$, and the [[Ideals|ideals]] of $R /A$.
> Let $\varphi : R \to R /A$ be the [[Ring Homomorphisms|homomorphism]] defined by
> $$\varphi(r) = r + A.$$
> This is a [[Ring Homomorphisms|homomorphism]] directly by the definition of the [[Quotient Rings|quotient ring operations]].
> 
> Let $\mathcal{I}_{R}$ denote the [[Ideals|ideals]] of $R$ containin $A$, and $\mathcal{I}_{R /A}$ denote the [[Ideals|ideals]] of $R /A$.
> 
> Let $\Phi : \mathcal{I}_{R} \to \mathcal{I}_{R /A}$ be defined by
> $$\Phi(I) = \varphi(I),$$
> which is an [[Ideals|ideal]] by [[Ideals#^homomorphism-properties|this theorem]] as $\varphi$ is obviously [[Surjective Functions|surjective]]. Similarly, let $\Psi : \mathcal{I}_{R /A} \to \mathcal{I}_{R}$ be defined by
> $$\Psi(J) = \varphi^{-1}(J),$$
> which is an [[Ideals|ideal]] by [[Ideals#^homomorphism-properties|this same theorem]], and these [[Ideals|ideals]] contain $A$ as $0 \in J$, so $A = \ker \varphi = \varphi^{-1}(0)\subseteq \varphi^{-1}(J)$.
> 
> $$\begin{align}
> 	\Psi(\Phi(I))
> 	&= \Psi(\varphi(I)) \\
> 	&= \varphi^{-1}(\varphi(I)) \\
> 	&= \{ x \in R : \varphi(x) \in \varphi(I) \} \\
> 	&= \{ x \in R : \exists a \in I : \varphi(x) = \varphi(a) \} \\
> 	&= \{\phantom{ x \in R : \exists a \in I}\hspace{-3em}"\!\!\!\hspace{3em} : \varphi(x - a) = 0\} \\
> 	&= \{\phantom{ x \in R : \exists a \in I}\hspace{-3em}"\!\!\!\hspace{3em} : x - a \in A \subseteq I \} && \ker \varphi = A \\
> 	&= \{ x \in R : x  \in I \} && x-a \in I \land a \in I \\
> 	&= I \\
> \end{align}$$
> $$\begin{align}
> 	\Phi(\Psi(J))
> 	&= \Phi(\varphi^{-1}(J)) \\
> 	&= \varphi(\varphi^{-1}(I)) \\
> 	&= I && \varphi \text{ is surjective} \\
> \end{align}$$
> Thus, $\Phi$ and $\Psi$ are each others [[Inverse Functions|inverse]], meaning they are both [[Bijective Functions|bijections]].
^lemma

> [!theorem]- Let $R$ be a [[Groups#^abelian-groups|commutative]] [[Rings|ring]] with [[Rings#^unity|unity]], and $A$ be a [[Subsets|proper]] [[Ideals|ideal]] of $R$.<center>$R/A$ is a [[Fields|field]] $\iff$ $A$ is a *maximal ideal* of $R$</center>
> $R/A$ inherits the structure of a [[Groups#^abelian-groups|commutative]] [[Rings|ring]] with [[Rings#^unity|unity]] from $R$.
>
> Using the notation of [[#^lemma|the lemma]], by the [[Field Ideal Test|field ideal test]],
> $\,$<div style="width: max-content; margin: auto; margin-top: -3em">
> $R / A$ is a [[Fields|field]] $\iff$ $R / A$ has no [[Subsets|proper]] non-trivial [[Ideals|ideal]].
> <span style="color:rgba(0,0,0,0) !important;">$R / A$ is a field</span> $\iff$ $\mathcal{I}_{R / A} = \{ R / A, \{ 0 \} \}$
> <span style="color:rgba(0,0,0,0) !important;">$R / A$ is a field</span> $\iff$ $\mathcal{I}_{R} = \{ R, A \}$
> <span style="color:rgba(0,0,0,0) !important;">$R / A$ is a field</span> $\iff$ $A$ is a *maximal ideal* of $R$.
> </div>


\[[[Quotient Rings]]\]