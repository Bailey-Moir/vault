---
tags:
  - atom
  - comp
---
A *min/max priority queue* is a type of [[Queues|queue]] where `dequeue()` pops the **minimum/maximum** value.

|                 | $1$ insert            | $1$ remove            | $n$ of each            | *Algorithm*                          |
| --------------- | --------------------- | --------------------- | ---------------------- | ------------------------------------ |
| Sorted List     | $\mathcal{O}(n)$      | $\mathcal{O}(1)$      | $\mathcal{O}(n^2)$     | *[[Insertion Sort\|Insertion sort]]* |
| Unsorted List   | $\mathcal{O}(1)$      | $\mathcal{O}(n)$      | $\mathcal{O}(n^2)$     | *[[Selection Sort\|Selection sort]]* |
| [[Heaps\|Heap]] | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(n\log n)$ |                                      |

\[[[Abstract Data Types]]\]