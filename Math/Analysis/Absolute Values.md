---
tags:
  - atom
  - math
---
![450|center](general-abs-value.excalidraw.md)
$$ \forall x \in \R, \hspace{1em}|x| = \left\{\begin{array}{lr}
	x & x \ge 0 \\
	-x & x < 0
\end{array}\right.$$
> [!theorem]- **1.9** $\forall a,b \in \R,$ <ol> <li>$|a| \ge 0$ and $|a| = 0 \leftrightarrow a = 0$ (Positive Definite)</li> <li>$\left| a \right| = \max\{ a,-a \}$</li> <li>$|-a| = |a|$</li> <li>$\left| ab \right| = \left| a \right|\left| b \right|$</li> </ol>
> 1. If $a \geq 0$, then $\left| a \right| = a \geq 0$
>    If $a \leq 0$, then $\left| a \right| = -a \geq 0$[^1]
>    
>    If $a = 0$, then $\left| a \right| = a = 0$.
>    If $\left| a \right| = 0$, then $\left| a \right| = \pm a = 0$, so $a = 0$[^2]
> 
> 2. If $a \geq 0$, then $-a \leq 0 \leq a$, so $-a \leq a$, meaning $\max \{a,-a \} = a$.
>    If $a < 0$, then $a < 0 < -a$[^1], so $-a > a$, and $\max \{a,-a \} = a$.
> 
> 3. Using 3,
>    $$\begin{align}
> 	\left| -a \right| &= \text{max}\{ -a,-(-a) \} \\
> 	&= \text{max}\{ -a,a \} && \text{Given by Field} \\
> 	&= \text{max}\{ a,-a \} \\
> 	&= \left| a \right| 
> \end{align}$$
> 4. Suppose $b \ge 0$. Then
>    $$\begin{align}
> 	\left| ab \right| &= \max\{ ab,-ab \} \\
> 	&= \max\{ a,-a \}b \\
> 	&= \left| a \right| b \\
> 	&= \left| a \right| \left| b \right| && b> =0 \\
> \end{align}$$
>    If $b < 0$, then $-b \geq 0$, meaning $\left| a(-b) \right| = \left| a \right|\left| -b \right|$, but
>    $$\begin{align}
>    \left| a(-b) \right| = \left| -ab \right| = \left| ab \right| && 4 \\
>    \left| -b \right| = \left| b \right|,  && 4
> 	\end{align}$$  
>    thus, $\left| ab \right| = \left| a \right|\left| b \right|$

> [!theorem]- **1.10** $\forall a \in \R, -\left| a \right| \le a \le \left| a \right|$
> Since $\max\{ a,-a \} = \left| a \right|$ (1.9.3),
> $$\begin{align}
> 	a &\le \left| a \right|  \\
> 	-a &\le \left| a \right|,
> \end{align}$$
> by [[Ordered Fields#Ordered Field Theorems|theorem 1.6.2]] and the [[Transitive Property|transitivity]] of [[Partial Order|partial order]],
> $$-\left| a \right| \le a \le \left| a \right| $$

[^1]: [[Ordered Fields#Ordered Field Theorems]], Theorem 1.6.3
[^2]: [[Fields#Field Theorems]], Theorem 1 & 2
