---
tags:
  - atom
  - math
---
If $F$ is a [[Fields|field]] with a [[Total Order|total order]], it is an ordered field if two axioms called $OF1$ and $OF2$ hold.
$$\begin{array}{rl}
	(OF1) & a \le b \implies a + c \le b + c \\
	(OF2) & 0 \le a \land 0 \le b \implies 0 \le ab \\
\end{array}$$
>[!theorem]- 1.7
> Let $a,b,c$ belong to an ordered field. Then 
> - $a \le b, 0 \le c \implies ac \le bc$
> > [!proof]-
> > We can use the multiplicative property from $OF2$. This references $0$. First, we turn $a \le b$ into an inequality involving $0$. If we apply  $OF1$ with the additive inverse of $a$, we get 
> > $$ 0 \le b - a $$
> > We can apply $OF2$ with $0 \le c$.
> > $$\begin{align*}
> > 	0 \le (b-a)c \\
> > 	0 \le bc - ac \\
> > \end{align*}$$
> > Applying $OF1$, adding $ac$ to both sides gives
> > $$ac \le bc$$
> - $a \le b, c \le 0 \implies bc \le ac$
> > [!proof]-
> > We have already $a \le b$ and $0 \le -c$ (with the additive identity). Applying the first property with $-c$ instead of $c$, we get
> > $$\begin{align*}
> >	a(-c) &\le b(-c) \\
> >	-ac &\le -bc \\
> >	bc &\le ac && \text{Additive inverse} \\
> > \end{align*}$$
> - In particular, $a \le b \implies -a \ge -b$
> >[!proof]-
> > $$\begin{align*}
> > 	a \le b \\
> > 	a - a \le b - a \\
> > 	0 \le b - a && \text{Additive inverse} \\
> > 	-b \le -b + b - a \\
> > 	-b \le -a && \text{Additive inverse} \\
> > 	-a \ge -b \\
> > \end{align*}$$

> [!theorem]- 1.8
> In an ordered field, $0 \le a^2$. Also $a^2 = 0 \iff a= 0$.
> > [!proof]-
> > If $0 \le a$, then applying $0F2$ where $b=a$ gives directly $0 \le a^2$.
> > If $a \le 0$, by theorem 1.7, multplying by $a$ revereses the inequality:
> > $$\begin{align*}
> > 	0 \times a &\le a \times a \\
> > 	0 &\le a^2 \\
> > \end{align*}$$
> > In either case, $0 \le a^2$.

\[[[Fields]]\]