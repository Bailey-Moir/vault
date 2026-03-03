---
tags:
  - atom
  - math
---
$$f \in \mathcal{C}(I) \iff \forall a \in I,\forall \varepsilon>0, \exists \delta>0: \forall x \in \R, d(x,a) < \delta \to d(f(x), f(a)) < \varepsilon$$

> [!theorem]- In $\R$,$$f \in \mathcal{C}(I) \iff \forall a \in I,\, \lim_{x\to a} f(x) = f(a).$$This implicitly requires $f(a)$ and $\displaystyle\lim_{x\to a} f(x)$ to exist.

> [!note] If $I = \{ a \}$ for some $a \in M$, this implicitly requires $f$ to be [[Defined Near|defined near]] $a$ and at $a$.

> [!theorem]- *(Continuity by Sequences)* $f(x) : I \to M$ is *continuous* at $x_{0} \in I$ iff for any [[Sequences|sequence]] $\left( x_{n} \right)$ in $I$ that [[Metric Sequence Convergence|converges]] to $x_{0}$, the [[Sequences|sequence]] $\left( f(x_{n}) \right)$ [[Metric Sequence Convergence|converges]] to $f(x_{0})$
> $\left( \implies \right)$
> Suppose $f$ is *continuous* at $x_{0}$, and let $\left( x_{n} \right)$ be any [[Sequences|sequence]] in $I$ such that $\lim x_{n} = x_{0}$.
> 
> Let $\varepsilon>0$ be given. Then there exists $\delta$ such that
> $$d(x_{n}, x_{0}) < \delta \to d(f(x_{n}), f(x_{0})) < \varepsilon.$$
> Similarly, there exists an $N \in \N$ such that for all $n \ge N$,
> $$d(x_{n}, x_{0}) < \delta.$$
> Thus, for all $\varepsilon > 0$, there exists $N \in \N$ such that $d(f(x_{n}), f(x_{0})) < \varepsilon$. Thus, $\left( f(x_{n}) \right)$ [[Metric Sequence Convergence|converges]] to $f(x_{0})$.
> 
> $\left( \impliedby \right)$
> Suppose $\left( x_{n} \right)$ in $I$ [[Metric Sequence Convergence|converges]] to $x_{0} \in I$, and $\lim_{ n \to \infty } f(x_{n}) = f(x_{0})$, but $f(x)$ is not *continuous* at $x_{0}$.
> 
> Then there exists $\varepsilon_{0} > 0$ such that for any $\delta_{n} = \dfrac{1}{n}$ where $n \in \N$, there exists $x_{n} \in I$ such that $d(x_{n}, x_{0}) < \delta_{n}$ and $d(f(x_{n}), f(x_{0})) \ge \varepsilon_{0}$.
> 
> This definition of $\left( x_{n} \right)$ does indeed form a [[Sequences|sequence]] that [[Metric Sequence Convergence|converges]] to $x_{0}$, because for all $\varepsilon>0$, by the [[The Real Numbers#^archimedean-property|Archimedean property]], there exists $N_{\varepsilon} \in \N$ such that $N_{\varepsilon} > \dfrac{1}{\varepsilon}$, and thus for all $n \ge N_{\varepsilon}$,
> $$d(x_{n}, x_{0}) < \delta_{n} = \dfrac{1}{n} \le \dfrac{1}{N_{\varepsilon}} < \varepsilon.$$
> Since $\lim_{ n \to \infty } f(x_{n}) = f(x_{0})$, this means there exists $N' \in \N$ such that for all $n \ge N'$,
> $$d(f(x_{n}), f(x_{0})) < \varepsilon_{0},$$
> leading to [[Contradictions|contradiction]].
^sequences

#TODO also prove this is equivalent to topological definition (same for convergence)
