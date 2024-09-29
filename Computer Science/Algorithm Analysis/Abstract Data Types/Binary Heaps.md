---
tags:
  - atom
  - comp
---
A *binary heap* is a **complete** [[Binary Trees|binary tree]] [[Heaps|heap]], **complete** meaning there are no gaps between [[Nodes|nodes]] reading from top to bottom, left to right.
```avatar
image: Assets/excali/binary-heap-5.excalidraw.svg
description: |-
  The [[Binary Trees|binary]] and **complete** properties of *binary heaps* [[Logical Implication|imply]] that all *binary heaps* with $n$ [[Nodes|nodes]] have the same structure. For example, any *binary heap* with $5$ [[Nodes|nodes]] has the structure seen on the left. 

  \[[[Graph Isomorphism]]\]
```
*Binary heaps* are normally represented as an array/list. [[Nodes|Nodes]] are numbered top to bottom, left to right, giving the indices of the [[Nodes|nodes]] in the array.

It can be found that:
- the [[Parent, Children, and Sibling Nodes|children]] of a [[Nodes|node]] at $i$ are at $2i$ and $2i+1$.
- the [[Parent, Children, and Sibling Nodes|parent]] of a [[Nodes|node]] at $i$ is at `i//2` ($\left\lfloor \frac{i}{2} \right\rfloor$).

# Methods
## Adding Key
When adding a new key, the [[Nodes|node]] is placed at the end of the array/list (bottom right). If the [[Nodes|node]] does not satisfy the [[Heaps|heap]] property with its [[Parent, Children, and Sibling Nodes|parent]], the two are swapped. This process it repeated until the property is satisfied or the [[Nodes|node]] is the [[Root|root]]. This is called percolating up.
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
## Dequeue
When dequeuing, the value of the [[Root|root]] is saved to return. The [[Nodes|node]] at the end of the array/list (bottom right) then replaces the [[Root|root]]. If the [[Nodes|node]] does not satisfy the [[Heaps|heap]] property with its [[Parent, Children, and Sibling Nodes|children]], the [[Nodes|node]] and the *max/min* [[Parent, Children, and Sibling Nodes|child]] are swapped. This process is repeated until the property is satisfied or the [[Nodes|node]] is a [[Leaf Nodes|leaf]]. This is called percolating down.
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