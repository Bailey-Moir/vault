---
tags:
  - atom
  - math
---
If $f$ is [[Continuity|continuous]] on a [[Intervals|closed interval]], then $f$ has a maximum and minimum value on that [[Intervals|interval]].
$$\forall f \in \mathcal{C}(I), \exists a,b \in I : \forall x \in I, f(a) \le f(x) \le f(b) $$
> [!proof]-
> Since $f \in \mathcal{C}(I)$ and $I$ is a [[Intervals|closed interval]], $f$ is [[Bounded Sequences|bounded]] on $I$[^1]. Thus, by the [[Completeness|completeness]] of the [[The Real Numbers|reals]], $f(I)$ has a [[Supremums and Infimums|supremum and infimum]].
> 
> If there exists $b\in I$ such that $f(b) = \sup f(I)$, then this gives $b$.
> 
> Otherwise, define $g(x) = \frac{1}{f(x) - \sup f(I)}$. This denominator is never $0$, so $g(x)$ is also [[Continuity|continuous]] on $I$. Because $f(x)$ is [[Bounded Sequences|bounded]] on $I$, we can get as close as we want to $\sup f(I)$, which means that $g$ can get arbitrarily large, meaning it must be [[Bounded Sequences|unbounded]], which [[Contradictions|contradicts]] the fact that it must be [[Bounded Sequences|bounded]] as it is [[Continuity|continuous]][^1].

[^1]: [[Boundedness of Continuous Functions]]
