---
tags:
  - atom
  - math
---
Let $p \in \P$[^1], and $f \in \Z[x]$[^2] with $\deg f \ge 1$. Let $\bar{f} \in \Z_{p}[x]$ be obtained by reducing all coefficients of $f$ [[Modular Arithmetic|modulo]] $p$.
If $\bar{f}(x)$ is [[Reducible Factors#^negation|irreducible]] over $\Z_{p}$, and $\deg \bar{f} = \deg f$, then $f$ is [[Reducible Factors#^negation|irreducible]] over $\Q$.

> [!proof]- [[Proof by Contraposition|by Contraposition]]
> If $f \in \Z[x]$ factors as
> $$f(x) = g(x)h(x)$$
> for some [[Rings#^unit|units]] $g,h \in \Z[x]$, since $\tilde\sigma_{p}$ is a [[Ring Homomorphisms|homomorphism]],
> $$\bar{f}(x) = \bar{g}(x)\bar{h}(x).$$
> As long as $\bar{g}$ and $\bar{h}$ have [[Polynomials#Degree|degree]] larger than $0$, this shows $\bar{f}$ is [[Reducible Factors|reducible]] in $\Z_{p}[x]$ by [[Reducible Factors#^field-units-are-constant|this lemma]].
> 
> If $\deg f = \deg \bar{f}$, then
> $$\begin{align}
> 	\deg g &= \deg \bar{g} \\
> 	\deg h &= \deg \bar{h}. \\
> \end{align}$$
> So any non-trivial factorisation of $f$ yields a non-trivial factorisation of $\bar{f}$.

[^1]: [[Primes]]
[^2]: [[Polynomial Rings]]