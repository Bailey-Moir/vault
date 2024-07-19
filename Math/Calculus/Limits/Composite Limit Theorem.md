---
tags:
  - math
  - atom
---
$$
f \in \mathcal{C}\left(\left\{\lim_{x\to a} g(x) \right\}\right) \iff \lim_{x\to a} f(g(x)) = f\left(\lim_{x\to a} g(x)\right)
$$
This is derived from the [[Definition of Continuity|definition of continuity]], where the interval in question is $\displaystyle \lim_{x\to a} g(x)$. A helpful supplementary theorem is
$$
	f \in \mathcal{C}\left(\{ g(a) \}\right) \land g \in \mathcal{C}\left(\{ a \}\right) \iff \left(f \circ g\right)(a) \in \mathcal{C}(\{ a \})
$$