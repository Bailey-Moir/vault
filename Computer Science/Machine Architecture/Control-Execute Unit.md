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

> [!-] There are three types of instructions:
> 1. Data transfer
> 2. Arithmetic/Logic
> 3. Branching

> [!-]- Complete instruction set vs. reduced instruction set
> | CISC                                                         | RISC |
> | ------------------------------------------------------------ | ---- |
> | [[ALU\|ALU]] operations access [[Registers\|registers]] and memory | [[ALU\|ALU]] operations access [[Registers\|registers]] only |
> | Variable instruction length | Separate data transfer function |
> | Variable clock cycles per instruction | One clock cycle per instruction |