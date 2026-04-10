---
tags:
  - atom
  - comp
---
Consider an [[Directed Graphs|undirected graph]] $G$, the *Girvan-Newman* [[Algorithms|algorithm]] constructs a hierarchy of densely linked clusters, i.e. *communities*, by iteratively removing the [[Edges|edges]] with highest **betweenness**. The resulting [[Components|components]] are the *communities*.

> [!definition] The **betweeness** of a given [[Edges|edge]] is the number of [[Shortest Paths|shortest paths]] that include that [[Edges|edge]].
^betweenness

Thus, we will need to calculate the **betweenness** of each [[Edges|edge]]. Let $u \in V(G)$ be given as our [[Root|root]] [[Vertices|vertex]] to perform a [[Breadth First Search|BFS]] on, giving all of its [[Shortest Paths|shortest paths]].
![500|center](Pastedimage20260409235020.png)
They say, "split flow up", but the base case of this inductive principle is iffy as fuck, and I don't know how you would actually want to go about doing this.