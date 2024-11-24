---
tags:
  - atom
  - math
  - discrete
---
**Definition**: An element $a \in \Z_n$ is *invertible* iff there is an element $a^{-1} \in \Z_n$ such that $a \times a^{-1} = 1$.
**Theorem**:
$$ \forall n \in \Z^+, \forall a \in \Z_n, (\exists! a^{-1} \in \Z_n : aa^{-1} = 1 \iff \underbrace{\gcd(a,n) = 1}_{a \text{ and } n \text{ are coprime}} ) $$
> [!proof]-
> $\left(\implies\right)$
> Assume $a$ is *invertible*, meaning $\exists! a^{-1} : a \times a^{-1} = 1$ in $\Z_n$, so 
> $$\begin{array}{l}
> 	a \times a^{-1} \equiv 1 \pmod n \\
> 	a \times a^{-1} - 1 = kn && \text{For some $k \in \Z$} \\
> 	a \times a^{-1} - kn =1 \\
> \end{array}$$
> From [[Bēzout's Identity#Extended Theorem|Bēzout's Extended Identity]], since $1$ can be written as a [[Linear Combinations|linear combination]] of $a$ and $n$ over the integers, $\gcd(a,n)|1$, meaning $\gcd(a,n) = 1$.
> 
> $\left(\impliedby\right)$
> Assume $\gcd(a,n) = 1$. By [[Bēzout's Identity]], 
> $$\begin{array}{rl}
> 	\exists r,s \in \Z :\!\!\!\!
> 	& 1 = ra + sn \\
> 	& 1 \equiv ra + sn \pmod n  \\
> 	& 1 \equiv ra \pmod n  \\
> \end{array}$$
> Let $0 \le r' < n$ (which is in $\Z_n$) be the principal remainder when dividing $r$ by $n$.
> $$r = qn + r'$$
> Therefore
> $$\begin{array}{l}
> 	1 \equiv ra \pmod n  \\
> 	1 \equiv (qn + r')a \pmod n  \\
> 	1 \equiv r'a \pmod n  \\
> \end{array}$$
> Thus $a^{-1} = r'$.

Note that this means that $\forall p \in \mathbb{P}$, every non-zero element of $\Z_p$ is invertible.

\[[[Greatest Common Divisor]], [[Cyclic Groups]]\]