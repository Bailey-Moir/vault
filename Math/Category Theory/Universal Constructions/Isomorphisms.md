---
tags:
  - atom
  - math
---
A morphism $\alpha : x \to y$  is an *isomorphism* iff there exists a morphism $\alpha^{-1} : y \to x$ such that $\alpha^{-1}\alpha = 1_{x}$ and $\alpha\alpha^{-1} = 1_{y}$.
```tikz
\usepackage{tikz-cd}
\begin{document}

\begin{tikzcd}
	\arrow[loop left, "1_x"] x \arrow[r, shift right, swap, "\alpha"] & y \arrow[l, shift right, swap, dashed, "\exists \alpha^{-1}"] \arrow[loop right, "1_y"]
\end{tikzcd}

\end{document}
```
*i.e. it has a complete inverse*

> [!definition-&-notation] Two objects $x$ and $y$ are **isomorphic** iff they have an *isomorphism* between them. This is notated by $x \cong y$.

> [!theorem-1]- A morphism is *isomorphic* iff it is [[Split Monic Morphisms|split monic]] and [[Split Epic Morphisms|split epic]].
> ($\implies$)
> $\alpha^{-1}$ directly gives $\beta$ for the definitions of [[Split Monic Morphisms|split monic]] and [[Split Epic Morphisms|split epic]] morphisms.
> 
> $\left( \impliedby \right)$
> Let $\alpha :x \to y$ be [[Split Monic Morphisms|split monic]] and [[Split Epic Morphisms|split epic]], so there exists $\beta,\gamma : y \to x$ such that $\beta\alpha = 1_{x}$ and $\alpha\gamma = 1_{y}$. Then
> $$\beta = \beta {1}_{y} = \beta\alpha\gamma = 1_{x}\gamma = \gamma,$$
> meaning $\alpha$ is an *isomorphism* with $\alpha^{-1} = \beta = \gamma$. $\square$

> [!theorem-2]- $\alpha^{-1}$ is unique
>  Let $\alpha : x \to y$ be an *isomorphism* with two inverses $\alpha_1^{-1},\alpha_2^{-1} : y \to x$. Then
> $$ \alpha_1^{-1} = 1_x\alpha_1^{-1} = \alpha_2^{-1}\alpha\alpha_1^{-1} = \alpha_2^{-1}1_y = \alpha_2^{-1}. \quad \square$$