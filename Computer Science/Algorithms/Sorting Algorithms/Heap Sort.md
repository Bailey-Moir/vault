---
tags:
  - atom
  - comp
---
*Heap sort* sorts the list in place in two phases:
1. The unsorted list is [[Partitions|partitioned]] into a [[Binary Heaps|binary heap]], containing only the first element, and an unsorted list, containing everything else. Items are then [[Binary Heaps#Add|added]] to the [[Heaps|heap]] from the start of the unsorted list until the unsorted list is empty. This could be done faster with [[Heapify|heapify]].
1. The heap is [[Partitions|partitioned]] into a [[Binary Heaps|binary heap]], containing everything, and the empty sorted list. Items are then [[Binary Heaps#Remove|dequeued]] from the [[Heaps|heap]] into the start of the sorted list until the [[Heaps|heap]] is empty.
![500|center](heap-sort-example.excalidraw)
> [!note]- Analysis
> First phase: $n$ items [[Binary Heaps#Add|added]], each takes less than $\log_{2} n$ comparisons.
> Second phase: $n$ items [[Binary Heaps#Remove|removed]], each takes less than $2\log_{2} n$ comparisons.
> Worst case: $\mathcal{O}\left( n\log n \right)$