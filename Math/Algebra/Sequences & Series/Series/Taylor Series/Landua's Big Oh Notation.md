---
tags:
  - atom
  - math
---
$$ f(x) = \mathcal{O}(x^n) \text{ as } x \to 0 $$
if there is some finite constant $K$ such that
$$ \left|f(x)\right| \le K\left| x^n \right|$$
for all $x$ sufficiently close to $0$.
# Rules
$\forall m,n,k,$
- $k \times \mathcal{O}(x^n) = \mathcal{O}(x^n) \text{ as } x \to 0$
- $m \le n \implies \mathcal{O}(x^m) + \mathcal{O}(x^n) = \mathcal{O}(x^m) \text{ as } x\to0$
- $x^m \times \mathcal{O}(x^n) = \mathcal{O}(x^{m+n}) \text{ as } x\to0$
- $\mathcal{O}(x^m) \times \mathcal{O}(x^n) = \mathcal{O}(x^{m+n}) \text{ as } x\to0$
- $\dfrac{1}{1+\mathcal{O}(x^n)} = 1 + \mathcal{O}(x^n) \text{ as } x\to0$
- $\displaystyle \lim_{x\to0} \mathcal{O}(x^n) = 0 \text{ as } x\to0$

# Formal Definition
Let $f$ be the [[Functions|functions]] to be estimated, and $g$ be the comparison [[Functions|function]].
For the ranges, let $f$ be [[The Real Numbers|real]] or [[Complex Numbers|complex]] valued, and let $g$ be [[The Real Numbers|real]] valued.
Let both [[Domain|domains]] be a [[Supersets|superset]] of some unbounded [[Subsets|subset]] of the positive [[The Real Numbers|real numbers]].
$$\begin{array}{c}
	f(x) = \mathcal{O}(g(x)) \text{ as } x \to \infty \\
	\Big\Updownarrow \\
	\exists M \in \R^+, x_0 \in \R : \forall x  \in [x_0,\infty), \left|f(x)\right| \le M \left| g(x) \right |
\end{array}$$
For any real $\alpha$,
$$\begin{array}{c}
	f(x) = \mathcal{O}(g(x)) \text{ as } x \to \alpha \\
	\Big\Updownarrow \\
	\exists M, \delta \in \R^+ : \forall x \in (\alpha - \delta,\alpha + \delta), \left|f(x)\right| \le M \left| g(x) \right |
\end{array}$$

> [!example]- $\alpha = 0$
> $$\begin{array}{c}
> 	f(x) = \mathcal{O}(g(x)) \text{ as } x \to 0 \\
> 	\Big\Updownarrow \\
> 	\exists M, \delta \in \R^+ : \forall x \in (-\delta,\delta), \left|f(x)\right| \le M \left| g(x) \right |
> \end{array}$$