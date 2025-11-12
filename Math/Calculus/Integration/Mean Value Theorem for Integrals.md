---
tags:
  - math
  - atom
---
![300|center](mvt-int.excalidraw.md)
$$\displaystyle f \in \mathcal{C}([a,b]) \implies \exists c \in [a,b] : \int_a^b f(x) \, dx = f(c)(b-a)$$
meaning $\displaystyle f(c) = f_\text{avg} = \dfrac{1}{b-a}\int_a^b f(x) \, dx$.

> [!proof]-
> By [[Extreme Value Theorem|extreme value theorem]], there exists $m = \inf \{ f(x) : x \in \left[ a,b \right] \}$ and $M = \sup \{ f(x) : x \in \left[ a,b \right] \}$.
> 
> By the [[Continuity|continuity]] of $f$ on $\left[ a,b \right]$, it is [[Bounded Sets|bounded]][^2] and [[Integrability|integrable]][^3], and thus[^4],
> $$\begin{array}{c}
> 	\displaystyle m(b-a)\leq \int_{a}^b f \, dx \le M(b-a) \\
> 	\displaystyle m\leq \underbrace{\dfrac{1}{b-a}\displaystyle\int_{a}^b f \, dx}_{f(c)} \le M.
> \end{array}$$
> Thus, by [[Intermediate Value Theorem|intermediate value theorem]], there exists $c \in \left[ a,b \right]$ such that
> $$f(c) = \dfrac{1}{b-a}\int_{a}^b f \, dx. \hspace{1em}\square$$

\[[[Average Value Function]], [[Intermediate Value Theorem]]\]

[^1]: [[Continuity Under Composition]]
[^2]: [[Boundedness of Continuous Functions]]
[^3]: [[Integrability of Continuous Functions]]
[^4]: [[Bounding Integration]]
