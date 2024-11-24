---
tags:
  - atom
  - comp
---
An $h$-sort [[Partitions|partitions]] the list by its indices into [[Equivalence Classes|equivalence classes]] (shells) [[Congruence|modulo]] $h$, and sorts each of those parts.

*Shell sort* works by performing a [[Sequences|sequence]] of decreasing $h$-sorts by [[Insertion Sort|insertion sort]], ending in a $1$-sort.

> [!complexity]-
> The time complexity varies depending on the gap [[Sequences|sequence]]. If it is chosen to be
$$\left\{ 2^{\lfloor \log_{2}n \rfloor -i} - 1 \right\}_{i=0}^{\lfloor \log_{2}n \rfloor -1} = \left\{ 2^{\lfloor \log_{2}n \rfloor} - 1, 2^{\lfloor \log_{2}n \rfloor-1} -1, \dots, 7, 3, 1 \right\}, $$
> then the time complexity has a **worst case** of $\mathcal{O}(n^{1.5})$.