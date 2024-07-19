---
tags:
  - atom
  - math
---
$$ \lambda \left(x_1, \dots, x_n\right) = \left(\lambda x_1, \dots, \lambda x_n\right) $$
Just like [[Vector Addition|vector addition]], scalar multiplication is an element-wise operation, just like [[Matrix Scalar Multiplication|scalar multiplication with matrices]].
$$\begin{align*} 
	|\lambda\mathbf{\underline{v}} | &= |\lambda| \cdot |\mathbf{\underline{v}}| \\
	\angle ( \lambda\mathbf{\underline{v}} ) &= \left\{\begin{array}{lcr}
		\angle\mathbf{\underline{v}} & \text{if} & \lambda > 0 \\
		\angle\mathbf{\underline{v}} + \pi & \text{if} & \lambda < 0 \\
		\text{undefined} & \text{if} & \lambda = 0 \\
	\end{array}\right. \\
\end{align*}$$
Multiplying a vector $\mathbf{\underline{v}}$ by a **real** scalar $\lambda$ results in a vector whose magnitude is $|\lambda|$ times the magnitude of $\mathbf{\underline{v}}$, and whose direction is the same if $\lambda > 0$, and opposite if $\lambda < 0$.

> [!proof]
> $$\begin{align*}
> 	\lambda \left( x_1, x_2 \right) \rangle &= \lambda \left(x_1\mathbf{\underline{\hat i}} + x_2\mathbf{\underline{\hat j}}\right) \\
> 	&= \lambda x_1\mathbf{\underline{\hat i}} + \lambda x_2\mathbf{\underline{\hat j}} \\
> 	&= \left(\lambda x_1 + \lambda x_2 \right) \\
> \end{align*}$$
> \[[[Basis Vectors]]\]

---

