---
tags:
  - atom
  - math
---
The *kernel* of a [[Ring Homomorphisms|ring homomorphism]] $\varphi : R \to S$ [[Sets|set]]
$$ \ker \varphi =  \varphi^{-1}(\{ 0 \}) = \{ r \in R : \varphi(r) = 0\}. $$

> [!note] [[Null Space|Null spaces]] of [[Linear Maps|linear maps]] are also called *kernels*.

> [!theorem]- The *kernel* of $\varphi : R \to S$ is a [[Subrings|subring]] of $R$.
> Let $a,b \in \ker R$, meaning $\varphi(a) = \varphi (b) = 0$. Then
> $$\begin{align}
> 	\varphi(a) - \varphi(b) &= 0 \\
> 	\varphi(a - b) &= 0 \\
> 	\to a - b &\in \ker R,
> \end{align}$$
> $$\begin{align}
> 	\varphi(a) \times \varphi(b) &= 0 \\
> 	\varphi(a \times b) &= 0 \\
> 	\to a \times b &\in \ker R.
> \end{align}$$
> By the [[Subrings#^subring-test|subring test]], $\ker \varphi$ is a [[Subrings|subring]] of $R$.
^subring

> [!theorem]- A [[Ring Homomorphisms|homomorphism]] $\varphi : R \to S$ is [[Injective Functions|injective]] iff $\ker \varphi = \{ 0 \}$
> $\left( \implies \right)$
> $$\begin{align}
> 	\varphi(0) + \varphi(0) &= \varphi(0 + 0) \\
> 	&= \varphi(0) \\
> 	\varphi(0) &= 0. \\
> \end{align}$$
> Since $\varphi$ is [[Injective Functions|injective]], no other element may map to $0$, so $\ker \varphi = \{ 0 \}$.
> 
> $\left( \impliedby \right)$
> Suppose $\ker \varphi = \{  0 \}$.
> 
> Suppose $\varphi(a) = \varphi(b)$ for $a,b \in R$. Then
> $$\begin{align}
> 	\varphi(a) - \varphi(b) = 0 \\
> 	\varphi(a - b) = 0 .\\
> \end{align}$$
> Thus, $a - b = 0$, so $a = b$, meaning $\varphi$ is [[Injective Functions|injective]].
^injectivity