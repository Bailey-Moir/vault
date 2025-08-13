---
tags:
  - atom
  - math
---
> [!proof]- If $\vecbf{x}' = A\vecbf{x}$ where $\vecbf{x}(t_{0})=\vecbf{x}_{0}$, then $\vecbf{x} = \Phi(0)\text{diag}(e^{\lambda_{k}t})\Phi(t_{0})^{-1}\vecbf{x}_{0}$
> $$\begin{align}
> 	\Phi(t) &= \left[ e^{\lambda_{1}}\vecbf{v}_{1} \;|\; \cdots \;|\; e^{\lambda_{m}}\vecbf{v}_{m} \right] \\
> 	&= \left[ \vecbf{v}_{1}\;|\;\cdots\;|\;\vecbf{v}_{m} \right] \begin{bmatrix}
> 		e^{\lambda_{1}} & \cdots & 0 \\
> 		\vdots & \ddots & \vdots \\
> 		0 & \cdots & e^{\lambda_{m}}
> 	\end{bmatrix} \\
> 	&= \Phi(0)\text{diag}(e^{\lambda_{k}t})
> \end{align}$$
> Thus, since $\vecbf{x}(t)=\Phi(t)\Phi(t_{0})^{-1}\vecbf{x}_{0}$[^1],
> $$\vecbf{x}=\Phi(0)\text{diag}(e^{\lambda_{k}t})\Phi(t_{0})^{-1} \vecbf{x}_{0}.$$

> [!proof]- $A = \Phi(0)\text{diag}(\lambda_{k})\Phi(0)^{-1}$
> By definition of the [[Eigenvectors & Eigenvalues|eigenpairs]],
> $$\begin{align}
> 	A\vecbf{v}_{1}&=\lambda_{1}\vecbf{v}_{1} \\
> 	&\;\;\vdots \\
> 	A\vecbf{v}_{m}&=\lambda_{m}\vecbf{v}_{m}. \\
> \end{align}$$
> Putting this into [[Linear Systems|matrix form]] gives
> $$\begin{align}
> 	\left[ A\vecbf{v}_{1}\;|\;\cdots\;|\;A\vecbf{v}_{m} \right] &= \left[ \lambda_{1}\vecbf{v}_{1}\;|\;\cdots\;|\;\lambda_{m}\vecbf{v}_{m} \right] \\
> 	A\left[ \vecbf{v}_{1}\;|\;\cdots\;|\;\vecbf{v}_{m} \right] &= \left[ \vecbf{v}_{1}\;|\;\cdots\;|\;\vecbf{v}_{m} \right]\begin{bmatrix}
> 			\lambda_{1} & \cdots & 0 \\
> 		\vdots & \ddots & \vdots \\
> 		0 & \cdots & \lambda_{m}
> 	\end{bmatrix} \\
> 	A\Phi(0) &= \Phi(0)\text{diag}(\lambda_{k}) \\
> 	A &= \Phi(0)\text{diag}(\lambda_{k})\Phi(0)^{-1} \\
> \end{align}$$

> [!lemma]- When would we use this?
> $$\begin{align}
> 	\vecbf{x}' &= A\vecbf{x} \\
> 	&= \Phi(0)\text{diag}(\lambda_{k})\Phi(0)^{-1}\vecbf{x} \\
> 	\Phi(0)\vecbf{x}' &= \text{diag}(\lambda_{k})\Phi(0)^{-1}\vecbf{x} \\
> 	\vecbf{y}'(t) &= \text{diag}(\lambda_{k})\vecbf{y}(t) && \vecbf{y}(t)=\Phi(0)^{-1}\vecbf{x}(t), \\
> \end{align}$$
> Which gives
> $$y_{k}' = \lambda_{k} y_{k}$$

\[[[Diagonalisation]]\]

[^1]: [[Solutions to Homogeneous DEs]]
