---
tags:
  - atom
  - math
---
A [[Sequences|sequence]] $(a_{n}) : \N \to M$ for some [[Metric Spaces|metric space]] $M$ *converges* to $\lambda \in M$ iff
$$\forall \varepsilon > 0, \exists N \in \N : \forall n \ge N, d(a_{n}, \lambda) < \varepsilon.$$
> [!theorem]- *(Uniqueness of Limits)* The *limit* of a [[Sequences|sequence]] is unique.
> Suppose $\left( a_{n} \right)^\infty_{n=1}$ converges  to $\lambda_{1},\lambda_{2} \in \R$.
> 
> Then for $\frac{\varepsilon}{2} > 0$, there exists $N_{\lambda_{1}}$ and $N_{\lambda_{2}}$ such that
> $$\begin{align}
> 	d(a_{n}, \lambda_{1}) &< \dfrac{\varepsilon}{2}, && \forall n \ge N_{\lambda_{1}} \\
> 	d(a_{n}, \lambda_{2}) &< \dfrac{\varepsilon}{2}. && \forall n \ge N_{\lambda_{2}} 
> \end{align}$$
> Thus, if $n \ge N = \max\{ N_{\lambda_{1}},N_{\lambda_{2}} \}$, then both will hold.
> 
> By the [[Triangle Ineqaulity|triangle inequality]],
> $$d(\lambda_{1}, \lambda_{2}) \le d(a_{n},\lambda_{1}) + d(a_{n}, \lambda_{2}) < \varepsilon.$$
> Thus, for any $\varepsilon > 0$, $d(\lambda_{1},\lambda_{2}) < \varepsilon$, so by [[Bounding with Epsilon|theorem 1.18.3]], $\lambda_{1} = \lambda_{2}$. $\square$
> 
> This is also given directly by [[Metric Spaces|Metric spaces]] inducing a [[Hausdorff Spaces|Hausdorff space]], and [[Hausdorff Spaces#^unique-limits|Hausdroff spaces have unique limits]].
^uniqueness

> [!theorem]- *(Const. Conv.)* If $a_{n} = c$ for all $n$, then $a_{n}$ *converges* to $c$.
> Let $\varepsilon > 0$ be given, and $N = 0$. Then for all $n \ge 0$,
> $$ d(a_{n}, c) = d(c, c) = 0 < \varepsilon. $$
^constant-convergence

> [!definition] A [[Sequences|sequence]] $\left( a_{n} \right)$ **diverges** iff $\forall \lambda \in M, \exists \varepsilon > 0 : \forall N \in \N, \exists n\ge N : d(a_{n}, \lambda) \ge \varepsilon$.
^divergence
## Examples
> [!example]- **2.3** $\left( \dfrac{1}{n} \right)^\infty_{n=1}$ converges to $0$ in $\R$.
> Let $\varepsilon > 0$ be given.
> $$\begin{align}
> 	\left| a_{n} - L\right| &= \left| \dfrac{1}{n} - 0 \right| \\
> 	&= \left| \dfrac{1}{n} \right| \\
> 	&= \dfrac{1}{n} \\
> \end{align}$$
> By the [[The Real Numbers#Properties of The Reals|the Archimedean property]] applied to $x = \dfrac{1}{\varepsilon}$, there is an $N$ such that $\dfrac{1}{\varepsilon} < N$.
> Now if $n \ge N$, then $n \ge N > \dfrac{1}{\varepsilon}$, meaning $n > \dfrac{1}{\varepsilon}$, and thus $\dfrac{1}{n} < \varepsilon$.

> [!example]- $a_{n} = 1 - \dfrac{1}{n^2 + 1}$ in $\R$.
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

> [!example]- $b_{n} = \dfrac{n^2-1}{2n^2+3}$ in $\R$.
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
