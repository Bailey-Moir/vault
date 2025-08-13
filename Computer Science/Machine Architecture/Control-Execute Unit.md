---
tags:
  - atom
  - comp
---
The *control/execute unit* of the [[CPU|CPU]]  instructs other units to carry out instructions (e.g. controlling the operations on the [[ALU|ALU]], the flow of data into it from the [[Registers|registers]]), specifically:
1. Loading the next instruction from memory and interpreting it as a finite state machine.
2. Loading the correct variables into the registers from memory.
3. Loading the variables into the [[ALU|ALU]] from the registers.
4. Instructing the [[ALU|ALU]] which operation to perform, and when.
5. Storing the output of the [[ALU|ALU]] operation in the correct register.