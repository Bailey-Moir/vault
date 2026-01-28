---
tags:
  - atom
  - math
---
A [[Topology|topological space]] is called *second countable* iff it has a [[Countability|countable]] [[Topological Bases|basis]].

> [!example]- $\R^n$ is *second countable*
> The [[Collections|collection]]
> $$\mathcal{B} = \{ B_{r}(p) : r \in \Q_{>0}, p \in \Q^n \}$$
> is [[Countability|countable]], as [[Countability|countable sets]] are closed under finite [[Cartesian Product|cartesian products]][^1], and $\left| \mathcal{B} \right| \le \left| \Q^{n+1} \right|$ (and $\Q$ is [[Countability|countable]]).
> 
> We will show that $\mathcal{B}$ is a valid [[Topological Bases|basis]] of $\R^n$ using the usual topology, meaning that $\R^n$ is *second countable*.
> 
> $\mathcal{B}$ is a [[Collections|collection]] of [[Open Sets|open sets]], so all that needs to be shown is that 
> $$\forall A \in \mathcal{T}, \exists \mathcal{C} \subseteq \mathcal{B} : A = \bigcup \mathcal{C}.$$
> For all $A \in \mathcal{T}$ and $p \in A$, there must exist some $\varepsilon \in \R_{>0}$ such that $B_{\varepsilon}(p) \subseteq A$[^2].
> By properties of [[Rational Numbers|rational numbers]], there exists some $q \in \Q_{>0}$ such that $q < \varepsilon$, giving $B_{q}(p) \subseteq A$.
> 
> Thus, for all $A \in \mathcal{T}$ and $p \in A$, there exists some $q \in \Q_{>0}$ such that $B_{q}(p) \subseteq A$. Thus,
> $$\begin{align}
> 	A \subseteq \bigcup_{p \in A} B_{q_{p}}(p) \subseteq A \\
> 	\to \bigcup_{p \in A} B_{q_{p}}(p) = A, \\
> \end{align}$$
> i.e. $\mathcal{C} = \{ \bigcup_{p \in A} B_{q_{p}}(p)  : p \in A \}$.

[^1]: [[Countability]], Theorem 1
[^2]: [[Open Sets]], Theorem 1
