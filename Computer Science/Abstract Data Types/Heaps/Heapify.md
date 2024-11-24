---
tags:
  - atom
  - comp
---
*Heapify* (or *fast-heapify*) converts a list into a [[Heaps|heap]]. Slow-heapify does this by performing the `enqueue` operation on every item of the list, taking $\mathcal{O}(n\log n)$. *Heapify* does this in $\mathcal{O}(n)$.

*Heapify* operates on the list in-place, checking the [[Heaps|heap property]] on each [[Vertices|vertex]] from back to front (starting with the [[Parent, Children, and Sibling Nodes|parents]] of [[Leaf Nodes|leaf nodes]]), and [[Binary Heaps#Remove|percolating down]] when it is not met.

```python
def heapify(self, alist):
	self._heap = [None] + alist[:]
	self.size = len(alist)
	i = self.size // 2 # parent of last node (first non-leaf)
	while i >= 1:
		self._perc_down(i)
		i -= 1
```