---
tags:
  - atom
  - math
  - linear
---
A *norm* of a [[Vector Spaces|vector space]] $V$ is a [[Functions|function]] $\| \cdot \| : V \to \R$ that assigns each $\vecbf{v} \in V$ a real number $\| \vecbf{v} \|$ such that for all $\vecbf{u},\vecbf{v} \in V$ and $c \in \R$,
1. **[[Inner Products|Positive Definite]]**
   $\mathit{\| \vecbf{v} \| \ge 0}$
   $\| \vecbf{v} \| = 0 \leftrightarrow \vecbf{v}=\vecbf{0}$
2. **[[Linear Maps|Absolute Homogeneity]]**
   $\| \lambda \vecbf{v} \| = \left| \lambda \right|\| \vecbf{v} \|$
3. **[[The Triangle Inequality|The Triangle Inequality]]**
   $\| \vecbf{u}+\vecbf{v} \| \le \| \vecbf{u} \|+\| \vecbf{v} \|$

> [!definition] *(Induced Norms)* In an [[Inner Products|inner product space]], an **induced norm** is the *norm* given by $$\| \vecbf{v} \|^2 = \left< \vecbf{v},\vecbf{v} \right> $$
 ^induced-norms

> [!theorem]- *(Positivity)* $\forall \vecbf{v} \in V, \| \vecbf{v} \| \ge 0$.
> $$\begin{align}
> 	0 &= \| \vecbf{v} - \vecbf{v} \| && \text{N1} \\ 
> 	&\le \| \vecbf{v} \| + \| -\vecbf{v} \| && \text{N3} \\ 
> 	&\le \| \vecbf{v} \| + \left| -1 \right| \| \vecbf{v} \| && \text{N2} \\ 
> 	&= 2\| \vecbf{v} \| \\ 
> 	\to 0 &\le \| \vecbf{v} \| \\ 
> \end{align}$$

> [!theorem]- A [[Vector Spaces|vector space]] has a *norm* $\| \cdot \| : V \to \R$ iff it has a [[Metric Spaces|metric]] $d : V\times V \to \R$ such that $\forall \vecbf{u}, \vecbf{v} \in V$,$$\| \vecbf{u} - \vecbf{v} \| = d(\vecbf{u},\vecbf{v})$$
