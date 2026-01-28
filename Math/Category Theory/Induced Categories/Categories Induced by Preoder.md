---
tags:
  - atom
  - math
---
If you have a [[Sets|set]] $P$ equipped with a [[Preorder|preorder]] $\le$, the [[Categories|category]] $P$ induced by the [[Preorder|preorder]] is defined such that
$$P(x,y) = \begin{cases}
	\{ x \to y \} & x \le y \\
	\emptyset & x \not{\hspace{-0.7ex}\le}\hspace{0.7ex} y \\
\end{cases}. \hspace{3em} \forall x,y \in P$$
> [!proof]-
> Let $\alpha: x \to y$, $\beta: y \to z$. Then $x \le y$ and $y \le z$, so by the [[Transitive Property|transitivity]] of [[Preorder|preorder]], $x \le z$. Thus, $P(x,z) = \{ x \to z \}$, so $\beta\alpha : x \to z$ can be defined, and it must inherently be unique.
> 
> Let $x \in P$. By the [[Reflexive Property|reflexivity]] of [[Preorder|preorder]], $x \le x$, so $P(x,x) = \{ x \to x \}$, meaning there is a unique morphism $1_{x} : x \to x$.

> [!note] In such a [[Categories|category]], the [[Initial and Terminal Objects|initial and terminal]]  are the least element and greatest element respectively (if they exist).