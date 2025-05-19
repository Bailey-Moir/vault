---
tags:
  - atom
  - math
  - linear
---
![1000|center](four-fundamental-subspaces.excalidraw.md)
Each [[Matrices|matrix]] $A \in \R^{m,n}$[^3] (or [[Linear Maps|linear map]]) is associated with *four fundamental subspaces*:
1. $\text{null}(A)$[^1]
2. $\text{row}(A) =\text{col}(A^T)$[^2]
3. $\text{null}(A^T)$[^1]
4. $\text{col}(A) =\text{row}(A^T)$[^2]

> [!example]-
> $$\begin{array}{cc}
> 	A = \begin{bmatrix}
> 		1 & 3 \\
> 		2 & 6
> 	\end{bmatrix}
> 	&
> 	A^T = \begin{bmatrix}
> 		1 & 2 \\
> 		3 & 6
> 	\end{bmatrix}
> \end{array}$$
> Written in [[EF & REF|REF]], we get
> $$\begin{array}{cc}
> 	\begin{bmatrix}
> 		1 & 3 \\
> 		0 & 0
> 	\end{bmatrix}
> 	&
> 	\begin{bmatrix}
> 		1 & 2 \\
> 		0 & 0
> 	\end{bmatrix}
> \end{array}$$
> 1. $\text{null}(A) =\text{span}\left\{ \begin{bmatrix}-3 \\ 1\end{bmatrix} \right\}$[^1]
> 2. $\text{row}(A) =\text{span}\left\{ \begin{bmatrix}1\\ 3\end{bmatrix} \right\}$[^2]
> 3. $\text{null}(A^T) =\text{span}\left\{ \begin{bmatrix}-2\\ 1\end{bmatrix} \right\}$[^1]
> 4. $\text{col}(A) =\text{span}\left\{ \begin{bmatrix}1\\ 2\end{bmatrix} \right\}$[^2]

> [!theorem]- For all $A \in \R^{m,n}$[^3], $\text{null}\,A =(\text{row}\,A)^\perp$[^4], and thus $\text{null}\,A^T =(\text{col}\,A)^\perp$[^4].
> Let $A = \begin{bmatrix} \vecbf{a}_{1} \\  \vecbf{a}_{2} \\  \vdots \\ \vecbf{a}_{n} \\  \end{bmatrix}$. Then $A\vecbf{x} = \begin{bmatrix} \vecbf{a}_{1} \\  \vecbf{a}_{2} \\  \vdots \\ \vecbf{a}_{n} \\  \end{bmatrix}\begin{bmatrix} x_{1} \\  x_{2} \\  \vdots \\ x_{n} \\  \end{bmatrix} = \begin{bmatrix} \vecbf{a}_{1}\cdot\vecbf{x} \\ \vecbf{a}_{2}\cdot\vecbf{x} \\ \vdots \\ \vecbf{a}_{3}\cdot\vecbf{x} \\ \end{bmatrix}$. Thus,
> $$\begin{align}
> 	& \vecbf{x} \in \text{null}\,A \\
> 	\iff& A\vecbf{x} = \vecbf{0} \\
> 	\iff& \vecbf{x} \text{ is orthogonal to } \vecbf{a}_{1},\dots,\vecbf{a}_{n}\\
> 	\iff& \vecbf{x} \text{ is orthogonal to } \text{span}\,\{\vecbf{a}_{1},\dots,\vecbf{a}_{n}\}\\
> 	\iff& \vecbf{x} \text{ is orthogonal to } \text{row}\,A \\
> 	\iff& \vecbf{x} \in \left( \text{row}\,A \right)^\perp \\
> \end{align}$$
> Thus, $\text{null}\,A = \left( \text{row}\,A \right)^\perp$, meaning
> $$\begin{align}
> 	\text{null}\,A^T &= \left( \text{row}\,A^T \right)^\perp \\
> 	\text{null}\,A^T &= \left( \text{col}\,A \right)^\perp
> \end{align}$$
> \[[[Orthogonal Complements]], [[Span]]\]

> [!theorem] For all $A \in \R^{m,n}$[^3] and $b \in \R^m$,
> - $A\vecbf{x}=\vecbf{b}$ has a solution iff $\vecbf{b} \in\text{col}\,A$[^2],
> - if $b \in\text{col}\,A$[^2], then $A\vecbf{x}=b\vecbf{v}$ has a **unique** solution $\vecbf{x}_{r}$ in $\text{row}\,A$, and
> - the set of solutions of $A\vecbf{x} = \vecbf{b}$ is $\vecbf{x}_{r} +\text{null}\,A$.
> > [!proof]-
> > Since $\text{col}\,A =\text{range}\,A$, the first bullet point follows from the definition of [[Range & Image|range]].
> > 
> > There exists an [[Orthogonal Decomposition|orthogonal decomposition]] $\R^n =\text{null}\,A \oplus \text{row}\,A$[^5]. Thus, each solution $\vecbf{x} \in \R^n$ can be [[Orthogonal Decomposition|orthogonally decomposed]] into
> > $$\vecbf{x} = \vecbf{x}_{r} + \vecbf{x}_{n},$$
> > where $\vecbf{x}_{r}$ and $\vecbf{x}_{n}$ are **unique** vectors in $\text{row}\,A$ and $\text{null}\,A$ respectively.
> > 
> > Suppose there are two solutions $\vecbf{x}_{r_{1}} + \vecbf{x}_{n_{1}}$ and $\vecbf{x}_{r_{2}} + \vecbf{x}_{n_{2}}$. Then
> > $$\begin{align}
> > 	A(\vecbf{x}_{r_{1}} + \vecbf{x}_{n_{1}}) &= A(\vecbf{x}_{r_{2}} + \vecbf{x}_{n_{2}}) = \vecbf{b} \\
> > 	A\vecbf{x}_{r_{1}} + A\vecbf{x}_{n_{1}} &= A\vecbf{x}_{r_{2}} + A\vecbf{x}_{n_{2}} \\
> > 	A\vecbf{x}_{r_{1}} + \vecbf{0}&= A\vecbf{x}_{r_{2}} + \vecbf{0} \\
> > 	A\vecbf{x}_{r_{1}} &= A\vecbf{x}_{r_{2}} = \vecbf{b} && \text{Existence}\\
> > 	A(\vecbf{x}_{r_{1}} - \vecbf{x}_{r_{2}}) &= \vecbf{0}. \\
> > \end{align}$$
> > Thus $\vecbf{x}_{r_{1}} - \vecbf{x}_{r_{2}} \in\text{null}\,A$. However, as shown, $\text{null}\,A \cap\text{row}\,A = \{ \vecbf{0} \}$, and $\vecbf{x}_{r_{1}},\vecbf{x}_{r_{2}} \in\text{row}\,A$, so $\vecbf{x}_{r_{1}} - \vecbf{x}_{r_{2}} \in\text{row}\,A$, meaning 
> > $$\begin{align}
> > 	\vecbf{x}_{r_{1}} - \vecbf{x}_{r_{2}} &= \vecbf{0} \\
> > 	\vecbf{x}_{r_{1}} &= \vecbf{x}_{r_{2}} && \text{Uniqueness}\\
> > \end{align}$$


[^1]: [[Null Space]]
[^2]: [[Column Space]]
[^3]: [[Sets of Matrices]]
[^4]: [[Orthogonal Complements]]

[^5]: [[Direct Sums]]
