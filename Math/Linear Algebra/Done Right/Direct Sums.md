---
tags:
  - atom
  - math
---
Suppose $V_1, \dots, V_m$ are [[Subspaces|subspaces]] of $V$.
- The sum $V_1 + \dots + V_m$ is called a direct sum if each element of $V_1 + \dots + V_m$ can be written in only one way as a sum $v_1 + \dots + v_m$, where each $v_k \in V_k$.
- If $V_1 + \dots + V_m$ is a direct sum, then it is denoted $V_1 \oplus \dots \oplus V_m$, with the $\oplus$ notation serving as an indication that this is a direct sum.

> [!note] Conditions for a Direct Sum
> $$ V_1 + \dots + V_m \text{ is a direct sum} \iff \left( v_1 + \dots + v_m = 0 \implies v_1 = \dots = v_m = 0 \right)  $$
> > [!proof]-
> > ($\implies$)
> > Suppose $V_1 + \dots + V_m$ is a direct sum. This implies that there is only one way to write $0$. This then implies that this way is taking each $v_k \in V_k$ equal to 0.
> > 
> > ($\impliedby$)
> > Suppose the only way to write $0$ as a sum of $v_1 + \dots + v_m$ is by taking each $v_k \in V_k$ equal to 0. To show that $V_1 + \dots + V_m$ is a direct sum, let $v \in V_1 + \dots + V_m$. We can write
> > $$ v = v_1 + \dots + v_m $$
> > where $v_k \in V_k$. To show that this representation is unique, suppose we also have
> > $$ v = v'_1 + \dots + v'_m $$
> > where $v'_k \in V_k$. Subtracting these two equations, we have
> > $$ 0 = (v_1 - v'_1) + \dots + (v_m - v'_m) $$
> > Since $v_k - v'_k \in V_k$, the above equation matches the original proposition, and thus $v_k - v'_k = 0$. Thus $v_k = v'_k$, as desired.

> [!note] Condition for Direct Sum of Two Subspaces
> $$ U \cap V = \{0\} \iff U \oplus W $$

\[[[Sums of Subspaces]]\]