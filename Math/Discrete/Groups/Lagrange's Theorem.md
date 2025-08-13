---
tags:
  - atom
  - math
  - discrete
---
Let $G$ be a finite [[Groups|group]], and $H \le G$. Then the [[Order in Groups|order]] of $H$ divides the [[Order in Groups|order]] of $G$.

> [!proof]-
> Let $g_{1}H, \dots, g_{n}H$ be the [[Cosets|cosets]] of $H$ in $G$.
> $$\begin{align}
> 	 \left| G \right| &= \sum_{i=1}^n \left| g_{i}H \right| && (1) \\
> 	 &= \sum_{i=1}^n \left| H \right| && (2) \\
> 	 &= n\left| H \right| \\
> \end{align}$$
> Thus, by the definition of [[Divisibility|divisibility]], $\left| H \right| \,{\big|} \left| G \right|$.

> [!lemma]- $\mathbf{(1)}$ If $H \le G$, the [[Cosets|left cosets]] of $H$ [[Partitions|partition]] $G$.
> 1. **Every $\mathbf{g\in G}$ lies in some [[Cosets|coset]] of $\mathbf{H}$.**
> $g = ge \in gH$ because $e \in H$ as $H$ is a [[Groups|group]]
> 
> 2. **Any two distinct [[Cosets|cosets]] of $\mathbf{H}$ must be [[Disjoint Sets|disjoint]].**
>    Suppose $g_{1}H \cap g_{2}H \ne \emptyset$, and $g \in g_{1}H \cap g_{2}H$.
> 
>    We can write $g = g_{1}h_{1}=g_{2}h_{2}$ for some $h_{1},h_{2} \in H$.
> 
>    Thus, $g_{1} = g_{2}h_{2}h_{1}^{-1}$, meaning if $g_{1}h$ is any element in $g_{1}H$, we have
> $$g_{1}h = g_{2}h_{2}h_{1}^{-1}h \in g_{2}H$$
>    Similarly, $g_{2} = g_{1}h_{1}h_{2}^{-1}$, meaning if $g_{2}h$ is any element in $g_{2}H$, we have
> $$g_{2}h = g_{1}h_{1}h_{2}^{-1}h \in g_{1}H$$
>    Thus, $g_{1}H=g_{2}H$.jj

> [!lemma]- $\mathbf{(2)}$ If $H \le G$, all [[Cosets|cosets]] of $H$ have the same [[Cardinality|cardinality]].
> Let $gH$ be a [[Cosets|coset]]. Consider the [[Functions|function]]
> $$\phi: H \to gH \hspace{2em} \phi(h) = gh$$
> If this is a [[Bijective Functions|bijection]], the two [[Cosets|cosets]] $H$ and $gH$ must have the same [[Cardinality|cardinality]]. 
> 
> - **[[Surjective Functions|Surjectivity]]**
>   If $a \in gH$, $a = gh = \phi(h)$ for some $h \in H$.
> - **[[Injective Functions|Injectivity]]**
>   If $\phi(h_{1}) = \phi(h_{2})$, then $gh_{1} = gh_{2}$. By [[Groups#Theorems|cancellation]], we have $h_{1} = h_{2}$.

> [!corollary]- Every [[Groups|group]] of [[Primes|prime]] [[Order in Groups|order]] is [[Cyclic Groups|cyclic]]
> Supposw $\left| G \right| = p \in \mathbb{P}$.
> 
> If $g \in G$ with $g \ne e$, then $\left| g \right| \,{\big|} \left| G \right|$
> 
> So $\left| g \right| = p$, meaning $\left< g \right> = G$.