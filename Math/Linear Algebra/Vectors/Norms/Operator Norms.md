---
tags:
  - atom
  - math
  - linear
---
The *operator norm* $\| A \|$ of a $A \in \R^{n,n}$ induced by a vector [[Norms|norm]] $\| \cdot \|$ on $\R^n$ is
$$\| A \| = \max_{\vecbf{x} \in \R^n} \dfrac{\| A\vecbf{x} \|}{\| \vecbf{x} \|} = \max_{\hat{\vecbf{x}}\in\R^n} \| A\hat{\vecbf{x}} \|$$
\[[[Matrix Norms]], [[Unit Vectors]]\]

> [!theorem] The *operator norm* induced by a vector [[Norms|norm]] on $\R^n$ is a [[Matrix Norms|compatible]] [[Matrix Norms|matrix norm]] on $\R^{n,n}$.

> [!theorem]- *Operator* $1$-[[P-Norms|norms]]
> The *operator* $1$-[[P-Norms|norm]] $\| A \|_{1}$ of $A \in \R^{n,n}$ is the maximum absolute **column** sum of $A$, that is,
> $$\| A \|_{1} = \text{max}\{ \| \vecbf{a}_{1} \|_{1}, \dots, \| \vecbf{a}_{n} \|_{1} \},$$
> where $A = \left[ \;\vecbf{a}_{1} \; \cdots \; \vecbf{a}_{n}\; \right]$.

> [!theorem]- *Operator* $\infty$-[[P-Norms|norms]]
> The *operator* $\infty$-[[P-Norms|norm]] $\| A \|_{\infty}$ of $A \in \R^{n,n}$ is the maximum absolute **row** sum of $A$, that is, > $$\| A \|_{1} = \text{max}\{ \| \vecbf{a}_{1} \|_{1}, \dots, \| \vecbf{a}_{n} \|_{1} \},$$
> where $A = \begin{bmatrix}\vecbf{a}_{1} \\ \vdots \\ \vecbf{a}_{n}\end{bmatrix}$.

> [!theorem]- *Operator* $2$-[[P-Norms|norms]]
> The *operator* $2$-[[P-Norms|norm]] $\| A \|_{2}$ of $A \in \R^{n,n}$ is the maximum [[Singular Value Decomposition|singular value]] of $A$,
> $$\| A \|_{2} = \text{max}\{ \sigma_{1},\sigma_{2},\dots, \sigma_{n}\}$$