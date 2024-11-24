---
tags:
  - comp
  - atom
---
```cpp
bool isPrime(int x) {
	for (int d = 2; d * d <= x; d++)
		if (x % d == 0) 
			return false; 
	
	return x >= 2;
}
```