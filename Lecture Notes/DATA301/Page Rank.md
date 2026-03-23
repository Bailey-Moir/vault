---
tags:
  - atom
  - comp
---
The [[Internet|web]] can be modelled as a [[Directed Graphs|directed]] [[Graphs|graph]] $G$ with weighted [[Vertices|vertices]] representing the **rank**/importance of each [[Vertices|vertex]]/page. The *rank* of pages are given by a [[Vectors|vector]] $\vecbf{r}$ satisfying
$$\begin{array}{c}
\vecbf{r} = \underbrace{\left( \beta M + (1 - \beta)\left[ \dfrac{1}{N} \right]_{N \times N}  \right)}_{A} \vecbf{r} &&
\| \vecbf{r} \|_{1} = 1,
\end{array}$$
where $M$ is a [[Stochastic Adjacency Matrix|uniform Stochastic adjacency matrix]]. This corresponds to following a random out-link with [[Probabilities|probability]] $\beta$, and teleporting to random [[Vertices|vertex]] with [[Probabilities|probability]] $1 - \beta$.

> [!theorem]- Solving for $\vecbf{r}$ can be done using [[The Power Method|the power method]], specifically:
> 1. Let $k = 0$, and $\vecbf{r_{0}} = \begin{bmatrix} 1 & \cdots & 1\end{bmatrix}^T$.
> 2. Set $\vecbf{r_{k+1}} = A\vecbf{r_{k}}$, and increment $k$.
>    *Normally you'd divide by some [[Norms|norm]], $A$ preserves the [[P-Norms|1-norm]] as it is, so this is unnecessary.*
> 3. Repeat until $( \vecbf{r_{n}} )$ [[Metric Sequence Convergence|converges]] (within some chosen $\varepsilon > 0$).

[^1]: [[Eigenspaces]]
