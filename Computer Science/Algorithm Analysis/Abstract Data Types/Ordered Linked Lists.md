---
tags:
  - atom
  - comp
---
![600|center](ordered-linked-list.excalidraw)

An *ordered linked list* is a [[Linked Lists|linked list]] that is always ordered. The structure is the same, but the methods/functions that manipulate it are different.
- The `add` method is now $O(n)$[^1] instead of $O(1)$[^1], as it must search for the position in the sequence to insert the new node.

\[[[Linked Lists]], [[Abstract Data Types]]\]

[^1]: [[Asymptotic Analysis]]