---
tags:
  - atom
  - math
---
The *real numbers*, $\R$, is a [[Sets|set]] defined by 4 axioms:
1. $\R$ is a [[Fields|field]] (algebra).
2. $\R$ has a [[Total Order|total order]] (order).
3. $\R$ is an [[Ordered Fields|ordered field]] (interaction of order and algebra).
4. $\R$ is [[Completeness|complete]] (finishes the topological structure).

In other words, the *real numbers* are defined as a [[Completeness|complete]] [[Ordered Fields|ordered field]].

> [!notation]- Order
> Let $\le$ be a [[Total Order|total order]] on $\R$. We will define some further basic notation, that $\forall a,b \in \R,$
> - $a \le b \iff b \ge a$
> - $a < b \iff a \le b \land a \ne b$, and
> - $a < b \iff b > a$.
# Properties of The Reals
> [!theorem]- \- **Archimedean Property** - $\forall x \in \R, \exists n \in \N: x < n$
> Suppose the [[Negation|negation]]: $\exists x \in \R, \forall n \in \N, x \ge n$.
> Then $x$ is an [[Bounded Sets|upper bound]] on the [[Natural Numbers|naturals]].
> By [[Completeness|completeness]], since $\N$ has an [[Bounded Sets|upper bound]] ($x$), it must have a [[Supremums and Infimums|supremum]].
> Then,
> $$\begin{align}
> 	\forall n \in \N, \hspace{2em} n &\le \sup \N \\
> 	n + 1 &\le \sup \N && \text{Inductive principle} \\
> 	n &\le \sup \N - 1 \\
> \end{align}$$
> This violates the definition of a [[Supremums and Infimums|supremum]], since $\sup(\N) -1$ is an [[Bounded Sets|upper bound]] that is strictly less than $\sup \N$. 
> Thus, the [[Negation|negation]] is a [[Contradictions|contradiction]], meaning $\forall x \in \R, \exists n \in \N : x < n$.
> 


[^1]: [[Number Sets]]
