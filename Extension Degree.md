---
tags:
  - atom
  - math
---
Let $E$ be an [[Subfields#^extension-field|extension field]] of $F$. We say the *degree* of $E$ over $F$ $[E:F] = n$ iff $E$ has [[Dimension|dimension]] $n$ as a [[Vector Spaces|vector space]] over $F$.

> [!definitions]
> - If $[E:F]$ is finite, $E$ is a **finite extension**
> - If $[E:F]$ is infinite, $E$ is a **infinite extension**
^finite-and-infinite

[!theorem] $[F(\alpha) : F] = \deg p$ where $p$ is the [[Algebraic and Transcendetal Simple Extensions#^minimal-polynomial|minimal polynomial]] of $\alpha$ over $F$.
The [[Structure of Simple Field Extensions|structure of simple field extensions]] gives that $1,\alpha,\dots,\alpha^{\deg p(x)-1}$ form a [[Vector Bases|basis]] for $F(\alpha)$, meaning the [[Dimension|dimension]] of $F(\alpha)$ over $F$ is $\deg p$.

> [!theorem]- [[#^finite-and-infinite|Finite extensions]] of $F$ are [[Algebraic Extensions|algebraic]].

Let $E$ be an [[Subfields#^extension-field|extension field]] of $F$ of *degree* $n$. Let $\alpha \in E$.

Consider $1,\dots,\alpha^n$. This is a [[Lists|list]] of $n+1$ elements, meaning they are [[Linear Independence|linearly dependent]][^1].
Thus, there exists $c_{0},\dots,c_{n} \in F$ that aren't all zero such that
$$c_{n}\alpha^n + \dots+c_{1}\alpha + c_{0} = 0.$$
Thus, $\alpha$ is a root of
$$f(x) = c_{n}x^n + \dots+c_{1}x + c_{0},$$
a non-zero polynomial

By definition, there exists $v_{1},\dots,v_{n} \in E$ such that
$$\alpha = c_{1}v_{1},\dots,c_{1}v_{n}$$
for some $c_{1},\dots,c_{n} \in F$.

#TODO look at lecture notes for proof
^finite-implies-algebraic

> [!theorem]- *(Tower Theorem)* $[K:F] = [K:E][E:F]$
> Let $K$ be an [[Subfields#^extension-field|extension field]] of $E$ such that $[K:E] = m$, and $E$ be an [[Subfields#^extension-field|extension field]] of $F$ such that $[E:F] = n$.
> 
> Thus, $E$ has a [[Vector Bases|basis]] $\alpha_{1},\dots,\alpha_{n} \in E$ on $F$, and $K$ has a [[Vector Bases|basis]] $\beta_{1},\dots,\beta_{m} \in K$ on $E$.
> 
> I claim $B = \{ \alpha_{i}\beta_{j} : i \in \{ 1,\dots,n \}, \beta \in \{ 1,\dots,m \} \} \subseteq K$ forms a [[Vector Bases|basis]] of $K$ on $F$.
> 
> **[[Span|Span]]**
> Let $c \in K$. Then by the [[Vector Bases|bases]] being [[Span#^spanning-set|spanning sets]],
> $$\begin{align}
> 	c 
> 	&= \sum_{j} b_{j}\beta_{j} && \forall j, b_{j} \in E \\
> 	&= \sum_{j} \left( \sum_{i} a_{i,j}\alpha_{i} \right)\beta_{j} && \forall i,j, a_{i,j} \in F . \\
> 	&= \sum_{i,j} a_{i,j}\alpha_{i}\beta_{j}. \\
> \end{align}$$
> Expanding, $c$ is a [[Linear Combinations|linear combination]] of elements of $B$ over $F$.
> 
> **[[Linear Independence|Linear Independence]]**
> Suppose $c = 0$. Then by the [[Linear Independence|linear independence]] of the two [[Vector Bases|bases]].
> $$\begin{align}
> 	0 
> 	&= \sum_{i,j} a_{i,j}\alpha_{i}\beta_{j}. \\
> 	&= \sum_{j} \left( \sum_{i} a_{i,j}\alpha_{i} \right)\beta_{j} \\
> 	\to \forall j, \quad 0&= \sum_{i} a_{i,j}\alpha_{i} \\
> 	\to \forall i,j, \quad 0&= a_{i,j}. \\
> \end{align}$$
> Thus, all coefficients are zero. $\quad\square$
^tower-theorem

[^1]: [[Linear Independence and Span with Dimension]]
