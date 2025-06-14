---
tags:
  - atom
  - math
  - linear
---
For $p \in \left[ 1,\infty \right)$, the *$\it p$-norm* of $\vecbf{v} \in \R^n$ is given by
$$\| \vecbf{v} \|_{p} = \sqrt[p]{\left| v_{1} \right|^p + \left| v_{2} \right|^p + \dots + \left| v_{n} \right|^p  },$$
and the $\infty$*-norm* is given by
$$\| \vecbf{v} \|_{\infty} = \max\{ \left| v_{1} \right|,\left| v_{2} \right| ,\dots,\left| v_{n} \right|  \},$$

> [!note] Special names
> - The **Manhattan norm** is the $1$-norm, and
> - The **Euclidean norm** is the $2$-norm, and
> - the **Max/Uniform norm** is the $\infty$-norm

> [!theorem]- The *p-norm* is induced by an [[Inner Products|inner product]] iff $p = 2$.
> Consider $\hat{\vecbf{e}}_{1}$ and $\hat{\vecbf{e}}_{2}$.
> $$\forall i \in \{ 1,2 \}, \| \hat{\vecbf{e}}_{i} \|_{p} = \sqrt[p]{ 1^p + 0^p + \dots + 0^p } = 1$$
> and
> $$\| \hat{\vecbf{e}}_{1} \pm \hat{\vecbf{e}}_{2} \|_{p} = \sqrt[p]{ 1^p + + 1^p +  0^p + \dots + 0^p } = \sqrt[p]{ 2 }$$
> then, if the [[Parallelogram Law|parallelogram law]] holds, then
> $$\begin{align}
>  \|\hat{\vecbf{e}}_{1} + \hat{\vecbf{e}}_{2}\|^2 + \|\hat{\vecbf{e}}_{1} - \hat{\vecbf{e}}_{2}\|^2 &= 2\|\hat{\vecbf{e}}_{1}\|^2 + 2\|\hat{\vecbf{e}}_{2}\|^2  \\
> 	\left( \sqrt[p]{ 2 } \right)^{2} + \left( \sqrt[p]{ 2 } \right)^{2} &= 2\left( 1 \right)^2 + 2\left( 1 \right)^2 \\
> 	2\sqrt[p]{ 4 } &= 4 \\
> 	\sqrt[p]{ 4 } &= 2, \\
> \end{align}$$
> and this is the case iff $p = 2$. Thus, every other $p$-norm cannot be induced by an [[Inner Products|inner product]]. Further, the $2$-norm can be induced by an [[Inner Products|inner product]], as it is induced by the [[Dot Product|dot product]].

> [!theorem] If $p > q$, then $\| \vecbf{v} \|_{p} \le \| \vecbf{v} \|_{q}$

\[[[Norms]]\]