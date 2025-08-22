---
tags:
  - atom
  - math
---
$$f \in \mathcal{C}(I) \iff \forall a \in I,\, \lim_{x\to a} f(x) = f(a) $$
> [!note] This implicitly requires $f(a)$ and $\displaystyle\lim_{x\to a} f(x)$ to exist.

> [!note] If $I = \{ a \}$ for some $a \in \R$, this implicitly requires $f$ to be [[Defined Near|defined near]] $a$ and at $a$.

> [!definition] $\varepsilon$-$\delta$
> $$\forall \varepsilon>0, \exists \delta>0: \forall x \in \R,  \left|x-a\right| < \delta \to  \left|f(x) - f(a)\right| < \varepsilon$$