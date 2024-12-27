---
tags:
  - atom
  - math
---
The *null space* of a [[Linear Maps|linear map]] is the [[Subsets|subset]] of its [[Domain|domain]] that gets mapped to $\vecbf{0}$;
$$\forall T \in \mathcal{L}(V,W),\hspace{1em} \text{null}\,T = \{ \vecbf{v} \in V : T\,\vecbf{v} = \vecbf{0} \}$$
- The *null space* is a [[Subspaces|subspace]] of the [[Domain|domain]].
  > [!proof]-
> **Additive Identity**
> Since $T \vecbf{0} = \vecbf{0}$, $\vecbf{0} \in \text{null}\,T$.
> 
> **Closed Under Addition**
Consider two vectors $\vecbf{u},\vecbf{v} \in \text{null}\,T$. It follows that
> $$\begin{align*}
> 	T(\vecbf{u} + \vecbf{v}) &= T\,\vecbf{u} + T\,\vecbf{v} \\
> 	&= \vecbf{0} + \vecbf{0} \\
> 	&= \vecbf{0}. \\
> \end{align*}$$
> Thus, $\vecbf{u}+\vecbf{v} \in \text{null}\,T$.
> 
> **Closed Under Scalar Multiplication**
> Consider $\vecbf{u} \in \text{null}\,T$ and $\lambda \in \F$. It follows that
> $$\begin{align*}
> 	T(\lambda\vecbf{u}) &= \lambda T\,\vecbf{u} \\
> 	&= \lambda\vecbf{0} \\
> 	&= \vecbf{0}. \\
> \end{align*}$$
> Thus, $\lambda\vecbf{u} \in \text{null}\,T$.

- $T$ is [[Injective Functions|injective]] iff $\text{null}\,T = \{ \vecbf{0} \}$.
  > [!proof]-
> ($\implies$)
> Suppose $T$ is [[Injective Functions|injective]]. 
> 
> Note $\vecbf{0} \in \text{null}\,T$. Suppose there was another vector $\vecbf{v} \in \text{null}\, T$. Then
> $$ T\,\vecbf{v} = 0 = T\,\vecbf{0}. $$
> Since $T$ is [[Injective Functions|injective]], $\vecbf{v} =0$, meaning $\vecbf{0}$ must be the only vector in $\text{null}\,T$.  
> 
> ($\impliedby$)
> Let $T \in \mathcal{L}(V,W)$ such that $\text{null}\,T = \{ \vecbf{0} \}$, and $\vecbf{u}, \vecbf{v} \in V$ such that $T \, \vecbf{u} = T\, \vecbf{v}$.
> $$\begin{align*}
> 	0 &= T\,\vecbf{u} - T\,\vecbf{v} \\
> 	&= T\,(\vecbf{u} - \vecbf{v}). && \text{Additivity} \\
> \end{align*}$$
> Thus, $\vecbf{u} - \vecbf{v} \in \text{null}\,T$, and since $\text{null}\,T = \{ \vecbf{0} \}$, $\vecbf{u}-\vecbf{v} = 0$, meaning $\vecbf{u} = \vecbf{v}$. Thus, $T$ is [[Injective Functions|injective]].