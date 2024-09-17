---
tags:
  - atom
  - math
we:
---
![500|center](cross-product.excalidraw)
If $\vecbf{x} = \left\langle x_1, x_2, x_3 \right\rangle$ and $\vecbf{y} = \left\langle y_1, y_2, y_3 \right\rangle$ are two [[Vectors|vectors]] in $\R^3$, then the [[Vectors|vector]]
$$ \vecbf{x} × \vecbf{y} = \left\langle x_2y_3 − x_3y_2, −(x_1y_3 − x_3y_1), x_1y_2 − x_2y_1 \right\rangle $$
is called the cross product of $\vecbf{x}$ and $\vecbf{y}$, characterized by being [[Orthogonal Vectors|orthogonal]] to both [[Vectors|vectors]].
# Properties of Cross Product
- The *cross product* is only defined for [[Vectors|vectors]] in $\R^3$.
- $\vecbf{x} \times \vecbf{y} = \vecbf{n} \implies \vecbf{n} \:\bot\: \vecbf{x} \land \vecbf{n} \:\bot\: \vecbf{y}$^[[[Orthogonal Vectors]]]
- $\vecbf{x} \times \vecbf{y} = -\vecbf{y} \times \vecbf{x}$ (not commutative)

> [!proof]-
> $$\begin{array}{c} 
> 	\vecbf{x} \:\bot\: \vecbf{n} \\ 
> 	\vecbf{y} \:\bot\: \vecbf{n} 
> \end{array} \implies \begin{array}{c} 
> 	\vecbf{x} \cdot \vecbf{n} = 0 \\
> 	\vecbf{y} \cdot \vecbf{n} = 0 
> \end{array} \implies \begin{array}{c} 
> 	x_1n_1 + x_2n_2 + x_3n_3 = 0 && (1)\\
> 	y_1n_1 + y_2n_2 + y_3n_3 = 0 
> \end{array}$$
> Scaling to eliminate $n_1$:
> $$\left\{\begin{array}{l}
> 	x_1y_1n_1 + x_2y_1n_2 + x_3y_1n_3 = 0 && \times y_1\\
> 	x_1y_1n_1 + x_1y_2n_2 + x_1y_3n_3 = 0 && \times x_1
> \end{array}\right.$$
> Therefore
> $$ (x_2y_1 - x_1y_2)n_2 + (x_3y_1 - x_1y_3)n_3 = 0 $$
> Note there are infinitely many choices for $\vecbf{n}$, so I will choose one that avoids fractions. Note we have the form $an_2 + bn_3 = 0$, so I will choose $n_2 = b$ and $n_3 = -a$, giving $ab - ab = 0$. 
> $$\begin{array}{l}
> 	n_2 = x_3y_1 - x_1y_3 \\
> 	n_3 = -(x_2y_1 - x_1y_2) \\
> 	\phantom{n_3} = x_1y_2 - x_2y_1 \\
> \end{array}$$
> To find $n_1$, we can substitute into $(1)$:
> $$\begin{align*}
> 	0 &= x_1n_1 + x_2(x_3y_1 - x_1y_3) + x_3(x_1y_2 - x_2y_1)\\
> 	-x_1n_1 &= x_2x_3y_1 - x_2x_1y_3 + x_3x_1y_2 - x_3x_2y_1 \\
> 	&= - x_2x_1y_3 + x_3x_1y_2 \\
> 	n_1 &= x_2y_3 - x_3y_2 \\
> \end{align*}$$
> Thus
> $$ \vecbf{n} = \left\langle x_2y_3 - x_3y_2, -(x_1y_3 - x_3y_1), x_1y_2 - x_2y_1 \right\rangle $$