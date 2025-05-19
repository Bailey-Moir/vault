---
tags:
  - atom
  - comp
---
```
    0   1   2   3   4
  +---+---+---+---+---+
0 | 6 | 7 | 4 | 7 | 8 |
  +---+---+---+---+---+
1 | 7 | 6 | 1 | 1 | 4 |
  +---+---+---+---+---+
2 | 3 | 5 | 7 | 8 | 2 |
  +---+---+---+---+---+
3 | 2 | 6 | 7 | 0 | 2 |
  +---+---+---+---+---+
4 | 7 | 3 | 5 | 6 | 1 |
  +---+---+---+---+---+
```

Given an array $W_{i,j}$ of the above form and two points, one in the top row, one in the bottom. Find the path that minimises the total weight, only using moves that go down (may be diagonal).

> [!solution]
> Let $C_{i,j}$ be the optimal cost of getting to square $(i,j)$. Then
> $$C_{i,j} = \left\{\begin{array}{lr}
> 	W_{i,j} & \text{if } i = 0 \\
> 	W_{i,j} + \underset{k \in \{ j-1, j, j+1 \}}{\min} C_{i-1,k} & \text{if } i \ne 0 \\
> \end{array}\right.$$