---
tags:
  - atom
  - comp
---
- **Map**
  extract something you care about
- **Group by key**
  sort/shuffle
- **Reduce**
  aggregate, summarise, filter, or transform

> [!example]-
> ```ts
> A.map(x => sqrt(x))
> 	.reduce((x, y) => x + y, 0)
> ```