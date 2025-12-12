---
tags:
  - atom
  - math
---
A [[Sequences|sequence]] $(a_{n})$ *converges* to $L$ iff
$$\forall \varepsilon > 0, \exists N \in \N : \forall n \ge N, \left| a_{n} - L \right| < \varepsilon.$$

> [!theorem]- \- **Uniqueness of Limits of Sequences** - The *limit* of a [[Sequences|sequence]] is unique.
> Suppose $\left( a_{n} \right)^\infty_{n=1}$ converges  to $L,M \in \R$.
> 
> Then for $\frac{\varepsilon}{2} > 0$, there exists $N_{L}$ such that for all $n \ge N_{L}$,
> $$ \left| a_{n} - L \right| < \dfrac{\varepsilon}{2}, $$
> and similarly, there exists $N_{M}$ such that for all $n \ge N_{M}$,
> $$ \left| a_{n} - M \right| < \dfrac{\varepsilon}{2}. $$
> If $n \ge \max\{ N_{L},N_{M} \}$, then both will hold.
> 
> By the [[Triangle Ineqaulity|triangle inequality]],
> $$\left| L-M \right| \le \left| -\left( a_{n} - L \right) \right| + \left| a_{n}-M \right| < \varepsilon. $$
> 
> Thus, for any $\varepsilon > 0$, $\left| L-M \right| < \varepsilon$, so by [[Bounding with Epsilon|theorem 1.18.3]], $L = M$.

> [!theorem]- **2.5** If $a_{n} = c$ for all $n$, then $a_{n}$ *converges* to $c$.
> Let $\varepsilon > 0$ be given, and $N = 0$. Then for all $n \ge 0$,
> $$\begin{align}
> 	\left| a_{n}-L \right| &= \left| c-c \right| \\
> 	&= \left| 0 \right| \\
> 	&= 0 < \varepsilon && \varepsilon > 0 \\
> \end{align}$$

> [!definition] A [[Sequences|sequence]] $\left( a_{n} \right)$ *diverges* iff $\forall L \in \R, \exists \varepsilon > 0 : \forall N, \exists n\ge N : \left| a_{n} - L \right| \ge \varepsilon$
## Examples
> [!example]- **2.3** $\left( \dfrac{1}{n} \right)^\infty_{n=1}$ converges to $0$.
> Let $\varepsilon > 0$ be given.
> $$\begin{align}
> 	\left| a_{n} - L\right| &= \left| \dfrac{1}{n} - 0 \right| \\
> 	&= \left| \dfrac{1}{n} \right| \\
> 	&= \dfrac{1}{n} \\
> \end{align}$$
> By the [[The Real Numbers#Properties of The Reals|the Archimedean property]] applied to $x = \dfrac{1}{\varepsilon}$, there is an $N$ such that $\dfrac{1}{\varepsilon} < N$.
> Now if $n \ge N$, then $n \ge N > \dfrac{1}{\varepsilon}$, meaning $n > \dfrac{1}{\varepsilon}$, and thus $\dfrac{1}{n} < \varepsilon$.

> [!example]- $a_{n} = 1 - \dfrac{1}{n^2 + 1}$
> We expect $L=1$ as a limit.
> 
> Let $\varepsilon > 0$ be given. We want to test
> $$\begin{align}
> 	\left| a_{n}-L \right| &= \left| 1-\dfrac{1}{n^2-1}-1 \right| \\
> 	&= \left| -\dfrac{1}{n^2-1} \right| \\
> 	&= \dfrac{1}{n^2-1} \\
> \end{align}$$
> Using $\dfrac{1}{\varepsilon} < N$ as in example **2.3**, we have if $n \ge N$, then
> $$ \dfrac{1}{\varepsilon} < N \le n \le n^2 \le n^2 + 1$$
> Thus,
> $$\left| 1-\dfrac{1}{n^2-1}-1 \right| = \dfrac{1}{n^2 + 1} < \varepsilon$$

> [!example]- $b_{n} = \dfrac{n^2-1}{2n^2+3}$
> We expect $L = \dfrac{1}{2}$
> $$\begin{align}
> 	\left| b_{n} - L \right| &= \left| \dfrac{n^2-1}{2n^2+3} - \dfrac{1}{2} \right|  \\
> 	&\;\;\vdots \\
> 	&= \dfrac{5}{4n^2+6}
> \end{align}$$
> Note that $\dfrac{5}{4n^2+6} < \dfrac{5}{4n^2}$.
> $$\dfrac{5}{4n^2}<\varepsilon \to \dfrac{5}{4\varepsilon} < n^2 \to \sqrt{ \dfrac{5}{4\varepsilon} } < n$$
> By the [[The Real Numbers#Properties of The Reals|the Archimedean property]], there is an integer $N$ such that
> $$\sqrt{ \dfrac{5}{4\varepsilon} } < N$$
> If $n \ge N$, then
> $$\dfrac{5}{4n^2} \le \dfrac{5}{4N^2} < \varepsilon.$$
> Hence, for such $n$,
> $$\left| b_{n} - \dfrac{1}{2} \right| = \dfrac{5}{4n^2 + 6} < \varepsilon$$

\[[[The Real Numbers#Properties of The Reals]], The Archimedean Property\]
