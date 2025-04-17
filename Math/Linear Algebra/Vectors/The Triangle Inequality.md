---
tags:
  - atom
  - math
  - linear
---

For $\vecbf{u},\vecbf{v} \in V$,
$$\| \vecbf{u} + \vecbf{v} \| \le \| \vecbf{u} \| + \| \vecbf{v} \|$$
\[[[Vector Length]]\]

> [!proof]-
> Since both sides are positive, it suffices show that $\| \vecbf{u} + \vecbf{v} \|^2 \le (\| \vecbf{u} \| + \| \vecbf{v} \|)^2$.
> $$\begin{align}
> 	(\| \vecbf{u} \| + \| \vecbf{v} \|)^2 - \| \vecbf{u} + \vecbf{v} \|^2 &= \| \vecbf{u} \|^2 + 2\| \vecbf{u} \|\| \vecbf{v} \| + \| \vecbf{v} \|^2 - \left( \vecbf{u}+\vecbf{v} \right)\cdot \left( \vecbf{u}+\vecbf{v} \right) \\
> 	&= \vecbf{u}\cdot \vecbf{u} + 2\| \vecbf{u} \|\| \vecbf{v} \| + \vecbf{v}\cdot \vecbf{v} - \vecbf{u}\cdot \vecbf{u} - 2\vecbf{u}\cdot \vecbf{v} - \vecbf{v}\cdot \vecbf{v} \\
> 	&= 2\left( \| \vecbf{u} \|\| \vecbf{v} \| - \vecbf{u}\cdot \vecbf{v} \right) \\
> 	&\ge 0 \hspace{2em} (1) \\
> \end{align}$$
> \[$(1)$ [Cauchy-Schwartz Inequality](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz_inequality)\]