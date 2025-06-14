---
tags:
  - atom
  - math
  - discrete
---
The *longest increasing subsequence* (*LIS*) can be solved in $O(n^2)$ time (and space) using [[Longest Common Subsequence|LCS]]:

> [!algorithm]
> Given a list $A$
> 1. Let $B$ be a sorted copy of $A$.
> 2. Run [[Longest Common Subsequence|LCS]] on $A$ and $B$,
> Thus result will be the *LIS*.

However, the space complexity can be reduced to be linear using the following [[Algorithms|algorithm]], which you can just guess the code for looking at the following example.

> [!example]- 8927406
> 
> | $i$    | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
> | ------ | --- | --- | --- | --- | --- | --- | --- |
> | $S[i]$ | 8   | 9   | 2   | 7   | 4   | 0   | 6   |
> | $L[i]$ | 1   | 2   | 1   | 2   | 2   | 1   | 3   |
> | $K[i]$ | -1  | 1   | -1  | 3   | 3   | -1  | 5   |
> 
> Thus, the *longest increasing subsequence* has length $3$, and the one described with $K$ is `2,4,6`.