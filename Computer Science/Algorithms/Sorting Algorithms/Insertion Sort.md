---
tags:
  - atom
  - comp
---
*Insertion sort* [[Partitions|partitions]] the list into a sorted list containing the first element, and an unsorted list containing everything else. The first item of the unsorted list is then inserted into the sorted list in order until the unsorted list is empty (similar to the first stage of [[Heap Sort|heap sort]]).
This is the same as [[Selection Sort|selection sort]], except instead of finding the element in the unsorted list to append to the sorted list, in *insertion sort*, given an element of the unsorted list, the location in the sorted list to insert the given element is found (instead of working with the unsorted list, it works with the sorted list).
- Best case of $n-1 = \mathcal{O}(n)$ as $n\to\infty$[^1].
- Average case of $T_{n-1}/2 = \mathcal{O}(n^2)$[^2] as $n\to\infty$[^1].
- Worst case of $T_{n-1} = \mathcal{O}(n^2)$[^2] as $n\to\infty$[^1].

Insertion sort is mainly used for nearly sorted list.

[^1]: [[Landua's Big Oh Notation]]
[^2]: [[Triangular Numbers]]