Without loss of generality, suppose $f$ is [[Polynomial Rings#^monic|monic]] (as you can just multiply by the inverse of the leading coefficient).

**Induction Statement**
For any [[Fields|field]] $E$, and $f(x) \in E[x]$ of [[Polynomials#Degree|degree]] $k\in \Z^+$, there exists $\alpha_{1},\dots,\alpha_{k}$ in some [[Subfields#^extension-field|extension field]] of $E$ such that
$$f(x) = \left( x - \alpha_{1} \right)\cdots\left( x - \alpha_{k} \right) \in E(\alpha_{1},\dots,\alpha_{k}).$$

**Base Case**
Let $F$ be a [[Fields|field]], and let $f \in F[x]$ such that $\deg f = 1$, so
$$f(x) = x - \alpha_{1}$$
for some $\alpha_{1} \in F$. Thus, $F(\alpha_{1}) = F$ is a *splitting field* for $f(x)$ over $F$.

**Induction Step**
Let $F$ be a [[Fields|field]], let $f(x) \in F[x]$ such that $\deg f = k > 1$, and suppose the **induction statement** for $k-1$

Since $F[x]$ is a [[Unique Factorisation Domain|UFD]][^1], $f(x) \in F[x]$ has an [[Reduciblity#^negation|irreducible factor]] $p(x) \in F[x]$. Construct
$$ F(\alpha_{k}) \cong F[x] / \left< p(x) \right>. $$
where $\alpha_{k}$ is a root of $p(x)$ and thus $f(x)$ in $F(\alpha_{k})[x]$ (by the construction in [[Kronecker's Theorem|Kronecker's theorem]] and the [[Structure of Simple Field Extensions|structure of simple field extensions]]).

Thus, by [[Division Algorithm|remainder theorem]],
$$f(x) = g(x)(x - \alpha_{k}) \in F(\alpha_{k})[x],$$
where $\deg g = k -1$. 

By the [[Induction|induction hypothesis]], there exists $\alpha_{1},\dots,\alpha_{k-1}$ in some [[Subfields#^extension-field|extension field]] of $F(\alpha_{k})$ such that
$$\begin{align}
	& g(x) = \left( x - \alpha_{1} \right) \cdots \left( x-\alpha_{k-1} \right) \in \left( F(\alpha_{k}) \right)(\alpha_{1},\dots,\alpha_{k-1})[x] \\
	& \phantom{g(x) = \left( x - \alpha_{1} \right) \cdots \left( x-\alpha_{k-1} \right) \in\;} F(\alpha_{0},\dots,\alpha_{k})[x] \\
	\implies & f(x) = (x - \alpha_{1}) \cdots \left( x-\alpha_{k-1} \right)\left( x-\alpha_{k} \right) \in F(\alpha_{0},\dots,\alpha_{k})[x]. \\
\end{align}$$
Thus, the [[Implication|implication]] for the [[Induction|induction]] is given!

Further, suppose there is some [[Subfields|sub]]/[[Subfields#^extension-field|extension]] [[Fields|field]] $L$ such that $F \subseteq L \subset F(\alpha_{0},\dots,\alpha_{n})$.

By [[Simple Field Extensions|definition]], $F(\alpha_{0},\dots,\alpha_{n})$ is the smallest [[Fields|field]] containing $F$ and $\alpha_{0},\dots,$ and $\alpha_{n}$. Thus, for some $\alpha_{i}$, $\alpha_{i} \notin$ $L$.

Then the above factorisation can not be formed over $L$, so $f$ *splits* differently in $L$, giving a different factorisation into [[Reduciblity#^negation|irreducibles]] in $F(\alpha_{0},\dots,\alpha_{n})$. This [[Contradictions|contradicts]] $F\left( \alpha_{0},\dots,\alpha_{n} \right)$[^1] being a [[Unique Factorisation Domain|UFD]].

Thus, $F(\alpha_{0},\dots,\alpha_{n})$ is a [[#^splitting-fields|splitting field]] of $f(x)$ over $F$.

**Conclusion**
For any [[Fields|field]] $F$, and non-constant $f(x) \in F[x]$, there exists $\alpha_{1},\dots,\alpha_{\deg f}$ in some [[Subfields#^extension-field|extension field]] of $F$ such that
$$f(x) = \left( x - \alpha_{1} \right)\cdots\left( x - \alpha_{\deg f} \right) \in F(\alpha_{1},\dots,\alpha_{\deg f}),$$
and $F(\alpha_{1},\dots,\alpha_{\deg f})$ is a [[#^splitting-fields|splitting field]] of $f(x)$ over $F$.