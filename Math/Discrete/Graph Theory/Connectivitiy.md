---
tags:
  - atom
  - math
  - discrete
---
[[Vertices]] $u$ and $v$ are *connected* iff there is a [[Walks|walk]] from $u$ to $v$. $\gamma$ denotes the [[Equivalence Relations|equivalence relation]] where $\left( u,v \right)\in \gamma$ iff $u$ is *connected* to $v$.
- This is not an [[Equivalence Relations|equivalence relation]] if $G$ is [[Directed Graphs|directed]] (as it is not [[Symmetric Property|symmetric]]).

> [!proof]- Equivalence Relation
> **[[Reflexive Property|Reflexive Property]]** - $\small\forall v\in V(G),\left( v,v \right) \in \gamma$
> Every [[Vertices|vertex]] $v \in V$ has a [[Walks|walk]] $\{v\}$. This [[Walks|walk]] starts at $v$ and ends at $v$, meaning they are *connected*.
>
> **[[Symmetric Property|Symmetric Property]]** - $\small\forall u,v\in V(G), \left(\left( u,v \right) \in \gamma \to \left( v,u \right)\in\gamma \right)$
> If $G$ is [[Directed Graphs|undirected]], any [[Walks|walk]] (such as from $u$ to $v$) can be traversed backwards (flipped), meaning there is a [[Walks|walk]] $v$ to $u$.
>
> **[[Transitive Property|Transitive Property]]** - $\small\forall u,v,w\in V(G),\left( \left( u,v \right)\in\gamma \land \left( v,w \right)\in\gamma \to \left( u,w \right)\in\gamma \right)$
> If there is a [[Walks|walk]] from $u$ to $v$ and $v$ to $w$, these [[Walks|walk]]/[[Sequences|sequences]] can be concatenated/joined such that  the resulting [[Sequences|sequence]] starts from $u$ to $v$, and then after $v$, has the sequence from $v$ to $w$ (skipping $v$ as to not repeat it). This is a [[Walks|walk]] from $u$ to $w$.