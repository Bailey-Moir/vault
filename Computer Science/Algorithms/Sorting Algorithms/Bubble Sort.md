---
tags:
  - atom
  - comp
---
*Bubble sort* works by going through the list backwards, swapping adjacent elements if they are out of order.
- The best, average, and worst case are all $T_{n-1} = \mathcal{O}(n^2)$[^1] as $n\to\infty$.[^2]
- This is worse than [[Selection Sort|selection sort]] as it swaps a lot of data.
```python
def bubble_sort(alist):
	comparisons = 0
	for passnum in range(len(alist)-1,0,-1):
		for i in range(0,passnum):
			comparisons += 1
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
```

# Short Bubble Sort
*Short bubble sort* is *bubble sort* that stops when no swaps are performed. For this variation, the best case is $n-1 = \mathcal{O}(n)$ as $n\to\infty$.[^1]

[^1]: [[Triangular Numbers]]
[^2]: [[Landua's Big Oh Notation]]