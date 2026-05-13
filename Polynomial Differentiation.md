---
tags:
  - atom
  - math
---
For $f(x) \in \F[x]$, *differentiation* $f'(x)$ is defined by
$$f(x) = a_{n}x^n + \dots + a_{1}x + a_{0} \mapsto f'(x) = na_{n}x^n + \dots + a_{1}.$$
\[[[Power Rule]]\]

## Properties
> [!note]- [[Linear Maps|Linearity]]
> Let $f(x) = \sum_{i = 0}^n a_{i}x^i$ and $g(x) = \sum_{j = 0}^n b_{i}x^i$. If either has a [[Polynomials#Degree|degree]] less than $n$, let higher coefficients be $0$. The [[Additive Property|additive property]] is given by
> $$\begin{align}
> 	\left( f(x) + g(x) \right)'
> 	&= \left( \sum_{i = 0}^{n} (a_{i} + b_{i})x^i \right)' \\
> 	&= \sum_{i = 1}^{n} i(a_{i} + b_{i})x^{i-1} \\
> 	&= \sum_{i = 1}^{n} ia_{i}x^{i-1} + \sum_{i=1}^n ib_{i}x^{i-1} \\
> 	&= f'(x) + g'(x). \\
> \end{align}$$
> Let $c \in F$. The homogenity is given by
> $$\begin{align}
> 	\left( cf(x) \right)'
> 	&= \left( \sum_{i = 0}^{n} ca_{i}x^i \right)' \\
> 	&= \sum_{i = 1}^{n} ica_{i}x^{i-1} \\
> 	&= c\sum_{i = 1}^{n} ia_{i}x^{i-1} \\
> 	&= cf'(x). \\
> \end{align}$$

> [!note]- **Chain Rule**

Let $f(x) = \sum_{i = 0}^n a_{i}x^i$ and $g(x) = \sum_{j = 0}^n b_{i}x^i$. If either has a [[Polynomials#Degree|degree]] less than $n$, let higher coefficients be $0$.
$$\begin{align}
	\left( f(g(x)) \right)'
	&= \left( \sum_{i=0}^na_{i}\left[ \sum_{i=0}^n b_{i}x^i \right]^i  \right)' \\
	&= \quad ????? \\
	&= \left[ \sum_{i=1}^n ia_{i}\left[ \sum_{i=0}^n b_{i}x^i \right]^{i-1} \right]\left[ \sum_{i=1}^n ib_{i}x^{i-1} \right]    \\
\end{align}$$
> [!note]- **Product Rule**

#TODO
Let $f(x) = \sum_{i = 0}^n a_{i}x^i$ and $g(x) = \sum_{j = 0}^n b_{i}x^i$. If either has a [[Polynomials#Degree|degree]] less than $n$, let higher coefficients be $0$.
$$\begin{align}
	\left( f(x) \times g(x) \right)'
	&= \left( \sum_{i=0}^{n} a_{i}x^i \times \sum_{i=0}^n b_{i}x^i  \right)' \\
	&= \left( \sum_{i=0}^{n} \sum_{j=0}^n a_{i}b_{j}x^{i+j}  \right)' \\
\end{align}$$
