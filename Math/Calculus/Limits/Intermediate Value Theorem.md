---
tags:
  - math
  - atom
---
![400|center](intermediate-value-theorem.excalidraw.md)
Suppose $f(x)$ is [[Continuity|continuous]] on $\left[a,b\right]$. The *intermediate value theorem* states that for every $y$ in $\left[f(a),f(b)\right]$ or $\left[ f(b),f(a) \right]$, there exists an input in $[a,b]$ that maps to it. 
$$\begin{align}
	f \in \mathcal{C}(\left[a,b\right]) \implies \forall N \in &\left[ \min\{f(a),f(b)\}, \max \{f(a),f(b)\} \right],  \\
	&\exists c \in \left[ a,b \right] : f(c) = N
\end{align}$$

> [!proof]-
> If $f(a) = f(b)$, let $c = a$. Otherwise, without loss of generality, we assume that $f(a) < f(b)$ (if $f(b) < f(a)$, we can flip it to $-f$).
> 
> Let $y \in \R$ such that $f(a) \le y \le f(b)$. Consider $I_{0} = \left[ a_{0},b_{0} \right]$, where $a_{0}=a$ and $b_{0} = b$.
> 
> Let $n \in \N$. Let $m_{n} = \frac{1}{2}(a_{n}+b_{n})$, and
> $$I_{n+1} = \left[ a_{n+1},b_{n+1} \right]  = \begin{cases}
> 	\left[ a_{n},m_{n} \right]  & f(m_{n})\ge y \\
> 	\left[ m_{n},b_{n} \right]  & f(m_{n})<y \\
> \end{cases}$$
> 
> Then by [[Induction|induction]],
> - $\left( a_{n} \right)$ is [[Monotone Sequences|increasing]] and [[Bounded Sequences|bounded above]] by $b$,
> - $\left( b_{n} \right)$ is [[Monotone Sequences|decreasing]] and [[Bounded Sequences|bounded below]] by $a$,
> - $\lim\left( b_{n}-a_{n} \right) = \lim\dfrac{b-a}{2^n} = 0$, and
> - $\forall n \in \N, f(a_{n}) \le y \le f(b_{n})$.
> 
> We now show that for all $\varepsilon>0$, $\left| f(c)-y \right|<\varepsilon$, meaning $f(c) = y$[^1].
> 
> Let $\varepsilon>0$ be given. Since $f \in \mathcal{C}(\{ c \})$[^2], there exists $\delta>0$ such that for all $x \in \R$,
> $$\left| x-c \right| < \delta \to \left| f(x)-f(c) \right| < \varepsilon.$$
> Both $\left( a_{n} \right)$ and $\left( b_{n} \right)$ [[Metric Sequence Convergence|converge]] by [[Monotone Convergence Theorem|monotone convergence theorem]] to $c$, so we can find $N$ for which for all $n \ge N$,
> $$\begin{array}{c}
> 	\left| a_{n}-c \right| < \delta, \\
> 	\left| b_{n}-c \right| < \delta. \\
> \end{array}$$
> Then
> $$\begin{array}{c}
> 	\left| f(a_{N})-f(c) \right| < \varepsilon, \\
> 	\left| f(b_{N})-f(c) \right| < \varepsilon. \\
> \end{array}$$
> This gives
> $$\begin{array}{c}
> 	f(a_{N})\leq y \leq f(b_{N}) \\
> 	-\varepsilon<f(a_{N}) - f(c)\leq y-f(c) \leq f(b_{N})-f(c)<\varepsilon \\
> 	-\varepsilon< y-f(c) <\varepsilon,
> \end{array}$$
> thus, $\left| y-f(c) \right| < \varepsilon$.

[^1]: [[Bounding with Epsilon]], Theorem 1.18.3
[^2]: [[Continuity]]
