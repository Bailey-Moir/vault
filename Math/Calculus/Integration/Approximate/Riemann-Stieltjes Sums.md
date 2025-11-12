---
tags:
  - atom
  - math
---
The *Riemann-Stieltjes sum* (*R-S*) of a [[The Real Numbers|real]] [[Functions|function]] $f$ with respect to another [[The Real Numbers|real]]-to-[[The Real Numbers|real]] [[Functions|function]] $g$ over a [[Interval Partitions|partition]] $P=( x_{0},\dots,x_{n} )$ of $\left[ a,b \right]$ is a [[The Real Numbers|real number]] $S(P;f,g)$ of the form
$$S(P;f,g) = \sum_{k=1}^n f(\xi_{k})\left( g(x_{k}) - g(x_{k-1}) \right)$$
where $x_{k-1} \le \xi_{k} \le x_{k}$ for $1 \leq k \leq n$.

> [!note] A [[Riemann Sums|Riemann sum]] is a *Riemann-Stieltjes sum* with $g(x) = x$.

# Upper and Lower Riemann-Stieltjes Sums
Let $f$ be a [[The Real Numbers|real]] [[Bounded Sets|bounded]] [[Functions|function]], and $P$ be a [[Interval Partitions|partition]] of $[a,b]$. Define
$$\begin{array}{c}
	\displaystyle M_{k}(f) = \hspace{-0.8em}\sup_{x \in \left[ x_{k-1},x_{k} \right] }\hspace{-0.8em} f(x) & 
	\displaystyle m_{k}(f) = \hspace{-0.8em}\inf_{x \in \left[ x_{k-1},x_{k} \right] }\hspace{-0.8em} f(x). \\
\end{array}$$
> **Upper *R-S Sum***
> $\displaystyle \overline{S}(P;f,g) = \sum_{k=1}^nM_{k}(f)(g(x_{k}) - g(x_{k-1}))$

> **Lower *R-S Sum***
> $\displaystyle \underline{S}(P;f,g) = \sum_{k=1}^nm_{k}(f)(g(x_{k}) - g(x_{k-1}))$
