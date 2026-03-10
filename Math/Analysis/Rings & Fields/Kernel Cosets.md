---
tags:
  - atom
  - math
---
Let $\varphi: R \to S$ be a [[Ring Homomorphisms|ring homomorphism]]. Then for all $s \in S$,
$$\varphi^{-1}\{ s \} = r + \ker \varphi \quad\text{s.t.}\quad r \in \varphi^{-1}\{ s \}.$$
Alternatively, for all $r \in R$,
$$\varphi^{-1}\{ \varphi(r) \} = r + \ker \varphi.$$
> [!proof]-
> $\left( \subseteq \right)$
> Let $a \in \varphi^{-1}\{ \varphi(r) \}$ for some $r \in R$. Then
> $$\begin{align}
> 	\varphi(a) &= \varphi(r) \\
> 	\varphi(a) - \varphi(r) &= 0 \\
> 	\varphi(a - r) &= 0. \\
> \end{align}$$
> Thus, $a-r \in \ker \varphi$. Thus, $a = r + (a-r) \in a + \ker \varphi$.
> 
> $\left( \supseteq \right)$
> Let $s \in r + \ker \varphi$. Thus, $s = r + k$ for some $k \in \ker \varphi$. Thus,
> $$\begin{align}
> 	\varphi(s) &= \varphi(r + k) \\
> 	&= \varphi(r) + \varphi(k) \\
> 	&= \varphi(r). \\
> \end{align}$$
> Thus, $s \in \varphi^{-1}\{ \varphi(r) \}$.
