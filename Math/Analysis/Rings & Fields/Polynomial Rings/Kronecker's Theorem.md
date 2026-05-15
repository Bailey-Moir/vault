---
tags:
  - atom
  - math
---
Let $F$ be a [[Fields|field]], and $f \in F[x]$[^1] be a non-constant [[Polynomial Rings|polynomial]].
Then there is an [[Subfields#^extension-field|extension field]] $E$ of $F$ over which $f$ has a root.

> [!proof]-
> Choose a non-constant [[Reduciblity#^negation|irreducible factor]] $g(x)$ of $f(x)$ over $F$.
> [[Maximal Ideals#^polynomials|Irreducible factors give maximal ideals]], so $\left< g(x) \right>$ is a [[Maximal Ideals|maximal ideal]] of $F[x]$.
> Thus, since [[Maximal Ideals#^quotient-field|quotients by maximal ideals give fields]], $E = F[x] / \left< g(x) \right>$ is a [[Fields|field]].
>
> Every element of $E$ is given by $h(x) + \left< g(x) \right>$ for some $h(x) \in F[x]$.
> By taking the remainder of $h(x)$ by $g(x)$ using the [[Division Algorithm|division algorithm]], we get $\deg h < \deg g = d$, meaning.
> $$E = \left\{ a_{0} + a_{1}x + \dots + a_{d-1}x^{d-1} + \left< g(x) \right> : a_{0},\dots,a_{d-1} \in F \right\}. $$
> Consider $\alpha = x + \left< g(x) \right> \in E$.
>
> $$
> \begin{align}
> 	\alpha &= x + \left< g(x) \right>  \in E \\
> 	\alpha^2 &= x^2 + \left< g(x) \right>  \in E \\
> 	\alpha^3 &= x^3 + \left< g(x) \right>  \in E \\
> 	&\dots
> \end{align}
> $$
>
> $$a_{0}+a_{1}\alpha+\dots+a_{n}\alpha^n = a_{0}+a_{1}x+\dots+a_{n}x^n + \left< g(x) \right> .$$
> In particular, $g(\alpha) = g(x) + \left< g(x) \right> = 0$, meaning $\alpha$ is a root of $g(x) \in E$.

[^1]: [[Polynomial Rings]]
