---
tags:
  - atom
  - math
---
> [!theorem]- **2.20.1** $\forall x \in \R,\varepsilon>0, \exists a \in \Q : \left| x-a \right|<\varepsilon$
> By [[The Real Numbers#Properties of The Reals|the Archimedian property]], there is an $n \in \Z^+$ such that
> $$\dfrac{1}{\varepsilon} < n.$$
> By [[Supremums with Archimedian Property|theorem 2.19.2]], there exists $m \in \Z$ such that
> $$\begin{array}{C}
> 	\dfrac{m}{n} \le x \le \dfrac{m+1}{n} \\
> 	0 \le x - \dfrac{m}{n} \le \dfrac{1}{n} \\
> 	\left| x - \dfrac{m}{n} \right| \le \dfrac{1}{n} < \varepsilon. \\
> \end{array}$$

> [!theorem]- **2.20.2** For all $x \in \R$, there is a [[Sequences|sequence]] $\left( x_{n} \right)$ of [[Number Sets|rational numbers]] with $\lim x_{n} = x$
> Let $\left( \varepsilon_{n} \right)$ be any [[Sequences|sequence]] where $\varepsilon_{n} > 0$ and  $\lim \varepsilon_{n} = 0$.
> 
> Thus, by *theorem 2.20.1*, we will define $x_{n} \in \Q$ such that
> $$\begin{align}
> 	\forall n, \hspace{0.5em}\left| x-x_{n} \right| &< \varepsilon_{n} \\
> 	\lim\left| x-x_{n} \right| &\leq \lim\varepsilon_{n} && \text{Proof?} \\
> 	\lim\left| x-x_{n} \right| &\leq 0 \\
> 	\lim\left| x-x_{n} \right| &= 0 \\
> 	\lim \left( x-x_{n} \right) &= 0 \\
> 	x - \lim x_{n} &= 0 \\
> 	\lim x_{n} &= x \\
> \end{align}$$

> [!theorem]- **2.22** Let $I_{n} = \left[ a_{n},b_{n} \right]$ be a [[Sequences|sequence]] of [[Intervals|closed intervals]] such that $I_{1} \supseteq I_{2} \supseteq I_{3} \supseteq \cdots$.<ol><li>$\exists p \in\R:\forall n,p \in I_{n}$</li><li>$\lim\left( b_{n}-a_{n} \right) = 0 \to \forall p,q, \left[ \left( \forall n, p,q \in I_{n} \right) \to p = q \right]$</li></ol>
> Since $I_{1} \supseteq I_{2} \supseteq I_{3} \supseteq \cdots$, $a_{1} \le a_{2} \le a_{3} \le \cdots$ and $b_{1} \ge b_{2} \ge b_{3} \ge \cdots$, so $\left( a_{n} \right)$ and $\left( b_{n} \right)$ are [[Monotone Sequences|monotonic]]. They are also [[Bounded Sequences|bounded]] since every term is in $I_{1}$.
> 
> Thus, $p = \lim a_{n}$ exists by [[Monotone Convergence Theorem|monotone convergence theorem]]. Since $a_{n}$ is [[Monotone Sequences|increasing]], for all $n$, $a_{n} \le p$.
> 
> Let $m$ be given. For all $n \ge m$, $a_{n} \le b_{n} \le b_{m}$. Thus, $p=\lim a_{n} \le b_{m.}$.
> 
> This gives $p = \lim a_{n} \in I_{n}$ for all $n$. $\square_{1}$
> 
> If $\lim\left( b_{n}-a_{n} \right) = 0$,
> $$\begin{align}
> 	\lim b_{n} &= \lim \left( b_{n} - a_{n} + a_{n} \right) \\
> 	&= \lim \left( b_{n} - a_{n} \right) + \lim a_{n} && (1) \\
> 	&= 0 + p = p \\
> \end{align}$$
> Thus, if $q \in I_{n}$ for all $n$, by [[Squeeze Theorem|squeeze theorem]], $p = q$. $\square_{2}$