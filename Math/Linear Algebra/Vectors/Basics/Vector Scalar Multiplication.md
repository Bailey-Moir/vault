---
tags:
  - atom
  - math
  - linear
---
$$ \lambda \left\langle x_1, \dots, x_n\right\rangle = \left\langle \lambda x_1, \dots, \lambda x_n\right\rangle $$
In *vector scalar multiplication*, each [[Components|component]] is multiplied by the scalar.
$$\begin{align*} 
	\|\lambda\vecbf{v}\| &= \|\lambda\| \cdot \|\vecbf{v}\| \\
	\angle ( \lambda\vecbf{v} ) &= \left\{\begin{array}{lcr}
		\angle\vecbf{v} & \text{if} & \lambda > 0 \\
		\angle\vecbf{v} + \pi & \text{if} & \lambda < 0 \\
		\text{undefined} & \text{if} & \lambda = 0 \\
	\end{array}\right. \\
\end{align*}$$

> [!proof]-
> $$\begin{align*}
> 	\lambda \left\langle x_1, x_2 \right\rangle &= \lambda \left(x_1\vecu{i} + x_2\vecu{j}\right) \\
> 	&= \lambda x_1\vecu{i} + \lambda x_2\vecu{j} \\
> 	&= \left\langle \lambda x_1, \lambda x_2 \right\rangle \\
> \end{align*}$$
> \[[[Basis]]\]

> [!note]- Parallel Vectors
> Two [[Math/Linear Algebra/Vectors/Vectors|vectors]] are **parallel** iff they are *scalar multiples* of one another;
> $$ \vecbf a \parallel \vecbf b \iff \exists \lambda \in \R : \vecbf a = \lambda \vecbf b $$