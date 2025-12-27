---
tags:
  - atom
  - math
---
![400|center](mean-value-theorem.excalidraw.md)
Suppose $f(x)$ is [[Math/Calculus/Limits/Continuity/Continuity|continuous]] on $[a,b]$ and [[Differentiation|differentiable]] on $(a,b)$. 
The *mean value theorem* states that there exists a point $c \in (a,b)$ such that $f'(c)$ is the slope of the [[Secants|secant]] through $a$ and $b$;
$$\exists c \in \left( a,b \right) : f'(c) = \dfrac{f(b) - f(a)}{b-a}$$

> [!proof]-
> Consider the [[Functions|function]] of the [[Secants|secant]] between $a$ and $b$,
> $$l(x) = \dfrac{f(b)-f(a)}{b-a}(x-a) + f(a).$$
> Note that $l(a) = f(a)$ and $l(b) = f(b)$.
> 
> Define $g = f - l$, which is then [[Math/Calculus/Limits/Continuity/Continuity|continuous]] on $\left[ a,b \right]$ and [[Differentiation|differentiable]] on $\left( a,b \right)$.
> 
> Thus, by [[Rolle's Theorem|Rolle's theorem]], there exists $c\in \left( a,b \right)$ such that $g'(c) = 0$.
> $$\begin{align}
> 	g'(c) &= f'(c) - l'(c) \\
> 	&= f'(c) - \dfrac{f(b)-f(a)}{b-a} = 0 \\
> 	&\hspace{7.9em} f'(c) = \dfrac{f(b)-f(a)}{b-a} \\
> \end{align}$$

> [!corollary]- Let $f,g$ satisfy *MVT* between $a$ and $b$. <ol><li>Suppose for all $x \in \left( a,b \right)$, $f'(x) = 0$. Then $f$ is constant on $[a,b]$.<br/>The only functions of the form $f:\R\to\R$ whose [[Differentiation|derivatives]] are identically zero are constant.</li><li>Suppose for all $x \in \left( a,b, \right)$, $f'(x) = g'(x)$. Then $f$ and $g$ differ by a constant.</li></ol>
> 1. Take $a<a_{1}<b_{1}<b$. Then by *MVT*, there exists $c \in \left( a_{1},b_{1} \right)$ such that
> $$\begin{align}
> 	0 &= f'(c) \\
> 	&= \dfrac{f(b_{1})-f(a_{1})}{b_{1}-a_{1}} \\
> 	f(a_{1})&= f(b_{1}). \\
> \end{align}$$
>    Thus, $f(a_{1}) = f(b_{1})$ for arbitrary $a_{1},b_{1}\in \left( a_{1},b_{1} \right)$.
> 2. By **1**, since $f-g$ is constant on $\left[ a,b \right]$. Thus, for all $x \in \left[ a,b \right]$,
> $$\begin{align}
> 	c &= (f-g)(x) \\
> 	  &= f(x) - g(x) \\
> 	f(x) &= g(x) + c \\
> \end{align}$$

> [!corollary]- Let $f,g$ satisfy *MVT* between $a$ and $b$. <ol><li>If $f'(x) \ge 0$ for all $x \in \left( a,b \right)$, the $f$ is [[Increasing and Decreasing Functions|increasing]] on $\left( a,b \right)$</li><li>If $f'(x) \le 0$ for all $x \in \left( a,b \right)$, the $f$ is [[Increasing and Decreasing Functions|decreasing]] on $\left( a,b \right)$</li></ol>
> 1. Consider $a \leq x < y \leq b$. $f$ is then [[Differentiation|differentiable]] on $\left( x,y \right)$, so by *MVT*, there exists $c \in \left( x,y \right)$ such that
> $$\begin{align}
> 	f'(c) = \dfrac{f(y) - f(x)}{y-x} &\geq 0 \\
> 	f(y) - f(x) &\geq 0 && y<x \to 0 < x - y \\
> 	f(x) &\leq f(y). \\
> \end{align}$$
>    Thus, for arbitrary $a\le x<y \le b$, $f(x) \le f(y)$, so $f$ is [[Increasing and Decreasing Functions|increasing]] on $\left( a,b \right)$.
> 2. For $f' \le 0$, $(-f)' \ge 0$ must be [[Increasing and Decreasing Functions|increasing]] by **1**, so $f$ is [[Increasing and Decreasing Functions|decreasing]].

[^1]: [[Math/Calculus/Limits/Continuity/Continuity]]
