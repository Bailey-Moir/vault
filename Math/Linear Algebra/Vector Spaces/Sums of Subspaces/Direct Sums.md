---
tags:
  - atom
  - math
  - linear
---
The [[Sums of Subspaces|sum]] $V_1 + \dots + V_m$ is called a *direct sum* iff each element has a unique representation $\vecbf{v}_1 + \dots + \vecbf{v}_m$, where $\vecbf{v}_i \in V_i$.
$$ \forall \vecbf{v} \in U \oplus W, \exists! \vecbf{u} \in U, \vecbf{w} \in W : \vecbf{v} = \vecbf{u} + \vecbf{w} $$

> [!note] Conditions for a Direct Sum
> $V_1 + \cdots + V_m \in V$ is a *direct sum* iff the only choice of $\vecbf{v}_1 \in V_{1}, \dots, \vecbf{v}_m \in V_{m}$ that makes
> $$ \vecbf{v}_1 + \dots + \vecbf{v}_m = \vecbf{0}$$
> is $\vecbf{v}_1 = \dots = \vecbf{v}_m = \vecbf{0}$
> > [!proof]-
> > ($\implies$)
> > Suppose $V_1 + \dots + V_m$ is a *direct sum*. This implies there is only one representation for $\vecbf{0}$: $\vecbf{v}_i = \vecbf{0}$.
> > 
> > ($\impliedby$)
> > Suppose the only way to represent $\vecbf{0}$ as a sum $\vecbf{v}_1 + \dots + \vecbf{v}_m$ where $\vecbf{v}_{i} \in V_{i}$ is when $\vecbf{v}_{i} = \vecbf{0}$. 
> > 
> > Let $\vecbf{v} \in V_1 + \dots + V_m$. Then $\vecbf{v} = \vecbf{v}_1 + \dots + \vecbf{v}_m$ where $\vecbf{v}_i \in V_i$. Suppose we also have $\vecbf{v} = \vecbf{v'}_1 + \dots + \vecbf{v'}_m$ where $\vecbf{v'}_i \in V_i$. Subtracting these two equations gives
> > $$ \vecbf{0} = (\vecbf{v}_1 - \vecbf{v'}_1) + \dots + (\vecbf{v}_m - \vecbf{v'}_m) $$
> > Since $\vecbf{v}_k - \vecbf{v'}_k \in V_k$, by the premise, $\vecbf{v}_k - \vecbf{v'}_k = 0$. Thus $\vecbf{v}_k = \vecbf{v'}_k$, meaning each vector $\vecbf{v} \in V_{1} + \cdots + V_{m}$ has only one representation, and thus $V_{1} + \dots + V_{m}$ is a *direct sum*.

> [!note] Condition for Direct Sum of Two Subspaces
> $$ U \cap V = \{\vecbf{0}\} \iff U \oplus V $$

\[[[Sums of Subspaces]]\]