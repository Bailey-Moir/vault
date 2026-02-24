---
tags:
  - atom
  - comp
---
## Map
*Map* takes elements of arbitrary type from [[Distributed File Systems|chunks]], and *maps* them to **any number** of key-value pairs. The output does not act as a dictionary, but simply as a list of pairs.

Technically, it maps key-value pairs to key-value pairs as to allow [[Composite Functions|composition]], but the keys inputted into the first map are normally irrelevant.
## Group by Key
Each $(v,k_{1}), \dots, (v,k_{n})$ is *grouped by their key* into $\left( v, \left[ k_{1},\dots,k_{n} \right] \right)$.
## Reduce
*Reduce* applies its **reducer** to each key-value**s** pair $\left( v, \left[ k_{1}, \dots, k_{n} \right] \right)$, and for each, gives **any number** of arbitrary key-value pairs.

> [!example]-
> ```ts
> A.map(x => sqrt(x))
> 	.reduce((x, y) => x + y, 0)
> ```