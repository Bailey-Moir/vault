---
tags:
  - atom
  - math
  - discrete
---
The *Pohlig-Hellman algorithm* is an [[Algorithms|algorithm]] for the [[Discrete Logarithm Problem|discrete logarithm problem]] using the [[Chinese Remainder Theorem|Chinese remainder theorem]].
1. Factor $\left| G \right| = n$ as
$$n = q_{1}\cdots q_{k} = p_{1}^{e_{1}}\cdots p_{k}^{e_{k}}$$
2. For each $i = 1,\dots,k$, let $g_{i} = g^{\frac{n}{q_{i}}}$ and $h_{i} = h^{\frac{n}{q_{i}}}$; then $\left| g_{i} \right| = q_{i}$.
3. For each $i$, solve $x_{i} = \log_{g_{i}}(h_{i}$).
4. Let $x$ be a solution to the system
$$\begin{array}{c}
	x \equiv x_{1} \mod q_{1} \\
	\vdots \\
	x \equiv x_{k} \mod q_{k}
\end{array}$$
5. Solving for $x$ using [[Chinese Remainder Theorem|CRT]] gives $\log_{g}(h)$.

> [!intuition]-
> The exponent $x$ in $g^x = h$ is a solution to some [[Congruence|congruence]] modulo $n = \left| G \right|$. We factor $n$ and solve the corresponding [[Congruence|congruences]] modulo its [[Primes|prime]] power factors, then [[Chinese Remainder Theorem|CRT]] allows us to stitch these together to obtain a solution to the original problem.

> [!example]- Compute $\log_{2}(5)$ in $\Z_{13}^\times$
> $$n = \left| \Z_{13}^\times \right| = 12 = 2^2 \times 3, $$
> with $g = 2$ as the [[Group Generators|generator]], $\left< 2 \right> = \Z_{13}^\times$.
> 
> 1. **Compute $\mathbf{g_{i} = g^{\frac{n}{q_{i}}}}$ and $\mathbf{h_{i} = h^{\frac{n}{q_{i}}}}$**
> $$\begin{array}{ll}
> 	g_{1} = 2^{\frac{12}{4}} = 2^3 = 8,& h_{1} = 5^3 = 8 \\
> 	g_{2} = 2^{\frac{12}{3}} = 2^4 = 3,& h_{1} = 5^4 = 1
> \end{array}$$
> Note that
> $$h_{i} = h^{\frac{n}{q_{i}}} = g^{x \frac{n}{q_{i}}} = g_{i}^x$$
> Thus $h_{i} \in \left< g_{i} \right>$, and
> $$x \equiv \log_{g_{i}}(h_{i}) \mod q_{i}$$
> where $q_{i} = \left| \left< g_{i} \right> \right|$
> 
> 2. **Find $\mathbf{\log_{g_{i}}(h_{i})}$ in $\mathbf{\left< g_{i} \right>}$ which has order $\mathbf{q_{i}}$**
> $$\begin{align}
> 	\log_{g_{1}}(h_{1}) &= \log_{8}(8) = 1 \\
> 	\log_{g_{2}}(h_{2}) &= \log_{3}(1) = 0
> \end{align}$$
> 
> 3. **Solve the system $\mathbf{x \equiv \log_{g_{i}}(h_{i}) \mod q_{i}}$ using [[Chinese Remainder Theorem|CRT]]**
> $$\begin{align}
> 	x &\equiv 1 \mod 4 \\
> 	x &\equiv 0 \mod 3,
> \end{align}$$
> giving
> $$x \equiv 9 \mod 12,$$
> meaning
> $$\log_{2}(5) = 9$$

