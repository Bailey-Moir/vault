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

However, the space can be reduced to linear using the following algorithm.
#TODO