---
tags:
  - atom
  - math
---
![400|center](hausdorff-space.excalidraw)
A [[Topology|topological space]] $\left( X,\mathcal{T} \right)$ is a *Hausdorff space* iff every pair of distinct points have [[Disjoint Sets|disjoint]] [[Neighbourhoods|neighbourhoods]];
$$\forall p,q \in X, \left( p \ne q \to \exists A_{p} \in \mathcal{N}_{p},A_{q} \in \mathcal{N}_{q} : A_{p} \cap A_{q} = \emptyset \right)$$
> [!theorem-1]- [[Sequence Convergence|Limits]] of [[Sequences|sequences]] in *Hausdorff spaces* are distinct.
> Suppose a [[Sequences|sequence]] $\left( a_{n} \right)$ in a [[Topology|topological space]] $\left( X,\mathcal{T} \right)$ [[Sequence Convergence|converges]] to both distinct $L$ and $M$. Thus,
> $$\begin{array}{c}
> 	\forall A_{L} \in \mathcal{N}_{L}, \exists N_{L} \in \N: \forall n \ge N_{L}, a_{n} \in A_{L} \\
> 	\forall A_{M} \in \mathcal{N}_{M}, \exists N_{M} \in \N: \forall n \ge N_{M}, a_{n} \in A_{M}. \\
> \end{array}$$
> Combining these gives that for any $A_{L}$ and $A_{M}$, for all $n \ge N = \text{max}\{ N_{L},N_{M} \}$, $a_{n} \in A_{L} \cap A_{M}$.
> 
> Thus, any pair of [[Neighbourhoods|neighbourhoods]] of $L$ and $M$ must be non-[[Disjoint Sets|disjoint]], meaning $\left( X,\mathcal{T} \right)$ is not a *Hausdorff space*.
> 
> Thus, the result is proven [[Proof by Contraposition|by contraposition]]. $\square$

> [!theorem-2]- Any finite [[Subsets|subset]] of a *Hausdorff space* is [[Closed Sets|closed]].
> Suppose $S$ is a finite [[Subsets|subset]] of a *Hausdorff space*.
> 
> Let $p \notin S$. Then since this is a *Hausdorff space*, for all $q \in S$, there exists $A_{q} \in \mathcal{N}_{p}$ such that $q \notin A_{q}$.
> 
> Since [[Open Sets|open sets]] are closed under finite [[Unions & Intersections|intersection]],
> $$\bigcap \{ A_{q} : q \in S \} \in \mathcal{T},$$
> giving $S \cap \left( \bigcap \{ A_{q} : q \in S \} \in \mathcal{T} \right) = \emptyset$.
> 
> Thus, by the [[Closures|characterisation of closures]]/[[Exteriors|exteriors]], $p \notin \bar{S}$. This gives
> $$\begin{align}
> 	&\,\forall p \in X, \left( p \notin S \to p \notin \bar{S} \right) \\
> 	\to &\,\forall p \in X, \left( p \in \bar{S} \to p \in S \right) && (1) \\
> 	\to &\,\bar{S} \subseteq S \\
> 	\to &\, S = \bar{S} && (2)\, S \subseteq \bar{S} \\
> 	\to &\, S^c \in \mathcal{T} && (3) \\
> \end{align}$$
> \[$(1)$ [[Converse, Inverse, and Contrapositive|Contrapositive]], $(2)$ [[Closures]], $(3)$ [[Closures]], Theorem 1\]

> [!theorem-3]- Every [[Metric Spaces|metric space]] is *Hausdorff* with the usual topology.
> #TODO

> [!theorem-4]- For a *Hausdorff space* $\left( X,\mathcal{T} \right)$, if $p \in X$ is a [[Limit Points|limit point]] of $S \subseteq X$, then every [[Neighbourhoods|neighbourhood]] of $p$ contains infinitely many points of $S$.
> Let $p \in X$ be a [[Limit Points|limit point]] of $S \subseteq X$ (where $\left( X,\mathcal{T} \right)$ is *Hausdorff*).
>
> We are going to show for any $n \in \N$, **there are $\mathbf{n}$ distinct points in $\mathbf{S}$** such that there is a [[Neighbourhoods|neighbourhood]] of $p$ that contains none.
> 
> **Base Case**
> There exists $U_{0} \in \mathcal{N}_{p}$ since [[Topology|topologies]] cover the space (e.g. take $U_{0} = X$).
> 
> **Induction Step**
> Suppose $U_{n} \in \mathcal{N}_{p}$ such that there exists distinct $q_{0},\dots,q_{n-1} \in S\setminus U_{n}$.
> 
> Since $p$ is a [[Limit Points|limit point]] of $S$, there must exist a point $q_{n} \in S \cap U_{n}$ such that $p \ne q_{n}$.
> Further, for all $k \in \Z_{n}$, $q_{k} \ne q_{n}$ as $q_{n} \in U_{n}$ and $q_{k} \notin U_{n}$
> 
> Since this is a *Hausdorff space*, there must exist some $V_{n} \in \mathcal{N}_{p}$ such that $q_{n} \notin V_{n}$.
> 
> Let $U_{n+1} = U_{n} \cap V_{n} \in \mathcal{N}_{p}$. This $U_{n}$ has none of $q_{0},\dots,q_{n-1}$ or $q_{n}$.
> 
> Thus, there exists distinct $q_{0},\dots,q_{n} \in S\setminus U_{n+1}$.

> [!theorem-5]- If two [[Continuous Maps|continuous maps]] $f,g$ between the same *Hausdorff spaces* are equal when restricted to a [[Dense Subsets|dense subset]], $f = g$.
> Suppose $f,g : X \to Y$ are [[Continuous Maps|continuous maps]] between *Hausdorff spaces*, and $D$ is a [[Dense Subsets|dense subset]] of $X$ such that $f\bigr|_{D} = g\bigr|_{D}$.
> Let $E\subseteq X$ be the [[Sets|set]] of points where $f$ and $g$ agree.
> Suppose $p \in E^c$, so $f(p) \neq g(p)$.
> Since $Y$ is *Hausdorff*, there exists [[Disjoint Sets|disjoint]] $U \in \mathcal{N}_{f(p)}$ and $V \in \mathcal{N}_{g(p)}$.
> By the [[Continuous Maps|continuity]] of $f$ and $g$, $f^{-1}(U)$ and $g^{-1}(V)$ are [[Open Sets|open]], meaning
> $$p \in W = f^{-1}(U) \cap g^{-1}(V) \in \mathcal{T}_{X}.$$
> For any $w \in W$, $f(w) \in U$ and $g(w) \in V$ which are [[Disjoint Sets|disjoint]], so $w \in E^c$.
> This gives that for any $p \in E^c$, there exists a $W \in \mathcal{N}_{p}$ contained in $E^c$, so $E^c \in \mathcal{T}$[^1].
> Since $E$ is [[Closed Sets|closed]] and $D \subseteq E$ and $D$ is [[Dense Subsets|dense]], $\overline{D} = X \subseteq E \subseteq X$.
> Thus, $E = X$, meaning $f = g$.


[^1]: [[Interiors]]