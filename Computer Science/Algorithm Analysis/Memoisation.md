---
tags:
  - atom
  - comp
---
*Memoisation* is storing calculates values for future use. It can be generalised with

```python
def memoise(f):
	mem = {}
	
	def new_func(*args):
		if args not in mem:
			mem[args] = f(*args)
		return mem[args]
		
	return new_func
```

This function already exists in python as `lru_cache`, which is normally used as a [[Python Decorators|decorator]].

> [!example]- [[Fibonacci Sequence|Fibonacci Numbers]]
> When calculating the the $n$-th [[Fibonacci Sequence|Fibonacci number]], the naive approach
> ```python
> def fib(n):
>     if n < 2:
>         return n
>     else:
>          return fib(n-1) + fib(n-2)
> ```
> can be improved by *memoising* the output of the function, which takes the function from $\Theta(\varphi^n)$ to $\Theta(n)$\* time.
> ```python
> mem = {0:0, 1:1}
> 
> def fib(n):
> 	if n not in mem:
> 		mem[n] = fib(n-1) + fib(n-2)
> 
> 	return mem[n]
> ```
> or
> ```python
> @lru_cache(maxsize=None) # None => ∞
> def fib(n):
>     if n < 2:
>         return n
>     else:
>          return fib(n-1) + fib(n-2)
> ```
> 
> \[[[Asymptotic Notation]]\]
