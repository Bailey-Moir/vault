---
tags:
  - atom
  - comp
---
*Insertion sort* works by creating a new list and iterating over the original list, adding each element to the new list in order.
- Best case of $n-1 = \mathcal{O}(n)$ as $n\to\infty$[^1].
- Average case of $T_{n-1}/2 = \mathcal{O}(n^2)$^[[[Triangular Numbers]]] as $n\to\infty$[^1].
- Worst case of $T_{n-1} = \mathcal{O}(n^2)$^[[[Triangular Numbers]]] as $n\to\infty$^[^1].

Insertion sort is mainly used for nearly sorted list.

[^1]: [[Landua's Big O Notation]]
[^2]: [[Triangular Numbers]]