---
tags:
  - atom
  - math
---
Heaviside's $\it{D}$ *operator* can be defined as
$$\begin{array}{ccc}
	D^0 := I, & D^n := \dfrac{d^n}{dt^n} & k \in \N,
\end{array}$$
where $I$ is the identity.
1. $D(f(t)+g(t)) = Df(t) + Dg(t)$ ([[Additive Property]])
2. $Dcf(t) = cDf(t)$ (Commutativity with Scalar Multiplication)
3. $D^aD^b f(t) = D^{a+b}f(t)$

> [!note] Properties 1 and 2 imply [[Linearity|linearity]].

> [!proof]- Translation operator $e^{hD}f(t) = f(t+h)$
> $$\begin{align*}
> 	f(x) &= \sum_{n=0}^\infty \dfrac{f^{(n)}(\alpha)}{n!} (x-\alpha)^n \\
> 	f(x) &= \sum_{n=0}^\infty \dfrac{D^nf(t)}{n!} (x-t)^n && \alpha \to t \\
> 	f(t+h) &= \sum_{n=0}^\infty \dfrac{D^nf(t)}{n!} (h)^n && x \to t + h\\
> 	&= \sum_{n=0}^\infty \dfrac{(hD)^n}{n!} f(t) \\
> 	&= e^{hD} f(t) \\
> \end{align*}$$