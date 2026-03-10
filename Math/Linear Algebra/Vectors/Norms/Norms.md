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
   $\| \vecbf{u}+\vecbf{v} \| \le \| \vecbf{u} \|+\| \vecbf{v} \|$.

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

> [!theorem]- *(Induced Metrics)* Every [[Vector Spaces|vector space]] with a *norm* $\| \cdot \| : V \to \R$ induces a [[Metric Spaces|metric]] $d : V\times V \to \R$ defined as,$$d(\vecbf{u},\vecbf{v}) = \| \vecbf{u} - \vecbf{v} \|$$
> Suppose $V$ is a [[Vector Spaces|vector space]] with *norm* $\| \cdot \| : V \to \R$.
> Let $d : V \times V \to \R$  be defined as
> $$d(\vecbf{u},\vecbf{v}) = \| \vecbf{u} - \vecbf{v} \|.$$
> (M1)
> $$\begin{align}
> 	d(\vecbf{u},\vecbf{v}) = 0 &\iff \| \vecbf{u} - \vecbf{v} \| = 0 \\
> 	&\iff \vecbf{u} - \vecbf{v} = 0 && \text{N1} \\
> 	&\iff \vecbf{u} = \vecbf{v} \\
> \end{align}$$
> (M2)
> $$d(\vecbf{u},\vecbf{v}) = \| \vecbf{u} - \vecbf{v} \| = \left| -1 \right|\| \vecbf{v} - \vecbf{u} \| = \| \vecbf{v} - \vecbf{u} \| = d(\vecbf{v},\vecbf{u}).$$
> (M3)
> $$\begin{align}
> 	d(\vecbf{u},\vecbf{v}) &= \| \vecbf{u} - \vecbf{v} \| \\
> 	&= \| \vecbf{u} - \vecbf{w} - \vecbf{v} + \vecbf{w} \| \\
> 	&\le \| \vecbf{u} - \vecbf{w} \| + \| -\vecbf{v} + \vecbf{w} \| && \text{N3} \\
> 	&\le \| \vecbf{u} - \vecbf{w} \| + \left| -1 \right| \| \vecbf{w} - \vecbf{v} \| && \text{N2} \\
> 	&\le d(\vecbf{u},\vecbf{w}) + d(\vecbf{w},\vecbf{v}). &&\square \\
> \end{align}$$
^induced-metrics