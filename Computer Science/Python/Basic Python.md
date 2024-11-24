---
tags:
  - "#comp"
---

| Concept    | Definition                                                  |
| ---------- | ----------------------------------------------------------- |
| Statement  | A Python program is a sequence of statements, one per line. |
| Expression | A code fragment that can be 'worked out' to yield a value.  |
| Assignment | Sets the value of the LHS to that of the RHS.               |
| Identifier | The name given to a variable                                |
# Floats
Floating point numbers (`floats`) are approximate (unlike `ints`).
```python
print(10 ** 20 + 1.0 - 10 ** 20) # out: 0.0
```
# Program State
![1000|center](program-state-table.png)

```python
acceleration = 10
mass = 3
force = mass * acceleration
print(force)
```

The program has three components at any given time:
- The line number that was just executed.
- A set of known variables names and their values.
- The output from the robot so far in its execution.
<p class="note">Note: variables are listed in the order they are declared</p>
# Variable Naming
- A letter or underscore followed by zero or more alphanumeric or underscore characters
<p class="note" style="color:red;">(syntactic validity)</p>
## Pylint
I would write everything you need to look for, but just use `Pre-check`, and you'll be fine.
# F-Strings
```python
x = 1 / 3
y = 9 / 7
print(f"x = {x}")
print(f"x rounded to 2 decimal places: {x:.2f}")
print(f"point rounded to 3 dp: ({x:.3f}, {y:.3f})")
print(f"point: ({x}, {y})")
print(f"x + y = {x + y}")
```
There are many format specifiers (such as `:.3f`).
# Lambda Functions
`lambda params: return_value_expression`

```python
	square = lambda x : x * x
	print(square(17)) # out: 289
```
# Types
It should be noted that casting a `float` to an `int` removes the decimal, effectively flooring the float. `int(x)`$= \lfloor x \rfloor$ 
# Collections
## Sequences
Sequences can be:
- Iterated over with a `for in` loop (`for item in seq:`)
- Indexed (`seq[i]`).
- [[#Slicing|Sliced]] (`seq[1:3]`).
- Plugged into `len` (`len(seq)`)
There are 4 <u>types</u> of sequences.
- [[#Lists]]
- [[#Tuples]]
- Strings
- [[#Range]]
### Lists
Note that when a list is copied via assignment, the reference is passed and no new object is created, creating an alias. A copy of a list can be created using [[#Slicing|slicing]] in the form `arr[:]`.
<p class="note">Note: items in lists can have different types.</p>

### Tuples
Tuples are immutable. They are most often used to group distinct pieces of related information. For example, `(x,y)`, `(number, street, city, postcode)`.
<p class="note">Note: items in tuples can have different types.</p>

### Ranges
Just like [[#Slicing|slicing]], ranges include their start, but exclude their stop.
```python
print(list(range(1,5))) # out: [1, 2, 3, 4]
```
### Slicing
![500|center](slicing.excalidraw)
Just like in [[#Range|ranges]], slicing does not include the stop (the second subscript/index).
```python title:Examples
cities = ['Auckland', 'Wellington', 'Christchurch', 'Dunedin']
print(cities[1:3]) # out: ['Wellington', 'Christchurch']
print(cities[2:]) # out: ['Christchurch', 'Dunedin']
print(cities[:2]) # out: ['Auckland', 'Wellington']
print(cities[::2]) # out: ['Auckland', 'Christchurch']
```
### Parallel Assignment
```python
person = ('Angus', 'McGurk', 33)
first, last, age = person 	
```
This works for all [[#Sequences|sequences]], so also [[#Lists|lists]] and [[#Ranges|ranges]]. If the RHS fills the left hand side from left to right, so `x, y = (10, 20, 30)` sets `x` to `10` and `y` to `20`.

Parallel assignment can be used to return multiple values.
> [!example]-
> ```python title:Example
> def euclidean_division(dividend, divisor):
>     """ Takes two ints: dividend and divisor. Divides dividend by divisor 
> 	and returns the quotient and remainder as two separate integers. """
>     quotient = dividend // divisor
>     remainder = dividend % divisor
>     return (quotient, remainder)   # Return a tuple
> 
> num_apples = 11
> num_people = 4
> apples_per_person, leftover = euclidean_division(num_apples, num_people)  
> ```
## Dictionaries
```python
atomic_weights = {
    'H': 1.0080,
    'He': 4.00260,
    'Li': 7.0,
    'Be': 9.012183,
    'B': 10.81,
    'C': 12.011,
    'N': 14.007,
    'O': 15.999,
    'F': 18.9980
}

print(atomic_weights['Be']) # out: 9.012183
```
Note that the `in` operator checks if an item is a **key** in the dictionary.
### Looping Through Dictionaries
Looping is done in the form `for key, value in dict.items():` (note that it's `dict.items()` and not just `dict`).
### Dictionary Inversion
```python title:"Basic Dictionary Inversion"
def  dict_reverse(d):
    """ Inverses the given one-to-one dictionary """
    result = dict()
    for key, val in d.items():
        result[val] = key
    return inverse
```
<p class="note">Note: this function only works for one-to-one dictionaries</p>

```python title:"Advanced Dictionary Inversion"
def reverser(student_dict):
    """ Inverses the given dictionary, putting keys into lists """
    inverse = dict()
    
    for key, val in student_dict.items():
        if val in inverse:
            inverse[val].append(key)
            inverse[val].sort()
        else:
            inverse[val] = [key]
    
    return inverse
```
## Sets
> An unindexed, unordered collection of unique immutable elements of varying types.
<p class="note">Note: elements are immutable, not the collection.</p>

They are created like a list but with curly braces (e.g. `{10, 20, 30}`) or by plugging a sequence into the `set` cast function (e.g. `set(sequence)`).
```python title:"Modifying Sets"
bods = {'Carol', 'Bob', 'Ted', 'Alice'}
bods.add(42)     # Puts 42 into bods
bods.remove('Carol')  # Takes 'Carol' out of bods
```
Looping through sets is the same as looping through a sequence, except the order is arbitrary.
### `sorted()`
The built-in `sorted()` function takes a set and the set as a sorted list.
## `in` Operator
`in` can be used in `for in` loops, but it can also be used in the same way `.contains()` is used in other language.
```python title:Examples
print(3 in [1, 3, 5, 9, 7, 44]) # out: True
print(4 in [1, 3, 5, 9, 7, 44]) # out: False

print("i" in "Bart Simpson") # out: True

print("imp" in "Bart Simpson")  # out: True
print([3, 5] in [1, 3, 5, 10])  # out: False (!!!!!!!!!)
```
## Sets vs. Sequences vs. Dictionaries
Checking inclusion (using the `in` operator) on sets and dictionaries is a lot faster than on sequences, as sequences require a linear search of the list.
![500|center](python-collections-in.excalidraw)
# Constants
Python doesn't have a way to make constants, but the standard for **global** constants is to use capitals, e.g. `MAX_ROWS`. There is no differentiation in style of local constants and normal local variables.
Constants should be used in place of "magic numbers".
# Modules
``` python title:example
"""Demo of importing and using a module"""
import statistics
# or
from statistics import median

def print_median(numbers):
    """Print the count and median of the given list of numbers"""
    median_value = statistics.median(numbers)  # Call the median function
    print(f"{len(numbers)} numbers received")
    print(f"Median is {median_value:.3f}")

nums = [17.3, 19, 23.1, 11.6, 13.1, 15.6, 20.1, 9, 8.2, 22.1, 11.3, 16.3, 17.0]
print_median(nums)
```
`import` can be used to import local files as well as modules, prioritizing local files. For example, `import my_file` imports `my_file.py`.

# Files
```python
infile = open('mydatafile.txt')
```
The value returned by the `open` function is a _file object_. It can be loosely thought of as a "proxy" for the disk file itself, containing:
- a copy of the actual file's data in memory
- a bookmark to say where we're up to in that copy of the data.

It should not be confused with the _file name_, which is just the name given to the collection of data on disk.
## Processing an entire file at once
```python
infile = open('essay.txt')

# Read the entire contents of the file into the variable essay.
essay = infile.read()

infile.close()
```
## Writing to Files
```python
outfile = open(outfile_name, "w")
outfile.write(content)
outfile.close()
```
# Exceptions
## Try Except
```python
try:
	#
except: # Disallowed by pylint
	# handle errors

try:
	#
except TypeError:
	# handle type errors
except ValueError:
	# handle value erros
...
```
## Raising Exceptions
Errors are raised with the syntax `raise exception_object`, where exception objects are created by `exception_name(optional_message)`.
> [!example]-
> ```python
> def average(nums):
>     """Return the average of the given list of nums"""
>     if len(nums) == 0:
>         raise ValueError('average of empty list')
>     else:
>         return sum(nums) / len(nums)
> 
> print(average([10, 20, 30])) # Good call
> print(average([]))  # Bad call
> ```
# Object-Oriented Programming
```python
class MyClassName:
	""" Class description
	Data attributes: my_attribute_name: description 
					 ...
	Methods: my_method1(), ...
	"""
	MY_CONSTANT = 0

	def __init__(self, ...):
		self.my_attribute_name = 1
		...
	
	def my_method1(self, ...):
		...
```
## `__str__`
An optional method that allows the programmer to define a friendly way of print the value of an object. This function is called by the `str` function, and also by the `print` function.
## `__repr__`
A representation of the object. The only way I can think to explain this is the below example.
```python
def __repr__(self):
    """Returns a string representation of the Student object"""
    return f"Student('{self.name}', {self.student_id}, {self.invigilated}, {self.uninvigilated})"
```
## Arithmetic with Objects
Arithmetic operations are defined for objects using double underscore functions:
- `a == b` $=$ `a.__eq__(b)`
- `a != b` $=$ `a.__ne__(b)`
- `a < b` $=$ `a.__lt__(b)`
- `a <= b` $=$ `a.__le__(b)`
- `a > b` $=$ `a.__gt__(b)`
- `a >= b` $=$ `a.__ge__(b)`
- `a + b` $=$ `a.__plus__(b)`*
- `a - b` $=$ `a.__minus__(b)`*
- `a * b` $=$ `a.__????__(b)`*
- `a / b` $=$ `a.__????__(b)`*
- `a ** b` $=$ `a.__????__(b)`*
- `a // b` $=$ `a.__????__(b)`*
- `a % b` $=$ `a.__????__(b)`*
<p class="note">Note: none of these functions should modify either of the two operands</p>
# Doctests
Doctests don't output anything unless they fail.
```python
def fn(...):
	"""
	>>> fn(INPUT)
	DESIRED OUTPUT
	>>> fn(2, "x")
	2x
	"""

if __name == "__main__":
	import doctest
	doctest.testmod()
```