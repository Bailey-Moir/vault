Given a list of [[Points|points]] $\{ p_{i} \}$
1. Select a [[Points|point]] $A$ with minimum $y$ as the starting point (anchor).
2. Sort all points in [[Signed Area|counter-clockwise]] order.

```py
from functools import cmp_to_key

# Converts a cmp function to a key function
def cmp(p1, p2):
	v1 = p1 - anchor
	v2 = p2 - anchor
	
	if v1.lensq() == 0:
		return -1
	if v2.lensq() == 0:
		return +1
		
	return v2.x * v1.y - v1.x * v2.y # negative signed area

simply_poly = sorted(points, key=cmp_to_key(cmp))
```