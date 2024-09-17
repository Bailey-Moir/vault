---
tags:
  - atom
  - comp
---
A *hash table* is an array of allocated memory called **slots**. Values being stored in the table are designated slots based on the [[Hash|hash]] of their value.
```python
# simplified idea 
mytable[hash(value)%slots] = value
```

- Hash tables are most efficient when you already know the range of values, as this can be considered when designing the hash function.

\[[[Abstract Data Types]]\]