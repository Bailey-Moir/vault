---
tags:
  - atom
  - comp
---
The *control registers* of the [[CPU|CPU]] store meta-information. The **status register** is a single [[Registers|register]] show below
![500|center](special-purpose-register.excalidraw)
that stores flags such as:
• **Carry Flag** (`C`): This indicates a carry in an arithmetic or logic operation.
• **Zero Flag** (`Z`): This indicates a zero result in an arithmetic or logic operation.
• **Negative Flag** (`N`): This indicates a negative result in an arithmetic or logic operation.

The other [[Registers|registers]] of the *control register* contain
• **Program Counter** (**PC**): The address of the next instruction in the program memory. 
• **Stack pointer** (**SP**): The address of the “top of the stack”, which is used for dynamic
variable handling.