---
tags:
  - atom
  - math
---
### Product Rule
Let $f$ and $g$ be [[Functions|functions]], and $a \in\text{dom}\,f \cap\text{dom}\,g$. If $f$ and $g$ are [[Differentiation|differentiable]] at $a$, then $fg$ is [[Differentiation|differentiable]] at $a$, and
$$\left( fg \right)'(a) = f'(a)g(a) + f(a)g'(a).$$
> [!proof]-
> By [[Limiting Function of Differentiation|theorem 5.2]], let $f(x) = f(a) + (x-a)\phi(x)$ and $g(x) = g(a) + (x-a)\psi(x)$.
> $$\begin{align}
> 	(fg)(x) &= \left( f(a) + (x-a)\phi(x) \right)\left( g(a) + (x-a)\psi(x) \right) \\
> 	&= f(a)g(a) + (x-a)\left( \phi(x)g(a) + \psi(x)f(a) + (x-a)\phi(x)\psi(x) \right) \\
> 	\dfrac{(fg)(x) - (fg)(a)}{x-a}&= \phi(x)g(a) + \psi(x)f(a) + (x-a)\phi(x)\psi(x) \\
> 	(fg)'(a)&= f'(a)g(a) + f(a)g'(a) + (a-a)f'(a)g'(a)\\
> 	(fg)'(a)&= f'(a)g(a) + f(a)g'(a)\\
> \end{align}$$
### Quotient Rule
Let $f$ and $g$ be [[Functions|functions]], and $a \in\text{dom}\,f \cap\text{dom}\,g$. If $f$ and $g$ are [[Differentiation|differentiable]] at $a$ and $g(a) \ne 0$, then $\frac{f}{g}$ is [[Differentiation|differentiable]] at $a$, and
$$\left( \dfrac{f}{g} \right)'(a) = \dfrac{f'(a)g(a) - f(a)g'(a)}{(g(a))^2}.$$
### Chain Rule
Let $f$ and $g$ be [[Functions|functions]], $c \in \R$, and $a \in\text{dom}\,f \cap\text{dom}\,g$. If $f$ is [[Differentiation|differentiable]] as $a$ and $g$ is [[Differentiation|differentiable]] at $f(a)$, then $g\circ f$ is [[Differentiation|differentiable]] at $a$ and
$$\left( g \circ f \right)'(a) = g'(f(a))f'(a)$$
> [!proof]-
> By [[Limiting Function of Differentiation|theorem 5.2]], let $f(x) = f(a) + (x-a)\phi(x)$ and $g(f(x)) = g(f(a)) + (f(x)-f(a))\psi(x)$, where $\phi(a)$ and $\psi(f(a))$ are [[Continuity|continuous]].
> By the [[Differentiation|differentiability]] of $f$ and $g$, $f(a)$ and $g(f(a))$ are [[Continuity|continuous]][^1]
> $$\begin{align}
> 	g(f(x)) &= g(f(a)) + (f(x) - f(a))\psi(f(x)) \\
> 	&= g(f(a)) + (x - a)\phi(x)\psi(f(x))\\
> 	&= g(f(a)) + (x - a)\phi(x)\psi(f(x)).\\
> \end{align}$$
> Thus, there exists a [[Continuity|continuous]] [[Functions|function]] $\phi(x)\psi(f(x))$ at $a$[^2] that satisfies [[Limiting Function of Differentiation|theorem 5.2]], so $g\circ f$ is [[Differentiation|differentiable]] at $a$, and it [[Differentiation|differentiates]] to
> $$\begin{align}
> 	\left( g\circ f \right)'(a) &= \phi(x)\psi(f(x)) \\
> 	&= f'(x)g'(f(x))
> \end{align}$$

[^1]: [[Continuity of Differentiable Functions]]
[^2]: [[Continuity of Combined Functions]] and [[Continuity Under Composition]]
