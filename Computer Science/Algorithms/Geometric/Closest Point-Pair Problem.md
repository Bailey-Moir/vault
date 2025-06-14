---
tags:
  - atom
  - comp
---
Given a [[Sets|set]] of $n$ [[Points|points]], find a pair of [[Points|points]] $P$ and $Q$ with minimum distance from each other.
![500|center](closest-point-pair-problem.excalidraw)
Imagine a vertical line/[[Hyperplanes|hyperplane]] [[Line-Sweep Algorithms|sweeping]] through the points, and a **frontier set** defined by being with the minimum distance behind the line/[[Hyperplanes|hyperplane]]. Only points in this **frontier set** need to be checked when the line/[[Hyperplanes|hyperplane]] moves.

This can be optimised by only doing the length squared comparison with each point in the **frontier set** if the [[Absolute Values|absolute]] difference in $y$-coordinates is less or equal to $d$ as well.

This can be done efficiently using a self-balancing [[Binary Trees|binary tree]].