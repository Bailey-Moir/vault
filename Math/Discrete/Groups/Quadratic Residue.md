---
tags:
  - atom
  - math
  - discrete
---
An integer $a$ is a *quadratic residue* (*QR*) mod $p$ iff there is a solution to
$$x^2 = a \hspace{2em} \text{in } \Z_{p}^\times$$

# Quadratic Residue (p)
For $p \in \mathbb{P} > 2$,

> [!theorem]-  Let $g$ be a [[Group Generators|generator]] of $\Z_{p}^\times$. Then $a = g^k$ is a *QR* $\iff$ $2|k$[^1]
> $(\implies)$
> Let $a$ be a *QR*, meaning $a = b^2$ for some $b \in \Z_{p}^\times$.
> 
> Then for some $t \in \Z_{p-1} = \Z_{\left| G \right|}$, $b = g^t$, meaning
> $$a = b^2 = \left( g^t \right)^2 = g^{2t}.$$
> Thus, $2|k$
> 
> $(\impliedby)$
> Let $a = g^k$ with $2|k$, meaning $k = 2t$ for some $t$.
> 
> Then
> $$a = g^{2t} = \left( g^t \right)g^2,$$
> meaning $a$ is a *QR*.

> [!corollary] Half of the elements in $\Z_{p}^\times$ are *quadratic residues*.

> [!corollary]- $a \in \Z_{p}^\times$ is a *QR* $\iff$ $a^{\frac{p-1}{2}} = 1$
> Let $g$ be a [[Group Generators|generator]] of $\Z_{p}^\times$
> $\left( \implies \right)$
> If $a$ is a *QR*, then $a = g^{2t}$ for some $t$.
> $$a^{\frac{p-1}{2}} = \left( g^{2t} \right)^{\frac{p-1}{2}} = g^{t(p-1)} = \left( g^{p-1} \right)^t = 1^t = 1$$
> Note $g^{p-1} = 1$ because $\left| g \right| = \left| \Z_{p}^\times \right| = p-1$.
> 
> $(\impliedby)$
> If $a$ is **not** a *QR*, then $a = g^{2t+1}$ for some $t$.
> $$a^{\frac{p-1}{2}} = \left( g^{2t+1} \right)^{\frac{p-1}{2}} = g^{t(p-1)}\times g^{\frac{p-1}{2}} = 1 \times g^{\frac{p-1}{2}} = g^{\frac{p-1}{2}},$$
> and $g^{\frac{p-1}{2}} \ne 1$ as $\dfrac{p-1}{2} < \left| \Z_{p}^\times \right| = p-1$. Thus, $a^{\frac{p-1}{2}} \ne 1$
> 
> \[[[Proof by Contraposition]]\]

> [!theorem]- If $a \in \Z_{p}^\times$ is a *QR*, then it has exactly $2$ square roots.
> Suppose $\Z_{p}^\times = \left< g \right>$[^2], and $a$ is a *QR*.
> 
> Then $a = g^{2t}$, meaning $b = g^t$ is a square root of $a$.
> 
> Then, for any $k$, $g^{2k} = g^{2t} \iff 1 = g^{2t-k}$, so
> $$\begin{align}
> 	& 2(t-k) \equiv 0 \mod {(p-1)} && p-1 = \left| g \right|  \\
> 	\iff & 2t = 2k + m(p-1) && (1) \\
> 	\implies & t = k + m\left( \dfrac{p-1}{2} \right). \\
> \end{align}$$
> Since $m \in \Z$, $t$ takes only $2$ values in $\Z_{\left| g \right|} = \{ 0,\dots,p-2 \}$:
> $$\begin{align}
> 	t &= k \\
> 	t &= k + \dfrac{p-1}{2} \\
> \end{align}$$
> 
> \[$(1)$ [[Congruence]]\]
# Quadratic Residue (n)
The square roots of non-prime *quadratic residues* are given by the square roots of it's [[Chinese Remainder Theorem|CRT]] prime equations.
#TODO fix wording?

> [!theorem] If $n$ is a product of $k$ different odd primes, and $a$ is a *quadratic residue*, then it has exactly $2^k$ square roots.

[^1]: [[Divisibility]]
[^2]: [[Generated Subgroups]]
