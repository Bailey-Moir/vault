---
tags:
  - atom
  - comp
---
$$O(\log n)$$
Best case: 1
Worst case: $O(\log n)$
```cpp
// searching for 'value' in sorted (ascending) vector 'vec' with type T
template<typename T>
auto fn = [](vector<T> vec, T value) {
	int l = 0,
		r = vec.size(); // n-1, len(vec) - 1
	while (l <= r) {
		int c = (l+r)/2; // integer division (//) in python
		if (value == vec[c]) return c;
		if (value < vec[c]) r = c - 1;
		else l = c + 1;
	}
	return -1;
};
```

```
# iterative
left = 0; right = n-1;
if middle element matches target
	return middle element
else if target less than middle element
	right = middle - 1
else
	left = middle + 1
```