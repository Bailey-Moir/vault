---
tags:
  - atom
  - math
  - linear
---
*Row reduction* applies a series of **row operations** that preserve the [[Linear Independence|linear independence]] of the columns. These are:
 - **Adding non-zero multiples**
   $R_n \leftarrow R_n + kR_m \hspace{1em} \text{s.t. } k \ne 0$
 - **Multiplying by non-zero constants**
   $R_n \leftarrow kR_m \hspace{1em} \text{s.t. } k \ne 0$
 - **Swapping**
   $R_n \leftrightarrow R_m$
 
> [!note]- *Row reductions* do not affect [[Linear Independence|linear independence]]. Once in [[EF & REF|REF]], the columns with [[Pivots and Free Variables|pivots]] form a [[Vector Bases|basis]] of the [[Column Space|column space]].