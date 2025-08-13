---
tags:
  - atom
  - math
  - linear
---
For $\vecbf{u},\vecbf{v}$ in an [[Inner Products|inner product space]] with [[Norms|induced norm]] $\| \cdot \|$,
$$\left| \left< \vecbf{u},\vecbf{v} \right>  \right| \le \| \vecbf{u} \|\,\| \vecbf{v} \|$$
> [!proof]-
> If $\vecbf{u} = \vecbf{0}$, then the inequality holds, as, by the definition of a [[Norms|norm]], if $\vecbf{u} = 0$, then $\| \vecbf{u} \| = 0$, and $\left< \vecbf{0},\vecbf{v} \right> = 0$ for all $\vecbf{v}$, which can be shown by the [[Linear Combinations|linearity]] of the [[Inner Products|inner product]], giving $0 \le 0$.
> 
> Thus, assume $\vecbf{u} \ne 0$, which allows [[Vector Projection|projection]] onto $\vecbf{u}$.
> 
> By the [[Pythagoreas' Theorem|Pythagorean theorem]],
> $$\begin{align}
> 	\| \vecbf{v} \|^{2} &= \| \text{proj}_{\vecbf{u}}\vecbf{v} \|^{2} + \| \text{perp}_{\vecbf{u}}\vecbf{v} \|^{2} \\
> 	\| \vecbf{v} \|^{2} &\ge \| \text{proj}_{\vecbf{u}}\vecbf{v} \|^{2}\\
> 	&\ge \left\| \dfrac{\left< \vecbf{u},\vecbf{v} \right>}{\left< \vecbf{u},\vecbf{u} \right>}\vecbf{u} \right\|^{2}\\
> 	\left< \vecbf{v},\vecbf{v} \right>  &\ge \dfrac{\left< \vecbf{u},\vecbf{v} \right>^{2}}{\left< \vecbf{u},\vecbf{u} \right>^{2}} \left< \vecbf{u},\vecbf{u} \right> \\
> 	\left< \vecbf{v},\vecbf{v} \right>  &\ge \dfrac{\left< \vecbf{u},\vecbf{v} \right>^{2}}{\left< \vecbf{u},\vecbf{u} \right>} \\
> 	\left< \vecbf{u},\vecbf{v} \right>^{2} &\le \| \vecbf{u} \|^2\| \vecbf{v} \|^2 \\
> 	\left| \left< \vecbf{u},\vecbf{v} \right> \right|  &\le \| \vecbf{u} \|\| \vecbf{v} \| \\
> \end{align}$$