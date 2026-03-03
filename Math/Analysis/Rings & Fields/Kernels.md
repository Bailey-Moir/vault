---
tags:
  - atom
  - math
---
The *kernel* of a [[Ring Homomorphisms|ring homomorphism]] $\varphi : R \to S$ [[Sets|set]]
$$ \ker \varphi =  \varphi^{-1}(\{ 0 \}) = \{ r \in R : \varphi(r) = 0\}. $$

> [!note] [[Null Space|Null spaces]] of [[Linear Maps|linear maps]] are also called *kernels*.

[!theorem]- A [[Ring Homomorphisms|homomorphism]] $\varphi : R \to S$ is an [[Ring Homomorphisms#^isomorphism|isomorphism]] iff $\ker \varphi = \{ 0 \}$
$\left( \implies \right)$
Trivial, I'll do this later (injectivity)

$\left( \impliedby \right)$
Suppose $\ker \varphi = \{  0 \}$.
$$\begin{align}
	\varphi(a-a) &\neq \varphi(a) - \varphi(a) \\
	\varphi(0) &\neq 0 \to \bot \\
\end{align}$$

$$\begin{align}
	\varphi(a+0) &\neq \varphi(a) + \varphi(0) \\
	\varphi(a) &\neq \varphi(a) \to \bot \\
	
	\varphi(0+b) &\neq \varphi(0) + \varphi(b) \\
	\varphi(b) &\neq \varphi(b) \to \bot \\
\end{align}$$