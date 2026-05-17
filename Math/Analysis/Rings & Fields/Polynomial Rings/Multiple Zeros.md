---
tags:
  - atom
  - math
---
A [[Polynomial Rings|polynomial]] $f(x)$ over a [[Fields|field]] $F$ has a *multiple zero* in some [[Subfields#^extension-field|extension field]] $E$ of $F$ iff $f(x)$ and $f'(x)$ have a common factor of positive [[Polynomials#Degree|degree]] in $F[x]$.

> [!proof]-
> $\left( \implies \right)$
> Suppose $\alpha \in E$ is a *multiple zero* of $f(x) \in F[x]$, i.e.
> $$f(x) = (x-\alpha)^kg(x)$$
> for some $k > 1$ and $g(x) \in E[x]$. [[Polynomial Differentiation|Differentiating]] gives
> $$\begin{align}
> 	f'(x) &= k(x-\alpha)^{k-1}g(x) + (x-\alpha)^kg'(x) \\
> 	f'(\alpha) &= 0 + 0 = 0. \\
> \end{align}$$
> By [[Division Algorithm#^remainder-theorem|remainder theorem]], $\left( x-\alpha \right) | f'(x)$.
> 
> Suppose $f(x),f'(x) \in F[x]$ were co-prime. Then by [[Bēzout's Identity|Bēzout's identity]], there exists $a(x),b(x) \in F[x]$ such that
> $$a(x)f(x)  + b(x)f'(x) = 1.$$
> By this [[Bēzout's Identity|same identity]], this would imply $f(x),f'(x) \in E[x]$ are coprime, a [[Contradictions|contradiction]].
> 
> Thus, $f(x)$ and $f'(x)$ have a common factor of positive [[Polynomials#Degree|degree]].
> 
> $\left( \impliedby \right)$
> Suppose $f(x),f'(x) \in F[x]$ have a common factor of positive [[Polynomials#Degree|degree]] $k > 0$. Thus,
> $$\begin{align}
> 	f(x) &= (x-\alpha)^kg(x) \\
> 	f'(x) &= (x-\alpha)^kh(x) \\
> \end{align}$$
> for some $g(x),h(x) \in F[x]$. [[Polynomial Differentiation|Differentiating]] $f(x)$ gives
> $$\begin{align}
> 	f'(x) &= k(x-\alpha)^{k-1}g(x) + (x-\alpha)^kg'(x) \\
> 	\left( x-\alpha \right)^kh(x) &= (x-\alpha)^{k-1}\left( kg(x) + (x-\alpha)g'(x) \right) \\
> 	\left( x-\alpha \right)h(x) &= \left( kg(x) + (x-\alpha)g'(x) \right) \\
> 	\to \left( x-\alpha \right)&| \left( kg(x) + (x-\alpha)g'(x) \right) \\
> 	\to \left( x-\alpha \right)&| kg(x) \\
> 	\to \left( x-\alpha \right)&| g(x). \\
> \end{align}$$
> Therefore,
> $$f(x) = \left( x - \alpha \right)^{k+1}j(x)$$
> where $j(x) \in F[x]$. Thus, $\alpha$ is a *multiple zero* of $f(x)$ over $F$ and thus any [[Subfields#^extension-field|extension field]] $E$.

> [!corollary]- If $f(x)$ is [[Reduciblity#^negation|irreducible]] over a [[Fields|field]] $F$ of [[Ring Characteristic|characteristic]] $0$, then $f(x)$ has no *multiple zero*
> #TODO lowkey fuck ts?