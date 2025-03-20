---
tags:
  - atom
  - math
  - discrete
---
![300|center](discrete-logarithm-problem.excalidraw)

 Given a [[Group Generators|generator]] $g$ of a [[Cyclic Groups|cyclic group]] $G$ and $h \in G$, compute $\log_{g}h$ (the [[Powers in Groups|power]] of $g$ that gives $h$).

 > [!definition]- *Discrete Logarithm*
Let $G$ be a finite [[Cyclic Groups|cyclic group]] with a [[Group Generators|generator]] $g \in G$, and let $h \in G$. We say that an integer $x \in \Z_{\left| G \right|}$ is the *discrete logarithm* of $h$ to base $g$ iff
$$g^x = h \iff x = \log_{g}h.$$
> Note $\mathit{x}$ must exist and be unique.

> [!note] The *discrete logarithm problem* is easy in any [[Groups|group]] using a quantum computer.