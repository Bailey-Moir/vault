---
tags:
  - atom
  - comp
---
*Disjoint set union* is a method for creating and using [[Equivalence Classes|equivalence classes]].

```python
def find_set(a, parent): 
    if a != parent[a]:
        parent[a] = find_set(parent[a], parent)
    return parent[a]

def union_sets(a, b, parent, size): 
    a = find_set(a, parent)
    b = find_set(b, parent)

    if a == b:
        return False

    if size[b] > size[a]: 
        a, b = b, a

    parent[b] = a
    size[a] += size[b]
    return True

n = 15
parent = [i for i in range(n)]
size = [1 for _ in range(n)]
```

> [!example] [[Connectivitiy|Connectivity]]

\[[[Disjoint Sets]], [[Unions & Intersections]]\]