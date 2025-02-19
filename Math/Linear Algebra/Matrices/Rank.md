---
tags:
  - atom
  - math
  - linear
---
Suppose $A \in \F^{m,n}$[^1].
- The *column rank* of $A$ is the [[Dimension|dimension]] of the [[Span|span]] of the columns of $A$ in $\F^{m}$.
- The *row rank* of $A$ is the [[Dimension|dimension]] of the [[Span|span]] of the rows of $A$ in $\F^n$.

> [!proof]- The *column* and *row rank* are the same.
> Let $c$ denote the *column rank* of $A$, and $A = CR$ be the [[Column-Row Factorization|column-row factorisation]] of $A$. Note $C \in \F^{m,c}$ and $R \in \F^{c,n}$.
> 
> Every row of $A$ must be a [[Linear Combinations|linear combination]] of the rows of $R$[^2].
> 
> $R$ has $c$ rows, meaning the *row rank* of $R$ (and thus $A$) is less than or equal to $c$.
> 
> To get the other direction, apply this result to $A^{T}$[^3].
> $$\begin{align}
> 	\text{column rank}\,A &= \text{row rank}\,A^T \\
> 	&\le \text{column rank}\,A^{T} \\
> 	&\le \text{row rank}\,A \\
> \end{align}$$
> Thus, $\text{column rank}\,A = \text{row rank}\,A$.

> [!proof]- The *column* and *row rank* are both less than or equal to $\min\{m,n\}$.
> The column rank is at most $n$ because there are only $n$ columns, and it is also at most $m$ as $\text{dim}\,\F^m = m$.
>
> The same can be said about rows.

[^1]: [[Sets of Matrices]]
[^2]:: [[Matrix Multiplication]]
[^3]: [[Transposition]]