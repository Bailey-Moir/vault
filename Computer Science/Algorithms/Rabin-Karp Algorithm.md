---
tags:
  - atom
  - comp
---
Suppose you have a [[Strings|string]] $T \in \Sigma^*$ to search for a pattern $P \in \Sigma^*$, where $m = \left| P \right| \le \left| T \right| = n$.

The *Rabin-Karp* [[Algorithms|algorithm]] [[Hash|hashes]] the pattern [[Strings|string]] $P$, and compares the [[Hash|hash]] of the current window [[Strings|string]] $W$ with the pattern [[Hash|hash]]. This would normally still be $O(nm)$, as computing the [[Hash|hash]] of a [[Strings|string]] is normally $O(n)$, but the special thing that *Rabin-Karp* does, is it computes the [[Hash|hash]] of the window from the last one in $O(1)$.

> [!definition] *Rabin-Karp* (Rolling) [[Hash|Hashing]] [[Functions|Function]]
> If $t_{i}\dots t_{i+m-1}$ is the text in the window,
> $$\text{hash}(t_{i}\dots t_{i+m-1}) = \left( t_{i}2^{m-1} + t_{i+1}2^{m-2} + \dots + t_{i+m-1}2^0\right) \mod q$$
> where $q$ is a large [[Primes|prime]] number.
> 
> Then the next [[Hash|hash]] is given [[Recursion|recursively]] by
> $$\text{hash}(t_{i+1}\dots t_{i+m}) = \left( 2\times\text{hash}(t_{i}\dots t_{i+m-1}) - t_{i}2^m + t_{i+m} \right) \mod q$$
> ## Optimizations
> - The [[Hash Tables|collisions]] can be reduced by using a base $b$ instead of $2$ such that $b > \left| \Sigma \right|$ .
> - $2^m \mod q$ (or $b^m \mod q$) can be pre-computed.

```python
BASE = 256
Q = 15487469 # Any largish prime

def rabin_karp_search(pat, text):
	m, n = len(pat), len(text) # hash value for pattern
	i = j = 0
	hash_p = 0
	hash_t = 0
	h = 1
	
	for i in range(m):
		h = (h * BASE) % Q # b^m % q
		hash_p = (BASE * hash_p + ord(pat[i])) % Q # pattern hash
		hash_t = (BASE * hash_t + ord(text[i])) % Q # window hash at i = 0
		
	for i in range(n - m + 1): # each window position
		if hash_p == hash_t:
			if pat == text[i : i + m]: # char-by char comparison only on hash hit
				print("Pattern found at index " + str(i))
		if i < n - m:
			hash_t = (Q + BASE * hash_t - ord(text[i]) * h + ord(text[i + m])) % Q # Update hash
```