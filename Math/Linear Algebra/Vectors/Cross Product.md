---
tags:
  - atom
  - math
---
![500|center](cross-product.excalidraw)
If $\vecbf{x} = \left\langle x_1, x_2, x_3 \right\rangle$ and $\vecbf{y} = \left\langle y_1, y_2, y_3 \right\rangle$ are two [[Vectors|vectors]] in $\R^3$, then the [[Vectors|vector]]
$$ \vecbf{x} × \vecbf{y} = \left\langle x_2y_3 − x_3y_2, −(x_1y_3 − x_3y_1), x_1y_2 − x_2y_1 \right\rangle $$
is called the cross product of $\vecbf{x}$ and $\vecbf{y}$, characterized by being [[Orthogonal Vectors|orthogonal]] to both [[Vectors|vectors]].
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

> [!note]- Trick for Validating
> A trick to validate that you have correctly calculated $\vecbf{n} = \vecbf{x}\times\vecbf{y}$ is to check that $\vecbf{n}\cdot\vecbf{x} = 0$ and $\vecbf{n}\cdot\vecbf{y} = 0$, given the *cross product* is [[#Properties of Cross Product|orthgonal to its operands]].
# Properties of Cross Product
The *cross product* is only defined for [[Vectors|vectors]] in $\R^3$. Thus, $\forall \vecbf{x}, \vecbf{y}, \vecbf{z} \in \R^3$
- **Orthogonal to Operands**
  $\vecbf{x} \times \vecbf{y} = \vecbf{n} \implies \vecbf{n} \:\bot\: \vecbf{x} \land \vecbf{n} \:\bot\: \vecbf{y}$[^1]
- **Pseudo-commutativity**
  $\vecbf{x} \times \vecbf{y} = -\vecbf{y} \times \vecbf{x}$
- **Distributive**
  $\vecbf{x} \times (\vecbf{y} + \vecbf{z}) = \vecbf{x} \times \vecbf{y} + \vecbf{x} \times \vecbf{z}$ 
  $(\vecbf{x} + \vecbf{y}) \times \vecbf{z} = \vecbf{x} \times \vecbf{z} + \vecbf{y} \times \vecbf{z}$ 
- **Associative Scalar Multiplications**
  $s(\vecbf{x} \times \vecbf{y}) = (s\vecbf{x}) \times \vecbf{y} = \vecbf{x} \times (s\vecbf{y}) \hspace{1em} s \in \R$ 
- $\vecbf{x} \times \vecbf{x} = 0$
- **NOT Associative**

[^1]: [[Orthogonal Vectors]]

