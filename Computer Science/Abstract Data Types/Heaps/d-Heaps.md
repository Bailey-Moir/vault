---
tags:
  - atom
  - comp
---
A *$\it{d}$-heap* is a [[Heaps|heap]] where each [[Vertices|vertex]] has $d$ [[Parent, Children, and Sibling Nodes|children]]. Comparing this to a [[Binary Heaps|binary heap]],
- **[[Binary Heaps#Add|Add]]**: $\log_{2}n\to \log_{d}n$
- **[[Binary Heaps#Remove|Remove]]**: $2\log_{2}n\to d\log_{d}n$

For a given [[Vertices|vertex]] $i$ in $d$-heap,
- its [[Parent, Children, and Sibling Nodes|children]] are at indices $\left\{ d(i-1) + k + 2 : k \in \Z_{d} \right\}$[^1].
- its [[Parent, Children, and Sibling Nodes|parent]] is at $\left\lfloor \dfrac{i+d-2}{d} \right\rfloor \tiny\color{gray} = \left\lfloor \dfrac{i-2}{d} \right\rfloor + 1$.

> [!note]- $\it{3}$-heaps and $\it{4}$-heaps
> $$\begin{align*}
> 	d\log_{d}n &= d \dfrac{\log_{2}n}{\log_{2}d} \\
> 	&= \dfrac{d}{\log_{2}d} \log_{2}n \\
> \end{align*}$$
> Thus, when this coefficient is less than or equal to $2$, a $d$-heap is a good alternative to a [[Binary Heaps|binary heap]] (*$\it{2}$-heap*) in both the add and remove functions. This is only true when $d\in \{ 2,3,4 \}$. When $d = 3$, this constant is approximately $1.89$, whereas when $d=4$, this constant is exactly $2$, so the [[Binary Heaps#Remove|remove]] function has the same worst case, but the add function is much better.

[^1]: [[Cyclic Groups]]