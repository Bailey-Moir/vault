---
tags:
  - atom
  - math
  - discrete
---
A closed [[Walks|walk]] that traverses each [[Math/Discrete/Graph Theory/Definitions/Edges|edge]] of the [[Graphs|graph]] **exactly once** is called a *Eulerian circuit*.
A connected [[Graphs|graph]] is *Eulerian* if it contains one of these circuits.
- A connected [[Graphs|graph]] $G$ is *Eulerian* [[Logical Equivalence|iff]] $\forall v \in V(G),2|\delta(v)$
> [!proof]- 
> $\left( \implies \right)$
> Each visit to a [[Vertices|vertex]] $v$ uses an [[Math/Discrete/Graph Theory/Definitions/Edges|edge]] to enter and an [[Math/Discrete/Graph Theory/Definitions/Edges|edge]] to exit. Therefore
> $$\#\text{ in edges} = \#\text{ out edges},$$
> meaning $\delta(v)$ is even.
> 
> $\left( \impliedby \right)$
> This can be used to construct a proof by [[Induction|induction]].
> ```python
> def eulerian(graph):
> 	circuit = find_circuit(graph)
> 	if len(graph.edges) = len(circuit.edges):
> 		return true
> 	else:
> 		for subgraph in connected_components(graph):
> 			if eulerian(subgraph):
> ```