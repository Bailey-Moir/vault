---
tags:
  - atom
  - math
  - discrete
---
A *bridge* is an [[Math/Discrete/Graph Theory/Definitions/Edges|edge]] on a **connected** [[Graphs|graph]] that if removed, results in a **disconnected** [[Graphs|graph]].
- A given [[Math/Discrete/Graph Theory/Definitions/Edges|edge]] is a *bridge* [[Logical Equivalence|iff]] it is not in a [[Walks|cycle]].
> [!proof]-
> Let $e = \{ a,b \}$ be the [[Math/Discrete/Graph Theory/Definitions/Edges|edge]], and $G$ be the connected [[Graphs|graph]].
> $\left( \implies \right)$ **If $e$ is a [[Bridges|bridge]], then is not a in [[Walks|cycle]]**
> Removing $e$ makes $G\setminus e$ disconnected, meaning there exists [[Vertices|vertices]] $u,v \in V(G\setminus e)$ with no [[Walks|path]] connecting them in $G\setminus e$.
> 
> [[Proof by Contradiction|By contradiction]], suppose $e$ were in a [[Walks|cycle]] in $G$. Therefore, there exists a [[Walks|path]] from $a$ to $b$ other than $a,e,b$. This implies $u,v$ is connected in $G\setminus e$, [[Contradictions|contradicting]] $e$ being a [[Bridges|bridge]].
> 
> Therefore $e$ can not be in a [[Walks|cycle]]
> 
> $\left( \impliedby \right)$ **If $e$ is not a in [[Walks|cycle]], then $e$ is a [[Bridges|bridge]]**
> Supposed the [[Negation|negation]] is true^[[[Proof by Contradiction]]], that $e$ is not in a [[Walks|cycle]] and it is **not** a [[Bridges|bridge]], i.e. $G\setminus e$ is connected.
> 
> This means there exists two paths from $a$ to $b$ in $G$, [[Contradictions|contradicting]] $e$ not being in a [[Walks|cycle]]. Thus, $e$ is a [[Bridges|bridge]].
- If $e$ is a [[Bridges|bridge]] of $G$^[[[Graphs]]], then $G\setminus e$ has precisely two components
> [!proof]-
> Supposed $u,v$ are [[Vertices|vertices]] in $G\setminus e$. Let $t$ be some third [[Vertices|vertex]] not connected to $u$. It follows that $v$ is connected in $G\setminus e$. Therefore, any [[Vertices|vertex]] no connected to $u$ must be connected to $v$. Therefore, there are precisely two components.
