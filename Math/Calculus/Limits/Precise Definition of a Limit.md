---
tags:
  - math
  - atom
---
![500|center](precise-definition-of-limit.excalidraw.md)
Let $f$ be a function defined on some open interval that contains the number $a$, except possibly at $a$ itself. Then we say that the limit of $f(x)$ as $x$ approaches $a$ is $L$, and we write $\displaystyle \lim_{x\to a} f(x) = L$ if for every number $\varepsilon > 0$ there is a number $\delta > 0$ such that if $0 < \left| x -a \right| < \delta$ then $\left| f(x) - L \right| < \varepsilon$.
$$
\begin{align*}
\lim_{x\to a} f(x) = L \iff \forall \varepsilon>0, \exists \delta>0 \ni
\left(\phantom{\int}\hspace{-1em} 0 < \left|x-a\right| < \delta \underset{\textcolor{gray}{\hspace{.9em}\not{\hspace{-.9em}\iff}}}{\implies} \left|f(x) - L\right| < \varepsilon \right)
\end{align*}
$$
# Precise Definition of One-Sided a Limit
![1000|center](precise-definition-of-onesided-limit.excalidraw.md)
$$
\begin{alignat}{3}
	\lim_{x\to a^+}& f(x) = L \iff \forall \varepsilon>0, \exists \delta>0 \ni
	(x \in &&\left(a, a+\delta\right) \underset{\textcolor{gray}{\hspace{.9em}\not{\hspace{-.9em}\iff}}}{\implies} \left|f(x) - L\right| < \varepsilon)
\\
	\phantom{\lim}_{x\to a^-}& &&(a-\delta,a)
\end{alignat}
$$
# Precise Definition of a Limit at Infinity
$$\begin{alignat}{3}
	\lim_{x\to\infty}& f(x) = L \iff \forall \varepsilon > 0, \exists N \ni ( x &&> N \implies |f(x) - L| < \varepsilon ) 
\\
	\phantom{\lim}_{x\to-\infty}& &&< \\
\end{alignat}$$
# Precise Definition of an Infinite Limit at Infinity
$$ \lim_{x\to\infty} f(x) = \infty \iff  \forall M > 0, \exists N \ni ( x > N \implies f(x) > M ) $$
