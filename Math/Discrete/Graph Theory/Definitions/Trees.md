---
tags:
  - atom
  - math
  - discrete
---
A *tree* is a connected [[Math/Discrete/Graph Theory/Graphs|graph]] with no [[Walks|cycles]].
- It follows that a [[Math/Discrete/Graph Theory/Definitions/Trees|tree]] is a [[Simple Graphs|simple graph]].
- A [[Math/Discrete/Graph Theory/Graphs|graph]] $G$ is a *tree* iff every [[Edges|edge]] is a [[Bridges|bridge]] .
> [!proof]-
> This is [[Logical Equivalence|logically equivalent]] to stating $G$ is not a *tree* [[Logical Implication|iff]] there exists an [[Edges|edge]] that is not a [[Bridges|bridge]][^1]. An [[Edges|edge]] is not a bridge iff it is in a [[Walks|cycle]][^2], meaning the original theorem [[Logical Equivalence|logically equivalent]] to stating $G$ is not a *tree* iff there is a [[Walks|cycle]], which is the same as stating $G$ is a *tree* iff there are no [[Walks|cycles]], the definition of a *tree*.
- A connected [[Math/Discrete/Graph Theory/Graphs|graph]] $G$ on where $\left| V(G) \right|=n$ is a *tree* iff $\left| E(G) \right| = n-1$ 
> [!proof]-
> $\left( \implies \right)$ **If $G$ is *tree* with $n$ [[Vertices|vertices]], then it has $n-1$ [[Edges|edges]]**
> **Base Case**
If $n = 1$, then $G$ has $1$ [[Vertices|vertex]], meaning it has $0$ ($n-1$) [[Edges|edges]].
> 
> **Induction Step**
> Suppose all *trees* on $k$ [[Vertices|vertices]] have $k-1$ [[Edges|edges]]. Adding a [[Vertices|vertex]] $v$ to $G$ can only result in a *tree* if $G$ with $v$ is [[Connectivitiy|connected]] and has no [[Walks|cycles]].
> - For $G$ with $v$ to be [[Connectivitiy|connected]], an [[Edges|edge]] must be created to connect $v$ to another [[Vertices|vertex]] $u$ in $G$.
> - For $G$ with $v$ to have no [[Walks|cycles]], $v$ can not be [[Edges|adjacent]] to two or more [[Vertices|vertices]] 
> 
> Therefore, adding one [[Vertices|vertex]] adds one [[Edges|edge]], implying a *tree* with $k+1$ [[Vertices|vertices]] has $k$ [[Edges|edges]].
Thus, the theorem has been proven by [[Induction|mathematical induction]].

[^1]: [[Negating Quantifiers]]
[^2]: [[Bridges]]