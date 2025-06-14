---
tags:
  - atom
  - comp
---
A *line-sweep [[Algorithms|algorithm]]* simulates the *sweeping* of a [[Hyperplanes|hyperplane]] (vertical line in $xy$-plane) across objects in one direction (no backing up). This is done by sorting the objects in ascending order of $x$-coordinates.

This is a type of [[Dynamic Programming|bottom-up dynamic programming]], as at any stage in the *sweep*, we know the solution to the problem for all points to the left of the line/[[Hyperplanes|hyperplane]].