---
tags:
  - atom
  - comp
---
*Syntax diagrams* can be used to represent (extended) [[Syntax Analysis|BNF]] [[Context-Free Grammars|grammar]] rules.
- Rectangles represent non-terminals, and ovals represent terminals.
- Each rectangle has exactly one incoming and outgoing arrow.
- Arrows represent sequence, choice, and iteration.

> [!example]- $Factor = (Expression) \,|\,\text{number}\,|\,\text{identifier}$
> ![800|center](syntax-tree-1.excalidraw)

> [!example]- $Expression = Term \, (Additive\, Term)^*$
> ![800|center](syntax-tree-2.excalidraw.md)

