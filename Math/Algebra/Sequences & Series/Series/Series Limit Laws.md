---
tags:
  - atom
  - math
---
Let $\sum_{k=1}^\infty a_{k}$ and $\sum_{k=1}^\infty b_{k}$ be [[Partial Sums|convergent]] [[Series|series]], and let $c \in \R$.

> [!theorem]- **3.4.1** $\sum_{k=1}^\infty ca_{k} +b_{k}$ is [[Partial Sums|convergent]], and $$\sum_{k=1}^\infty a_{k} +b_{k}=\sum_{k=1}^\infty a_{n} + \sum_{k=1}^\infty b_{n}$$
> Let $\varepsilon > 0$ be given, and $\lim a_{n} = L$, and $\lim b_{n} = M$.
> 
> Then there exists $N$ (the maximum of $N_{a}$ and $N_{b}$) such that for all $n \ge N$,
> $$\begin{align}
> 	\left| a_{n} - L \right| &< \dfrac{\varepsilon}{2} \\
> 	\left| b_{n} - M \right| &< \dfrac{\varepsilon}{2}. \\
> \end{align}$$
> By the [[Triangle Ineqaulity|triangle inequality]],
> $$\begin{align}
> 	\left| \left( a_{n} + b_{n}  \right) - (L + M) \right| \le \left| a_{n} -L \right| + \left| b_{n} - M \right| < \varepsilon.
> \end{align}$$
> Thus, for all $\varepsilon > 0$, there exists $N$ such that for all $n \ge N$, $\left| (a_{n}+b_{n}) - \left( L+M \right) \right| < \varepsilon$, meaning the [[Sequence Convergence|limit]] of $\left( a_{n}+b_{n} \right)_{n=1}^\infty = L+M$.

> [!theorem]- **3.4.2** $\sum_{k=1}^\infty ca_{n}$ is [[Sequence Convergence|convergent]], and $$\sum_{k=1}^\infty ca_{n}=c\sum_{k=1}^\infty\lim a_{n}$$
> Suppose $c = 0$, then $ca_{n}$ is a constant [[Sequences|sequence]] $0$, so it converges to $0 = c \lim a_{n}$.
> 
> Let $\varepsilon > 0$, and $\lim a_{n} = L$, and $c \ne 0$.
> 
> Then there exists $N$ such that for all $n \ge N$ such that
> $$\begin{align}
> 	\left| a_{n} - L \right| < \dfrac{\varepsilon}{\left| c \right| } \\
> 	\left| c \right| \left| a_{n} - L \right| < \varepsilon \\
> 	\left| c\left( a_{n} - L \right) \right| < \varepsilon \\
> 	\left| ca_{n} - cL \right| < \varepsilon \\
> \end{align}$$
> Thus, the [[Sequence Convergence|limit]] of $\left( ca_{n} \right)_{n=1}^\infty$ is $cL = c\lim a_{n}$.

[^1]: [[Bounded Sequences]]. Theorem 2.8
