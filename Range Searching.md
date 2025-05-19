---
tags:
  - atom
  - comp
---
## 1-dimensional
Create a [[Binary Search Trees|binary search tree]] that has the [[Median|median]]\* attached to each non-[[Leaf Nodes|leaf node]]. For such a [[Vertices|node]] with [[Median|median]] $m$, the left subtree contains numbers $\le m$ and the right subtree contains number $> m$ . This [[Binary Search Trees|BST]] can then be searched using the following [[Algorithms|algorithm]].

```
function search(range, tree):
	if tree is a leaf node:
		return [tree.value] if value is in range else []
	else: # it is an interval node
		items = []
		if range.min <= node.value:
			items += search(range, tree.left)
		if range.max > node.value:
			items += search(range, tree.right)
		return items
```

![[Pasted image 20250519112815.png]]

