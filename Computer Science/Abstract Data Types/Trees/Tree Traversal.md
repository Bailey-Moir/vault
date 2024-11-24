---
tags:
  - atom
  - comp
---
# Pre-order
Left to right (e.g. outlines)
```python
def traverse_preorder(self, subtree)
	if subtree:
		print(subtree.value) # or perform given operation
		traverse_preorder(subtree.left)
		traverse_preorder(subtree.right)
```
# In-order
Gives smallest to largest
```python
def traverse_inorder(self, subtree)
	if subtree:
		traverse_inorder(subtree.left)
		print(subtree.value) # or perform given operation
		traverse_inorder(subtree.right)
```
# Post-order
```python
def traverse_preorder(self, subtree)
	if subtree:
		traverse_preorder(subtree.left)
		traverse_preorder(subtree.right)
		print(subtree.value) # or perform given operation
```

> [!note]- Flag Trick
> ![1000|center](tree-traversal-flag-trick.excalidraw)
> To visualize the different types of *tree traversals*, add a flag to the corresponding side of each [[Vertices|vertex]]:
> - left in [[#Pre-order|pre-order]].
> - bottom in [[#In-order|in-order]].
> - right in [[#Post-order|post-order]].
>
> Then imagine traveling around the [[Computer Science/Abstract Data Types/Trees/Trees|tree]] anti-clockwise starting at the top of the [[Root|root]], and operate (e.g. print) whenever you pass a flag.

\[[[Prefix, Infix, and Postfix Notation]]\]