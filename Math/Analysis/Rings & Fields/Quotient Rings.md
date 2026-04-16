---
tags:
  - atom
  - math
---
The *quotient ring* $R/\hspace{-.2em} A$ of a [[Rings|ring]] $R$ modulo an [[Ideals|ideal]] $A$ is the [[Rings|ring]] of [[Cosets|cosets]] of $A$ under the operations
$$\begin{align}
	\left( s + A \right) + \left( t + A \right) &= \left( s + t \right) + A \\
	\left( s + A \right)\left( t + A \right) &= \left( st \right) + A. \\
\end{align}$$
> [!theorem]- The [[Cosets|cosets]] $\{ r + A : r \in R \}$ under these operations forms a [[Rings|ring]] iff $A$ is an [[Ideals|ideal]].
> $\left( \impliedby \right)$
> I will leave this as an exercise for the reader.
> 
> $\left( \implies \right)$
> He didn't prove this

> [!example]- $\Z/\hspace{-.2em}\left< n \right> \cong \Z_{n}$.
> Define $\varphi:\Z/\hspace{-.2em}\left< n \right> \to \Z_{n}$ by 
> $$\varphi(a + \left< n \right>) = a \mod n.$$
> **[[Functions|Well-Defined]]**
> This is well-defined because by [[Ring Cosets#^equality|this theorem]],
> $$\begin{align}
> 	a + \left< n \right> = b + \left< n \right> &\iff a - b \in \left< n \right> \\
> 	&\iff a-b \equiv 0 \mod n \\
> 	&\iff a \equiv b \mod n. \\
> \end{align}$$
> **[[Ring Homomorphisms|Homomorphism]]**
> This map is additive, as
> $$\begin{align}
> 	\varphi(\left( a + \left< n \right>  \right) + \left( b + \left< n \right>  \right)) &= \varphi(a + \left< n \right> ) + \varphi(b + \left< n \right> ) \\
> 	&= \left( a \hspace{-0.5em}\mod n \right) + \left( b \hspace{-0.5em}\mod n \right) \\
> 	&= a + b \mod n \\
> 	&= \varphi(\left( a + b \right) \mod n). \\
> \end{align}$$
> Similarly, this map is multiplicative by doing the same as the above, but replacing the $+$s with $\times$s.
> 
> **[[Bijective Functions|Bijection]]**
> For all $a \in \Z_{n}$, we have $\varphi(a + \left< n \right>) = a \mod n$. Thus, $\varphi$ is [[Surjective Functions|surjective]].
> 
> Let $a + \left< n \right> \in \Z/\hspace{-.2em}\left< n \right>$ such that $\varphi(a + \left< n \right>) = 0$, so $a \equiv 0 \mod n$. Thus $a \in \left< n \right>$, and so $a + \left< n \right> = 0 + \left< n \right>$. Thus, $\ker \varphi = \{ 0 \}$, so by [[Math/Analysis/Rings & Fields/Kernels#^injectivity|this theorem]], $\varphi$ is [[Injective Functions|injective]].

\[[[Translates]]\]