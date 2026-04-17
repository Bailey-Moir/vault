---
tags:
  - atom
  - math
---
A [[Functions|map]] $T$ from a [[Metric Spaces|metric space]] $\left( X,d \right)$ to itself is called a *contraction mapping* on $X$ with **contraction constant** $c \in \left[ 0,1 \right)$ iff
$$\forall x,y \in X, \quad d(T(x),T(y)) \le cd(x,y).$$
> [!example]- $T(x) = 1 + \dfrac{1}{2}\sin(x)$ is a *CM* on $\R$ with **contraction constant** $\dfrac{1}{2}$.
> Let $x,y \in \R$ be given.
> $$\begin{align}
> 	\left| T(x) - T(y) \right| &= \left| 1 + \dfrac{1}{2}\sin(x) - 1 - \dfrac{1}{2}\sin(y) \right| \\
> 	&= \dfrac{1}{2}\left| \sin(x) - \sin(y) \right| \\
> 	&\le \dfrac{1}{2}\left| 2\cos \left( \dfrac{x+y}{2} \right)\sin \left( \dfrac{x-y}{2} \right) \right| && (1) \\
> 	&\le \left| \sin \left( \dfrac{x-y}{2} \right) \right| \\
> 	&\le \dfrac{1}{2}\left| x - y \right|, \\
> \end{align} $$
> as $\forall \theta \in \R, \left| \sin \theta \right| \le \left| \theta \right|$.
> 
> \[$\left( 1 \right)$ [[Sum to Product Identities]]\]


> [!theorem]- Suppose $T$ is a *contraction map*  with **contraction constant** $c$ on a [[Completeness|complete]] [[Metric Spaces|metric space]] $\left( X,d \right)$.$$\exists ! x^* \in X : \quad T(x^*) = x^*.$$This is called a **fixed point** of $T$. Further,$$\forall x \in X, n \in \N, \quad d(x^*, T^n\,x) \le \dfrac{c^n}{1-c}d(x,T\,x)$$
> Let $x \in X$. Consider the [[Sequences|sequence]] $\left( T^n \, x \right)_{n=0}^\infty$. For all $n \in \Z^{+}$,
> $$\begin{align}
> 	d(T^n\,x, T^{n-1}\,x) &\le cp(T^{n-1}\,x, T^{n-2} x) \\
> 	&\le \cdots \\
> 	&\le c^{n-1}p(T\,x, T x) \\
> \end{align}$$
> Without loss of generality, assume $0 \le n < m$. Then
> $$\begin{align}
> 	d(T^m\,x, T^n\,x) &\le d(T^m\,x, T^{m-1}\,x) + \dots + d(T^{n+1}\,x, T^{n} \,x) \\
> 	&= c^{m-1}d(T\,x, x) + \dots + c^{n}d(T\,x, x) \\
> 	&= (c^{m-1} + c^{m-2} + \dots + c^n)d(T\,x, x) \\
> 	&= \dfrac{c^n(1 - c^{m-n})}{1-c}d(T\,x, x) && (1) \\
> 	&= \dfrac{c^n - c^{m}}{1-c}d(T\,x, x) \\
> 	&\le \dfrac{c^n}{1-c}d(T\,x, x) \to 0 \text{ as } n \to \infty && 1 \\
> \end{align}$$
> Thus, $\left( T^n\,x \right)$ is [[Cauchy Sequences|Cauchy]], so by the [[Completeness|completeness]] of $X$, $\left( T^n x \right)$ is [[Metric Convergence|convergent]] to some $x^*$.
> #TODO do this a better way (by contradiction) cause this is shit 
> $$d(T\,x^*, x^*) \le d(T\,x^*, T^{n+1}\,x) + d(T^{n+1}\,x, T^{n}\,x) + d(T^{n}\,x,x^*)$$
> This first term is less than $\frac{\varepsilon}{3}$ by the [[Metric Continuity 1|continuity]] of $T$, the second term is less than $\frac{\varepsilon}{3}$ since $\left( T^n\,x \right)$ is [[Cauchy Sequences|Cauchy]], and the third term is less than $\frac{\varepsilon}{3}$ by the [[Metric Convergence|convergence]] of $\left( T^n \, x \right)$. Thus,
> $$\forall \varepsilon > 0, d(T\,x^*, x^*) < \varepsilon \to d(T\,x^*, x^*) = 0 \to T\,x^* = x^*.$$
> 
> Let $x^*,y^* \in X$ such that $T\,x^* = x^*$ and $T\,y^* = y^*$. Then
> $$d(T\,x^*, T^*\,y) = d(x^*, y^*),$$
> violating the *contraction mapping* assumption that $c < 1$ if neither are zero. Thus, both are zero, giving $x^* = y^*$.
> 
> If you let $m \to \infty$ in $1$, this gives the final [[Inequalities|inequality]].





\[$\left( 1 \right)$ [[Geometric Series#Partial Sum Formula]]\]

^fixed-point-theorem