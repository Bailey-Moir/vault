---
tags:
  - atom
  - math
  - discrete
---
![400|center](hasse-diagrams.excalidraw.md)
The *Hasse Diagram* for a [[Partial Order|partial order]] $\rel$[^1] on $A$ is a [[Graphs|graph]] with the properties:
- Each [[Vertices|vertex]] is labelled by an element of $A$.
- If $(a,b) \in \rel \land a \ne b$, $a$ is drawn below $b$.
- If $(a,b) \in \rel \land a \ne b$, an [[Edges|edge]] connects them iff there is no element $c$ such that $(a,c)\in\rel \land (c,b)\in\rel$.

[^1]: [[Relations]]
