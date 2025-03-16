---
tags:
  - atom
  - math
  - discrete
---
For $a \in G$[^1], if $\left| a \right|$[^2] is finite,
$$\left< a \right> = \{ e,a,a^2,\dots,a^{\left| a \right| -1} \}, \hspace{1em} (1)$$
and all of these elements are distinct

\[$(1)$ [[Powers in Groups]]\]

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

\[[[Cyclic Groups]]\]

[^1]: [[Groups]]
[^2]: [[Order of a Group and Group Elements]]
[^3]: [[The Division Algorithm]]
