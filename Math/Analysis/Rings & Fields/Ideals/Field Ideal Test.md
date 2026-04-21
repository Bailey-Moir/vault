---
tags:
  - atom
  - math
---
A [[Groups#^abelian-groups|commutative]] [[Rings|ring]] $R$ with [[Rings#^unity|unity]] is a [[Fields|field]] iff it has no proper non-trivial [[Ideals|ideals]] (i.e. [[Ideals|ideals]] other than $\{ 0 \}$ and $R$).

[!proof]-
$\left( \implies \right)$
Let $I$ be an [[Ideals|ideal]] of a [[Fields|field]] $R$, where $I \ne \left< 0 \right> = \{ 0 \}$.

Then there exists $a \ne 0 \in I$. Let $r \in R$ be given. Then
$$a\left( a^{-1}r \right) = r,$$
so by the [[Ideals|absorbing property of ideals]], since $a^{-1}r \in R$ by $R$ being a [[Fields|field]], $r \in A$.

Thus, $R \subseteq I$, but $I \subseteq R$, meaning $I = R$, giving that all [[Ideals|ideals]] of $R$ are $\{ 0 \}$ or $R$.

$\left( \impliedby \right)$
Let $R$ be a [[Groups#^abelian-groups|commutative]] [[Rings|ring]] with [[Rings#^unity|unity]] that's not a [[Fields|field]] (i.e. it has non-[[Rings#^unit|unit]] elements).

Let $a \ne 0$ be a non-[[Rings#^unit|unit]] of $R$. Then by definition,
$$\forall r \in R, ar \ne 1.$$
Consider the [[Sets|set]] $A = \{ ar : r \in R \}$. Let $r,s \in R$. then
$$\begin{align}
	ar - as &= a(r-s) \\
	&\in A && r,s \in R \to r-s \in R. \\
	\\
	s \times ar = ar \times s &= ars && \text{Commutative} \\
	&= a(rs) \\
	&\in A && r,s \in R \to rs \in R.
\end{align}$$
Thus, by the [[Ideals#^ideal-test|ideal test]], $A$ is an [[Ideals|ideal]] of $R$.

However, $1\notin A$, so $A \ne \{ 0 \}$ and $A \ne R$, so the implication is proven by [[Proof by Contraposition|contraposition]].