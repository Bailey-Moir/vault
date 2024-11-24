---
tags:
  - atom
  - comp
---
## Cons of Lists
- When a Python list reaches its maximum, it reallocates the memory (with more bytes), copying the links to the elements into the new memory.
- If you want to prepend something to a list in Python, Python shifts every element to the right.
- Python lists have extra memory used in case more data is appended.

## Cons of Linked Lists
- Data access time is $O(n)$, because accessing any node requires that the prior node to first be accessed 

\[[[Linked Lists]]\]