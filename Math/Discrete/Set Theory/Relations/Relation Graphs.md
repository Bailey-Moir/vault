---
tags:
  - atom
  - math
  - discrete
---
Relations $\rel \in A^2$^[[[Cartesian Product]]] can be represented with an [[Weighted Graphs|unweighted]] [[Directed Graphs|directed graph]] permitting loops, with $E = \rel$.

> [!note] Representation of [[Reflexive Property|Reflexive Property]]
> ![300|center](graph-loops.excalidraw)
> $\rel \in A^2$ is [[Reflexive Property|reflexive]] [[Logical Equivalence|iff]] there is a loop on every [[Vertices|vertex]].

> [!note] Representation of [[Symmetric Property|Symmetric Property]]
> ![300|center](inverted-edges.excalidraw)
> $\rel \in A^2$ is [[Symmetric Property|symmetric]] [[Logical Equivalence|iff]] there is an [[Inverted Edges|inverted edge]] for every [[Math/Discrete/Graph Theory/Definitions/Edges|edge]].

> [!note] Representation of [[Antisymmetric Property|Antisymmetric Property]]
> $\rel \in A^2$ is [[Antisymmetric Property|antisymmetric]] [[Logical Equivalence|iff]] there are no [[Inverted Edges|inverted edges]] (excluding loops).

> [!note] Representation of [[Transitive Property|Transitive Property]]
> ![300|center](transitive-graphs.excalidraw)
> $\rel \in A^2$ is [[Transitive Property|transitive]] [[Logical Equivalence|iff]], if there is an [[Math/Discrete/Graph Theory/Definitions/Edges|edge]] from $a$ to $b$ and $b$ to $c$, then there is an [[Math/Discrete/Graph Theory/Definitions/Edges|edge]] from $a$ to $c$ (a shortcut).