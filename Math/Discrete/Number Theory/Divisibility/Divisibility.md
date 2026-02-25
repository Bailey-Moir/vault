---
tags:
  - atom
  - math
  - discrete
---
If $a$ is a *divisor*/factor of $b$ (or $b$ is a multiple of $a$), then it is said that $a|b$.
$$\begin{align*}
	\forall a,b \in \Z, ( a|b &\iff \exists n \in \Z : b = an ) \\
	&\iff \dfrac{b}{a} \in \Z
\end{align*}$$
# Properties of Divisibility
$\forall a,b,c \in \Z, a,b,c \ne 0,$[^1]

0. $a|a$ ([[Reflexive Property|reflexive property]])
1. $1|a \land a|0$[^2]
2. $a|b \land b|a \implies a =\pm b$ [^2][^3] (almost [[Antisymmetric Property|antisymmetric property]])
3. $a|b \land b | c \implies a | c$[^2][^3] ([[Transitive Property|transitive property]])
4. $a|b \implies \forall r \in \Z, a|br$[^1][^2][^3]
5. $a|b \land a|c \implies \forall r,s \in \Z, a|(br+ cs)$[^1][^2][^3]
6. $a|(b+c) \land a|b \implies a|c$[^2][^3]

\[[[Divisibility]]\]

[^1]: [[Universal Quantifier]]
[^2]: [[Conjunction]]
[^3]: [[Logical Implication]]