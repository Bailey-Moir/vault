---
tags:
  - atom
  - math
  - discrete
---
The smallest [[Subgroups|subgroup]] containing $a$ in $G$ is the [[Subsets|subset]]
$$\left< a \right> = \{ a^m : m \in \Z \}$$
\[[[Powers in Groups]]\]

> [!proof]-
> Let $g,h \in \left< a \right>$. Then $g = a^m$ and $h = a^n$ for $m,n \in \Z$.
> 
> Thus $gh^{-1} = a^ma^{-n} = a^{m-n}$. Since $m-n \in \Z$, this must be in $\left< a \right>$.
> 
> This then passes the [[Subgroups|one-step subgroup test]], meaning $\left< a \right> \le G$.