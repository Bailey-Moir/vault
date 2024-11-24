---
tags:
  - atom
  - comp
---
An algorithm for finding all [[Primes|primes]] below or equal to $n$, with a time complexity of $\mathcal{O}(n\log\log n)$. 
```cpp
int n;
vector<bool> is_prime(n+1, true);
is_prime[0] = is_prime[1] = false;
for (int i = 2; i <= n; i++) 
	if (is_prime[i] && (long long) i * i <= n) 
		for (int j = i * i; j <= n; j += i) 
			is_prime[j] = false;
```