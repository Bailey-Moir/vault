---
tags:
  - atom
  - comp
---
A $\mathit{k}$*-d tree* is a [[Binary Trees|binary]] [[Partitions|partitioning]] [[Trees|tree]] where the split operation is performed cyclically along each axis using axis-aligned [[Hyperplanes|hyperplanes]].

> [!example]
> ![1000|center](k-d-tree-eg.excalidraw)

```python
def kd_tree(points, depth=0)
	if len(points) < A or depth > B: # for some A and B
		return Leaf(points)
	else:
		axis = depth % 2 # 2 is dimension
		sorted_points = sorted(points, key=lambda p: p[axis])
		mid = len(points) // 2
		median = points[mid - 1][axis]
		left = kd_tree(points[:mid], depth + 1)
		right = kd_tree(points[mid:], depth + 1)
		return Node(axis, median, left, right)
```