---
tags:
  - atom
  - comp
---
*Quick sort* splits the list such that everything in the left list is smaller than everything in the right. It then [[Recursion|recursively]] performs *quick sort* on these lists, and then simply adds them back together.

It splits by first picking a **pivot**. It then iterates through the original list, adding it to a new left list if it is smaller than the **pivot**, and adding it to a new right list if it is greater than the **pivot**. This is $\mathcal{O}(n)$.

- **Worst-case**
  If the **pivot** picked is always the smallest/largest value, $\mathcal{O}(n^2)$.
- **Average & Best-case** $\mathcal{O}(n\log n)$
- **Extra Space** $\mathcal{O}(1)$ (for in-place *quicksort*)

*Quick sort* has a costly split and an inexpensive join, while [[Merge Sort|merge sort]] has an inexpensive split and a costly merge/join.

# Median of Three
For the **pivot**, an estimate of the [[Median|median]] a list can be estimated as the [[Median|median]] of three of the values. When implementing this, we chose this as the first, middle, and last element.
# In-Place Quick Sort Partition
The pivot is swapped to the start of the list. Two pointers (`l` and `r`) at at each end of the list (ignoring the pivot) are created. 
- `l` increments through the list until its value is larger than the pivot.
- `r` decrements through the list until its value is smaller than the pivot.

The values at these pointers are then swapped, `l += 1` and `r -= 1`, and the pointers continue incrementing as before. This continues until the pointers cross over (`r <= l`).

```python
def partition(alist, first, last):
	pivotvalue = alist[first]
	
	l = first+1 # not pivot
	r = last

	while True:
		while l <= r and alist[l] <= pivotvalue:
			l += 1

		while l <= r and alist[r] >= pivotvalue:
			r -= 1

		if  r < l:
			break
		else:
			alist[l], alist[r] = alist[r], alist[l]
			l += 1
			r -= 1
	
	alist[first], alist[r] = alist[r], alist[first]
```