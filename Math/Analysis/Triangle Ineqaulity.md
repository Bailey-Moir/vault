---
tags:
  - atom
  - math
---
The *triangle inequality* (1.11) for [[Absolute Values|absolute values]] states that for all $a,b \in \R,$
$$\left| a+b \right| \le \left| a \right| + \left| b \right|$$
Note this makes the *absolute value* a [[Norms|norm]] on $\R$.

> [!proof]-
> By [[Absolute Values|theorem 1.10]] (or [[Absolute Values|1.9.2]]),
> $$\begin{array}{rcr}
> 	a \le \left| a \right| && b \le \left| b \right|  \\
> 	-a \le \left| a \right| && -b \le \left| b \right|.
> \end{array}$$
> adding along each rows gives
> $$\begin{align}
> 	a + b &\le \left| a \right| + \left| b \right| \\
> 	-a-b= -(a + b) &\le \left| a \right| + \left| b \right| \\
> \end{align}$$
> Thus, $\left| a+b \right| \le \left| a \right| + \left| b \right|$.

> [!corollary]- **1.12.1** $\forall x,y \in \R, \left| x-y \right| \ge \left| \left| x \right| - \left| y \right| \right|$
> $$\begin{align}
> 	x &= x - y + y \\
> 	\left| x \right| &= \left| \left( x - y \right) + y \right|  \\
> 	&\le \left| x - y \right| + \left| y \right| && \text{Ant.}  \\
> 	\left| x \right| - \left| y \right| &\le \left| x - y \right| \\
> \end{align}$$
> Swapping $x$ and $y$ gives
> $$ \left| y \right| - \left| x \right| \le \left| y - x \right| = \left| x-y \right|  $$
> Thus,
> $$\begin{align}
> 	\left| \left| x \right| - \left| y \right|  \right| &= \max\{ \left| x \right| -\left| y \right| ,-\left( \left| x \right| - \left| y \right|  \right) \} \\
> 	&= \max\{ \left| x \right| -\left| y \right| ,\left| y \right| - \left| x \right| \} \\
> 	&\le \left| x - y \right|  \\
> \end{align}$$

> [!corollary]- **1.12.2** $\forall x,y,z\in\R, \left| x-z \right| \le \left| x-y \right| + \left| y - z \right|$
> Let $a = x-y$ and $b = y - z$. Then $a + b = x - z$. Thus,
> $$\left| x-z \right| = \left| a + b \right| \le \left| a \right| + \left| b \right|  = \left| x-y \right| + \left| y-z \right| $$