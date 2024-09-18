---
tags:
  - atom
  - comp
---
| Name    | Form  |
| ------- | ----- |
| Infix   | $a*b$ |
| Postfix | $ab*$ |
| Prefix  | $*ab$ |

Compiling [[Binary Operations|binary operations]] is often much easier with *postfix/prefix* as opposed to *infix* notation as they work very well with [[Stacks|stacks]]. Thus, *infix* notation is often converted into *postfix/prefix* notation.  

```
for each symbol s
	if s is an operand
		output s
	else if it is a left parenthesis
		push s
	else if it is a right parenthesis
		pop to output until corresponding left parenthesis popped
	else
		pop all greater than or equal precedance operators (check s) to output until top of stack is lower precedence operator or the stack is empty
		push s

pop all remaining operators to output
```