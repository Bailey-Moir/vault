---
tags:
  - atom
  - math
---
Let $a,b \in \R$. Then:
- $|ab| = |a||b|$
> [!proof]-
> $$\begin{align*}
> 	(|ab|)^2 &= (ab)^2 && \forall z \in \R, |z|^2 = z^2 \\
> 	&= a^2b^2 \\
> 	&= |a|^2|b|^2 && \forall z \in \R, |z|^2 = z^2 \\
> 	&= (|a||b|)^2 \\
> 	|ab| &= |a||b| \\
> \end{align*}$$
> 
> Proof that you can perform that last square root:
> $\forall x \ge 0, y \ge 0 \in \R,$ $$\begin{align*}
> 	& x \le y \iff x^2 \le y^2 \\
> 	& x \ge y \iff x^2 \ge y^2 \\
> 	\therefore\hspace{1em} & x = y \iff x^2 = y^2 && (1)
> \end{align*}$$
> \[(1) [[Antisymmetric Property]] of [[Partial Order]]\]

- $|a + b| \le |a| + |b|$ (Triangle Inequality)
> [!proof]-
> $$\begin{align*}
> 	|a+b|^2 &= (a+b)^2 && \forall z \in \R, |z|^2 = z^2 \\
> 	&= a^2 + 2ab + b^2 \\
> 	&\le a^2 + 2|ab| + b^2 && \forall z \in \R, z \le |z| \\
> 	&\le a^2 + 2|a||b| + b^2 \\
> 	&\le |a|^2 + 2|a||b| + |b|^2 && \forall z \in \R, |z|^2 = z^2 \\
> 	&\le (|a| + |b|)^2\\
> 	|a+b| &\le |a| + |b| && \forall x \ge 0, y \ge 0 \in \R, (x \le y \iff x^2 \le y^2)
> \end{align*}$$

\[[[Absolute Values]]\]