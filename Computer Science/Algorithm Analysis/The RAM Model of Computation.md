---
tags:
  - atom
  - comp
---
We measure the running time of an [[Algorithms|algorithm]] by counting the number of steps
it takes to complete.

- **Accessing memory takes a constant time.**
	```python
	x
	numbers[1002]
	name[-1]
	numbers[i]
	```
- **Basic arithmetic, and simple comparisons and assignments take a constant time.**
	```python
	a + b
	x <= 0
	x = 100_000
	data[i] = "abc"
	values = numbers # note this is not copying
	```
- **Loops take time proportional to the number of iterations**
	```python
	for x in numbers:    # takes len(numbers) steps
		s += x           # takes 2 steps 
	```
- **Subroutine calls take time equal to the time it takes to execute its body.**
	```python
	sum(numbers)    # takes len(numbers) steps
	```