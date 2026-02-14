---
tags:
  - atom
  - math
---
Let $\{ c_i \}_{i \in I}$ be a [[Collections|family]] of objects in a [[Categories|category]] $\mathcal{C}$.

> [!definition]- Auxiliary Category
> The **auxiliary category** $\mathcal{D} = \mathcal{D}_\text{pr}$ is defined with
> - objects being the pairs $\left( x, \{\alpha_i\}_{i \in I} \right)$, where $x \in \mathcal{C}$ and $\alpha_i : x \to c_i$ for all $i \in I$,
> - morphisms from an object $\left( x, \{\alpha_i\}_{i \in I} \right)$ to $\left( y, \{\beta_i\}_{i \in I} \right)$ being the morphisms $\gamma : x \to y$ in $\mathcal{C}$ that [[Commutative Diagrams|commute]] with both families of morphisms, i.e., such that the following diagram is [[Commutative Diagrams|commutative]] for all $i$:
> ```tikz
> \usepackage{tikz-cd}
> \begin{document}
> 
> \begin{tikzcd}
> 	x \arrow[dr, swap, "\alpha_i"] \arrow[rr, "\gamma"] & & y \arrow[dl, "\beta_i"] \\
> 	& c_i
> \end{tikzcd},
> 
> \end{document}
> ```
> - and [[Composite Functions|composition]] being the same as in $\mathcal{C}$.
 ^auxiliary-category
 
A [[Initial and Terminal Objects|terminal object]] $\left( p, \{ \pi_i \}_{i \in I} \right)$ in the [[#^auxiliary-category|auxiliary category]] is called a *product* of the [[Collections|family]] $\{ c_i \}_{i \in I}$. 
By the [[Initial and Terminal Objects|definition of terminal objects]], for any $\left( x, \{\alpha_i\}_{i \in I} \right) \in \mathcal{D}$, there exists a unique $\gamma : x \to p$ in $\mathcal{C}$ such that $\forall i, \pi_i\gamma = \alpha_i$, i.e., such that the following diagram is [[Commutative Diagrams|commutative]] for all $i$:
```tikz
\usepackage{tikz-cd}
\begin{document}

\begin{tikzcd}
	x \arrow[dr, swap, "\alpha_i"] \arrow[rr, "\exists!\gamma"] & & p \arrow[dl, "\pi_i"] \\
	& c_i
\end{tikzcd}.

\end{document}
```

> [!note]- Uniqueness++
> By [[Initial and Terminal Objects#^uniqueness-up-to-isomorphism|the uniqueness of terminal objects up to]] [[Isomorphisms|isomorphism]], *products* (if they exist) are unique up to [[Isomorphisms|isomorphism]] in $\mathcal{D}$, which amounts to [[Isomorphisms|isomorphism]] in $\mathcal{C}$ that preserves the [[Commutative Diagrams|commutativity]].
 ^uniqueness

> [!definition] We say that a "**product exists**" in $\mathcal{C}$ iff a *product* exists for every [[Collections|family]] of objects in $\mathcal{C}$.
^product-exists

# Binary Product
```tikz
\usepackage{tikz-cd}
\begin{document}

\large\begin{tikzcd}[column sep={2em}, row sep={2em}]
	& x \arrow[d, dashed, "\exists!f"] \\
	& \arrow[dl, "\pi_1"] a \times b \arrow[dr, swap, "\pi_2"] \\[-2em]
	a && b
	\arrow[from=1-2, to=3-1, bend right, "f_1"']
	\arrow[from=1-2, to=3-3, bend left, "f_2"]
\end{tikzcd}

\end{document}
```
When $\{ c_i \}_{i \in I} = \{ a,b \}$, and $p$ is denoted $a \times b$, you get the above. Stated without the language of the [[#^auxiliary-category|auxiliary category]],
> Objects $a,b \in \mathcal{C}$ have a *product* $a \times b$ and $\pi_1,\pi_2$ iff for every $x \in \mathcal{C}$, there exists a unique morphism $f : x \to (a \times b)$ such that the above diagram is [[Commutative Diagrams|commutative]] for all $f_1$ and $f_2$.
