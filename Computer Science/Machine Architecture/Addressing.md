---
tags:
  - atom
  - comp
---
Each byte (not [[Words|word]]) has its own *address*. In opcode, there are 4 types of *addressing*:
1. **Immediate**
   Value stored in instruction
2. **Indirect**
   Inferred from the instruction to use either `X`, `Y`, or `Z`.
3. **Direct**
   Address is specified in instruction, where the whole following instruction is the 16-bit address (this is not really used anymore).
4. **Register**
   Register specified inside instruction (`R0`-`R31`).
