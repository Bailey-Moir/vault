---
tags:
  - atom
  - math
---
For any [[Rings|ring]] $R$ with [[Rings#^unity|unity]] $e$, the mapping $\varphi : \Z \to R$ given by
$$\varphi(n) = ne := \underbrace{e + \dots + e}_{n}$$
is a [[Ring Homomorphisms|ring homomorphism]].

> [!proof]-
> **[[Functions|Well-Defined]]**
> $\varphi$ is well-defined, as its output is defined uniquely and directly in terms of its whole input $n$.
> 
> **[[Ring Homomorphisms|Homomorphism]]**
> Let $n,m \in \N$. Then
> $$\begin{align}
> 	\varphi(n) + \varphi(m) &= \underbrace{e + \dots + e}_{n} + \underbrace{e + \dots + e}_{m} \\
> 	&= \underbrace{e + \dots + e}_{n + m} \\
> 	&= \varphi(n + m). \\
> 	\\
> 	\varphi(n) \times \varphi(m) &= (\underbrace{e + \dots + e}_{n}) \times (\underbrace{e + \dots + e}_{m}) \\
> 	&= \underbrace{ e \times (\underbrace{e + \dots + e}_{m}) }_{n} \\
> 	&= \underbrace{e + \dots + e}_{n \times m} && \forall a \in R, e \times a = a \\
> 	&= \varphi(n \times m).
> \end{align}$$