---
tags:
  - atom
  - math
  - discrete
---
![1000|center](unions-and-intersections.excalidraw.md)
$$\begin{array}{cl}
	\forall A,B, \left( A \cup B = \left\{ x: x \in A \lor x \in B \right\} \right) & \text{Union}\\
	\forall A,B, \left( A \cap B = \left\{ x: x \in A \land x \in B \right\} \right) & \text{Intersection}
\end{array}$$
# Properties of Unions
$\forall A,B,C,$
- $A \subseteq A \cup B \textcolor{gray}{\land B \subseteq A \cup B}$
- $A \subseteq B \iff A \cup B = B$
- $A \cup B \subseteq C \iff A \subseteq C \land B \subseteq C$
# Properties of Intersections
$\forall A,B,C,$
- $A \cap B \subseteq A \textcolor{gray}{\land A \cap B \subseteq B}$
- $A \subseteq B \iff A \cap B = A$
- $C \subseteq A \cap B \iff C \subseteq A \land C \subseteq B$