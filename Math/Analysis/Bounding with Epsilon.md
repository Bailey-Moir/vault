---
tags:
  - atom
  - math
---
> [!theorem]- **1.18.1** Let $S = \{ x \in \R : \forall \varepsilon \in \R , (\varepsilon > 0 \to x < \varepsilon) \}$. Then $0$ is an [[Bounded Sets|upper bound]] for $S$.
> Suppose $0$ is not an [[Bounded Sets|upper bound]] for $S$.
> 
> Then there exists $x \in S$ such that $x > 0$.
> 
> Letting $\varepsilon = x$ gives $x < x$, a [[Contradictions|contradiction]],

> [!theorem]- **1.18.2** If $a,b \in \R$ such that $\forall \varepsilon > 0, a < b + \varepsilon$, then $a \leq b$.
> $$\begin{align}
> 	a < b + \varepsilon  \\
> 	a - b < \varepsilon  \\
> \end{align}$$
> Thus, $a-b \in S$ from 1.18.1, so $a-b \le 0$ ($a \le b$) .

> [!theorem]- **1.18.3** If $\forall \varepsilon > 0, \left| x-p \right|<\varepsilon$, then $x = p$.
> We have $x - p < \varepsilon$ and $p-x < \varepsilon$, so by 1.18.2, $x \le p$ and $p \le x$. Thus, $x = p$.