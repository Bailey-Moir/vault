---
tags:
  - atom
  - math
  - discrete
---
Each letter is viewed as an element in $\Z_{26}$[^1], with $A=00, B=01, \dots, Z=25$. 
**Definition**: The *affine cipher* is a substitution cipher, where for some fixed $a,b \in \Z_{26}$[^1], each letter $x$ is to encrypted to
$$ e(x) = ax + b $$
in $\Z_{26}$[^1].

$e(x)$ is a [[Permutations|permutation]] of $\Z_{26}$[^1] iff $a$ is an [[Math/Discrete/Number Theory/Modular Arithmetic/Invertibility|invertible]] element of $\Z_{26}$[^1].
> [!proof]-
> $(\implies)$
> If $a=0$, the theorem holds.
> [[Proof by Contraposition|Contrapositive]]: if $a \in \Z_{26} \setminus \{0\}$ is not [[Math/Discrete/Number Theory/Modular Arithmetic/Invertibility|invertible]], then $e(x)$ ($ax+b$) is not a [[Permutations|permutation]].
> Assume that $a$ is not [[Math/Discrete/Number Theory/Modular Arithmetic/Invertibility|invertible]], then $a$ is a zero divisor, so there is some $z \in \Z_{26} \setminus \{0\}$ such that
> $$az = 0$$
> Write $z = t_1 - t_2$ for some $t_1,t_2 \in \Z_{26}$. Then 
> $$\begin{align*}
> 	a(t_1-t_2) &= 0 \\
> 	at_1 &= at_2 t_2 \\
> 	at_1+b &= at_2+bat_2+b \\
> \end{align*}$$
> Hence $x \to ax + b$ is not a [[Permutations|permutation]].
> ^this part did not make sense
> 
> $(\impliedby)$
> Assume $a$ is [[Math/Discrete/Number Theory/Modular Arithmetic/Invertibility|invertible]], then there is some $z \in \Z_{26}$ such that
> $$\begin{align*}
> 	az &= 1 \\
> 	az + b &= b + 1
> \end{align*}$$
> so $ax + b$ is a [[Permutations|permutation]].

[^1]:  [[Cyclic Groups]]