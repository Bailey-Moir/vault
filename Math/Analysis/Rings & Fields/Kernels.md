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

# Properties
Let $R$ and $S$ be [[Rings|rings]], $\varphi : R \to S$ be a [[Ring Homomorphisms|homomorphism]] between them, and $A$ and $B$ be [[Subrings|subrings]] of $R$ and $S$ respectively.
1. $\varphi(0) = 0$.
2. $\forall r \in R, \varphi(-r) = -\varphi(r)$
3. $\forall r \in R, n \in \N, \varphi(nr) = n\varphi(r) \land \varphi(r^n) = (\varphi(r))^n$
4. $\varphi(A)$ is a [[Subrings|subring]] of $S$.
5. $\varphi^{-1}(B)$ is a [[Subrings|subring]] of $R$.
6. If $R$ is [[Groups#^abelian-groups|commutative]], then $\varphi(R)$ is [[Groups#^abelian-groups|commutative]].
7. If $R$ is has a [[Rings#^unity|unity]] that isn't mapped to $0$, it is mapped to the [[Rings#^unity|unity]] of $\varphi(R)$.

1
$$\begin{align}
	\varphi(0) + \varphi(0) &= \varphi(0 + 0) \\
	&= \varphi(0) \\
	\varphi(0) &= 0. \\
\end{align}$$
2. Let $r \in R$.
$$\begin{align}
	\varphi(r - r) &= \varphi(0) \\
	\varphi(r) + \varphi(-r) &= 0 && \text{1.} \\
\end{align}$$
By the [[Groups#^inverse-uniqueness|uniqueness of the additive inverse]], $\varphi(-r) = -\varphi (r)$.
3. ?
4. Let $s,s' \in \varphi(A)$, where $s = \varphi(a)$ and $s' = \varphi(a')$ for some $a,a' \in A$. Then
$$\begin{align}
	s - s' &= \varphi(a) - \varphi(a') \\
	&= \varphi(a - a') \in \varphi(A) \\
\end{align}$$
$$\begin{align}
	s \times s' &= \varphi(a) \times \varphi(a') \\
	&= \varphi(a \times a') \in \varphi(A) \\
\end{align}$$
Thus, by the [[Subrings#^subring-test|subring test]], $\varphi(A)$ is a [[Subrings|subring]] of $S$.
5. Let $r,r' \in \varphi^{-1}(B)$, and denote $b = \varphi(r)$ and $b' = \varphi(r')$. Then
#TODO
$$\begin{align}
	b - b' &= \varphi(r) - \varphi(r') \\
	&= \varphi(a - a') \in \varphi(A) \\
\end{align}$$
$$\begin{align}
	s \times s' &= \varphi(a) \times \varphi(a') \\
	&= \varphi(a \times a') \in \varphi(A) \\
\end{align}$$
Thus, by the [[Subrings#^subring-test|subring test]], $\varphi(A)$ is a [[Subrings|subring]] of $S$.
6. 