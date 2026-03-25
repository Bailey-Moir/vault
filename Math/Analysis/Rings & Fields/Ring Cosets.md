---
tags:
  - atom
  - math
---
Let $S$ be a [[Subrings|subring]] of a [[Rings|ring]] $R$. A *coset* of $S$ in $R$ is a [[Sets|set]] of the form
$$u+S = \{ u+s : s \in S \}$$
where $u \in R$.

> [!note] *Ring cosets* are just [[Cosets|cosets]] in the addition [[Groups|group]]

> [!theorem]- $u +S = v + S \iff v - u \in S$ 
> $\left( \implies \right)$
> $$\begin{align}
> 	u + S &= v + S\\
> 	u + s_{1} &= v + s_{2}\\
> 	u &= v + s_{3} && s_{3} = s_{2} - s_{1} \in S\\
> 	u - v &= s_{3}\\
> 	u - v &\in S\\
> \end{align}$$
> $\left( \impliedby \right)$
> $$\begin{align}
> 	u - v &\in S \\
> 	u - v &= s_{1} \\
> 	u + 0  &= v + s_{1} \\
> 	\to u + S &= v + S \\
> \end{align}$$
^equality

> [!theorem]- The *ring cosets* of a [[Subrings|subring]] $S$ of a [[Rings|ring]] $R$ is a [[Rings|ring]] itself, where $$\begin{align} \left( u + S \right) + \left( v + S \right) &= \left( u+v \right) + S \\ \left( u + S \right) \times \left( v + S \right) &= \left( u \times v \right) + S, \end{align}$$iff $S$ is an [[Ideals|ideal]].
> ### Addition
> We need to prove that this addition is well defined, meaning that if you add two equal pairs of *cosets*, then their sum is the equal. Thus, suppose
> $$\begin{align}
> 	u_{1} + S &= u_{2} + S \\
> 	v_{1} + S &= v_{2} + S. \\
> \end{align}$$
> Then
> $$\begin{array}{rc}
> 	&(u_{1} + v_{1}) + S = \left( u_{2} + v_{2} \right) + S \\
> 	\iff & \left( u_{1} + v_{1} \right) - \left( u_{2}-v_{2} \right) \in S \\
> 	& \left( u_{1} - u_{2} \right) - \left( v_{2}-v_{2} \right) \in S \\
> \end{array}$$
> We already have $u_{1} - u_{2} \in S$ and $v_{1}-v_{2} \in S$, thus their difference is in $S$. $\square$
> 
> ### Multiplication
> Similarly, suppose
> $$\begin{align}
> 	u_{1} + S &= u_{2} + S \\
> 	v_{1} + S &= v_{2} + S. \\
> \end{align}$$
> Write $u' = u + s_{1}$ and $v' = v = s_{2}$ for some $s_{1},s_{2} \in S$.
> $$\begin{align}
> 	u'v' &= \left( u + s_{1} \right)\left( v + s_{2} \right) \\
> 	u'v' - uv&= s_{1}v + us_{2} + s_{1}s_{2}. \\
> \end{align}$$
> So
> $$\begin{align}
> 	uv + S = u'v' + S &\iff s_{1}v + us_{2} + s_{1}s_{2} \in S \\
> 	&\iff s_{1}v + us_{2} \in S. \\
> \end{align}$$
> Since $s_{1},s_{2} \in S$ could be anything, we require $us \in S$ and $vs \in S$ for all $s \in S$.
^subring