---
tags:
  - math
  - atom
---
$$ \lim_{x\to a} f(x) = L \iff \lim_{x\to a^-} f(x) = L = \lim_{x\to a^+} f(x) $$
> [!example]-
> $$
> \begin{array}{r l}
> \text{e.g.} & \displaystyle \text{Prove that} \lim_{x\to 0} \dfrac{\left|x\right|}{x} \text{ is undefined}. \\
> \\
> & \begin{alignat}{3}
> \lim_{x\to0^+}\dfrac{\left|x\right|}{x} &= \hspace{1ex} \lim_{x\to0^+}\dfrac{x}{x} &&= 1 \\
> \lim_{x\to0^-}\dfrac{\left|x\right|}{x} &= \lim_{x\to0^-}-\dfrac{x}{x} &&= -1
> \end{alignat}
> \end{array}
> $$