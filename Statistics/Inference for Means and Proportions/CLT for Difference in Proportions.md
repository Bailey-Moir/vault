---
tags:
  - atom
  - stats
---
This only deals with proportions from two distinct groups (i.e., it would have to be coincidence for $n_1 = n_2$).
When selecting random samples of size $n_1$ and $n_2$ from populations with proportions of $p_1$ and $p_2$ respectively, the distribution of difference in sample proportions ($\hat p_1 - \hat p_2$) is below, provided $n_1$ and $n_2$ are sufficiently large.
$$ \hat p_1 - \hat p_2 \sim  \mathcal{N}\left( p_1 - p_2, \sqrt{\dfrac{p_1(1-p_1)}{n_1} + \dfrac{p_2(2-p_2)}{n_2}} \right) $$

> [!note]
> This is a good approximation as long as
> $$\begin{array}{ccc}
> 	n_1p_1 \ge 10 & \text{and} & n_1(1-p_1) \ge 10  \\
> 	n_2p_2 \ge 10 & \text{and} & n_2(1-p_2) \ge 10  \\
> \end{array}$$
> 

\[[[Difference in Proportions]], [[CLT for Proportions]], [[Central Limit Theorem]]\]