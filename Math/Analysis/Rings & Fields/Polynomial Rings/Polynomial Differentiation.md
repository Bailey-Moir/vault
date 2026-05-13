---
tags:
  - atom
  - math
---
For $f(x) \in \F[x]$, *differentiation* $f'(x)$ is defined by
$$\begin{align}
	f(x) = a_{n}x^n + \dots + a_{1}x + a_{0} &\mapsto f'(x) = na_{n}x^{n-1} + \dots + a_{1} \\
	f(x) = \sum_{k=0}^n a_{k}x^k &\mapsto f'(x) = \sum_{k=1}^nka_{k}x^k.
\end{align}$$
\[[[Power Rule]]\]

## Properties
> [!note]- [[Linear Maps|Linearity]]
> Let $f(x) = \sum_{k = 0}^n a_{k}x^k$ and $g(x) = \sum_{j = 0}^n b_{k}x^k$. If either has a [[Polynomials#Degree|degree]] less than $n$, let higher coefficients be $0$. The [[Additive Property|additive property]] is given by
> $$\begin{align}
> 	\left( f(x) + g(x) \right)'
> 	&= \left( \sum_{k = 0}^{n} (a_{k} + b_{k})x^k \right)' \\
> 	&= \sum_{k = 1}^{n} k(a_{k} + b_{k})x^{k-1} \\
> 	&= \sum_{k = 1}^{n} ka_{k}x^{k-1} + \sum_{k=1}^n kb_{k}x^{k-1} \\
> 	&= f'(x) + g'(x). \\
> \end{align}$$
> Let $c \in F$. The homogenity is given by
> $$\begin{align}
> 	\left( cf(x) \right)'
> 	&= \left( \sum_{k = 0}^{n} ca_{k}x^k \right)' \\
> 	&= \sum_{k = 1}^{n} kca_{k}x^{k-1} \\
> 	&= c\sum_{k = 1}^{n} ka_{k}x^{k-1} \\
> 	&= cf'(x). \\
> \end{align}$$

> [!note]- **Chain Rule**
> Let $f(x) = \sum_{k = 0}^n a_{k}x^k$ and $g(x) = \sum_{j = 0}^n b_{k}x^k$. If either has a [[Polynomials#Degree|degree]] less than $n$, let higher coefficients be $0$.
> $$\begin{align}
> 	\left( f(g(x)) \right)'
> 	&= \left( \sum_{k=0}^na_{k}\left[ \sum_{k=0}^n b_{k}x^k \right]^i  \right)' \\
> 	&= \quad ????? \\
> 	&= \left[ \sum_{k=1}^n ka_{k}\left[ \sum_{k=0}^n b_{k}x^k \right]^{k-1} \right]\left[ \sum_{k=1}^n kb_{k}x^{k-1} \right]    \\
> \end{align}$$
> [!note]- **Product Rule**

> [!note]- **Product Rule**
> #TODO
> Let $f(x) = \sum_{k = 0}^n a_{k}x^k$ and $g(x) = \sum_{j = 0}^n b_{k}x^k$. If either has a [[Polynomials#Degree|degree]] less than $n$, let higher coefficients be $0$.
> $$\begin{align}
> 	\left( f(x) \times g(x) \right)'
> 	&= \left( \sum_{k=0}^{n} a_{k}x^k \times \sum_{k=0}^n b_{k}x^k  \right)' \\
> 	&= \left( \sum_{j=0}^{n} \sum_{k=0}^n a_{j}b_{k}x^{j+k}  \right)' \\
> \end{align}$$