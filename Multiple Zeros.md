---
tags:
  - atom
  - math
---
A [[Polynomial Rings|polynomial]] $f(x)$ over a [[Fields|field]] $F$ has a *multiple zero* in some [[Subfields#^extension-field|extension field]] $E$ of $F$ iff $f(x)$ and $f'(x)$ have a common factor of positive [[Polynomials#Degree|degree]] in $F[x]$.

[!proof]-
#TODO

[!corollary]- If $f(x)$ is [[Reduciblity#^negation|irreducible]] over a [[Fields|field]] $F$ of [[Ring Characteristic|characteristic]] $0$, then $f(x)$ has no *multiple zero*
#TODO


Suppose $f(x)$ has a *multiple zero*, meaning
$$f(x) = (x - \alpha)^kg(x)$$
for some $\alpha \in F$, $k > 2$, and $g(x) \in F[x]$. Then
$$\begin{align}
	f'(x) &= k(x-\alpha)^{k-1}g(x) + (x-\alpha)g'(x) \\
	f'(\alpha) &= 0 + 0 = 0. \\
\end{align}$$
Then $\left( x-a \right) | f(x)$ by [[Division Algorithm#^remainder-theorem|remainder theorem]]. Thus, $f$ is [[Reduciblity#^negation|irreducible]].

Wait whatttt isn't this obvious. If it's irreducible it has no roots, obviously. Like what???????