---
tags:
  - atom
  - math
  - linear
---

For $\vecbf{u},\vecbf{v}$ in an [[Inner Products|inner product space]],
$$\| \vecbf{u} + \vecbf{v} \| \le \| \vecbf{u} \| + \| \vecbf{v} \|$$
\[[[Vector Length]]\]

> [!proof]-
> Since both sides are positive, it suffices show that $\| \vecbf{u} + \vecbf{v} \|^2 \le (\| \vecbf{u} \| + \| \vecbf{v} \|)^2$.
> $$\begin{align}
> 	(\| \vecbf{u} \| + \| \vecbf{v} \|)^2 - \| \vecbf{u} + \vecbf{v} \|^2 &= \| \vecbf{u} \|^2 + 2\| \vecbf{u} \|\| \vecbf{v} \| + \| \vecbf{v} \|^2 - \left< \vecbf{u}+\vecbf{v},\vecbf{u}+\vecbf{v} \right>  \\
> 	&= \left< \vecbf{u},\vecbf{u} \right>  + 2\| \vecbf{u} \|\| \vecbf{v} \| + \left< \vecbf{v},\vecbf{v} \right> - \left( \left< \vecbf{u},\vecbf{u} \right> + 2\left< \vecbf{u},\vecbf{v} \right> + \left< \vecbf{v},\vecbf{v} \right>  \right) \\
> 	&= 2\left( \| \vecbf{u} \|\| \vecbf{v} \| - \left< \vecbf{u},\vecbf{v} \right>  \right) \\
> 	&\ge 0 \hspace{2em} (1) \\
> \end{align}$$
> \[$(1)$ [[Cauchy-Schwartz Inequality]]\]