---
tags:
  - atom
  - comp
---
A *binary **search** tree* (BST) is a [[Binary Trees|binary]] [[Search Trees|search tree]]: when adding an element `x` to a *binary search tree* node `node`,
- If `node` is None, set it to a new node with value `x`
- If `x < node.value`, the same process is done on `node.left`.
- If `x > node.value`, the same process is done on `node.right`.

```python
# this would be part of the BinaryNode class
def add(self, item):
	if item < node.value:
		if (node.left is None):
			node.left = new BinaryNode(item)
		else:
			node.left.add(item)
	else: # greater
		if (node.right is None):
			node.right = new BinaryNode(item)
		else:
			node.right.add(item)
```
# Best Case and Worse Case
b.c. $O(1)$
a.c. $O(\log n)$
w.c. $O(n)$