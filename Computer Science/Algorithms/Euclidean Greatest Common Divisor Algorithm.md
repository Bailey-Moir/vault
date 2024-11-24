---
tags:
  - atom
  - comp
---
An algorithm for finding the greatest common divisor, with a time complexity of $O( \log \min(a,b) )$.
```cpp
int gcd(int a, int b) {
	if (b == 0) 
		return a; 
	else 
		return gcd(b, a % b);
}
// OR
int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }
```

\[[[The Euclidean Algorithm]]\]