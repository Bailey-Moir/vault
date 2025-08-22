---
tags:
  - atom
  - comp
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
> 	\lim\left| x-x_{n} \right| &= 0 && \text{Proof?} \\
> 	\lim \left( x-x_{n} \right) &= 0 \\
> 	x - \lim x_{n} &= 0 \\
> 	\lim x_{n} &= x \\
> \end{align}$$

![[Pasted image 20250818110842.png]]