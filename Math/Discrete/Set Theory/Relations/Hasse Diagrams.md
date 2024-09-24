---
tags:
  - atom
  - math
  - discrete
---
![400|center](hasse-diagrams.excalidraw)
The *Hasse Diagram* for a [[Partial Order|partial order]] $\rel$^[[[Relations]]] on $A$ is a [[Graphs|graph]] with the properties:
- Each [[Vertices|vertex]] is labelled by an element of $A$.
- If $(a,b) \in \rel \land a \ne b$, $a$ is drawn below $b$.
- If $(a,b) \in \rel \land a \ne b$, an [[Math/Discrete/Graph Theory/Edges|edge]] connects them [[Logical Equivalence|iff]] there is no element $c$ such that $(a,c)\in\rel \land (c,b)\in\rel$.