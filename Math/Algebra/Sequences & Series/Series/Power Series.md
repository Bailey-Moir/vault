---
tags:
  - atom
  - math
---
A *power series* about $a$ is a [[Series|series]] of the form
$$ \sum_{n=0}^\infty c_n\left( x-\alpha \right)^n = c_0 + c_1\left( x-\alpha \right) + c_2\left( x-\alpha \right)^2 + \cdots $$
The sum of a *power series* is a [[Functions|function]] with a [[Domain|domain]] of the [[Interval of Convergence|interval of convergence]].

> [!note]- When $\alpha=0$ and $\exists k : \forall n, c_n = k$, this is a [[Geometric Series|geometric series]] with a ratio of $x$.

> [!note]- Term-by-Term Integration and Differentiation
> For any *power series*,
> - $\displaystyle \dfrac{d}{dx}\left[ \sum _{n=0}^\infty c_{n}(x-\alpha)^n \right] = \sum _{n=0}^\infty \dfrac{d}{dx}\left[ c_{n}(x-\alpha)^n \right]$
> - $\displaystyle \int \left[ \sum _{n=0}^\infty c_{n}(x-\alpha)^n \right] \, dx = \sum _{n=0}^\infty \int \left[ c_{n}(x-\alpha)^n \right] \, dx$