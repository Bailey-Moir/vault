---
tags:
  - atom
  - comp
---
- Load a lot of data into a structure
- **Map**: extract something you care about
- **Group by key**: sort/shuffle (if relevant)
- **Reduce**: aggregate, summarise, filter, or transform

> [!example]-
> ```ts
> A.map(x => sqrt(x))
> 	.reduce((x, y) => x + y, 0)
> ```