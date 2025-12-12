---
tags:
  - atom
  - math
---
> [!theorem]- **2.19.1** - $\forall x \in \R, \exists m \in \Z : m \le x < m + 1$
> Let $x \in \R$.
> 
> By the [[The Real Numbers#Properties of The Reals|the Archimedian principle]], there exists $N \in \Z$ such that $x < N$.
> 
> [[Recursion|Recursively]] define a [[Sequences|sequence]] $\left( a_{n} \right)$ by
> $$\begin{array}{l}
> 	a_{0} = N \\
> 	a_{n+1} = \left\{\begin{matrix}
> 		a_{n} - 1 & x < a_{n} - 1 \\
> 		a_{n} & \text{otherwise.} \\
> 	\end{matrix}\right.
> \end{array}$$
> $\left( a_{n} \right)$ is [[Monotone Sequences|monotonically decreasing]] and [[Bounded Sequences|bounded below]] by $x$, so it must [[Metric Sequence Convergence|converge]][^1]. This [[Sequences|sequence]] [[Monotone Sequences|decreases]] by one until it reaches a term $a_{k}$ where $x \geq a_{k}-1$, at which point every subsequent term is equal to $a_{k}$. Since every term has a difference of one up until it reaches $k$, $k$ must exist (to allow [[Metric Sequence Convergence|convergence]]).
> 
> From the definition of $k$, $a_{k} = a_{k-1}-1$, so by the [[Recursion|recursive]] definition of $\left( a_{n} \right)$, $x < a_{k-1}-1$.
> 
> Combining these inequalities gives
> $$\begin{array}{c}
> 	 a_{k} - 1 \le x < a_{k-1}-1 = a_{k} \\
> 	 m \le x < m + 1 && m = a_{k} - 1
> \end{array}$$
> ![500|center](240-thrm-2.19.1.excalidraw)

> [!theorem]- **2.19.2** - $\forall x \in \R, \forall n \in \Z^+, \exists m \in \Z : \dfrac{m}{n} \le x < \dfrac{m+1}{n}$
> Apply 1 to $nx$ to obtain
> $$\begin{array}{c}
> 	m \le nx \le m + 1 \\
> 	\dfrac{m}{n} \le x \le \dfrac{m + 1}{n} \\
> \end{array}$$

[^1]: [[Monotone Convergence Theorem]]
