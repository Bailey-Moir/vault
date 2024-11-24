---
tags:
  - atom
  - math
---
The *co-factor* of $a_{ij}$ is defined as $\left( -1 \right)^{i+j}M_{ij}$, where $M_{ij}$ is the [[Minors|minor]] of $a_{ij}$. The alternating coefficient $\left( -1 \right)^{i+j}$ gives a check board pattern:
$$\begin{array}{ccc}
	\begin{bmatrix}
		+&-&+&-\\
		-&+&-&+\\
		+&-&+&-\\
		-&+&-&+
	\end{bmatrix}
	&&
	\begin{bmatrix}
		+&-&+\\
		-&+&-\\
		+&-&+
	\end{bmatrix}
\end{array}
$$
The [[Determinants|determinant]] of a [[Matrices|matrix]] can be calculated as the sum of the products of entries with their *co-factors* along any given row or column:
$$\begin{align*}
	\left| A \right| &= \sum_{k=1}^n \left( -1 \right)^{k+j} a_{kj} M_{kj} && 1 \leq j \le n \\
	&= \sum_{k=1}^n \left( -1 \right)^{i+k} a_{ik} M_{ik} && 1 \leq i \le n
\end{align*}$$