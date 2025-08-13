---
tags:
  - atom
  - comp
---
A *decoder* converts a [[Binary|binary number]] with maximum value $n$ into $n$ outputs, where the $i$-th outputs is on iff the [[Binary|binary number]] is representing $i$.

> [!example]  2-bit *decoder*
> | $A_{1}$ | $A_{0}$ | $O_{1}$ | $O_{2}$ | $O_{3}$ | $O_{4}$ |
> | ------- | ------- | ------- | ------- | ------- | ------- |
> | 0       | 0       | 1       | 0       | 0       | 0       |
> | 0       | 1       | 0       | 1       | 0       | 0       |
> | 1       | 0       | 0       | 0       | 1       | 0       |
> | 1       | 1       | 0       | 0       | 0       | 1       |

As expected, an *encoder* does the [[Inverse Functions|inverse]].