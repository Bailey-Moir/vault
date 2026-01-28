---
tags:
  - atom
  - math
---
We define the elementary language of [[Categories|category theory]] as the two sorted [[Fiest-Oreer Languages|first order language]] with
- objects and morphisms as the distinct sorts, together with 
- [[Relations|relations]] of an object being the source or target of a morphism, and
- a symbol for [[Composite Functions|composition]] morphisms.

Let $\sigma$ be a [[Statements and Propositions|statement]] in this language. The *dual* of this statement $\sigma^\text{op}$ is the same as $\sigma$, except:
- The "source" and "target" [[Relations|relations]] are swapped, and
- The order of [[Composite Functions|composition]] is swapped (every $f \circ g$ becomes $g \circ f$).

> [!definition] A [[Statements and Propositions|statement]]/[[Sets|set]]/[[Classes|class]] is **self-dual** iff it is equal to its *dual*.

> [!lemma] $\sigma$ is true in $\mathcal{C}$ iff $\sigma^\text{op}$ is true in $\mathcal{C}^\text{op}$.

> [!theorem]- If $\sigma$ holds for a **self-dual** [[Classes|class]] of [[Categories|categories]] $C$, so does $\sigma^\text{op}$.
> Let $C$ be a [[Classes|class]] of [[Categories|categories]] that is **self-dual**.
> Let $\sigma$ be a [[Statements and Propositions|statement]] in the elementary language of [[Categories|categories]] that holds for all $\mathcal{C} \in C$.
> Since $C$ is **self-dual**, $\sigma$ holds for $\mathcal{C}^\text{op}$.
> Thus, by the lemma above (and the fact that the dual of the dual is itself), $\sigma^\text{op}$ holds for $\mathcal{C}$. $\square$