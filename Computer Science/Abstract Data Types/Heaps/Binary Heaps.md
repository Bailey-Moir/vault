---
tags:
  - atom
  - comp
---
A *binary heap* is a **complete** [[Binary Trees|binary tree]] [[Heaps|heap]], **complete** meaning there are no gaps between [[Vertices|vertices]] reading from top to bottom, left to right.
```avatar
image: Assets/excali/binary-heap-5.excalidraw.svg
description: |-
  The [[Binary Trees|binary]] and **complete** properties of *binary heaps* [[Logical Implication|imply]] that all *binary heaps* with $n$ [[Vertices|vertices]] have the same structure. For example, any *binary heap* with $5$ [[Vertices|vertices]] has the structure seen on the left. 
```
*Binary heaps* are normally represented as an array/list. [[Vertices|Vertices]] are numbered top to bottom, left to right, giving the indices of the [[Vertices|vertices]] in the array (with the [[Root|root]] being 1 not 0).

- The [[Parent, Children, and Sibling Nodes|children]] of a [[Vertices|vertex]] at $i$ are at $2i$ and $2i+1$.
- The [[Parent, Children, and Sibling Nodes|parent]] of a [[Vertices|vertex]] at $i$ is at $\left\lfloor \dfrac{i}{2} \right\rfloor$.
# Methods
## Add
When adding a new key, the [[Vertices|vertex]] is placed at the end of the array/list (bottom right). If the [[Vertices|vertex]] does not satisfy the [[Heaps|heap]] property with its [[Parent, Children, and Sibling Nodes|parent]], the two are swapped. This process it repeated until the property is satisfied or the [[Vertices|vertex]] is the [[Root|root]]. This is called percolating up.
```python
def queue(self, value):
	self._heap.append(value)
	cur_indx = len(self._heap) - 1
	while cur_indx // 2 >= 1: # not root
		parent_idx = cur_idx // 2
		if self._heap[parent_idx] > self._heap[current_idx]: # min heap
			self._heap[cur_idx], self._heap[parent_idx] = (self._heap[parent_idx], self._heap[cur_idx])
		cur_idx = parent_idx
```
> [!complexity]- Percolate Up
> 1 key comparison at each level.
> - **Worst case** $T(n) = T(\frac{n}{2}) + 1 =  \log_2 n = \mathcal{O}(\log n)$ as $n\to \infty$.[^1]
> - **Best case** $T(n) = 1 = \mathcal{O}(1)$ as $n\to \infty$.[^1]
## Remove
When dequeuing, the value of the [[Root|root]] is saved to return. The [[Vertices|vertex]] at the end of the array/list (bottom right) then replaces the [[Root|root]]. If the [[Vertices|vertex]] does not satisfy the [[Heaps|heap]] property with its [[Parent, Children, and Sibling Nodes|children]], the [[Vertices|vertex]] and the *max/min* [[Parent, Children, and Sibling Nodes|child]] are swapped. This process is repeated until the property is satisfied or the [[Vertices|vertex]] is a [[Leaf Nodes|leaf]]. This is called percolating down.
```python
def dequeue(self):
	result = self._heap[1]
	cur_idx = len(self._heap) - 1
	self._heap[cur_idx], self._heap[1] = (self._heap[1], self._heap[cur_idx])
	cur_idx = 1
	value = self._heap[cur_idx]
	while 2*cur_indx < len(self._heap): # not leaf
		l_indx = 2*cur_indx
		r_indx = l_indx+1
		l = self._heap[l_indx]
		r = self._heap[r_indx]

		# min heap
		if l <= r:
			if value > l: 
				self._heap[cur_idx], self._heap[l_indx] = (self._heap[l_indx], self._heap[cur_idx])
				cur_idx = l_indx
			else:
				break
		else:
			elif value > r
				self._heap[cur_idx], self._heap[r_indx] = (self._heap[r_indx], self._heap[cur_idx])
				cur_idx = r_indx
			else:
				break

	return result
```

\[[[Priority Queues]]\]
> [!complexity]- Percolate down
> 2 key comparisons at each level.
> - **Worst case** $T(n) = T(\frac{n}{2}) + 2 =  2 \log_2 n = \mathcal{O}(\log n)$ as $n\to \infty$.[^1]
> - **Best case** $T(n) = 2 = \mathcal{O}(1)$ as $n\to \infty$.[^1]

[^1]: [[Landua's Big Oh Notation]]