---
tags:
  - atom
  - math
  - discrete
---
$$\begin{align*}
	\forall n \in \mathbb{Z^+}, a,b, \in \Z, (a \equiv b \pmod{n} \iff \hspace{.2em}&n | a - b ) \\
	\hspace{.2em}& \exists q \in \Z : a = qn + b
\end{align*}$$
This means that $a$ and $b$ are *congruent modulo $\mathit{n}$*. 
\[[[Divisibility]]\]
# Properties of Congruence
$\forall n \in \Z^+, a,b,c \in \Z, a_1, a_2, b_1, b_2 \in \Z$,
- **[[Reflexive Property|Reflexive Property]]**
	$a \equiv a \pmod n$
- **[[Symmetric Property]]**
	$a \equiv b \pmod n \iff b \equiv a \pmod n$
- **[[Transitive Property]]**
	$a \equiv b \pmod n \land b \equiv c \pmod n \implies a \equiv c \pmod n$

$a \equiv b \pmod n \implies$
- $c + a \equiv c + b \pmod n$
- $ac \equiv bc \pmod n$
- $\forall k \in \Z, a^k \equiv b^k \pmod n$