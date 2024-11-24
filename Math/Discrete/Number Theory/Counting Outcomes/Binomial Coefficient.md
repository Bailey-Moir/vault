---
tags:
  - atom
  - math
  - stats
  - discrete
---
The number of unordered [[Subsets|subset]] of $r$ elements from a fixed [[Sets|set]] of $n$ elements. 
$$ \prescript{n}{}C_{r} = \begin{pmatrix}
	n \\ r
\end{pmatrix} = \dfrac{n!}{r! \left( n - r \right)!} $$
There are many different applications of this coefficient. It gives:
- The number of [[Subsets|subsets]] of size $r$ from a [[Sets|set]] of size $n$.
- The coefficient of the $x^r$ term in $(x + 1)^n$.
- The number of arrangements of $r$ successes among $n$ trials[^1]].
# Properties
$\forall n,r \in \N, r \le n \implies$
- $\begin{pmatrix}n\\r\end{pmatrix}=\begin{pmatrix}n\\n-r\end{pmatrix}$
> [!proof]-
> $$\begin{align*}
> 	\begin{pmatrix}
> 	n\\n-r
> \end{pmatrix}&=\dfrac{n!}{\left( n-r \right)!\left( n-\left( n-r \right) \right)!} \\
> 	&=\dfrac{n!}{\left( n-r \right)!r!} \\
> 	&=\begin{pmatrix}
> 	n\\r
> \end{pmatrix}
> \end{align*}$$
- $\begin{pmatrix}n\\r\end{pmatrix}=\begin{pmatrix}n-1\\r-1\end{pmatrix} + \begin{pmatrix}n-1\\r\end{pmatrix}$ (rule for [[Pascal's Triangle|Pascal's triangle]])
> [!proof]-
> Let $A$ be a [[Sets|set]] of size $n$ and $S$ be any [[Subsets|subset]] of $A$ of size $r$. The [[Sample Space|sample space]] of possible $S$s can be [[Partitions|partitioned]] by whether or not a given element $a\in A$ is in $S$.
> - If $a\in S$, then the remaining $r-1$ elements of $S$ need to be *chosen* from the remaining $n-1$ elements of $A$.
> $$\begin{pmatrix}
> 	n-1\\r-1
> \end{pmatrix}$$
> - If $a\notin S$, then the remaining $r$ elements of $S$ need to be *chosen* from the remaining $n-1$ elements of $A$.
> $$\begin{pmatrix}
> 	n-1\\r
> \end{pmatrix}$$
> Thus, in total,
> $$ \begin{pmatrix}n\\r\end{pmatrix}=\begin{pmatrix}n-1\\r-1\end{pmatrix} + \begin{pmatrix}n-1\\r\end{pmatrix} $$

[^1]: [[Binomial Random Variable]]