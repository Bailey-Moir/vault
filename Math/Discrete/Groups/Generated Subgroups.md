---
tags:
  - atom
  - math
  - discrete
---
The smallest [[Subgroups|subgroup]] containing $a$ in $G$ is the [[Subsets|subset]]
$$\begin{align}
	\left< a \right> &= \{ a^m : m \in \Z \} \\
\end{align}$$
> [!proof]-
> Let $g,h \in \left< a \right>$. Then $g = a^m$ and $h = a^n$ for $m,n \in \Z$.
> 
> Thus $gh^{-1} = a^ma^{-n} = a^{m-n}$. Since $m-n \in \Z$, this must be in $\left< a \right>$.
> 
> This then passes the [[Subgroups|one-step subgroup test]], meaning $\left< a \right> \le G$.

# Finite Generated Subgroups
For $a \in G$[^1], if $\left| a \right|$[^2] is finite,
$$\left< a \right> = \{ e,a,a^2,\dots,a^{\left| a \right| -1} \},$$
and all of these elements are distinct

> [!proof]-
> **Equality**
> Since $\left| a \right|$[^2] is finite, $\{ a^m : m \in \Z\}$ is finite, meaning there must be some integers $m < n$ such that $a^m = a^n$.
> 
> Then $a^{n-m} = e$. In particular, there is some positive power of $a$ that is equal to the identity.
> 
> Let $k$ be the smallest positive power of $a$ such that $a^k = e$.
> 
> For any $m \in \Z$, we can write $m = kq + r$ with $0 \le r < k$[^3]. Thus
> $$\begin{align}
> 	a^m &= a^{kq + r} \\
> 	&= a^{kq}a^r \\
> 	&= e^{q}a^r \\
> 	&= a^r. \\
> \end{align}$$
> Thus, every element of $\left< a \right>$ is in the set $\{ e,a,\dots, a^{k-1} \}$.
> 
> **Distinctness**
> Suppose $a^i = a^j$ for some integers $0 \le i, j < k$. Then $e = a^{j-i}$, meaning $k|j-i$.
> 
> Since $k \le j-i \le k$, $j-i = 0k = 0$, meaning $i=j$.
> 
> Thus, the elements in $\{ e,a,\dots, a^{k-1} \}$ are distinct.

> [!note] This shows that $\left| a \right|$ is the smallest positive integer such that $a^\left| a \right| = e$.

\[[[Powers in Groups]], [[Cyclic Groups]]\]

[^1]: [[Groups]]
[^2]: [[Order in Groups]]
[^3]: [[Division Algorithm]]
