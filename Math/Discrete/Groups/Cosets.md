---
tags:
  - atom
  - math
  - discrete
---
Let $H$ be a [[Subgroups|subgroup]] of $G$. A (left) *coset* of $H$ in $G$ is a [[Subsets|subset]] of $G$ of the form
$$g*H = \{ g*h : h \in H \}$$
for some $g \in G$.

> [!theorem]- $g * G = h * G \iff h^{-1} * g \in G$ 
> $\left( \implies \right)$
> $$\begin{align}
> 	g * G &= h * G\\
> 	g * r_{g} &= h * r_{h}\\
> 	g &= h * r && r = r_{h} * r_{g}^{-1} \in G\\
> 	h^{-1} * g  &= r \\
> 	h^{-1} * g  &\in G\\
> \end{align}$$
> $\left( \impliedby \right)$
> $$\begin{align}
> 	h^{-1} * g &\in G \\
> 	h^{-1} * g  &= r \\
> 	g * e  &= h * r \\
> 	\to g * G &= h * G \\
> \end{align}$$
^equality

> [!example] $a \left< b \right> = \{ a*b^n : m \in \Z \}$

\[[[Lagrange's Theorem]]\]