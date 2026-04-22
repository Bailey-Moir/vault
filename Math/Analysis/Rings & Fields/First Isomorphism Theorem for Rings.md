---
tags:
  - atom
  - math
---
Let $\varphi : R \to S$ be a [[Ring Homomorphisms|homomorphism]] between [[Rings|rings]] $R$ and $S$. Then the mapping $\tilde{\varphi} : R/\hspace{-.1em}\ker{\varphi} \to \varphi(R)$ given by
$$r + \ker \varphi \mapsto \varphi(r)$$
is an [[Isomorphisms|isomorphism]]; $R/\hspace{-.1em}\ker{\varphi} \overset{\tilde{\varphi}}\cong\ \varphi(R)$.

> [!proof]-
> **[[Functions|Well-Defined]]**
> If $r + \ker \varphi = r' + \ker \varphi$, then by [[Ring Cosets#^equality|this theorem]], $r - r' \in \ker \varphi$, so
> $$\begin{align}
> 	\varphi(r - r') &= 0 \\
> 	\varphi(r) - \varphi(r') &= 0 \\
> 	\varphi(r) &=  \varphi(r'). \\
> \end{align}$$
> Thus,
> $$\tilde{\varphi}(r + \ker\varphi) = \varphi(r) = \varphi(r') = \tilde{\varphi}(r' + \ker \varphi)$$
> 
> **[[Ring Homomorphisms|Homomorphism]]**
> For $*$ as $\times$ or $+$,
> $$\begin{align}
> 	\tilde{\varphi}(\left( r + \ker \varphi \right) * \left( r' + \ker \varphi \right))
> 	&= \tilde{\varphi}(r * r' + \ker \varphi) \\
> 	&= \varphi(r * r') \\
> 	&= \varphi(r) * \varphi(r') \\
> 	&= \tilde{\varphi}(r + \ker \varphi) * \tilde{\varphi}(r' + \ker \varphi). \\
> \end{align}$$
> **[[Bijective Functions|Bijection]]**
> Given $s \in \varphi(R)$, there exists $r \in R$ such that $\varphi(r) = S$. Thus,
> $$\tilde{\varphi}(r + \ker\varphi) = \varphi(r) = s.$$
> 
> If $\tilde{\varphi}(r + \ker\varphi) = 0$, then $\varphi(r) = 0$, so $r \in \ker \varphi$, and so $r + \ker\varphi = 0 + \ker \varphi$. Thus, by [[Math/Analysis/Rings & Fields/Kernels#^injectivity|this theorem]], $\tilde{\varphi}$ is [[Injective Functions|injective]].

> [!example]- $\R[x] / \left< x^2+1 \right> \cong \C$
> Consider the evaluation [[Ring Homomorphisms|homomorphism]] $\varphi : \R[x] \to \C$ defined by
> $$f(x) \mapsto f(i).$$
> 
> Let $f \in \ker \varphi$. By the [[Division Algorithm|division algorithm]], there exists $q,r \in \R[x]$
> $$f(x) = q(x)(x^2 + 1) + r(x),$$
> where $r(x) = ax + b$ for some $a,b \in \R$. Thus,
> $$\begin{align}
> 	 0 = f(i) &= q(i)(i^2 + 1) + ai + b \\
> 	&= q(i)(-1 + 1) + ai + b \\
> 	&= ai + b \\
> 	\iff 0 &= a = b \\
> 	\iff r(x) &= 0.
> \end{align}$$
> Thus, for all $f \in \ker \varphi$, $(x^2 + 1)|f(x)$, giving $\ker \varphi \subseteq \left< x^2 + 1 \right>$.
>
> $$\varphi(x^2 + 1) = i^2 + 1 = -1 + 1 = 0,$$
> thus, any [[Divisibility|multiple]] of $x^2 + 1$ maps to $0$ as well (as $\varphi$ preserves multiplication), so $\left< x^2 + 1 \right> \subseteq \ker \varphi$.
> 
> Together, this gives $\ker \varphi = \left< x^2 + 1 \right>$[^1].
> 
> Further, $\varphi$ is [[Surjective Functions|surjective]], as any $a + bi \in \C$ is given by $bx + a \in \R[x]$.
> 
> Finally, by *first isomorphism theorem*, $\R[x] / \left< x^2+1 \right> \cong \C$. $\square$
> 
> [^1]: [[Principal Ideals]]

\[[[Quotient Rings]]\]

