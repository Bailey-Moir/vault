---
tags:
  - atom
  - math
---
If $f,g \in \mathcal{C}(I)$[^1], then the following [[Functions|functions]] are [[Continuity|continuous]] on $I$:
1. $f \pm g$
2. $cf$
3. $fg$
4. $\dfrac{f}{g}$ if $\forall x \in I, g(x) \ne 0$

> [!proof]- \- **4.8.1**
> Since $f$ and $g$ are [[Continuity|continuous]] on $I$, for any $a\in I$ and $\varepsilon > 0$, there exists $\delta_{f},\delta_{g}>0$ such that
> $$\begin{align}
> 	\left| x-a \right| &< \delta_{f} \to \left| f(x) - f(a) \right| < \dfrac{\varepsilon}{2} \\
> 	\left| x-a \right| &< \delta_{g} \to \left| g(x) - g(a) \right| < \dfrac{\varepsilon}{2}.
> \end{align}$$
> Let $\delta =\text{min}\{ \delta_{f},\delta_{g} \}$. Then
> $$\begin{align}
> 	\left| x-a \right| < \delta &\to \varepsilon>\left| f(x) - f(a) \right| + \left| g(x)-g(a) \right| \\
> 	&\to \phantom{\varepsilon} \geq \left| f(x) - f(a) + g(x)-g(a) \right| && (1) \\
> 	&\to \phantom{\varepsilon} = \left| (f+g)(x) - (f+g)(a) \right|. \\
> \end{align}$$
> \[$(1)$ [[Triangle Ineqaulity]]\]
> 
> Thus, $(f+g)(x)$ must also converge to $(f+g)(a)$, meaning $f+g$ is [[Continuity|continuous]] on $a$, meaning it is [[Continuity|continuous]] on $I$.
> 
> If you let $g$ be $-g$ using 2, this shows the same for $f-g$.

> [!proof]- \- **4.8.2**
> **Case $\mathbf{c = 0}$**
> $cf = 0$, which is constant and thus [[Continuity|continuous]].
> 
> **Case $\mathbf{c \ne 0}$**
> Since $f$ is [[Continuity|continuous]] on $I$, for any $a\in I$, $c \in \R$ and $\varepsilon > 0$, there exists $\delta>0$ such that
> $$\begin{align}
> 	\left| x-a \right| < \delta &\to \left| f(x) - f(a) \right| < \dfrac{\varepsilon}{\left| c \right| } \\
> 	&\to \left| c \right| \left| f(x) - f(a) \right| < \varepsilon \\
> 	&\to \left| cf(x) - cf(a) \right| < \varepsilon. \\
> \end{align}$$
> Thus, $cf(x)$ must also converge to $cf(a)$, meaning $cf$ is [[Continuity|continuous]] on $a$, meaning it is [[Continuity|continuous]] on $I$.

> [!proof]- \- **4.8.3**
> $\psi(y) = y^2$ is [[Continuity|continuous]], so by [[Continuity Under Composition|composition rules]], if $f(x)$ is [[Continuity|continuous]], then so is $\left( \psi \circ f \right) = (f(x))^2$.
> 
> By 1, $\left( f+g \right)^2$ and $\left( f-g \right)^2$ are [[Continuity|continuous]]. Thus
> $$fg = \dfrac{1}{4}(f+g)^2 - \dfrac{1}{4}(f-g)^2$$
> is [[Continuity|continuous]] by 1 and $2$.

> [!proof]- \- **4.8.4**
> $\psi(y) = \frac{1}{y}$ is [[Continuity|continuous]] for $y \ne 0$, so by [[Continuity Under Composition|composition rules]], if $f(x)$ is [[Continuity|continuous]], then so is $\left( \psi \circ g \right) = \frac{1}{g(x)}$ where $g(x) \ne 0$.
> 
> Thus, if $g(x) \ne 0$ for all $x \in I$, then $\frac{f}{g}$ is [[Continuity|continuous]] by 2, as it is the product of $f(x)$ and $\dfrac{1}{g(x)}$, which are both [[Continuity|continuous]].


[^1]: [[Continuity]]
