---
tags:
  - atom
  - comp
---
![600|center](linked-list.excalidraw)

*Linked lists* are part of every advanced data structure. The principal benefit of a *linked list* over a conventional array is that the list elements can be easily inserted or removed **without reallocation or reorganization** of the entire structure, although data access becomes $\mathcal{O}(n)$. The most basic node in a linked list has:
- the `next` field, which gives the next node in the sequence. 
- the `value` field, which gives value stored in the current node. 

They can have methods such as:
- `add(value)`: Add value to the start of the sequence. 
> [!example]- Python Implementation
> ```python
> def add(self, item): # insert item at head of list
> 	temp = Node(item)
> 	temp.next = self.head
> 	self.head = temp
> ```
- `search(value)`: Check if a node with the value is in the sequence / Returns a node with the value if found.
> [!example]- Python Implementation
> ```python
> def search(self, item):
> 	current = self.head
> 	while current != None:
> 		if current.data == item:
> 			return True
> 			# or
> 			return current
> 		else:
> 			current = current.next
> 	return False
> 	# or
> 	return None
> ```

\[[[Abstract Data Types]]\]