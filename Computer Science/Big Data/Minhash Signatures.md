---
tags:
  - atom
  - comp
---
Let a [[Characteristic Set Matrices|characteristic matrix]] $M$ be given. Let the [[Minhashing|minhash]] [[Functions|functions]] for $m$ random [[Permutations|permutations]] of the [[Universal Set|universal set]]/rows be given by $h_{1},\dots,h_{m}$.

The *minhash signature* of a column $S$ of $M$ is then $\left[ h_{1}(S),\dots,h_{m}(S) \right]^T$, and the *signature matrix* is given by replacing each column with its *minhash signature*.
$$\begin{bmatrix}
	h_{1}(S_{1}) & h_{1}(S_{2}) & \cdots & h_{1}(S_{n}) \\
	h_{2}(S_{2}) & h_{2}(S_{2}) & \cdots & h_{2}(S_{n}) \\
	\vdots & \vdots & \ddots & \vdots \\
	h_{m}(S_{m}) & h_{m}(S_{2}) & \cdots & h_{m}(S_{n}) \\
\end{bmatrix}$$
Then by the [[Minhashing#^theorem|minhashing theorem]], the [[Jaccard Distance|Jaccard similarity]] between two [[Sets|sets]] is approximated by the [[Proportion|proportion]] of rows where the two columns agree (as each row can be viewed as an [[Independent Events|independent]] experiment).