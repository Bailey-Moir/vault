---
tags:
  - atom
  - math
  - discrete
---
The *baby-step giant-step algorithm* is an [[Algorithms|algorithm]] for the [[Discrete Logarithm Problem|discrete logarithm problem]].

![350|center](b-step-g-step.excalidraw.md)

Let $G$ be a [[Cyclic Groups|cyclic group]] with a [[Group Generators|generator]] $g$ and $h \in G$.
1. Let $m = \left\lceil \sqrt{ \left| G \right| } \right\rceil$ and computer $g^{-m}$.
2. Create two lists:
$$\begin{align}
	L_{1} &:\hspace{1em} g^0, g^1, g^2, \dots, g^m \\
	L_{2} &:\hspace{1em} h, hg^{-m}, hg^{-2m}, \dots, hg^{-m^2}
\end{align}$$
3. Find a match between the two lists, say $g^i = hg^{-jm}$.
4. Then the [[Discrete Logarithm Problem|discrete logarithm]] $\log_{g}(h) = i + jm$

> [!note]- Why $\left\lceil \sqrt{ \left| G \right| } \right\rceil$?
> We know $h = g^a$ for some $a \in \Z_{\left| G \right|}$.
> 
> $n \le m^2$, so we can write $a = i + jm$ with $0 \le i,j \le m$.
> 
> This means we will find a collision.

> [!analysis]- $O(\sqrt{ n }\log n)$
> There are $m$ baby-steps and $m$ giant-steps, so the number of steps is $O(m) = O(\sqrt{ n })$. A standard search and sort algorithm will find a match in resulting list in $O(m \log m) = O(\sqrt{ n }\log n)$.
> 
> The algorithm requires $2m$ elements in the list(s), each of which has $\log_{2}(n)$ bits, so the total storage requirement is $O(m\log n) = O(\sqrt{ n }\log n)$.