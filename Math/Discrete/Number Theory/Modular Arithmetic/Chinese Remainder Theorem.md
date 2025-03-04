---
tags:
  - atom
  - math
  - discrete
---
For [[Linear Systems|linear system]] of [[Congruence|congruences]] of the form
$$\begin{array}{ccc}
	x = a_{1} \mod m_{1}  \\
	\vdots \\
	x = a_{k} \mod m_{k}, \\
\end{array}$$
if $m_{1},\dots,m_{k}$ are pairwise co-prime integers (and $a_{1},\dots,a_{k} \in \Z$), has a **unique** solution modulo $m_{1}\cdots m_{k}$.

> [!proof]-
> **Base Case**
For $n = 1$, $x = a_{1} \mod m_{1}$ has a unique solution $a_{1}$ modulo $m_{1}\cdots m_{k}$
> 
> **[[Induction|Induction]] Step**
> Assume the theorem is true for all $n \in \N$, and suppose we are trying to solve a [[Linear Systems|system]]
> $$\begin{array}{ccc}
> 	x \equiv a_{1} \mod m_{1}  \\
> 	\vdots \\
> 	x \equiv a_{n} \mod m_{n}, \\
> 	x \equiv a_{n+1} \mod m_{n+1}, \\
> \end{array}$$
> where $m_{1},\dots,m_{n+1}$ are pairwise co-prime.
> 
> By the induction hypothesis, the first $n$ [[Congruence|congruences]] have a unique solution modulo $m = m_{1}\cdots m_{n}$. Let this solution be $x = c + mk$ for $k \in \Z$.
> 
> Substituting these solutions into $x \equiv a_{n+1} \mod m_{n+1}$ and solving for $k$ gives
> $$\begin{align}
> 	c + mk \equiv a_{n+1} \mod m_{n+1} &\iff k \equiv m^{-1}(a_{n+1} - c) \mod m_{n+1}
> \end{align}$$
> Let $d \in \Z$ represent $m^{-1}(a_{n+1}-c)$ in $\Z_{m_{n+1}}$. $x = c + mk$ satisfies the $(n+1)$-th [[Congruence|congruence]] iff $k \equiv d \mod m_{n+1}$, meaning $x$ satisfies all $(n+1)$ [[Congruence|congruences]] iff
> $$\begin{align}
> 	x &= c+mk \\
> 	x &= c+m(d+m_{n+1}l) && l \in \Z\\
> 	x &= (c+md) + mm_{n+1}l \\
> 	x &= (c+m_{1}\cdots m_{n}d) + m_{1}\cdots m_{n+1}l \\
> \end{align}$$