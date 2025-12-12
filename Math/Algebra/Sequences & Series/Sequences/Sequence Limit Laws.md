---
tags:
  - atom
  - math
---
Let $\left( a_{n} \right)_{n=1}^\infty$ and $\left( b_{n} \right)_{n=1}^\infty$ be [[Metric Sequence Convergence|convergent sequences]], and let $c \in \R$.
> [!theorem]- **2.6.1** $\left( ca_{n} \right)_{n=1}^\infty$ is [[Metric Sequence Convergence|convergent]], and $$\lim(ca_{n})=c\lim a_{n}$$
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
> Thus, the [[Metric Sequence Convergence|limit]] of $\left( ca_{n} \right)_{n=1}^\infty$ is $cL = c\lim a_{n}$.

> [!theorem]- **2.6.2** $\left( a_{n} +b_{n} \right)_{n=1}^\infty$ is [[Metric Sequence Convergence|convergent]], and $$\lim(a_{n}+b_{n})=\lim a_{n}+\lim b_{n}$$
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
> Thus, for all $\varepsilon > 0$, there exists $N$ such that for all $n \ge N$, $\left| (a_{n}+b_{n}) - \left( L+M \right) \right| < \varepsilon$, meaning the [[Metric Sequence Convergence|limit]] of $\left( a_{n}+b_{n} \right)_{n=1}^\infty = L+M$.

> [!theorem]- **2.11** $\left( a_{n}b_{n} \right)_{n=1}^\infty$ is [[Metric Sequence Convergence|convergent]], and $$\lim(a_{n}b_{n})=\lim a_{n}\times\lim b_{n}$$
> Since $\left( a_{n} \right)$ is [[Metric Sequence Convergence|convergent]], it is [[Bounded Sequences|bounded]][^1]. Thus, there exists $K \in \R$ such that $\left| a_{n} \right| \le K$ for all $n$.
> $$\begin{align}
> 	\left| a_{n}^2 - L^2 \right| &= \left| \left( a_{n}-L \right)\left( a_{n}+L \right) \right| \\
> 	&= \left| a_{n}-L \right|\left| a_{n}+L \right| \\
> 	&\le \left| a_{n}-L \right|\left( \left| a_{n} \right| + \left| L \right| \right) \\
> 	&\le \left| a_{n}-L \right|\left( K + \left| L \right| \right) .\\
> \end{align}$$
> $\left( a_{n} \right)$ [[Metric Sequence Convergence|converges]], so $\lim \left| a_{n}-L \right| = 0$, meaning
> $$\begin{align}
> 	\lim \left( \left| a_{n}-L \right| \left( K+ \left| L \right|  \right) \right)  &= \left( K+\left| L \right|  \right)\lim\left| a_{n}-L \right| && 2.6.1 \\
> 	&= \left( K+\left| L \right|  \right)0  \\
> 	&= 0  \\
> \end{align}$$
> Thus, by [[Squeeze Theorem for Sequences|squeeze theorem]], since for all $n$,
> $$0 \le \left| a_{n}^2 - L^2 \right| \le \left| a_{n}-L \right| \left( K + \left| L \right|  \right), $$
> and $\lim 0 = 0 = \lim \left( \left| a_{n}-L \right| \left( K+ \left| L \right|  \right) \right)$, this gives
> $$\lim \left| a_{n}^2 - L^2 \right| = 0.$$
> 
> From the *limit laws* already proven, the limit of
> $$\dfrac{\left( a_{n}+b_{n} \right)^2 - \left( a_{n}-b_{n} \right)^2}{4} = a_{n}b_{n}$$
> gives
> $$\dfrac{\left( \lim a_{n} + \lim b_{n} \right)^2 - \left( \lim a_{n} - \lim b_{n} \right)^2}{4} = \lim a_{n} \times \lim b_{n}$$

> [!theorem]- **2.13** if $b_{n} \ne 0$ for all $n \in \N$, and $\lim b_{n} \ne 0$, then $$\lim \dfrac{a_{n}}{b_{n}} = \dfrac{\lim a_{n}}{\lim b_{n}}$$
> #TODO

> [!note] **2.6** implies [[Metric Sequence Convergence|limit of sequences]] is a [[Linear Maps|linear map]].

[^1]: [[Bounded Sequences]]. Theorem 2.8
