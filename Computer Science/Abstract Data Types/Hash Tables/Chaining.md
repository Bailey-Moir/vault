---
tags:
  - atom
  - comp
---
Instead of filling slots with values, chaining fills them with [[Linked Lists|linked list]] nodes, and on collision, adds new values to the [[Linked Lists|linked list]]. This avoids [[Rehashing|rehashing]]. However, most programming languages use chaining with a maximum [[Load Factor|load factor]], e.g. 50%, at which point they [[Rehashing|rehashing]].

\[[[Hash Tables]]\]