---
tags:
  - atom
  - math
---
![300|center](general-abs-value.excalidraw)
The absolute value of $x$ ($|x|$) can be thought of as the distance of the number $x$ from 0 on the number line.
$$ |x| = \left\{\begin{array}{lr}
	x & x \ge 0 \\
	-x & x < 0
\end{array}\right.$$
- $|x| \ge 0$
- $|x|^2 = x^2$
- $|x| = 0 \iff x = 0$
- $|-x| = |x|$
- $|x| \le a \iff -a \le x \le a$
- $|x| \ge a \iff x \le -a \lor a \le x$

> [!proof]-
> $$\left.\begin{array}{l}
> 	|x| < a \\
> 	\begin{array}{rcll}
> 		\text{If $x$ is non-negative} & & \text{If $x$ is negative} \\
> 		x < a & \text{or} & -x < a \\
> 		x < a & \text{or} & x > -a
> 	\end{array} \\
> 	-a < x < a
> \end{array}\hspace{1em}\right|\hspace{1em}
> \begin{array}{l}
> 	|x| > a \\
> 	\begin{array}{rcl}
> 		\text{If $x$ is non-negative} & & \text{If $x$ is negative} \\
> 		x > a & \text{or} & -x > a \\
> 		x > a & \text{or} & x < -a
> 	\end{array} \\
> 	x < -a \text{ or } x > a
> \end{array}
> $$