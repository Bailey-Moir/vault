---
tags:
  - atom
  - math
  - discrete
---
The *Euclidean Algorithm* finds the [[Greatest Common Divisor|greatest common divisor]] by leveraging the fact that $\text{gcd}(a,b) = \text{gcd}(b,a \mod b)$.

![[Euclidean Greatest Common Divisor Algorithm]]

> [!proof]-
> You can prove that the [[Greatest Common Divisor|greatest common divisor]] of two numbers are equal by proving they have the same [[Sets|set]] of  [[Common Divisors|common divisors]].
> Let the [[Sets|set]] of [[Common Divisors|common divisors]] of two numbers $x,y$ be denoted $\text{cd}(x,y)$;
> $$\forall x,y, \text{cd}(x,y) = \left\{ c : c|x \land c|y \right\}$$
> ## $\left( \subseteq \right)$
> Let $c$ be some element of $\text{cd}(a,b)$. By the definition of [[Divisibility|divisibility]], $\exists! n,m \in \Z : a = nc \land b = mc$. Substituting into $a = qb + r$[^1],
> $$\begin{align*}
> 	nc &= qmc + r \\
> 	c(n - qm) &= r \\
> \end{align*}$$
> Since $n - qm \in \Z$, $c|r$. Since $c|b \land c|r$, $c \in \text{cd}(b,r)$, meaning $\text{cd}(a,b) \subseteq \text{cd}(b,r)$.
> 
> ## $\left( \supseteq \right)$
> Let $c$ be some element of $\text{cd}(b,r)$. By the definition of [[Divisibility|divisibility]], $\exists! n,m \in \Z : b = nc \land r = mc$. Substituting into $a = qb + r$[^1],
> $$\begin{align*}
> 	a &= qnc + mc \\
> 	&= c(qn+m) \\
> \end{align*}$$
> 
> Since $qn + m \in \Z$, $c|a$. Thus $c|a \land c|b$, $c \in \text{cd}(a,b)$, meaning $\text{cd}(b,r) \subseteq \text{cd}(a,b)$.
> 
> ## Conclusion
> $\text{cd}(a,b) \subseteq \text{cd}(b,r) \land \text{cd}(b,r) \subseteq \text{cd}(a,b) \implies \text{cd}(a,b) = \text{cd}(b,r)$[^2]
> 
> Since the [[Common Divisors|common divisors]] are the same, the [[Greatest Common Divisor|greatest of the common divisor]] must be the same, meaning $\gcd(a,b) = \gcd(b,r)$
> 
> \[[[Subsets]], [[Universal Quantifier]]\]

> [!proof]- (Intuitive Version)
> In $a = qb + r$[^1], 
> - $a$ is a [[Linear Combinations|linear combination]] of $b$ and $r$, so if some $c$ [[Divisibility|divides]] $b$ and $r$, it must divide $a$, and similarly,
> - $r$ is a [[Linear Combinations|linear combination]] of $a$ and $b$, so if some $c$ [[Divisibility|divides]] $a$ and $b$, it must divide $r$.
> ![500|center](euclidean-algorithm-proof.excalidraw.md)
>
> Thus, any divisor of $a$ and $b$ must be a divisor of $b$ and $r$, and vice versa, so they must have the same set of [[Common Divisors|common divisors]]. Thus, the [[Greatest Common Divisor|greatest of these common divisors]] must be the same.

\[[[Greatest Common Divisor]]\]

[^1]: [[The Division Algorithm]]
[^2]: [[Set Equality]]