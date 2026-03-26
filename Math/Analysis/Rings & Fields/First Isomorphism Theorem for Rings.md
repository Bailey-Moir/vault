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
> 	\varphi(r) &=  - \varphi(r'). \\
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


\[[[Quotient Rings]]\]