---
tags:
  - atom
  - math
---
Let $F$ be a [[Fields|field]], and $p(x) \in F[x]$ be [[Reduciblity#^negation|irreducible]] over $F$.
If $\alpha$ is a zero of $p(x)$ in some [[Subfields#^extension-field|extension field]] $E$ of $F$, then
$$ F(\alpha) \cong F[x] / \left< p(x) \right>. $$
Further, $1,\alpha,\dots,\alpha^{\deg p(x)-1}$ form a [[Vector Bases|basis]] for $F(\alpha)$ as a [[Vector Spaces|vector space]] over $F$.

> [!proof]-
> Define $\varphi : F[x] \to E$ by
> $$f(x) \mapsto f(\alpha).$$
> This is a [[Ring Homomorphisms|homomorphism]] as it is simple evaluation.
> 
> Since $\varphi(p(x)) = p(\alpha) = 0$,
> $$ \left< p(x) \right> \subseteq \ker \varphi \subseteq F[x]. $$
> But $\left< p(x) \right>$ is a [[Maximal Ideals|maximal ideal]] as $p(x)$ is [[Reduciblity#^negation|irreducible]] over $F$[^1]. Since $\varphi(1) = 1 \ne 0$, meaning $\ker \varphi \ne F[x]$,
> $$ \ker \varphi = \left< p(x) \right>. $$
> By the definition of [[Simple Field Extensions|simple field extensions]],
> $$\begin{align}
> 	& F \subseteq \varphi(F[x]) && \forall a \in F, \varphi(a) = a. \\
> 	& \alpha \in \varphi(F[x]) && \varphi(x) = \alpha \\
> 	\to\quad & F(\alpha) \subseteq \varphi(F[x]). \\
> \end{align}$$
> If $f(x) \in F[x]$, then $f(\alpha) \in F(\alpha)$, so $\varphi(F[x]) \subseteq F(\alpha)$. Together, this gives
> $$ \varphi (F[x]) = F(\alpha). $$
> Thus, by [[First Isomorphism Theorem for Rings|first isomorphism theorem]],
> $$\begin{align}
> 	F[x] / \left< p(x) \right> \cong F(\alpha). && \square_{1}
> \end{align}$$
> 
> From the construction in the proof of [[Kronecker's Theorem|Kronecker's theorem]], #TODO
> $$ F(\alpha) = \left\{ c_{0} + c_{1}\alpha + \dots + c_{n-1}\alpha^{n-1} : c_{0},\dots,c_{n-1} \in F \right\}. $$
> All the remains to be shown is that $1,\alpha,\dots,\alpha^{n-1}$ are [[Linear Independence|linearly independent]]. Suppose
> $$ c_{0} + c_{1}\alpha + \dots + c_{n-1}\alpha^{n-1} = 0. $$
> Thus,
> $$\begin{align}
> 	\varphi(c_{0}+c_{1}x+\dots+c_{n-1}x^{n-1}) &= 0 \\
> 	c_{0}+c_{1}x+\dots+c_{n-1}x^{n-1} &\in \ker \varphi =  \left< p(x) \right>  \\
> 	c_{0}+c_{1}x+\dots+c_{n-1}x^{n-1} &= g(x) p(x) && g(x) \in F[x] \\
> 	c_{0}+c_{1}x+\dots+c_{n-1}x^{n-1} &= 0 && \deg \text{LHS} < \deg p(x) \\
> 	c_{0},\dots,c_{n-1} &= 0.
> \end{align}$$
> Thus, $1,\alpha,\dots,\alpha^{n-1}$ are [[Linear Independence|linearly independent]]. $\quad\square_{2}$

> [!example]- $\Q(\sqrt{ 2 }) = \{ a + b\sqrt{ 2 } : a,b \in \Q \}$.
> Let $p(x) = x^2 - 2 \in \Q[x]$,  an [[Reduciblity#^negation|irreducible polynomial]] by [[Eisenstein's Criterion|Eisenstein's criterion]] with a [[Primes|prime]] of $2$.
> $\sqrt{ 2 }$ is a root of $p(x)$ in $\R[x]$, an [[Subfields|extension field]] of $F$. Thus,
> $$\begin{align}
> 	\Q(\sqrt{ 2 })
> 	&= \left\{ c_{0} + c_{1}\sqrt{ 2 } : a,b \in \Q \right\} \\
> 	&= \left\{ a + b\sqrt{ 2 } : a,b \in \Q \right\}. && \square
> \end{align}$$

> [!corollary]- Let $F$ be a [[Fields|field]], and $p(x) \in F[x]$ be [[Reduciblity#^negation|irreducible]] over $F$. If<ul><li>$\alpha$ is a zero of $p(x)$ in some [[Subfields#^extension-field|extension field]] $E$ of $F$, and</li><li>$\beta$ is a zero of $p(x)$ in some [[Subfields#^extension-field|extension field]] $E'$ of $F$,</li></ul>then $F(\alpha) \cong F(\beta)$.
> Applying the theorem to both zeros gives
> $$ F(\alpha) \cong F[x] / \left< p(x) \right> \cong F(\beta). $$

[^1]: [[Maximal Ideals#^polynomials]]
