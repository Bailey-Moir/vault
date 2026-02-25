---
tags:
  - atom
  - math
---
The *polynomial [[Rings|ring]]* $R[x]$ over a [[Rings|rings]] $R$ is defined as
$$R[x] := \left\{ \sum_{i= 0}^n a_{i}x^i : n \in \N, a_{0},\dots,a_{n} \in R \right\},$$
where $n$ gives the [[Polynomials#Degree|degree]] of the given [[Polynomials|polynomial]], and $+$ and $\times$ are given by
$$\begin{align}
	\sum_{i = 0}^n a_{i}x^i + \sum_{i = 0}^m b_{i}x^i &= \sum_{i = 0}^n \left( a_{i} + b_{i} \right)x^i \\
	\sum_{i = 0}^n a_{i}x^i \times \sum_{i = 0}^m b_{i}x^i &= \sum_{i = 0}^n \sum_{j=0}^m a_{i}b_{j}x^{i+j}. \\
\end{align}$$

> [!definition] A **monic polynomial** is a [[Polynomials|polynomial]] with a leading coefficient ($a_{n}$) of $1$.
^monic

> [!theorem]- If $D$ is an [[Integral Domains|integral domain]], then $D[x]$ is an [[Integral Domains|integral domain]].
> Let $D$ be an [[Integral Domains|integral domain]]. We need to show that $D[x]$
> - is [[Groups#^abelian-groups|commutative]], 
> - has a [[Rings#^unity|unity]], 
> - and has no [[Zero-divisors|zero-divisors]].
> 
> $$\begin{align}
> 	\sum_{i = 0}^n a_{i}x^i \times \sum_{i = 0}^m b_{i}x^i &= \sum_{i = 0}^n \sum_{j=0}^m a_{i}b_{j}x^{i+j} \\
> 	&= \sum_{i = 0}^m \sum_{j=0}^n b_{j}a_{i}x^{j+i} && (1) \\
> 	&= \sum_{i = 0}^m b_{i}x^j \times \sum_{i = 0}^n a_{i}x^i.
> \end{align}$$
> where $(1)$ is by the [[Groups#^abelian-groups|commutativity]] of $\left( R,\times \right)$ and $\left( \N, + \right)$, and the [[Groups#^associtativity|associativity]] of $\left( R[x], + \right)$. Thus, $R[x]$ is [[Groups#^abelian-groups|commutative]].
> 
> $$\begin{align}
> 	\left( \sum_{i = 0}^n a_{i}x^i \right) \times 1 &= \sum_{i = 0}^n a_{i}x^i \times \sum_{i = 0}^0 1x^i \\
> 	&= \sum_{i = 0}^n \sum_{j=0}^0 a_{i}1x^{i+j} \\ 
> 	&= \sum_{i = 0}^n a_{i}x^{i}.
> \end{align}$$
> Thus, $1 \in D$ is also the [[Rings#^unity|unity]] in $R[x]$.
> 
> $$\begin{align}
> 	0 &= \sum_{i = 0}^n a_{i}x^i \times \sum_{i = 0}^m b_{i}x^i \\
> 	&= \sum_{i = 0}^n \sum_{j=0}^m a_{i}b_{j}x^{i+j} \\
> 	\to  \quad  a_{i}b_{j} &= 0 && \forall i \in \N_{\le n}, \forall j \in \N_{\le m} \\
> \end{align}$$
> Thus, if $\exists i \in \N_{\le n} : a_{i} \ne 0$, then $i \in \N_{\le n}$, then $\forall j \in \N_{\le m}, b_{j} = 0$ - by the lack of [[Zero-divisors|zero-divisors]] - which gives that $\sum_{i = 0}^m b_{i}x^i = 0$. By the [[Groups#^abelian-groups|commutativity]] of $D[x]$, this works in the other direction as well (as these are arbitrary [[Polynomials|polynomials]]).
> 
> Thus, if two [[Polynomials|polynomials]] multiply to $0$, at least one of them must be $0$, meaning there are no [[Zero-divisors|zero-divisors]].
> 
> 
> 