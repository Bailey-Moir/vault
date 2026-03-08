---
tags:
  - atom
  - math
  - discrete
---
If $G$ is a [[Simple Graphs|simple graph]], then 
$$\chi(G) \le \Delta +1 \hspace{2em} (1)$$
where $\Delta$ is the largest [[Vertices|degree]] of any [[Vertices|vertex]] in $G$ ($\Delta =\underset{v \in V(G)}{\text{max}}\,\delta(v)$).

\[$(1)$ [[Chromatic Numbers]]\]

> [!proof]- Is this bound sharp?
> In other words, are there any [[Graphs|graphs]] which achieve this [[Bounded Sets|bound]]?
>
> Let $C$ be a [[Sets|set]] of $\Delta + 1$ colours. To colour $G$, we colour the [[Vertices|vertices]] of $G$ one by one (the order is not important). We do this by assigning a colour from $C$ to a [[Vertices|vertex]] that it is not the colour of one of its [[Neighbourhoods|neighbours]]. Since any [[Vertices|vertex]] of $G$ has at most $\Delta$ [[Vertex Neighbourhoods|neighbours]], we can always choose an unused colour of $C$ to colour $v$.
> 
> Thus, the bound is sharp.

[^1]: [[Chromatic Numbers]]