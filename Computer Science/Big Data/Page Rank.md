---
tags:
  - atom
  - comp
---
The [[Internet|web]] can be modelled as a [[Directed Graphs|directed]] [[Graphs|graph]] $G$ with [[Vertices|vertices]] representing pages, and [[Edges|edges]] representing links between them. These [[Vertices|vertices]] are given weights representing the **rank**/importance of each [[Vertices|vertex]]/page. The *ranks* are given by a [[Vectors|vector]] $\vecbf{r}$ satisfying
$$\begin{array}{c}
\vecbf{r} = \underbrace{\left( \beta M + (1 - \beta)\left[ \dfrac{1}{N} \right]_{N \times N}  \right)}_{A} \vecbf{r} &&
\| \vecbf{r} \|_{1} = 1,
\end{array}$$
where $M$ is a [[Stochastic Adjacency Matrix|uniform Stochastic adjacency matrix]]. This corresponds to following a random out-link with [[Probabilities|probability]] $\beta$, and teleporting to random [[Vertices|vertex]] with [[Probabilities|probability]] $1 - \beta$.

> [!theorem]- Solving for $\vecbf{r}$ can be done using [[The Power Method|the power method]], specifically:
> 1. Let $k = 0$, and $\vecbf{r_{0}} = \begin{bmatrix} \frac{1}{N} & \cdots & \frac{1}{N}\end{bmatrix}^T$.
> 2. Set $\vecbf{r_{k+1}} = A\vecbf{r_{k}}$, and increment $k$.
>    *Normally you'd divide by some [[Norms|norm]], but $A$ preserves the [[P-Norms|1-norm]] as it is, so this is unnecessary.*
> 3. Repeat until $( \vecbf{r_{n}} )$ [[Metric Convergence|converges]] (within some chosen $\varepsilon > 0$).

> [!implementation]-
> $$\begin{array}{rl}
> \hline
> 
> \scriptsize1& \textbf{procedure} \; \text{P{\scriptsize AGE}-R{\scriptsize ANK}-I{\scriptsize TERATION}}(r^\text{old}) \\
> 
> \scriptsize2& \hspace{1em} r^\text{new} \leftarrow \begin{bmatrix} 1/N & \cdots & 1/N \end{bmatrix}^T \text{ of same size as } r^\text{old} \\
> 
> \scriptsize3& \hspace{1em} \textbf{for} \; i \; \textbf{in} \; V(G)  \\
> 
> \scriptsize4& \hspace{2em} \textbf{load} \; r_{i}^\text{old}, \delta_{i}, \, \textbf{and} \; \text{dest}_{1}, \dots, \text{dest}_{\delta_{i}} \\
> 
> \scriptsize5& \hspace{2em} \textbf{for} \; j \; \textbf{from} \; 0 \; \textbf{to} \; \delta_{i}  \\
> 
> \scriptsize6& \hspace{3em} \large r^\text{new}_{\text{dest}_{j}} {\hspace{0.2em}+\hspace{-0.3em}=\hspace{0.5em}} \beta r^\text{old}_{i} / \delta_{i} \\
> 
> \scriptsize7& \hspace{1em} \textbf{return} \; r^\text{new} \\
> 
> \hline
> \end{array}$$

^implementation

[^1]: [[Eigenspaces]]
