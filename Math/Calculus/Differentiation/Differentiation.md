---
tags:
  - atom
  - math
---
Let $f$ be a [[Functions|function]] and $a \in\text{dom}\,f$. Then the *derivative* of $f$ at $a$, denoted $f'(a)$, is
$$f'(a) = \lim_{ x \to a } \dfrac{f(x)-f(a)}{x-a} \;{\color{gray} = \lim_{ h \to 0 } \dfrac{f(a+h) - f(a)}{h} }.$$
> [!definition] $f$ is said to be **differentiable** at $p$ is this [[Math/Calculus/Limits/Limits|limit]] exists.

> [!example]- $f(x) = x^2 - x + 1$
> $$\begin{align}
> 	f'(a) &= \lim_{ x \to a } \dfrac{f(x) - f(a)}{x - a}  \\
> 	&= \lim_{ x \to a } \dfrac{x^2 - x + 1 - a^2 + a - 1}{x - a}  \\
> 	&= \lim_{ x \to a } \dfrac{x^2 - x - a^2 + a}{x - a}  \\
> 	&= \lim_{ x \to a } \left[ \dfrac{x^2 - a^2}{x - a} - \dfrac{x - a}{x-a} \right]   \\
> 	&= \lim_{ x \to a } \left[ x+a - 1 \right]   \\
> 	&= 2a - 1  \\
> \end{align}$$

> [!example]- $f(x) = \left| x \right|$
> If $a < 0$,
> $$\begin{align}
> 	f'(a) &= \lim_{ x \to a } \dfrac{f(x) - f(a)}{x - a}  \\
> 	&= \lim_{ x \to a } \dfrac{\left| x \right| + a}{x - a}  \\
> 	&= \lim_{ x \to a } \dfrac{-x + a}{x - a} && \text{Restrict } x< 0 \\
> 	&= -1. \\
> \end{align}$$
> If $a > 0$,
> $$\begin{align}
> 	f'(a) &= \lim_{ x \to a } \dfrac{f(x) - f(a)}{x - a}  \\
> 	&= \lim_{ x \to a } \dfrac{\left| x \right| - a}{x - a}  \\
> 	&= \lim_{ x \to a } \dfrac{x - a}{x - a} && \text{Restrict } x > 0 \\
> 	&= 1. \\
> \end{align}$$