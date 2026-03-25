---
tags:
  - atom
  - math
---
A *principal ideal domain* is an [[Integral Domains|integral domain]] where every [[Ideals|ideal]] is a [[Principal Ideals|principal ideal]]

> [!theorem]- $\F[x]$ is a *PID*, and for any non-zero [[Ideals|ideal]] $I \subseteq \F[x]$ and $g \in \F[x]$, then $I = \left< g \right>$ iff $g$ is a non-zero [[Polynomial Rings|polynomial]] of minimum [[Polynomials#Degree|degree]] in $I$.
> Let $I \subseteq \F[x]$ be an [[Ideals|ideal]], and $g \in I$ be a non-zero [[Polynomial Rings|polynomial]] of minimum [[Polynomials#Degree|degree]] in $I$. We will show $I = \left< g \right>$.
> 
> $\left< g \right> \subseteq I$ because $I$ has the [[Ideals|absorbing property]].
> 
> Let $f \in I$. By the [[Division Algorithm|division algorithm]], we write
> $$f = qg+r$$
> with $r = 0$ or $\deg r < \deg g$. Then $r = f - qg \in I$, as $f \in I$, and $qg \in \left< g \right> \subseteq I$.
> 
> By the minimality of $\deg g$ in $I$, we can't have $\deg r < \deg g$, so $r = 0$. Thus, $f = qg \in \left< g \right>,$ so $I \subseteq \left< g \right>$.
> 
> Together, these give $I = \left< g \right>$.

---

> [!example]- $\Z$ is a *PID*
> [[Ideals#^ideals-of-z-are-nz|Ideals of]] $\Z$ [[Ideals#^ideals-of-z-are-nz|are]] $\{ n\Z : n \in \Z \}$, which are by definition [[Principal Ideals|principal ideals]].

> [!example]- $\Z[x]$ is not a *PID*
> $$A = \{ f(x) \in \Z[x] : 2|f(0) \}$$
> is an [[Ideals|ideal]] but not a [[Principal Ideals|principal ideal]]. To prove this, let $a \in A$. We need to show that $\left< a \right> \ne A$.
> - If $\deg a > 0$, then $\forall b \in \left< a \right>, \deg b > 0$, so $\left< a \right>$ does not contain the constant [[Polynomial Rings|polynomial]], such as $f(x) = 2 \in A$.
> - If $\deg a = 0$, then $a$ is an even integer, so every coefficient of the [[Polynomial Rings|polynomial]] in $\left< a \right>$ is even. This does not contain $f(x) = x + 2 \in A$.