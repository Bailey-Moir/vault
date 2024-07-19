---
tags:
  - atom
  - comp
---
$$O(\log n)$$
```cpp
// searching for 'value' in sorted (ascending) vector 'vec' with type T
template<typename T>
auto fn = [](vector<T> vec, T value) {
	int l = 0,
		r = vec.size();
	while (l <= r) {
		int c = (l+r)/2;
		if (vec[c] == value) return c;
		if (vec[c] > value) l = c + 1;
		else r = c - 1;
	}
	return -1;
};
```