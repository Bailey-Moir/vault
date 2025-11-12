---
tags:
  - atom
  - comp
---
![400|center](gpio-ports.excalidraw)
A *port* is used to refer to 8 pins, numbered 0-7, and *ports* are identified by letters. Each *GPIO port* has three [[Registers|registers]] associated with it.

- The **DDRx** [[Registers|register]] is the **data direction register**, which gives programmable bidirecitonality.
- The **PORTx** [[Registers|register]] gives the output state (if configured as an output),
- The **PINx** [[Registers|register]] gives the input state (if configured as an input),

where "**x**" is the port letter.

> [!definition]- **GPIO** is **general purpose input and output**, and its pins input or output $0$ or $1$.
