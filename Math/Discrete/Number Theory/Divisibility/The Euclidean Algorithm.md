---
tags:
  - atom
  - math
  - discrete
---
![[Euclidean Greatest Common Divisor Algorithm]]

> [!proof]-
Let the [[Sets|set]] of [[Common Divisors|common divisors]] of two numbers $x,y$ be denoted $\text{cd}(x,y)$.
> $\forall c \in \text{cd}(a,b), c|a \land c|b$. By the definition of [[Divisibility|divisibility]], $\exists! n,m \in \Z : a = nc \land b = mc$. Substituting into $a = qb + r$ (see [[The Division Algorithm]]),
> $$\begin{align*}
> 	nc &= qmc + r \\
> 	c(n - qm) &= r \\
> \end{align*}$$
> Since $n - qm \in \Z$, $c|r$. Since $c|b \land c|r$, $c \in \text{cd}(b,r)$, meaning $\text{cd}(a,b) \subseteq \text{cd}(b,r)$.
> 
> $\forall c \in \text{cd}(b,r), c|b \land c|r$. By the definition of [[Divisibility|divisibility]], $\exists! n,m \in \Z : b = nc \land r = mc$. Substituting into $a = qb + r$ (see [[The Division Algorithm]]),
> $$\begin{align*}
> 	a &= qnc + mc \\
> 	&= c(qn+m) \\
> \end{align*}$$
> 
> Since $qn + m \in \Z$, $c|a$. Thus $c|a \land c|b$, $c \in \text{cd}(a,b)$, meaning $\text{cd}(b,r) \subseteq \text{cd}(a,b)$.
> 
> $\text{cd}(a,b) \subseteq \text{cd}(b,r) \land \text{cd}(b,r) \subseteq \text{cd}(a,b) \implies \text{cd}(a,b) = \text{cd}(b,r)$ (see [[Set Equality]])
> 
> Since [[Common Divisors|common divisors]] are the same, the [[Greatest Common Divisor|greatest of the common divisor]] must be the same, meaning $\gcd(a,b) = \gcd(b,r)$
> 
> \[[[Subsets]], [[Universal Quantifier]]\]

> [!proof]- (Intuitive Version)
> $$\begin{align*}
> 	\text{cd}(a,b) = \text{cd}(b,r) &\hspace{0.5ex}\implies \gcd(a,b) = \gcd(b,r) \\
> 	\\
> 	\text{cd}(a,b) = \text{cd}(b,r) &\hspace{0.5ex}\iff c|a \land c|b \iff c|b \land c|r \\
> 	&\hspace{0.5ex}\iff (c|a \land c|b \implies c|r) \land (c|b \land c|r \implies c|a) \\
> \end{align*}$$
> In $a = qb + r$, $a$, $b$, and $r$ are [[Linear Combinations|linear combinations]] of each other over the integers, so if two of them are multiples of $c$, the other must be, thus proving the two [[Logical Implication|one way implications]], and thus that $\gcd(a,b) = \gcd(b,r)$.



\[[[Greatest Common Divisor]]\]