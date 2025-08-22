---
tags:
  - math
  - atom
---
![500|center](epsilon-delta-limit.excalidraw.md)
Let $f$ be a [[Functions|function]] [[Defined Near|defined near]] to $a \in \R$. We say that $L \in \R$ is a *limit* of $f$ as $x$ approaches $a$ iff for every $\varepsilon>0$, there exists $\delta > 0$ such that for all $x \in \R$ with $0 < \left| x-p \right| < \delta$, we have that $x \in \text{domain}(f)$ and that $\left| f(x) - L \right| < \varepsilon$; iff
$$\forall \varepsilon>0, \exists \delta>0: \forall x \in \R,  0 < \left|x-a\right| < \delta \to  \left|f(x) - L\right| < \varepsilon$$
> [!theorem]- \- **Uniqueness of Limits of Functions** - Let $f$ be a [[Functions|function]] defined near to $a \in \R$. If $L$ and $M$ are both limits of $f$ as $x$ approaches $a$. Then $L = M$.
> 
> Let $f$ be a [[Functions|function]] defined near $a \in \R$. Suppose $L$ and $M$ are both limits of $f$ as $x \to a$.
> 
> Let $\varepsilon > 0$ be given. Since $L$ and $M$ are limits, there exists $\delta_{L},\delta_{M} > 0$ such that
> $$\begin{array}{rl}
> 	\left| f(x) - L \right| < \dfrac{\varepsilon}{2} & \text{if } 0 < \left| x - a \right| < \delta_{L} \\
> 	\left| f(x) - M \right| < \dfrac{\varepsilon}{2} & \text{if } 0 < \left| x - a \right| < \delta_{M}. \\
> \end{array}$$
> Then for all $x$ such that $0 < \left| x - a \right| <\text{min}\{ \delta_{L},\delta_{M} \}$,
> $$\begin{array}{c}
> 	\left| f(x) - L \right| < \dfrac{\varepsilon}{2} \\
> 	\left| f(x) - M \right| < \dfrac{\varepsilon}{2}. \\
> \end{array}$$
> Hence,
> $$\begin{align}
> 	\left| L - M \right| &= \left| L - f(x) + f(x) - M \right| \\
> 	&\le \left| L - f(x) \right| + \left| f(x) - M \right| && (1) \\
> 	&\le \dfrac{\varepsilon}{2} + \dfrac{\varepsilon}{2} \\
> 	&\le \varepsilon. \\
> \end{align}$$
> Since $\varepsilon > 0$ is arbitrary, we conclude $L = M$[^1]

> [!example]- $\displaystyle \forall c > 0, \lim_{ x \to \infty } \sqrt{ x } = \sqrt{ c }$
> Let $c>0$ and $\varepsilon>0$ be given, and subsequently, let $\delta =\text{min}\{ c,\varepsilon \sqrt{ c } \}$. Then for all $x \in \R$, if
> $$\left| x-c \right| < \delta = \text{min}\{ c,\varepsilon \sqrt{ c } \},$$
> then by definition,
> $$\begin{align}
> 	\left| x-c \right| &< \varepsilon \sqrt{ c } \\
> 	\to \left| x-c \right| &< \varepsilon \left| \sqrt{ x }+\sqrt{ c } \right|, && (1)  \\
> \end{align}$$
> as
> $$\begin{align}
> 	&\phantom{<}\,\left| x-c \right| < c  \\
> 	-c &< x-c  \\
> 	0 &< x \\
> 	0 &< \sqrt{ x } \\
> 	\sqrt{ c } &< \sqrt{ x } + \sqrt{ c } = \left| \sqrt{ x } + \sqrt{ c } \right|.  \\
> \end{align}$$
> Thus, continuing from $(1)$,
> $$\begin{align}
> 	\dfrac{\left| x-c \right|}{\left| \sqrt{ x }+\sqrt{ c } \right| } &< \varepsilon \\
> 	\left| \dfrac{\left( \sqrt{ x } + \sqrt{ c } \right)\left( \sqrt{ x }-\sqrt{ c } \right)}{\sqrt{ x }+\sqrt{ c }} \right|  &< \varepsilon \\
> 	\left| \sqrt{ x }-\sqrt{ c } \right|  &< \varepsilon \hspace{1em}\square \\
> \end{align}$$
> > [!motivation]-
> > Let $\varepsilon > 0$ be given. To show $f(x) \to \sqrt{ c }$ as $x\to c$ for all $c>0$, suppose
> > $$\begin{align}
> > 	\left| \sqrt{ x } - \sqrt{ c } \right| &< \varepsilon \\
> > 	\iff \left| \dfrac{x-c}{\sqrt{ x }+\sqrt{ c }} \right| &< \varepsilon \\
> > 	\iff \left| x-c \right| &< \varepsilon \left| \sqrt{ x }+\sqrt{ c }  \right|. \\
> > \end{align}$$
> > Let $\delta \le c$. Then
> > $$\begin{align}
> > 	\left| x-c \right| &< \delta = c \\
> > 	-c < x-c &<  c \\
> > 	0 < x &< 2c \\
> > 	0 < \sqrt{ x } &< \sqrt{ 2c } \\
> > 	\sqrt{ c } < \sqrt{ x } + \sqrt{ c } &< \left( 1+\sqrt{ 2 } \right)\sqrt{ c }. \\
> > \end{align}$$
> > Substituting this in,
> > $$\begin{align}
> > 	\impliedby \left| x-c \right| &< \varepsilon \sqrt{ c }.
> > \end{align}$$


\[$(1)$ [[Triangle Ineqaulity]]\]

[^1]: [[Bounding with Epsilon]], Theorem 1.18.3