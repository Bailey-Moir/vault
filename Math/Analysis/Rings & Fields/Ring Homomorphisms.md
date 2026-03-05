---
tags:
  - atom
  - math
---
A *ring [[Concrete Categories#^homomorphisms|homomorphism]]* is a [[Functions|function]] $\varphi : R \to S$ that commutes with addition and multiplication, i.e.
$$\begin{align}
	\varphi(a+b) &= \varphi(a) + \varphi(b) \\
	\varphi(a\times b) &= \varphi(a) \times \varphi(b). \\
\end{align}$$
> [!note] The [[Bijective Functions|bijective]] [[Concrete Categories#^homomorphisms|homomorphisms]] between [[Rings|rings]] are exactly the [[Isomorphisms|isomorphisms]].
^isomorphism

\[[[Category of Rings]]\]
# Properties
Let $R$ and $S$ be [[Rings|rings]], $\varphi : R \to S$ be a [[Ring Homomorphisms|homomorphism]] between them, and $A$ and $B$ be [[Subrings|subrings]] of $R$ and $S$ respectively.
1. $\varphi(0) = 0$.
2. $\forall r \in R, \varphi(-r) = -\varphi(r)$
3. $\forall r \in R, n \in \N, \varphi(nr) = n\varphi(r) \land \varphi(r^n) = (\varphi(r))^n$
4. $\varphi(A)$ is a [[Subrings|subring]] of $S$.
5. $\varphi^{-1}(B)$ is a [[Subrings|subring]] of $R$.
6. If $R$ is [[Groups#^abelian-groups|commutative]], then $\varphi(R)$ is [[Groups#^abelian-groups|commutative]].
7. If $R$ has a [[Rings#^unity|unity]], it is either mapped to $0$ or the [[Rings#^unity|unity]] of $\varphi(R)$.

> [!proof]- 1
> $$\begin{align}
> 	\varphi(0) + \varphi(0) &= \varphi(0 + 0) \\
> 	&= \varphi(0) \\
> 	\varphi(0) &= 0. \\
> \end{align}$$

> [!proof]- 2
> Let $r \in R$.
> $$\begin{align}
> 	\varphi(r - r) &= \varphi(0) \\
> 	\varphi(r) + \varphi(-r) &= 0 && \text{1.} \\
> \end{align}$$
> By the [[Groups#^inverse-uniqueness|uniqueness of the additive inverse]], $\varphi(-r) = -\varphi (r)$.

> [!proof]- 4
> Let $s,s' \in \varphi(A)$, where $s = \varphi(a)$ and $s' = \varphi(a')$ for some $a,a' \in A$. Then
> $$\begin{align}
> 	s - s' &= \varphi(a) - \varphi(a') \\
> 	&= \varphi(a - a') \in \varphi(A) \\
> \end{align}$$
> $$\begin{align}
> 	s \times s' &= \varphi(a) \times \varphi(a') \\
> 	&= \varphi(a \times a') \in \varphi(A) \\
> \end{align}$$
> Thus, by the [[Subrings#^subring-test|subring test]], $\varphi(A)$ is a [[Subrings|subring]] of $S$.

> [!proof]- 5
> Let $r,r' \in \varphi^{-1}(B)$, and denote $b = \varphi(r)$ and $b' = \varphi(r')$. Then
> $$\begin{align}
> 	\varphi(r - r') &= \varphi(r) - \varphi(r') \\
> 	&= b - b' \in B \\
> 	\to r-r' &\in \varphi^{-1}(B),
> \end{align}$$
> $$\begin{align}
> 	\varphi(r \times r') &= \varphi(r) \times \varphi(r') \\
> 	&= b \times b' \in B) \\
> 	\to b-b' &\in \varphi^{-1}(B).
> \end{align}$$
> Thus, by the [[Subrings#^subring-test|subring test]], $\varphi^{-1}(B)$ is a [[Subrings|subring]] of $R$.

> [!proof]- 6
> Suppose $R$ is [[Groups#^abelian-groups|commutative]]. Then for any $\varphi(r),\varphi(r') \in \varphi(R)$,
> $$\begin{align}
> 	\varphi(r \times r') &= \varphi(r' \times r) \\
> 	\varphi(r) \times \varphi(r') &= \varphi(r') \times \varphi(r). \\
> \end{align}$$
> Thus, $\varphi(R)$ is [[Groups#^abelian-groups|commutative]].

> [!proof]- 7
> Suppose $R$ has a [[Rings#^unity|unity]] that isn't mapped to $0$. Then for any $\varphi(r) \in \varphi(R)$,
> $$ \varphi(r) = \varphi(r \times 1) = \varphi(r) \times \varphi(1) $$
> By the [[Groups#^identity-uniqueness|uniqueness of the multiplicative identity]], $\varphi(1) = 1$.