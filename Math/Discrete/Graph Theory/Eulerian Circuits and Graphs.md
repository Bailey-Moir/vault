---
tags:
  - atom
  - math
  - discrete
---
A [[Walks|circuit]] that traverses each [[Edges|edge]] of the [[Math/Discrete/Graph Theory/Graphs|graph]] **exactly once** is called a *Eulerian circuit*. A [[Connectivitiy|connected]] [[Math/Discrete/Graph Theory/Graphs|graph]] is *Eulerian* if it contains one of these [[Walks|circuits]].
> [!note]- Similarity to [[Hamiltonian Cycles and Graphs|Hamiltonian Cycles]]
> This has the same as the definition as [[Hamiltonian Cycles and Graphs|Hamiltonian cycles]], except *Eulerian circuits* traverse each **[[Edges|edge]]** (not [[Vertices|vertex]]) exactly once, and thus they are [[Walks|circuits]] not [[Walks|cycles]].
- A [[Connectivitiy|connected]] [[Math/Discrete/Graph Theory/Graphs|graph]] $G$ is *Eulerian* iff $\forall v \in V(G),2|\delta(v)$
> [!proof]- 
> $\left( \implies \right)$
> Each visit to a [[Vertices|vertex]] $v$ uses an [[Edges|edge]] to enter and an [[Edges|edge]] to exit. Therefore
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
- A [[Connectivitiy|connected]] [[Math/Discrete/Graph Theory/Graphs|graph]] $G$ has a *Eulerian [[Walks|trail]]* iff $\left| \left\{ v \in V(G) : \neg 2|\delta(v) \right\} \right| \le 2$