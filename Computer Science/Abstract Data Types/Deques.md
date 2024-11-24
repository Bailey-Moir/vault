---
tags:
  - atom
  - comp
---
A *deque* is a a double sided [[Queues|queue]]. The most basic *deque* has four functions:
- `addFront(item)`
- `addRear(item)`
- `removeFront()`
- `removeRear()`

> [!example]- Meaning of Functions
> ```python
> dq = new Deque([1,2,3,4])
> dq.addFront(0)     # [0,1,2,3,4]
> dq.addRear(5)      # [0 1,2,3,4,5]
> dq.removeFront()   # [1,2,3,4,5]
> dq.removeRear()    # [1,2,3,4]
> ```

\[[[Queues]], [[Abstract Data Types]]\]