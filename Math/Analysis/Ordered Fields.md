---
tags:
  - atom
  - math
---
A [[Fields|field]] $\F$ with a [[Total Order|total order]] is an *ordered field* iff two axioms called $OF1$ and $OF2$ hold:
$$\begin{array}{rll}
	\forall a,b,c \in \F & a \le b \implies a + c \le b + c & \text{(OF1)} \\
	\forall a,b \in \F & a,b \ge 0 \implies ab \ge 0 & \text{(OF2)} \\
\end{array}$$
# Ordered Field Theorems 
> [!theorem]- **1.6.1** $a \le b, c \ge 0 \implies ac \le bc$
> $$\begin{align}
> 	a \le b \,&\implies a+(-a) \le b + (-a) && \text{(OF1)} \\
> 	&\implies 0 \le b - a && \text{Additive Inverse} \\
> \end{align}$$
> $$\begin{align}
> 	b - a, c\ge 0 \,&\implies (b-a)c \ge 0 && \text{(OF2)} \\
> 	&\implies bc - ac \ge 0 && \text{Distributivity} \\
> 	&\implies bc - ac + ac \ge 0 + ac  \\
> 	&\implies bc \ge ac && \text{Additive Identity \& Inverse} \\
> \end{align}$$

> [!theorem]- **1.6.2** $a \le b, c \le 0 \implies ac \ge bc$
> $$\begin{align}
> 	a \le b \,&\implies a+(-a) \le b + (-a) && \text{(OF1)} \\
> 	&\implies 0 \le b - a && \text{Additive Inverse} \\
> \end{align}$$
> $$\begin{align}
> 	c \le 0 \,&\implies c+(-c) \le 0 + (-c) && \text{(OF1)} \\
> 	&\implies 0 \le -c && \text{Additive Identity \& Inverse} \\
> \end{align}$$
> $$\begin{align}
> 	b - a, -c \ge 0  \,&\implies (b-a)(-c) \ge 0 && \text{(OF2)} \\
> 	&\implies -bc + ac \ge 0 && \text{Distributivity} \\
> 	&\implies bc - bc + ac \ge bc + 0 \\
> 	&\implies ac \ge bc && \text{Additive Identity \& Inverse} \\
> \end{align}$$

>[!theorem]- **1.6.3** $a \le b \implies -a \ge -b$
> $$\begin{align*}
> 	a \le b \\
> 	a - a \le b - a \\
> 	0 \le b - a && \text{Additive Inverse} \\
> 	-b \le -b + b - a && \text{Additive Identity}\\
> 	-b \le -a && \text{Additive Inverse} \\
> 	-a \ge -b \\
> \end{align*}$$

> [!theorem]- **1.7** $a^2 \ge 0 \land \left( a^2 = 0 \leftrightarrow a= 0 \right)$ (Positive Definite)
> $\mathbf{\left( a^2 \ge 0 \right)}$
> If $a \ge 0$, then applying $\text{OF2}$ where $b=a$ directly gives $0 \le a^2$.
> If $a \le 0$, by **(2)**, multiplying by $a$ reverses the inequality:
> $$\begin{align*}
> 	a &\le 0 \\
> 	a \times a &\ge 0 \times a && \textbf{(2)} \\
> 	a^2 &\ge 0 && (1) \\
> \end{align*}$$
> Thus, in either case, $0 \le a^2$.
> 
> $\mathbf{\left( a^2 = 0 \iff a = 0 \right)}$
> $(\implies)$
> Suppose $a^2 = 0$ and $a \ne 0$. Then $a$ must have a multiplicative inverse.
> $$\begin{align}
> 	a &= 0 \\
> 	a \times a^{-1} &= 0 \times a^{-1} \\
> 	1 &= 0 \times a^{-1} && \text{Multiplicative Inverse} \\
> 	1 &= 0 && (1) \\
> 	a \times1 &= a \times 0 \\
> 	a &= 0 && (1) \\
> \end{align}$$
> Thus, $a \ne 0$ and $a = 0$. This is a [[Proof by Contradiction|contradiction]], so if $a^2 = 0$, then $a = 0$.
> 
> $\left( \impliedby \right)$
> If $a = 0$, then $a^2 = a \times a = 0 \times 0 = 0$ by $(1)$.
> 
> \[$(1)$ [[Fields]], Theorem 1\]

> [!corollary]- of **1.7** $1 > 0$
> Using $a = 1$ in $\mathbf{(4)}$ gives $1 \times 1 = 1 \ge 0$ (by the multiplicative identity).
> If $1 = 0$, then for all $a$, $a = 0$. This would mean $\F\setminus \{ 0 \} = \emptyset$, but there is a (multiplicative) [[Groups|group]] on this set, meaning it must contain an identity, which is a [[Contradictions|contradiction]]. Thus, $1 \ne 0$.
> Thus, $1 > 0$.

\[[[Fields]]\]