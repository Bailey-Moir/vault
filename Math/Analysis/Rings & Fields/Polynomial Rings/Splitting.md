---
tags:
  - atom
  - math
---
Let $E$ be an [[Subfields#^extension-field|extension field]] of $F$, and let $f(x) \in F[x]$.
We say that $f(x)$ *splits* in $E$ iff $f(x)$ can be factored as a product of linear factors of $E[x]$; iff
$$ f(x) = \beta\prod_{i \in I} \left( x - \alpha_{i} \right) \quad \beta \in E[x], \forall i \in I, \alpha_{i} \in E[x] $$
> [!definition] *(Splitting Fields)* We call $E$ a *splitting field* for $f(x)$ over $F$ iff $E$ is a [[Maximal vs. Maximum|minimal]] [[Fields|field]] containg $F$ that *splits* $f$
^splitting-fields

> [!theorem]- Let $F$ be a [[Fields|field]] and $f \in F[x]$ be non-constant. Then there exists a [[#^splitting-fields|splitting field]] $E$ for $f(x)$ over $F$.
> > [!intuition]-
> > Just keep adjoining roots until everything is a linear term. The resulting field is just the original with each root adjoined, so any intermediate field must have a different factorisation as it is missing a root, which is a contradiction as the polynomials over the field with adjoined roots form a unique factorisation domain. Thus, the resulting field is a splitting field.
> 
> Without loss of generality, suppose $f$ is [[Polynomial Rings#^monic|monic]] (as you can just multiply by the inverse of the leading coefficient).
> 
> **Induction Statement**
> For any [[Fields|field]] $E$, and $f(x) \in E[x]$ of [[Polynomials#Degree|degree]] $k\in \Z^+$, there exists $\alpha_{1},\dots,\alpha_{k}$ in some [[Subfields#^extension-field|extension field]]of $E$ such that
> $$f(x) = \left( x - \alpha_{1} \right)\cdots\left( x - \alpha_{k} \right) \in E(\alpha_{1},\dots,\alpha_{k}).$$
> 
> **Base Case**
> Let $F$ be a [[Fields|field]], and let $f \in F[x]$ such that $\deg f = 1$, so
> $$f(x) = x - \alpha_{1}$$
> for some $\alpha_{1} \in F$. Thus, $F(\alpha_{1}) = F$ is a *splitting field* for $f(x)$ over $F$.
> 
> **Induction Step**
> Let $F$ be a [[Fields|field]], let $f(x) \in F[x]$ such that $\deg f = k > 1$, and suppose the **induction statement** for $k-1$
> 
> Since $F[x]$ is a [[Unique Factorisation Domain|UFD]][^1], $f(x) \in F[x]$ has an [[Reduciblity#^negation|irreducible factor]] $p(x) \in F[x]$. Construct
> $$ F(\alpha_{k}) \cong F[x] / \left< p(x) \right>. $$
> where $\alpha_{k}$ is a root of $p(x)$ and thus $f(x)$ in $F(\alpha_{k})[x]$ (by the construction in [[Kronecker's Theorem|Kronecker's theorem]] and the [[Structure of Simple Field Extensions|structure of simple field extensions]]).
> 
> Thus, by [[Division Algorithm|remainder theorem]],
> $$f(x) = g(x)(x - \alpha_{k}) \in F(\alpha_{k})[x],$$
> where $\deg g = k -1$. 
> 
> By the [[Induction|induction hypothesis]], there exists $\alpha_{1},\dots,\alpha_{k-1}$ in some [[Subfields#^extension-field|extension field]] of $F(\alpha_{k})$ such that
> $$\begin{align}
> 	& g(x) = \left( x - \alpha_{1} \right) \cdots \left( x-\alpha_{k-1} \right) \in \left( F(\alpha_{k}) \right)(\alpha_{1},\dots,\alpha_{k-1})[x] \\
> 	& \phantom{g(x) = \left( x - \alpha_{1} \right) \cdots \left( x-\alpha_{k-1} \right) \in\;} F(\alpha_{0},\dots,\alpha_{k})[x] \\
> 	\implies & f(x) = (x - \alpha_{1}) \cdots \left( x-\alpha_{k-1} \right)\left( x-\alpha_{k} \right) \in F(\alpha_{0},\dots,\alpha_{k})[x]. \\
> \end{align}$$
> Thus, the [[Implication|implication]] for the [[Induction|induction]] is given!
> 
> Further, suppose there is some [[Subfields|sub]]/[[Subfields#^extension-field|extension]] [[Fields|field]] $L$ such that $F \subseteq L \subset F(\alpha_{0},\dots,\alpha_{n})$.
> By [[Simple Field Extensions|definition]], $F(\alpha_{0},\dots,\alpha_{n})$ is the smallest [[Fields|field]] containing $F$ and $\alpha_{0},\dots,$ and $\alpha_{n}$. Thus, for some $\alpha_{i}$, $\alpha_{i} \notin$ $L$.
> Then the above factorisation can not be formed over $L$, so $f$ *splits* differently in $L$, giving a different factorisation into [[Reduciblity#^negation|irreducibles]] in $F(\alpha_{0},\dots,\alpha_{n})$. This [[Contradictions|contradicts]] $F\left( \alpha_{0},\dots,\alpha_{n} \right)$[^1] being a [[Unique Factorisation Domain|UFD]].
> Thus, $F(\alpha_{0},\dots,\alpha_{n})$ is a [[#^splitting-fields|splitting field]] of $f(x)$ over $F$.
> 
> **Conclusion**
> For any [[Fields|field]] $F$, and non-constant $f(x) \in F[x]$, there exists $\alpha_{1},\dots,\alpha_{\deg f}$ in some [[Subfields#^extension-field|extension field]] of $F$ such that
> $$f(x) = \left( x - \alpha_{1} \right)\cdots\left( x - \alpha_{\deg f} \right) \in F(\alpha_{1},\dots,\alpha_{\deg f}),$$
> and $F(\alpha_{1},\dots,\alpha_{\deg f})$ is a [[#^splitting-fields|splitting field]] of $f(x)$ over $F$.
^non-constants-have-splitting-fields

> [!theorem]- Let $F$ be a [[Fields|field]] and $f \in F[x]$. Then any two [[#^splitting-fields|splitting fields]] for $f(x)$ over $F$ are [[Isomorphisms|isomorphic]].
> **Preface**
> We will prove a more general theorem:
> > Let $\varphi : F_{1} \to F_{2}$ be a [[Ring Homomorphisms|field homomorphism]]. If
> > $$\begin{align}
> > 	f_{1}(x) &= a_{0} + a_{1}x + \dots + a_{n}x^n \in F_{1}[x] \\
> > 	f_{2}(x) &= \varphi(a_{0}) + \varphi(a_{1})x + \dots + \varphi(a_{n})x^n \in F_{2}[x], \\
> > \end{align}$$
> > Then any [[#^splitting-fields|splitting fields]] $E_{1}$ and $E_{2}$ of $f_{1}$ over $F_{1}$ and $f_{2}$ over $F_{2}$ respectively are [[Isomorphisms|isomorphic]].
> 
> Then, our theorem is given when $F_{1} = F_{2}$, and $\varphi$ is the identity [[Functions|function]].
> 
> **Proof**
> Let $\varphi : F_{1} \to F_{2}$ be a [[Ring Homomorphisms|field homomorphism]]. Define a $\phi : F_{1}[x] \to F_{2}[x]$ by
> $$\sum_{i = 0}^n a_{i}x^i \mapsto \sum_{i = 0}^n \varphi(a_{i})x^i.$$
> This is well-defined as it is defined directly and uniquely from the input. It is a [[Ring Homomorphisms|ring homomorphism]]  because
> $$\begin{align}
> 	\phi \left( \sum_{i = 0}^n a_{i}x^i + \sum_{i = 0}^m b_{i}x^i \right) &= \phi \left( \sum_{i = 0}^{\max \{ n,m \}} \left( a_{i} + b_{i} \right)x^i \right) \\
> 	&= \sum_{i = 0}^{\max \{ n,m \}} \varphi\left( a_{i} + b_{i} \right)x^i \\
> 	&= \sum_{i = 0}^{\max \{ n,m \}} \left( \varphi(a_{i}) + \varphi(b_{i} )\right)x^i \\
> 	&= \sum_{i = 0}^n \varphi(a_{i})x^i + \sum_{i = 0}^m \varphi(b_{i})x^i \\
> 	&= \phi \left( \sum_{i = 0}^n a_{i}x^i \right) + \phi \left( \sum_{i = 0}^m b_{i}x^i \right). \\
> 	\\
> 	\phi \left( \sum_{i = 0}^n a_{i}x^i \times \sum_{i = 0}^m b_{i}x^i \right) &= \phi \left( \sum_{i = 0}^n \sum_{j=0}^m a_{i}b_{j}x^{i+j} \right) \\
> 	&= \sum_{i = 0}^n \sum_{j=0}^m \varphi(a_{i}b_{j})x^{i+j} \\
> 	&= \sum_{i = 0}^n \sum_{j=0}^m \varphi(a_{i})\varphi(b_{j})x^{i+j} \\
> 	&= \sum_{i = 0}^n \varphi(a_{i})x^i \times \sum_{i = 0}^m \varphi(b_{i})x^i \\
> 	&= \phi\left( \sum_{i = 0}^n a_{i}x^i \right) \times \phi \left( \sum_{i = 0}^m b_{i}x^i \right). \\
> \end{align}$$
> Let $f_{1} \in F_{1}[x]$ and $p_{1} \in F_{1}[x]$ be a non-constant [[Reduciblity#^negation|irreducible factor]] of $f_{1}$. Then let $f_{2} = \phi(f_{1}) \in F_{2}[x]$, and $p_{2} = \phi(p_{1}) \in F_{2}[x]$, an [[Reduciblity#^negation|irreducible factor]] of $f_{2}$. Let $\alpha_{1}$ and $\alpha_{2}$ be roots of $p_{1}$ and $p_{2}$ respectively.
> 
> Define $\pi : F_{2}[x] \to F_{2}[x] / \left< p_{2}(x) \right>$ by $\pi(x) = x + \left< p_{2}(x) \right>$, which is a known [[Ring Homomorphisms|ring homomorphism]].
> 
> Finally, consider $\lambda = \pi \circ \phi : F_{1}[x] \to F_{2}[x] / \left< p_{2}(x) \right>$.
> 
> For any $g(x)p_{1}(x) \in \left< p_{1}(x) \right> \subseteq F_{1}[x]$,
> $$\begin{align}
> 	\lambda(g(x)p_{1}(x))
> 	&= \lambda(g(x)) \times \lambda(p_{1}(x))  \\
> 	&= \lambda(g(x)) \times \pi(\phi(p_{1}(x))) \\
> 	&= \lambda(g(x)) \times \pi(p_{2}(x)) \\
> 	&= \lambda(g(x)) \times \left( 0 + \left< p_{2}(x) \right> \right) \\
> 	&= 0 + \left< p_{2}(x) \right> \\
> \end{align}$$
> Thus, $\left< p_{1}(x) \right> \subseteq \ker \lambda$. $p_{1}(x)$ is [[Reduciblity#^negation|irreducible]], [[Maximal Ideals#^polynomials|so]] $\left< p_{1}(x) \right>$ is a [[Maximal Ideals|maximal ideal]] of $F_{1}[x]$. Thus, $\ker \lambda = \left< p_{1}(x) \right>$.
> 
> $\phi$ is an [[Isomorphisms|isomorphism]], so it is [[Surjective Functions|surjective]], and $\pi$ is obviously [[Surjective Functions|surjective]], so $\lambda$ is [[Surjective Functions|surjective]]. By [[First Isomorphism Theorem for Rings|first isomorphism theorem]],
> $$F_{1}(\alpha_{1}) \cong F_{1}[x] / \left< p_{1}(x) \right> \cong F_{2} / \left< p_{2}(x) \right> \cong F_{2}(\alpha_{2}). $$
> Repeating this process (by [[Induction|induction]]) with,
> $$\begin{array}{cc}
> F_{1} \leftarrow F_{1}(\alpha_{1}), & F_{2} \leftarrow F_{2}(\alpha_{2}), \\
> f_{1} \leftarrow f_{1} / (x - \alpha_{1}), & f_{2} \leftarrow f_{2} / (x - \alpha_{2}). \\
> \end{array}$$
> this creates fields $E_{1}$ and $E_{2}$ that are [[Isomorphisms|isomorphic]] and [[#^splitting-fields|splitting fields]] of $F_{1}$ and $F_{2}$ respectively (by the construction from [[#^non-constants-have-splitting-fields|the previous proof]]).




^isomorphic

[^1]: [[Unique Factorisation Domain#^examples]]
[^2]: [[Simple Field Extensions]]
