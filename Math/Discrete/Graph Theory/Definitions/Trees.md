---
tags:
  - atom
  - math
  - discrete
---
A *tree* is a connected [[Graphs|graph]] with no [[Walks|cycles]].
- It follows that a [[Math/Discrete/Graph Theory/Definitions/Trees|tree]] is a [[Simple Graphs|simple graph]].
- A [[Graphs|graph]] $G$ is a *tree* [[Logical Equivalence|iff]] every [[Math/Discrete/Graph Theory/Definitions/Edges|edge]] is a [[Bridges|bridge]] .
> [!proof]-
> This is [[Logical Equivalence|logically equivalent]] to stating $G$ is not a *tree* [[Logical Implication|iff]] there exists an [[Math/Discrete/Graph Theory/Definitions/Edges|edge]] that is not a [[Bridges|bridge]]^[[[Negating Quantifiers]]]. An [[Math/Discrete/Graph Theory/Definitions/Edges|edge]] is not a bridge [[Logical Equivalence|iff]] it is in a [[Walks|cycle]]^[[[Bridges]]], meaning the original theorem [[Logical Equivalence|logically equivalent]] to stating $G$ is not a *tree* [[Logical Equivalence|iff]] there is a [[Walks|cycle]], which is the same as stating $G$ is a *tree* [[Logical Equivalence|iff]] there are no [[Walks|cycles]], the definition of a *tree*.
- A connected [[Graphs|graph]] $G$ on where $\left| V(G) \right|=n$ is a *tree* [[Logical Equivalence|iff]] $\left| E(G) \right| = n-1$ 
> [!proof]-
> $\left( \implies \right)$ **If $G$ is *tree* with $n$ [[Vertices|vertices]], then it has $n-1$ [[Math/Discrete/Graph Theory/Definitions/Edges|edges]]**
> **Base Case**
If $n = 1$, then $G$ has $1$ [[Vertices|vertex]], meaning it has $0$ ($n-1$) [[Math/Discrete/Graph Theory/Definitions/Edges|edges]].
> 
> **Induction Step**
> Suppose all *trees* on $k$ [[Vertices|vertices]] have $k-1$ [[Math/Discrete/Graph Theory/Definitions/Edges|edges]]. Adding a [[Vertices|vertex]] $v$ to $G$ can only result in a *tree* if $G$ with $v$ is connected and has no [[Walks|cycles]].
> - For $G$ with $v$ to be *connected*, an [[Math/Discrete/Graph Theory/Definitions/Edges|edge]] must be created to connected $v$ to another [[Vertices|vertex]] $u$ in $G$.
> - For $G$ with $v$ to have no [[Walks|cycles]], $v$ can not be [[Math/Discrete/Graph Theory/Definitions/Edges|adjacent]] to two or more [[Vertices|vertices]] 
> 
> Therefore, adding one [[Vertices|vertex]] adds one [[Math/Discrete/Graph Theory/Definitions/Edges|edge]], implying a *tree* with $k+1$ [[Vertices|vertices]] has $k$ [[Math/Discrete/Graph Theory/Definitions/Edges|edges]].
Thus, the theorem has been proven by [[Induction|mathematical induction]].