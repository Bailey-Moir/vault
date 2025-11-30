---
tags:
  - atom
  - math
  - linear
---
The *orthogonal complement* of a [[Subspaces|subspace]] $U$ of an [[Inner Products|inner product space]] $V$ is the [[Sets|set]] of vectors in $V$ that are [[Orthogonal Vectors|orthogonal]] to every vector in $U$, denoted $U^\bot$.
$$\begin{align}
	U^\bot &= \{ \vecbf{x} \in V : \forall \vecbf{u} \in U, \left< \vecbf{x},\vecbf{u} \right>  = 0  \} \\
	&= \hspace{0.5em} \text{null}\;\left[ \vecbf{u}_{1} \; \cdots \; \vecbf{u}_{m} \right] ^T && (1)
\end{align}$$
> [!lemma]
> 1. For a [[Vector Basis|basis]] $\vecbf{u}_{1},\dots,\vecbf{u}_{m}$ of $U$,
>   $\vecbf{x} \in U^\bot \iff \forall i \in \{1,2,\dots,m\}, \left< \vecbf{x},\vecbf{u}_{i} \right> = 0$
> 2. $U^\bot$ is a [[Subspaces|subspace]] of $V$.
> 3. $\text{dim}\,U +\text{dim}\,U^\bot =\text{dim}\,V$.
>
> > [!proof]- 1
> > $(\implies)$
> > Since $\vecbf{u}_{i} \in U$, $\vecbf{x} \in U^\bot$ must be [[Orthogonal Vectors|orthogonal]] to them.
> > $\left( \impliedby \right)$
> > Suppose $\forall i \in \{1,2,\dots,m\}, \left< \vecbf{x},\vecbf{u}_{i} \right> = 0$. Since $\vecbf{u}_{1,}\dots,\vecbf{u}_{m}$ is a [[Vector Basis|basis]] of $U$,
> > $$\begin{align}
> >      \left< \vecbf{x},\vecbf{u} \right>  &= \left< \vecbf{x},c_{1}\vecbf{u}_{1} + \cdots +  c_{m}\vecbf{u}_{m} \right>  \\
> >      &= c_{1}\left< \vecbf{x},\vecbf{u}_{1} \right> + \cdots + c_{m}\left< \vecbf{x},\vecbf{u}_{m} \right>  \\
> >      &= c_{1}\times0 + c_{m}\times0 \\
> >      &= 0 \\
> > \end{align}$$
> 
> > [!proof]- 2
> > For a [[Vector Basis|basis]] $\vecbf{u}_{1},\dots,\vecbf{u}_{m}$ of $U$,
> > $$\begin{align}
> > 	\vecbf{x} \in U^\bot &\iff \forall i \in \{ 1,2,\dots,m \}, \left< \vecbf{u}_{i},\vecbf{x} \right>  = 0 \\
> > 	&\iff \forall i \in \{ 1,2,\dots,m \}, \vecbf{u}_{i}^T\vecbf{x} = 0 && (1)\\
> > 	&\iff \left[ \vecbf{u}_{1} \; \cdots \; \vecbf{u}_{m} \right] ^T\vecbf{x} = \vecbf{0} \\
> > 	&\iff \vecbf{x} \in \text{null}\;\left[ \vecbf{u}_{1} \; \cdots \; \vecbf{u}_{m} \right] ^T \\
> > 	U^\bot &\hspace{0.5em}=\hspace{0.5em} \text{null}\;\left[ \vecbf{u}_{1} \; \cdots \; \vecbf{u}_{m} \right] ^T \\
> > \end{align}$$
> > Since the [[Null Space|null space]] is a [[Vector Spaces|vector space]], $U^\bot$ must be a [[Subspaces|subspace]]. Since $U^\bot \subseteq V$, it is then a [[Subsets|subspace]] of $V$.
> 
> > [!proof]- 3
> > The [[Rank|rank]] of $A = \left[ \vecbf{u}_{1} \; \cdots \; \vecbf{u}_{m} \right] ^T$ is $m$ (as $\vecbf{u}_{1}, \dots,\vecbf{u}_{m}$ is a [[Vector Basis|basis]], meaning they are [[Linear Independence|linearly independent]]), which is the [[Dimension|dimension]] of $U$. By [[Rank-Nullity Theorem|rank-nullity theorem]],
> > $$\begin{align}
> > 	\text{dim}\,V &= \text{nullity}\,A  - \text{rank}\, A \\
> > 	&= \text{dim}\,U^\bot + \text{dim}\,U \\
> > \end{align}$$

> [!note] Similar to [[Complement|set complements]], *orthogonal complements* require an equivalent to the [[Universal Set|universal set]], $V$.