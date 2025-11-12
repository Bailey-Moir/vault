---
tags:
  - atom
  - math
---
![500|center](taylors-remainder-theorem.excalidraw.md)
Suppose $f$ is $n+1$ times [[Differentiation|differentiable]] on $\left( a,b \right)$, and $\alpha \in \left( a,b \right)$.
Then for every $x \in \left( a,b \right)$, there exists $\xi_{L} \in \left( \alpha,x \right)$ such that
$$R_{n}(x) = \dfrac{f^{(n+1)}(\xi_{L})}{(n+1)!}(x-\alpha)^{n+1} $$
> [!proof]-
> Fix $\alpha,x \in \left( a,b \right)$. Let $g(t)$ give the remainder of the first $n$ terms of the [[Taylor Series|Taylor series]] of $f$ around $t$, meaning
> $$g(t) = f(x) - \sum_{k=0}^n \dfrac{f^{(k)}(t)}{k!} (x-t)^k.$$
> Then by the [[Power Rule|power]] and [[Differentiation Rules|chain rule]],and [[Continuity of Differentiable Functions|continuity of differentiable functions]], $g$ is [[Continuity|continuous]] and [[Differentiation|differentiable]] on $\left( a,b \right)$.
> 
> Note that $g(x) = 0$, and
> $$\begin{align}
> 	g'(t) &= 0 - \left( \sum_{k=0}^n \dfrac{f^{(k+1)}(t)}{k!} (x-t)^k - \sum_{k=1}^{n-1} \dfrac{f^{\left( k \right)}(t)}{(k-1)!}(x-t)^{k-1} \right)  \\
> 	&= -\sum_{k=0}^n \dfrac{f^{(k+1)}(t)}{k!} (x-t)^k + \sum_{k=0}^{n-1} \dfrac{f^{\left( k+1 \right)}(t)}{k!}(x-t)^{k}  \\
> 	&= -\dfrac{f^{(n+1)}(t)}{n!} (x-t)^n  \\
> \end{align}$$
> 
> Let
> $$h(t) = g(t) - \left( \dfrac{x-t}{x-\alpha} \right)^{n+1}g(\alpha).$$
> Then similarly, by the [[Power Rule|power]] and [[Differentiation Rules|chain rule]], [[Linearity of Differentiation|linearity of differentiation]], and [[Continuity of Differentiable Functions|continuity of differentiable functions]], $h$ is [[Continuity|continuous]] and [[Differentiation|differentiable]] on $\left( a,b \right)$.
> 
> Note that
> $$h'(t) = \left( -\dfrac{f^{(n+1)}(t)}{n!}(x-t)^n  \right)+ \dfrac{n+1}{(x-c)^{n+1}}\left( x-t \right)^ng(c)$$
> 
> By [[Rolle's Theorem|Rolle's theorem]], since $h(x) = 0$ and $h(\alpha) = 0$, there exists $\xi_{L} \in \left( \alpha,x \right)$ such that $h'(\xi_{L}) = 0$. Thus,
> $$\begin{align}
> 	\dfrac{f^{(n+1)}(t)}{n!}(x-t)^n &= \dfrac{n+1}{(x-\alpha)^{n+1}}\left( x-t \right)^n g(\alpha) \\
> 	\dfrac{f^{(n+1)}(t)}{(n+1)!}(x-\alpha)^{n+1} &= g(\alpha) \\
> \end{align}$$

> [!note] You find the maximum by assuming the largest value of $f^{(n+1)}(\xi_{L})$ in $\xi_{L} \in(\alpha,x)$.

\[[[Taylor Series]]\]