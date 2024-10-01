---
tags:
  - atom
  - math
  - discrete
---
A [[Walks|cycle]] that traverses each [[Vertices|vertex]] of a [[Graphs|graph]] **exactly once** is called a *Hamiltonian cycle*.
A connected [[Graphs|graph]] is *Hamiltonian* if it contains one of these [[Walks|cycles]].
> [!note]- Similarity to [[Eulerian Circuits and Graphs|Eulerian Circuits]]
> This has the same as the definition as [[Eulerian Circuits and Graphs|Eulerian circuits]], except *Hamiltonian cycles* traverse each **[[Vertices|vertex]]** (not [[Math/Discrete/Graph Theory/Definitions/Edges|edge]]) exactly once, and thus they are [[Walks|cycles]] not [[Walks|circuits]].
- If a [[Walks|cycle]]/[[Graphs|graph]] is *Hamiltonian*, it must be [[Eulerian Circuits and Graphs|Eulerian]]. Note the [[Converse, Inverse, and Contrapositive|contrapositive]] is true.
- The only [[Walks|cycle]] contained in a [[Walks|cycle]] is itself, which is somehow helpful.
- Let $G$ is a [[Simple Graphs|simple graph]] with $n$ [[Vertices|vertices]], where $n\ge 3$. If the [[Vertex Degrees|degree]] of each [[Vertices|vertex]] is at least $n/2$, $G$ is *Hamiltonian*.