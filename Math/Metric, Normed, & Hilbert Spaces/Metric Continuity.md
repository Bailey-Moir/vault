---
tags:
  - atom
  - math
---
$$f \in \mathcal{C}(I) \iff \forall a \in I,\forall \varepsilon>0, \exists \delta>0: \forall x \in \R, d(x,a) < \delta \to d(f(x), f(a)) < \varepsilon$$

> [!theorem]- In $\R$,$$f \in \mathcal{C}(I) \iff \forall a \in I,\, \lim_{x\to a} f(x) = f(a).$$This implicitly requires $f(a)$ and $\displaystyle\lim_{x\to a} f(x)$ to exist.

> [!note] If $I = \{ a \}$ for some $a \in M$, this implicitly requires $f$ to be [[Defined Near|defined near]] $a$ and at $a$.

> [!definition] $\varepsilon$-$\delta$
> $$\forall a \in \R,\forall \varepsilon>0, \exists \delta>0: \forall a,x \in \R,  \left|x-a\right| < \delta \to  \left|f(x) - f(a)\right| < \varepsilon$$

> [!theorem]- *(Continuity by Sequences)* $f(x) : I \to M$ is *continuous* at $x_{0} \in I$ iff for any [[Sequences|sequence]] $\left( x_{n} \right)$ in $I$ that [[Metric Sequence Convergence|converges]] to $x_{0}$, the [[Sequences|sequence]] $\left( f(x_{n}) \right)$ [[Metric Sequence Convergence|converges]] to $f(x_{0})$

$\left( \implies \right)$
Suppose $f$ is *continuous* at $x_{0}$, and let $\left( x_{n} \right)$ be any [[Sequences|sequence]] in $I$ such that $\lim x_{n} = x_{0}$.

Let $\varepsilon>0$ be given. Then there exists $\delta$ such that
$$\left| x_{n} - x_{0} \right| < \delta \to \left| f(x_{n}) - f(x_{0}) \right| < \varepsilon.$$
Similarly, there exists an $N \in \N$ such that for all $n \ge N$,
$$\left| x_{n} - x_{0} \right| < \delta.$$
Thus, for all $\varepsilon > 0$, there exists $N \in \N$ such that $\left| f(x_{n}) - f(x_{0}) \right| < \varepsilon$. Thus, $\left( f(x_{n}) \right)$ [[Metric Sequence Convergence|converges]] to $f(x_{0})$.

$\left( \impliedby \right)$
Suppose in $I$, for any [[Sequences|sequence]] $\left( x_{n} \right)$ that [[Metric Sequence Convergence|converges]] to $x_{0}$, $f(x_{n}) \to f(x_{0})$ as $n \to \infty$, but $f(x)$ is not *continuous* at $x_{0}$.

Then there exists $\varepsilon_{0} > 0$ such that for $\delta = \dfrac{1}{n}$, $n \in \N$,
$\exists x_{n} \in I$ and $\left| x_{n} - x_{0} \right| < \delta_{n}$ such that
$\left| f(x_{n}) - f(x_{0}) \right| \ge \varepsilon_{0}$

$\left( x_{n} \right)$ forms a [[Sequences|sequence]] that [[Metric Sequence Convergence|converges]] to $x_{0}$ because
For all $\varepsilon>0$ by the [[The Real Numbers#^archimedean-property|Archimedean property]], there exists $N' \in \N$ such that $N' > \dfrac{1}{\varepsilon}$.
Therefore, for all $n \ge N'$, $\left| x_{n} - x_{0} \right| < \delta_{n} = \dfrac{1}{n} \le \dfrac{1}{N'} < \varepsilon$.
Since $\lim_{ n \to \infty } f(x_{n}) = f(x_{0})$, this means there exists $N'' \in \N$ such that for all $n \ge N''$,
$$\left| f(x_{n}) - f(x_{0}) \right| < \varepsilon_{0},$$
leading to [[Contradictions|contradiction]].

#TODO fix this up

#TODO also prove this is equivalent to topological definition (same for convergence)

^sequences