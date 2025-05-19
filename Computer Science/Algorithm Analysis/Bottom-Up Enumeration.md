---
tags:
  - atom
  - comp
---
*Bottom-up enumerations* tabulates in ascending order.

> [!example]- [[Fibonacci Sequence|Fibonacci Numbers]]
> ```py
> def fib(n):
> 	mem = [0]*(n+1)
> 	mem[1] = 1
> 	
> 	for i in range(2, n+1):
> 		mem[i] = mem[i-1] + mem[i-2]
> 	
> 	return mem[n]
> ```
> which can be optimized to
> ```py
> def fib(n):
> 	a, b = 0, 1
> 	for i in range(n):
> 		a, b = b, a + b
> 	return a
> ```