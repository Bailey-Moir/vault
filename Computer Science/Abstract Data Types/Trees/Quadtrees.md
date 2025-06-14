---
tags:
  - atom
  - comp
---
A *quadtree* is a spatial [[Partitions|partition]] [[Trees|tree]] constructed such that until a region contains less than a specified number of points or a maximum depth is reached, the given node is subdivided into 4 equal squares.

```python
def quad_tree(points, centre, size, depth=0, max_leaf_points=2):
	points = [p for p in points if in_square(p, centre, size)]
	children = []
	if len(points) > max_leaf_points and depth < max_depth:
		for i in range(4):
			compute child_centre, child_size
			children.append(quad_tree(
				points, centre - Vec((-1)**Math.floor(i/2) * size/4,(-1)**i * size/4), size/2, depth + 1
			))
	return Node(points, centre, size, children)
```