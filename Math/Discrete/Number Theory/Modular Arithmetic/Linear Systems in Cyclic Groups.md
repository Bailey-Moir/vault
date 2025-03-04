---
tags:
  - atom
  - math
  - discrete
  - linear
---
#TODO

> [!note] $ax \equiv b \mod n$ has a **unique** solution in $\Z_n$ iff $a$ is [[Invertibility|invertible]].

> [!example]- $$\begin{align}	2x \equiv 1 \mod 3 && (1)\\ 5x \equiv 2 \mod 7 && (2) \end{align}$$
> $(1)$ In $\Z_3$, we have $x = 2^{-1} = 2$, with solutions in $\Z$ of $x = 2 + 3k$.
> 
> $$\begin{align}
> 	5(2+3k) \equiv 2 \mod 7 \\
> 	10+15k \equiv 2 \mod 7 \\
> 	3+k \equiv 2 \mod 7 && \\
> 	k \equiv -1 \mod 7 \\
> 	k \equiv 6 \mod 7 \\
> \end{align}(2)$$
> In $\Z_7$, we have $k = 6$, with solutions in $\Z$ of $k = 6 + 7l$.
> 
> Thus, the solution set is given by
> $$ \{ 2 + 3(6+7l) : l \in \Z \} = \{ 20 + 21l : l \in \Z \} $$

\[[[Linear Systems]], [[Cyclic Groups]]\]